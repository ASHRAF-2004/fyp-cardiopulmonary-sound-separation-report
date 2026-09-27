# M1 identity and authorization implementation and test notes

## Current production identity and backup design — 27 September 2026

This dated addendum supersedes earlier production ADC/WIF options and does not
revise submitted FYP1 or relabel historical tests. The owner chose to keep FastAPI,
the application authorization database, private audio, processing and future GPU
work on the self-hosted server, with a tiny Cloud Run service only for Firebase
revocation/current-account checks.

The current source path is:

```text
FastAPI request → local Firebase RS256/public-certificate + claim validation
  → Cloud Run HTTPS current-user/revocation check → UID-linked local account
  → local status/role/owner/grant/assignment authorization
```

Local signature/claim checking uses public Firebase signing certificates and needs
no privileged ADC. The Cloud Run Admin SDK's `verify_id_token(check_revoked=True)`
and `get_user(uid)` need `firebaseauth.users.get`; a proposed project custom role
contains only that supported permission. No Firebase user write/list/email-send or
custom-claim operation is used. A dedicated native Cloud Run service identity is
proposed; it has not been created. No credential JSON or ADC is mounted in the
self-hosted API. The public verifier requires a valid token, uses only its signed
UID, returns minimal identity status and has no enumeration, role or mutation
route. Residual abuse/rate-limit limits are recorded in the implementation deploy
runbook. StethoFuse remains the sole authority for application authorization.

The verifier code and local tests are `implemented` and `tested` only against
controlled/mock provider boundaries; they are not `verified live`. Earlier real
Firebase/local FastAPI acceptance remains valid evidence for that earlier local
provider revision, but does not verify this new Cloud Run path. No Cloud Run/IAM,
production route, Firebase domain or application deployment write occurred.

The owner created the private Backblaze B2 bucket `stethofuse-prod-backup-927f5b7d`
in EU Central at `s3.eu-central-003.backblazeb2.com` and the bucket-restricted
application key. Restic `0.18.1` initialized the encrypted S3 repository. On
2026-09-27 the synthetic-only remote drill uploaded a snapshot, ran `restic check`
with no errors, restored into an isolated temporary directory, and passed
`PRAGMA integrity_check=ok`, SHA-256 manifest, exact file-set and byte-comparison
checks. This is `tested` remote recovery evidence for synthetic data, not a backup
of the running StethoFuse application, production deployment, or scheduled backup.
On 2026-09-27, the owner independently entered the offline paper-copy Restic
password through a hidden prompt; the existing encrypted repository unlocked and
the known synthetic `runtime.env` restored with its expected SHA-256. The test
did not use the installed password credential and removed its temporary credential
and restore files. **Offline password escrow recovery is verified.** Key ID, key
secret, and Restic password are
separate root-owned `0400` files delivered through systemd private credentials;
their values are not recorded. Prepared retention remains 7 daily, 4 weekly, 6
monthly, with pruning gated; no timer, prune marker, or production snapshot exists.
Same-host archive checks alone do not prove off-host recovery. See
[`PRODUCTION_IDENTITY_AND_BACKUP.md`](../../planning/PRODUCTION_IDENTITY_AND_BACKUP.md)
and [`auth-verifier runbook`](../../implementation/deploy/auth-verifier/README.md).

The historical evidence and status records below remain unchanged and retain the
scope/time boundaries under which they were collected.

Working evidence record, 26 September 2026. The M1 backend and frontend are **implemented, integrated and tested locally with simulated identities/SDK mocks** within the scope below. The latest backend provisioning-hardening run records **99 cases plus 26 subtests passed**. Subsequent keyless ADC/provider reads and the authorized primary-admin bootstrap are **verified live within their stated operator scope**. M1 as a whole is **not fully verified live or recorded as complete**: post-promotion real browser/API checks and the wider genuine-provider acceptance matrix remain pending. Historical local evidence records 86 backend cases plus 26 subtests, 14 mocked authentication-browser checks, seven API-client checks and six real-local-API cross-layer checks; demo regressions, the focused rerun and the latest full backend run are recorded separately, not combined into a unique grand total.

The coordinator created recoverable pre-M1 checkpoints: implementation `c6818398d8e545834535afb08441f17eac3c2c6d` and documentation `47c10af9527ccc1425f7a8904210c55a72db10b7`. Concurrent working changes require their own evidence before they are described as integrated or tested. This documentation work does not commit, configure providers, bootstrap an admin, deploy or collect recordings.

The coordinator committed the locally tested implementation milestone as **`56ecc2d`** and reported a clean implementation worktree. The [final test-artifact manifest](provenance/m1-final-test-evidence-2026-09-26.sha256) pins eight result files separately, including the ignored local backend JUnit artifact; verify paths from the documentation repository. The revision and hashes identify this local evidence snapshot, not provider or deployment acceptance.

The subsequent role-provisioning hardening and operational guide are committed in implementation **`3d95270`** (`fix: verify role-change targets and document admin provisioning`). Its scoped change contains no frontend source/art changes. The later 99-case/26-subtest backend artifact is recorded separately below; the earlier milestone manifest is not relabeled to cover this newer revision.

## Confirmed scope

Firebase project: `stethofuse-c18cd-3cca0`. Confirmed production target: `https://stethofuse.ashraf-alsaloul.com`; target does not mean deployed. Academic title: **Machine Learning-Based System for Cardiopulmonary Sound Separation**, unchanged. Identity is Firebase's responsibility; roles, account status, ownership, grants and review authority remain server-controlled. Public account sync defaults to `healthcare_staff`.

The intended primary administrator is identified in continuation-pack `00_DECISIONS_AND_STATUS.md`; no personal email, UID or account-row contents are reproduced here. The user's current request authorized the trusted primary promotion, which has now been completed and independently checked as recorded below. Email was used only to locate the provider record; the verified existing UID, matching active verified local account and explicit operator approval governed the mutation. There is no email allowlist, first-signup rule, client role field or invented UID as a privilege source.

### Confirmed signup, sign-in and actor policy

The user explicitly confirmed that **an existing administrator may also promote accounts**. The implemented policy therefore remains unchanged: public onboarding defaults to `healthcare_staff`; `audio_analyst` is assigned by an authorized administrator; the first `admin` uses trusted operator bootstrap, and later promotions may use authenticated, confirmed, audited administrator account management. Public registration never selects analyst/admin. Signup creates an identity/account; sign-in proves identity and retrieves the existing server-controlled role; promotion changes that role through a separate authorized operation. All roles use the same sign-in flow, not a separate admin registration form.

The latest clarification requires promotion/demotion to be backend-enforced, audited, restricted to **existing verified accounts**, and protected by the last-active-admin invariant. That narrow hardening is now **implemented, integrated and tested locally**: every role-bearing admin PATCH rechecks the target's exact server-owned UID against the current provider record and requires an existing, enabled, verified identity. The store also requires the local target to remain verified inside the role/status/audit transaction. Target rejection returns 403, not an acting-admin session-expiry 401; provider unavailability returns 503 without mutation. The independently inspected latest JUnit records 99 cases plus 26 subtests passed, including 13 added provisioning cases. The provider outcomes in those tests are simulated; they do not establish a genuine web-admin promotion workflow. See the [roles and account-provisioning guide](../../implementation/docs/ROLES_AND_ACCOUNT_PROVISIONING.md).

| Actor | Main use cases / authority | Provisioning boundary |
| --- | --- | --- |
| Visitor | Register, sign in, Google sign-in, forgot/reset password | Public signup creates Healthcare Staff only; no privileged role selector |
| Healthcare Staff | `healthcare_staff`: own recordings/results/history, WAV/device intake, ensemble request, sharing/assignment | Default public account; a workflow label, not proof of professional qualifications |
| Audio Analyst | `audio_analyst`: review explicitly assigned content | Existing verified account promoted by Admin; role alone grants no other user's files |
| Administrator | `admin`: manage other verified accounts/roles/status, safe operational metadata and audit access | First Admin by trusted server bootstrap; future Admin by another Admin; cannot change own role/status; last-active-admin protection |
| Firebase Authentication | External identity, account verification and recovery support | Does not assign StethoFuse application roles |
| Google Identity Provider | External identity provider used by Firebase sign-in | Supporting system, not an application role |
| Digital Stethoscope / Audio Input Device | Supplies audio for device capture | Compatible hardware integration remains planned |
| Developer/operator | Infrastructure and trusted first-admin bootstrap | Operational actor only, not a normal application role |

Ensemble Learning is an internal subsystem, not a UML actor. FastAPI and the application
database are also internal components. Submitted FYP1 actors/artifacts remain unchanged;
these FYP2 boundaries refine the later design. Administrator status gives no automatic
access to another account's private audio or analyst review authority.

The focused self-management correction is now **implemented** in FastAPI and the live
admin UI: an administrator's own row is identified by the backend Firebase UID, shows
the authoritative role/status with a `You` marker, and has no editable controls. Self
role/status mutations return `403`; another verified account remains promotable or
demotable subject to the existing audit and last-active-admin rules. The UI refreshes
the authoritative `/me` account and re-fetches the user list after mutations; this is
not an email-based or browser-state role decision. The editable role/use-case source is
[`role-use-cases.mmd`](design/role-use-cases.mmd); Graphify was not configured, so the
existing Mermaid workflow is retained.

The current Mermaid set also records the M1 system boundary and the observed versus
proposed deployment route: [`m1-system-architecture.mmd`](design/m1-system-architecture.mmd)
and [`deployment-topology.mmd`](design/deployment-topology.mmd). The architecture marks
ensemble execution and physical capture as planned. The topology shows the healthy
Axora-only Cloudflare tunnel/Caddy route as observed and StethoFuse ingress as proposed;
there is no StethoFuse DNS record, public hostname mapping, production service, or
verified `/api` proxy yet.

## Repository preservation and tooling

The implementation and documentation repositories remain separate Git repositories.
Their owner-maintained branches are `fyp2/application` and `fyp2/documentation`, using the
established human-authored identity
`ASHRAF-2004 <adoashraf103@gmail.com>` recovered from prior project commits and matched to
the authenticated GitHub account. Both branches were pushed without force; remote SHAs
match local HEAD. Draft PR #9 and #2 are open. Earlier duplicate draft PR #8 and #1 were
closed as superseded; their codex-named branches and history remain preserved. No merge or
main-branch write occurred. GitHub and Cloudflare read-only access are verified; no
Cloudflare write occurred. Graphify is unavailable, so diagrams remain editable Mermaid
source. These tooling facts establish provenance and environment state, not application
functionality.

## Local API smoke check — 26 September 2026

After the stopped local services were restarted on their existing loopback ports, health
returned `200` and the frontend root returned `200`. Without a Firebase token, the local
backend returned `401` for `/api/admin/users`, `/api/recordings`, `/api/jobs`, and a direct
`/api/media/{id}` request. A request carrying a deliberately invalid bearer string and a
forged `{ "role": "admin" }` body also returned `401`. This is **LOCAL BACKEND** unauthenticated
denial evidence; it does not prove the signed-in admin `200`, ordinary-user `403`, a valid
Firebase token path, ownership/grant behavior, or any production route.

The normal external Google Chrome flow has now completed for both existing verified
accounts; the previous embedded/automation-browser rejection is not treated as evidence of
a provider defect. A separate Chrome profile was used without reading or changing the user's
existing Brave profile. Browser automation attached only to Chrome's loopback-bound debugging
port. No credentials, ID tokens, cookies or UIDs were written to these notes.

## Real-provider M1 acceptance — 27 September 2026

**REAL FIREBASE + LOCAL BACKEND:** The primary account `thalththanwyd@gmail.com` had a
verified Firebase session; `/api/auth/me` returned 200 with the matching backend identity,
`admin` role and active status. The Firebase UID matched the backend account UID without
recording either value. The protected `GET /api/admin/users` returned 200. The existing
ordinary account `adoashraf103@gmail.com` likewise had a verified Firebase session mapped
to the active `healthcare_staff` account; the same protected Admin Users API returned 403.
No email-string or browser-role shortcut was used.

**LOCAL BACKEND with REAL FIREBASE identities:** Staff direct navigation to the admin-users
route resolved to the private-access page. A request attempting to submit a forged `admin`
role returned 403. Firebase sign-out cleared the Staff session, after which `/api/auth/me`
without a bearer token returned 401. Session restoration after refresh was observed for the
real Google account. This establishes local frontend/API behavior, not production hosting.

A 0.01-second silent PCM WAV was generated in-browser and uploaded as a development-only
fixture owned by the Administrator. The owner read its metadata and media successfully (200).
Before a grant, Healthcare Staff received 403 for recording metadata, direct media and the
download URL. The owner then issued a read grant scoped to the single original-audio resource;
Staff could read metadata listing exactly one resource, and that media and its download
returned 200. Following revocation (204), those same metadata, media and download requests
returned 403 again. This is **REAL FIREBASE + LOCAL BACKEND** authorization evidence against
synthetic data, not patient audio, production media, an ensemble result, or a real analyst
assignment. In the reverse ownership direction, a second silent fixture was uploaded by
Healthcare Staff; the Administrator received 403 for its recording metadata, direct media
and download, and it was absent from the Admin's own recording list. This directly checks
that Admin does not automatically gain private-audio access. Both synthetic recordings are
intentionally retained in the isolated development database; they contain silence only.

**NOT TESTED:** Email/password registration and login, email verification delivery/action,
forgot/reset-password delivery and action-code expiry. No email was sent. There is no
separate verified Audio Analyst session, so analyst review was not tested live. There are no
processing results/jobs in this acceptance fixture; result, heart/lung, waveform and
spectrogram artifact authorization is supported by focused mock/local policy tests only.
No production test was performed.

## Provider configuration progress — 26 September 2026

This entry records the coordinator's subsequent official CLI/API observations and completed configuration actions. It supersedes the earlier **current-state** description of no Web App, uninitialized Authentication and pending CLI consent; it does not change the historical missing-configuration screenshots or mocked/local test results below.

- User-operated Firebase CLI consent completed. A subsequent `projects:list` read confirmed the selected project `stethofuse-c18cd-3cca0`, project number `923213197696`. This is developer CLI authorization, not an application-user session or backend ADC.
- The initial `apps:list` was empty. One Web App, **StethoFuse web**, was then registered with app ID `1:923213197696:web:e1810085b8db2b77a2d165`. Public client configuration is now in the git-ignored `implementation/frontend/.env.local`. This documentation update did not read or reproduce its key or configuration contents.
- Basic Firebase Authentication was initialized; the project remained on **Spark**. Official API reads confirmed email/password enabled with password required, Google enabled with an OAuth client configured, anonymous authentication disabled, and improved email privacy enabled. These observations verify configuration state, not successful sign-in, email delivery or token acceptance.
- The user approved **StethoFuse** as the Google product label and their designated public support contact. This contact setting grants no application role or privilege; the personal address is not reproduced here.
- Authorized domains currently contain only `localhost`, `stethofuse-c18cd-3cca0.firebaseapp.com` and `stethofuse-c18cd-3cca0.web.app`. The final hostname `stethofuse.ashraf-alsaloul.com` is **not yet authorized**. Custom reset/verification action URLs are absent/default; application action-handler routing and real delivery have not been verified.
- The user subsequently **explicitly approved restricted backend setup**. Official Google Cloud CLI **586.0.0** was installed privately after checksum verification; installation provenance and its separate consent/IAM boundaries are recorded in [`planning/tools/GCLOUD_INSTALL.md`](../../planning/tools/GCLOUD_INSTALL.md).
- The dedicated `stethofuse-m1-auth-reader` service account in the selected project was created and granted project role `roles/firebaseauth.viewer`. The approved source user was granted `roles/iam.serviceAccountTokenCreator` **on this service account only**, not project-wide. Official reads verified IAM, IAM Credentials and Identity Toolkit APIs as `ENABLED`, and verified this service account's `USER_MANAGED` key count as **0**. These observations describe restricted IAM/configuration, not application role assignment.
- Source-user browser ADC consent was pending at the earlier checkpoint. It has now completed, and **keyless impersonated backend ADC has been read-tested** by the coordinator. Developer credentials and provider reads remain distinct from the application's user ID token and application-admin role.
- A fresh frontend build with genuine public Web App configuration passed. The coordinator visually and accessibility-tree inspected the actual local login screen at `localhost:4180` and confirmed enabled login controls. This is configured frontend/rendering evidence only: no successful login, provider email delivery or backend token acceptance is inferred. The earlier missing-configuration test captures remain valid historical evidence.

At the 26 September provider-configuration checkpoint, the real-provider acceptance gate
was still open. The 27 September acceptance section above supersedes that checkpoint for
the specific Google-session, role, owner/grant/revocation, media and logout cases it tested;
all remaining gaps below stay open. No local/mock evidence is relabeled as verified live.

### Primary-admin operation and bounded live evidence — 26 September 2026

The user reported completing genuine Google sign-in and seeing the default Healthcare Staff role. Official Firebase lookup corroborated an enabled, email-verified Google identity, and its exact UID matched the already-created active, verified local staff account. This corroborates the reported onboarding but is not a replayed or captured end-to-end browser/token test. The default staff role before promotion was the intended signup policy, not a role-selection defect.

Before mutation, the coordinator confirmed no administrator and no consumed bootstrap marker, and verified the integrity of a private SQLite backup. With the user's explicit primary-promotion authorization, the existing `scripts/bootstrap_m1_admin.py` apply operation succeeded. A separate official provider lookup and `store.require_admin` check succeeded afterward. An exact same-account retry returned unchanged; one active administrator and one bootstrap audit event were confirmed. No real application-user token was extracted, and no personal UID, email or database-row contents are included in this record.

This is **verified live provider-read/trusted-bootstrap evidence**, not successful post-promotion browser/API authorization evidence. Those browser/API checks remain pending. A separate focused local pytest rerun reported **22 cases and 21 subtests passed, 64 deselected**, with the existing non-failing Starlette warning. It is not added to the earlier 86-case/26-subtest total or treated as a full-suite rerun.

## Design and implementation record

The [illustrative authorization sequence](design/m1-auth-sequence.mmd) is a target design, not execution evidence. It separates Firebase identity verification from fresh backend account/object checks and separates trusted admin bootstrap from public registration. It is an editable Mermaid source only; it is not a report-numbered final figure.

| Area | Requirement IDs | Report sections | Current accepted evidence | Next evidence needed |
| --- | --- | --- | --- | --- |
| Firebase browser flows and state restoration | R-AUTH-01-05,07 | 4.6, 4.9, 5.3, 6.3-6.4 | Google sign-in and SDK session restoration after refresh are **verified live** against the selected Firebase project; logout cleared the current user and tokenless API call returned 401. Earlier mocked/missing-configuration checks remain separate | Email/password signup/login, verification delivery/action and password recovery/action-code expiry are not tested. Final-hostname authorization and action-handler/delivery verification remain pending. Session persistence is SDK-managed, not an HttpOnly session |
| Verified token and account mapping | R-AUTH-06, R-ROLE-01 | 4.6, 4.8-4.9, 5.3, 6.3 | Real signed Google ID tokens were verified by local FastAPI for the existing primary Admin and Staff accounts; each Firebase UID matched its backend UID without retaining/displaying either UID. `/api/auth/me` returned the expected active role | Invalid/expired/wrong-project issued-token matrix and production verifier path remain untested. Mock provider outcomes are not live evidence |
| Ownership and direct media | R-OWN-01-05, R-RES-01-03 | 4.8-4.9, 5.4, 6.3-6.4 | Real Admin and Staff tokens were checked in both directions: non-owner metadata/media/download `403`; Admin collection did not list Staff-owned recording. Exact-granted original audio succeeded; owner succeeded | Production proxy/storage checks; derived result, heart/lung, waveform and spectrogram artifact URLs lack a real-result fixture. Retained legacy routers must never be mounted as an alternate application |
| Grants and review | R-SHARE-01-04, R-ROLE-02,05 | 4.3, 4.8-4.9, 5.7, 6.3 | Exact-resource read grant allowed Staff to see exactly one original resource (`200`); owner revocation returned `204` and future metadata/media/download returned `403`. Broader policy/mock tests cover expiry and analyst gates | No verified Audio Analyst session; live review workflow, result-scoped grants, owner feedback display and administrative reassignment remain untested/not implemented |
| Administration and bootstrap | R-ROLE-03-05, R-ADM-01-03,05 | 4.6, 5.7, 6.3 | Admin Users returned `200` to the bootstrapped Admin and `403` to real Staff. Forged Staff role PATCH returned `403`; direct route navigation resolved to the private page. Self-change/last-admin protection has prior focused mock/integration evidence. Latest full backend run remains 99 cases +26 subtests | Real web-admin promotion/demotion of another account and production/provider-side last-admin recovery remain untested |
| Persistent intake/history | R-REC-01-02,04-05, R-OWN-02 | 4.8, 5.4, 6.4 | Real Admin token uploaded a bounded synthetic silent WAV; owner metadata/media read returned `200`. Earlier scoped local persistence tests cover temporary DB reopen | Cross-browser real-account persistence and actual server-restart/recovery evidence; full attribute form/history/retention scope and backup/restore remain bounded gaps |
| Jobs and ensemble | R-PROC-01-05, R-ENS-01-06 | 4.7, 5.5-5.6, 6.6 | Availability/owner checks `implemented`, `integrated`, `tested`: processing returns 503 without inserting a job; benchmark route also unavailable. Actual ensemble remains `planned`; demo jobs/audio `simulated` | Real executor, provenance, verified experts/fusion and controlled evaluation. Tests of fixture-derived media do not prove separation output |
| Deployment and feedback | R-DEP-01-05 | 4.11, 5.8-5.9, 6.7-6.8 | Target hostname confirmed; deployment and post-deployment feedback `planned` | Config review, separate deployment approval, real HTTPS/auth/media/restart checks and genuine authorized feedback |

## Test evidence ledger

| Evidence ID | Environment and result | Source and limitation |
| --- | --- | --- |
| M0-POLICY | `tested`, `simulated`: 38 test cases plus 26 subtests, no failures/errors/skips, 2026-09-26 16:22:17 +08:00 | `../.local/workspace-preparation/access-and-database-tests.xml` relative to documentation. JUnit aggregate `tests=64`; 38 testcase elements. Includes 36 policy/SDK-seam tests and two existing database smoke cases. Not a protected-route or live-provider run. |
| M0-UI | `tested`, `simulated`: existing preparation build and 56 focused browser outcomes recorded by coordinator | `../planning/FRONTEND_FOUNDATION_STATUS.md` and `../.local/workspace-preparation/frontend/`. Historical to this M1 pass; not rerun by documentation worker and not added to overlapping earlier totals. |
| M1-API | Historical pre-provisioning-hardening run: `tested`, `simulated` identities/SDK boundary, **86 passed plus 26 subtests passed** = 49 M1 API cases + 36 foundation cases + one operator-safety case | Coordinator's then-final `../.local/m1-tests/backend-final-junit.xml`, timestamp 2026-09-26T19:04:06.564929+08:00: 86 testcase elements, aggregate `tests=112`, zero failures/errors/skips. Actual code/tests inspected. Real temporary SQLite, files and HTTP/TestClient routes; no genuine issued token. Earlier 85+26 independent run retained as `backend-junit.xml`, not added to the total. One non-failing Starlette httpx-to-httpx2 deprecation warning. |
| M1-ADMIN-PROVISIONING | Latest full backend run: `tested`, `simulated` identities/provider outcomes, **99 passed plus 26 subtests passed** = 62 M1 API cases + 36 foundation cases + one operator-safety case | Independently inspected `../.local/m1-tests/admin-provisioning-junit.xml`, timestamp 2026-09-26T20:26:56.298642+08:00: 99 testcase elements, aggregate `tests=125`, zero failures/errors/skips. Includes 13 added provisioning cases and expanded last-active-admin assertions. Real local HTTP/SQLite transactions; no genuine provider promotion/demotion or issued-token test. Coordinator reports the existing non-failing Starlette warning. Separate from, not added to, prior runs; this newer artifact is not part of the earlier eight-file milestone manifest. |
| M1-REAL-PROVIDER-LOCAL | `verified live` narrowly for Google sign-in/session restoration/logout and Firebase ID-token verification by the local API; Admin Users Admin `200`, Staff `403`; two-way owner isolation, exact scoped sharing/revocation and protected metadata/media/download checked using synthetic silent WAVs | 27 September 2026, user-operated normal Google Chrome sessions plus same-origin browser requests through the live local Vite/FastAPI services. No tokens, UIDs or credentials recorded. This is not production; no email/password, reset/verification email, analyst session, results/derived artifacts, or production route tested. |
| M1-BACKEND-ENV | `tested`: backend implementer reports `pip check` and compileall passed | Minimal `.local/venvs/backend-smoke`; pinned `requirements-m1.txt`, including Firebase Admin 7.7.0/FastAPI 0.136.0/Starlette 1.7.0/Pydantic 2.13.5. No ML weights/Torch installed for this milestone. Not an application deployment test. |
| M1-CLIENT | `implemented`, `integrated`; final `npm run build` passed per coordinator/frontend implementer; **seven client checks passed** | `../implementation/frontend/output/playwright/m1/client-final/results.json`, 2026-09-26T11:05:51.446Z; actual TypeScript client with mocked token source/transport, no backend/provider requests. Earlier identical seven-case result retained in `client/`, not added. Official client SDK is Firebase 12.19.0. |
| M1-AUTH-BROWSER | `tested`, `simulated`: **14 checks passed**, Chrome 151.0.7922.137; zero recorded runtime errors | `../implementation/frontend/output/playwright/m1/browser-final/results.json`, 2026-09-26T11:06:23.000Z. Actual fail-closed missing-config UI plus network-substituted official-SDK modules and mocked API; not an emulator or real provider/local API. Covers login/Google/register/verification/reset/logout, restoration, scoped presentation, awaited upload/grant/review, preferences and mobile containment. Supersedes the earlier 14-pass `browser-run3` after the bounded protected-media MIME correction. |
| M1-CROSS-LAYER | `tested`, `simulated` identity boundary: **six checks passed**, actual Chrome + local FastAPI + temporary SQLite/private WAV; zero recorded JS/server errors | `../implementation/frontend/output/playwright/m1/cross-layer-final/results.json`, 2026-09-26T11:07:13.292Z. Actual upload, owner-derived persistence, protected bytes, refresh, logout/A-B isolation and staff admin denial. Firebase SDK and backend verified-identity seam are mocked; no real Firebase/emulator/production request. Supersedes the earlier six-pass `cross-layer-v2` after the MIME correction; not added to it. |
| M1-UI-REGRESSION | `tested`: **16 workflow, five homepage and six owl checks passed**, kept as separate suites | Under `../implementation/frontend/output/playwright/m1/`: `workflows/workflows/results.json`, `home/results.json`, `motion/motion/results.json`. Only the development-only workflow demo uses `simulated` audio/jobs/capture; public homepage checks use the actual default-live UI. Emulated desktop/mobile/reduced-motion checks are not physical-device tests or genuine clinical UAT. |
| M1-VISUAL-PRESERVATION | `tested`: **1,282 protected files match** pre-M1 checkpoint `c681839`; zero mismatches | `../implementation/frontend/output/playwright/m1/preservation/results.json`, 2026-09-26T11:04:26.248Z. All selected tracked public assets, CSS and approved owl/scenery/rendering source are byte-identical. This is preservation evidence, not a new owl approval or complete visual certification. |
| M1-PROVIDER-PREREQUISITES | Approved/configured: dedicated Auth Viewer service account, source-user impersonation role scoped only to that account; API enablement and zero user-managed keys read-verified. Subsequent ADC consent completed and keyless backend credentials read-tested | Coordinator official API observations in the dated provider-progress entry. Private Google Cloud CLI 586.0.0 installation/checksum record: `../planning/tools/GCLOUD_INSTALL.md`. Scope is live backend credential/provider reads, not an application-user token or complete real-provider authentication suite. |
| M1-CONFIGURED-LOGIN | `tested`, bounded configuration/rendering: fresh frontend build with genuine public config passed; enabled local login controls visually/accessibility-tree inspected by coordinator | Actual `localhost:4180` login, not a successful application-user login. No new automated auth-suite result or provider/email/token acceptance is added to historical test totals. Public config/key contents were not read or reproduced by this documentation update. |
| M1-REAL-FIREBASE | Partial genuine evidence: live ADC/provider reads and intended identity verified; user-reported Google app login corroborated by provider and existing local account. Full real-provider acceptance is not complete | See the dated primary-admin entry and `../planning/M1_PROVIDER_AND_ROUTING_STATUS.md`. Earlier no-Web-App/Get-started/no-CLI/ADC-pending observations are historical. No application token extracted; post-promotion real browser/API checks and the wider genuine-provider/error/email matrix remain pending. Final hostname is not yet authorized and custom action URLs remain absent/default. |
| M1-PRIMARY-ADMIN | `verified live`, narrowly: explicitly approved trusted primary bootstrap succeeded; separate official provider lookup plus `store.require_admin` succeeded; retry unchanged; one active admin and one bootstrap audit event confirmed | Coordinator operation using existing CLI after exact verified provider/local UID match and private backup integrity verification. Email lookup identified the record only; it did not authorize promotion. Does not establish post-promotion browser/API access or create an additional administrator. No personal identifiers/token/row contents reproduced. |
| M1-ROLE-FOCUSED-RERUN | Historical `tested` local regression: coordinator reports **22 cases + 21 subtests passed, 64 deselected**, existing non-failing Starlette warning | Coordinator-reported terminal result; no dedicated artifact supplied for this run. Not a full rerun or additional unique total, and not evidence for the subsequent current-provider/verified-target hardening. This documentation worker did not rerun it; the separate M1-ADMIN-PROVISIONING row records the later full-backend result. |
| M1-PRODUCTION | `planned`, outside this local milestone | Observed Caddy/cloudflared containers serve unrelated Axora services; they are not proof of a StethoFuse route. Protected Caddy configuration is unreadable without separately approved access. No DNS/tunnel/service/deployment authorization or production success claimed. |

## Inspected source and route changes

Backend entrypoint `implementation/app/main.py` now creates the M1 application instead of importing legacy routers. `app/m1/api.py` connects token verification, current account lookup, object/role policy and sanitized responses to actual endpoints. `config.py` requires explicit isolated paths; `provider.py` is disabled unless enabled with separately configured server credentials; `media.py` implements bounded uploads and checked delivery; `store.py` and `schema.sql` extend the existing policy store in the same transaction domain. `scripts/bootstrap_m1_admin.py` is trusted operator-only, dry-run by default, with no public HTTP bootstrap. See the complete [route audit](../../implementation/docs/M1_ROUTE_AUDIT.md) and [contract](../../implementation/docs/M1_API_CONTRACT.md).

The later role-provisioning diff was independently reviewed in `app/m1/api.py` (admin PATCH), `app/access_foundation/store.py` (`change_account`) and `tests/test_m1_api.py`. The actor is authorized before target lookup; the target provider UID is taken from server data, never from a client role/UID claim. Current provider verification and exact UID matching precede the mutation; local actor/target checks, last-active-admin protection and audit occur in the same write transaction. The added cases cover ordinary-user denial, successful promotion/demotion with audit, both directions of unverified/disabled/deleted/mismatched/outage provider rejection, local unverified/unknown targets, and audit-failure rollback. No concrete defect was identified in this bounded diff review. External provider state and the local database cannot form one atomic transaction; this does not guarantee protection against later provider-side disablement/deletion or eliminate the separate operator-recovery boundary.

Ten former explicit handlers plus mounts/docs routes are accounted for. Old upload/separate/result/download/history and visualization URLs now return 410 without private data. `/models` and `/methods` require admin; `/` and health expose safe status only. The private `/visualizations` mount is removed; `/static` contains application source assets only; API docs are disabled. Canonical `/api/media/{resource_id}` authenticates and authorizes GET, HEAD and single ranges before reading. Legacy router/ML source remains on disk unchanged and is **not retrofitted with authorization**: bypassing the supported entrypoint by mounting it elsewhere would reintroduce risk.

The isolated M1 schema refuses both legacy databases and the older seven-table preparation schema; no production migration or implicit upgrade occurred. Unowned legacy records stay quarantined, not assigned to the first login/admin. Test files are generated PCM fixtures. M1 upload accepts file/title and extracts audio attributes, but does not claim the complete original contextual-metadata/device workflow. Review notes persist for an active assigned analyst against exact original-audio or result scope; they are not yet owner feedback or administrative reassignment features.

The final operator-safety correction refuses an existing storage directory with group/other permissions instead of changing its permissions or adopting it. `tests/test_m1_operator_safety.py` verifies the unrelated directory remains mode 0755 and no database is created after refusal; this is the additional 86th backend case.

Frontend source inspection confirms `frontend/src/auth/firebase.ts`, `src/config/runtime.ts`, `src/data/{api,live,liveTypes}.ts[x]`, `src/pages/LiveAuthPages.tsx`, `LiveWorkspacePages.tsx` and `src/main.tsx` connect an explicit live-mode path. It uses the official Firebase client API, SDK-managed session persistence, token headers, backend role mapping and an empty presentation state rather than fixture fallback. Unknown role/status responses are rejected. Session storage remains JavaScript-readable, not an HttpOnly/XSS-proof session. The old `apiAdapter` interface remains unavailable; actual live workspace requests use the new API client, so its old stubs are not evidence that the entire live path is absent. Final media rendering uses the authenticated Blob MIME, not a guessed assignment type/URL; real provider configuration/acceptance remains a separate gate.

## Backend command and evidence boundaries

Executed by the backend implementer/coordinator from the StethoFuse root, not rerun by the documentation worker. The historical pre-provisioning-hardening suite adds the operator-safety case and retains its original JUnit output:

```sh
.local/venvs/backend-smoke/bin/python -m pytest implementation/tests/test_m1_api.py implementation/tests/test_access_foundation.py implementation/tests/test_m1_operator_safety.py -q --junitxml=.local/m1-tests/backend-final-junit.xml
.local/venvs/backend-smoke/bin/python -m pip check
```

Named cases in `tests/test_m1_api.py` cover account sync/no client privilege, owner-derived durable upload, GET/HEAD/Range access and revocation, original-audio review persistence, overlapping grants and revoke-all, admin/last-admin boundaries, disabled/suspended state, legacy aliases, schema/path/symlink/collision safety, chunked/declared upload limits, safe validation and explicit unavailable ensemble behavior. `test_official_sdk_exception_types_are_mapped_without_network` and foundation seam tests substitute SDK outcomes; labels such as expired or wrong-project are **not real expired/wrong-project Firebase tokens**. The reopened TestClient application verifies local persistence, not an operating-system restart or production recovery drill.

The coordinator subsequently reran these three backend test modules after the role-provisioning hardening, recording `../.local/m1-tests/admin-provisioning-junit.xml` (relative to the documentation repository). Its 99 cases plus 26 subtests and zero failures/errors/skips were independently read from the artifact; no tests or provider operations were rerun by this documentation update. The earlier 86-case result and focused 22-case result retain their historical boundaries.

## Browser and cross-layer boundaries

Reproduction harnesses are `implementation/frontend/tests/m1/{browser,client,regression,preservation,cross-layer}.mjs` and `api_fixture.py`. Run from the frontend directory with a fresh `EVIDENCE_ROOT` to avoid overwriting retained evidence; see [exact commands and scope](../../implementation/frontend/tests/m1/README.md). Default-live preview uses loopback 4180; fixture workflows require the explicitly enabled development-demo server on 4182. These harnesses do not configure Firebase or authorize production changes. The coordinator stopped the temporary API fixture and demo server after final checks, leaving the pre-existing 4180 preview unchanged.

The cross-layer harness generates an 844-byte, 0.1-second, 4 kHz PCM WAV, not a human recording. Its actual backend uses temporary isolated files/SQLite and fictional injected identities. Direct unauthenticated media returns 401; another account's media and normal-staff admin requests return 403. Browser refresh retrieves the uploaded record; sign-out removes loaded media before the second account's denial check. The harness closes Chrome and terminates its temporary API fixture.

**Visual review is separate from automation.** The documentation worker inspected `cross-layer-v2/real-api-owned-recording.png` and `real-api-cross-account-denial.png`: the first shows an owner-scoped saved original and honest unavailable ensemble/deletion state; the second shows a permission denial without an audio player. The coordinator also visually inspected the actual missing-config login capture. Screenshots do not establish identity cryptography, complete accessibility or physical audio quality.

Earlier browser results under `browser/` and `browser-run2/`, and cross-layer results under `cross-layer/`, remain available. The implementers identified premature asynchronous checkbox expectations and an exact login-URL expectation that rejected a legitimate safe return query; waits and pathname/form assertions were corrected. The initial cross-layer run had four passes before that URL timeout; the subsequent six-pass run is identified explicitly rather than deleting the failure or summing retries.

### Acceptance cases still needing genuine provider or wider workflow evidence

The real operator bootstrap/provider lookup and unchanged retry are now evidenced as described above. The reported genuine Google login has provider/local-account corroboration, but post-promotion real browser/API assertions remain pending. Complete the wider acceptance matrix separately: registration, email/password login, Google login, sign-out, refresh restoration, reset request/action invalid/expired states, verification handling, verified token acceptance, missing/invalid/wrong-project/revoked token rejection, disabled/suspended account denial, default role and role-tampering rejection, A/B isolation, direct/range media authorization, scoped sharing, revocation including overlapping grants, exact-assignment review, admin denial/allowance, last-admin guard and safe logs. Each result must identify mocked SDK, injected local verifier, emulator, real provider/local API or production.

Do not mark all cases passed because a subset passed. Record a 503/unavailable route as tested failure handling, not as an implemented ensemble. Browser Blob URLs or previously downloaded bytes cannot be retroactively recalled by revocation; test future server requests and sign-out cleanup without promising impossible recall.

Provider acceptance is the real-live gate, not a reason to stop local code, mock/API tests or documentation. CLI consent, basic Web App/provider setup, restricted IAM, read-tested keyless ADC and the approved primary bootstrap have progressed as recorded above. The next evidence boundary is **post-promotion real browser/API validation**, followed by the wider genuine-provider acceptance matrix. These outcomes are not inferred from IAM grants, a provider lookup or an administrator row alone. Routing inspection remains separate from local M1.

## Isolated production-like runtime preparation — 27 September 2026

The current `fyp2/application` implementation adds `deploy/compose.yaml`, a Firebase ADC
overlay, a hash-pinned backend runtime image, and a multi-stage Vite/Caddy web image. The
two services use an isolated Compose network; Caddy provides same-origin SPA and `/api`
routing, FastAPI is not host-published, and the API alone mounts external SQLite/private
storage. Containers run non-root with read-only roots, dropped capabilities, health checks,
resource limits and bounded logs. ADC is an external read-only runtime mount; the developer
ADC used during local validation is not a production credential. Local build/client Firebase
values are public Web SDK configuration supplied with BuildKit secret mounts and are never
Admin credentials.

Status: runtime files are `implemented` and the package is `tested` locally. On 27 September,
both images built; `/` and `/app/admin/users` returned 200; API health reported storage and
Firebase provider configured while `ensemble_available` remained false; tokenless `/api/auth/me`,
`/api/admin/users`, and `/api/media/{id}` returned 401. Guessed `/private/...` was not served as
media. A synthetic-only M1 SQLite account and private marker survived container restart. A
synthetic offline archive/restore copy passed SQLite `PRAGMA integrity_check` and byte equality.
These are `LOCAL BACKEND` package checks, not real-user authorization, production, or a full
off-host backup/recovery drill. No real ID token or private audio was used in this package test.

The current app does not contain a durable job worker, connected ensemble executor, GPU
service, or production model assets. Ensemble job creation remains unavailable; no separation
quality or performance claim follows from this runtime. Production deployment and routing are
still `planned`, with no DNS/tunnel/Caddy/Firebase-domain/service write. See
[`PRODUCTION_RUNTIME_PROPOSAL.md`](../../planning/PRODUCTION_RUNTIME_PROPOSAL.md) for the
shared-Axora versus isolated-tunnel comparison, chosen proposal, backup/rollback plan, and
remaining deployment gate; see [`implementation/deploy/README.md`](../../implementation/deploy/README.md)
for reproducible local commands.

## Remaining factual gaps

Current FYP2 rubric/teaching plan/template and supervisor decisions; remaining final-hostname authorization, reset/verification action routing and wider provider-flow validation; post-promotion real browser/API and issued-token acceptance evidence; wider real-account sharing/review and recovery workflows beyond the named mocked/local checks; production routing, recovery, quotas, rate limits and retention/deletion; legacy ownership migration; owner review-feedback display/admin reassignment; physical capture device; candidate expert fidelity/checkpoints and controlled evaluation; genuine post-deployment feedback. See [source audit](provenance/M1_SOURCE_AUDIT.md). No new studies, participants or model scores are supplied here.

## Superseding production Firebase identity and backup discovery — 27 September 2026

Source inspection of the current implementation branch confirms that protected
requests call Firebase Admin `verify_id_token(..., check_revoked=True)`. That SDK
mode performs an Auth user-record read to reject revoked tokens and disabled users;
the application also checks current provider verification/enabled state during
account synchronization and before an Admin changes a role. No runtime Auth
user-management writes, email sends or custom-claim writes are present. The
Firebase Authentication Viewer role's `firebaseauth.users.get` permission is
the only Firebase Auth permission currently justified. StethoFuse application
roles/status/ownership/grants remain in its trusted backend store. No IAM change
was made. See current source in `implementation/app/access_foundation/identity.py`,
`implementation/app/m1/provider.py`, and `implementation/app/m1/api.py`.

Graphify MCP was queried first, but the StethoFuse index remains at historical
`main` `559ddba2…` and omits M1. Direct reads were limited to the three relevant
source paths above. The host reports no Google VM/container identity, Kubernetes
identity, or actual external OIDC/SAML/X.509 source. **Production keyless ADC is
blocked** until a genuine source is provided or the auth-dependent backend is
deliberately moved to a Google-hosted service identity. Developer ADC, copied
browser sessions and service-account JSON keys are not production options.

Read-only storage discovery found no remote filesystem/backup destination,
Restic/Borg/rclone tooling, or StethoFuse backup configuration. Local `/srv` and
`/var/backups` do not protect from host-disk loss. Restic-to-private-Backblaze-B2
via S3 is the conditional recommendation, pending region/privacy and cost
approval. The helper in `implementation/deploy/backup-restic.sh` is prepared,
not installed, and has not made a remote backup. Existing local synthetic
archive/restore evidence remains local-only; no encrypted off-host restore drill
exists. Production deployment remains `planned`; both production ADC and remote
restore prerequisites are `blocked`. No Firebase, IAM, billing, provider,
production server, DNS, tunnel or service write occurred in this pass. The
workspace-level operational decision record is
`planning/PRODUCTION_IDENTITY_AND_BACKUP.md`; the FYP2 repository records the
verified status above without a cross-repository link.
