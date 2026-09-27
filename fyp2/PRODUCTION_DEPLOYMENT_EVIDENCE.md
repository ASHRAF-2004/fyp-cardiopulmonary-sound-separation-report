# Production deployment evidence — 27 September 2026

Status: **implemented, integrated, tested, verified live** only for the bounded
checks below. Application release `921c40d0e5a9672d3917d98aea6d8802ec1d1b92` is
deployed at https://stethofuse.ashraf-alsaloul.com . This supersedes earlier
planned/blocked production snapshots, without rewriting FYP1 or old test results.

## Design actually deployed (Chapters 4–5)

Normal browser → Cloudflare HTTPS → dedicated `stethofuse-production` Tunnel →
loopback Caddy `127.0.0.1:8088` → static React SPA / same-origin FastAPI `/api`.
FastAPI port `8000` is internal to the isolated Compose network. SQLite and private
media are separate protected bind mounts, not web assets. Axora uses its unchanged
separate tunnel/network/services.

A final transport check initially found plain HTTP serving the SPA. A Cloudflare
Single Redirect scoped only to the StethoFuse hostname now sends HTTP to the same
HTTPS path/query with 308. Zone-wide settings and Axora are unchanged. The
implementation deployment receipt records the exact rule and rollback identifiers.

FastAPI verifies the Firebase JWT signature/claims using public certificates,
then presents the same token to Firebase Auth REST `accounts:lookup`. It validates
the matching UID, enabled/verified state and `iat >= validSince` (seconds), then
uses trusted local account/status/role/owner/grant records. A missing false
`disabled` boolean is permitted; explicit malformed values fail closed. The
server key is restricted to Identity Toolkit. No production ADC, service-account
key, Cloud Run, Artifact Registry, IAM role or Google billing change is involved.
Cloud Run remains a **superseded-before-deployment** design, not a deployed feature.

Firebase's authorized-domain list was extended only with the production hostname;
existing authDomain, Google provider and callback/sign-in configuration remain
unchanged. The two previously verified local accounts/roles and two explicitly
synthetic fixtures were copied using a consistent SQLite backup and private-file
copy. No repeated bootstrap, legacy migration, patient data or participant study.

## Bounded verification (Chapter 6)

| Requirement / concern | Observation | Evidence classification |
| --- | --- | --- |
| R01/R02/R13 identity and backend role | Real Google Admin: `/api/auth/me` 200 with matching Firebase UID/local admin; Admin Users 200. Real Staff: own identity 200/local healthcare_staff; Admin Users 403 and direct UI route denied. | PRODUCTION + REAL FIREBASE; verified live |
| R03/R11 ownership and private media | Owner metadata/media/download 200; downloaded synthetic bytes match SHA-256. Staff denied another owner's metadata/media/download (403). Admin likewise denied Staff-owned private content (403). Anonymous media and invalid token 401. | PRODUCTION + REAL FIREBASE / PRODUCTION; verified live |
| R03/R17 persistence | Controlled API restart preserved both users/roles, recordings/owners and two file hashes; SQLite integrity `ok`; service healthy. | PRODUCTION; tested |
| R17 ingress/isolation | Public HTTPS/TLS and SPA refresh work; health 200; API not host-published; web container has no private mount. Axora public HTTPS 200, original tunnel version/route and healthy services unchanged. | PRODUCTION; verified live |
| R17 backup operations | Restic snapshot `e0772dc0f83823e7d04b692ab0f54031f3fd8731bba811340de964383dca1df4`, 12:50 +08, completed and was listed remotely in encrypted B2. Services resumed healthy. | REAL B2 + PRODUCTION DATA; backup completion verified live |
| Error/revocation boundaries | Existing focused MOCK tests cover disabled/revoked and malformed/upstream failures. The optional-boolean parser correction passed 13 focused cases. | MOCK; tested, not live mutation of a real account |

Production acceptance used the two designated real Google identities through
normal external Chrome. Tokens/Authorization headers/key values were not included
in evidence; a bounded runtime-log scan found none. No broad regression suite was
repeated, and no new automated test functions were created during deployment.
Operational HTTP/browser/backup checks are not a new theoretical test campaign.

## Additional bounded action-link evidence (Chapter 6)

A continuation check on 27 September 2026 exercised the deployed missing-reset
link and deliberately invalid reset/verification links in separate tabs of normal
external Chrome, preserving the Admin session. Real Firebase returned HTTP400
`INVALID_OOB_CODE` for both invalid codes. The frontend removed the query, showed
the invalid-link state without displaying the code, and did not expose a reset
form or claim success. No email-send request occurred. Invalid-code rejection is
**PRODUCTION + REAL FIREBASE; verified live**; missing-code handling is
**PRODUCTION UI; tested**. This does not establish genuine expired-link behavior,
successful password registration/login/reset, email delivery, or verification.
No new automated test functions, account changes or broad suite reruns.

## Dedicated email/password acceptance (Chapter 6)

Subsequent bounded live acceptance used the owner-designated test-only account
`malaysiaashrafo@gmail.com`, separate from both established Google identities.
Registration through email/password and receipt of the verification email in Spam
were **owner-reported**. An independent real Firebase read confirmed a password
provider account, enabled and already email-verified. The verification-link click
and false-to-true transition were not observed; no duplicate verification email
was requested. These distinctions preserve the provenance of the evidence.

| Requirement / concern | Observation | Evidence classification |
| --- | --- | --- |
| R01 identity and default registration role | Initially no production application account; real email/password login through the StethoFuse UI succeeded, session onboarding created the matching active `healthcare_staff` account, and `/api/auth/me` returned `200`. Verification did not grant Analyst/Admin privileges. | PRODUCTION + REAL FIREBASE; verified live. Registration click remains owner-reported. |
| R01 session lifecycle | Refresh restored the same account; UI logout cleared the session, refresh stayed on login, tokenless identity returned `401`; subsequent email/password login succeeded. | PRODUCTION + REAL FIREBASE; verified live |
| R01 recovery | Actual Forgot Password UI received Firebase `200` and showed a safe conditional acknowledgement. Owner opened the official reset page and entered a new password personally. Old disposable password was rejected (`400`); owner-entered new password login succeeded with backend identity `200`. | PRODUCTION + REAL FIREBASE; verified live |
| R01/R02 identity continuity | Firebase UID unchanged after reset; email remained verified, local account active and role `healthcare_staff`. UID SHA-256 fingerprint `17869e6c6ecdb157538a3ec9918b6176568200da9627b11db1a572bfd7bdfccc`. | PRODUCTION + REAL FIREBASE; verified live |
| R02/R03/R11 pre-promotion isolation | Admin Users API `403`; unrelated Admin-owned and Staff-owned synthetic recording metadata/original media/download each `403`. | PRODUCTION + REAL FIREBASE; verified live |

Passwords, tokens, cookies, mailbox contents and reset links/action codes are not
evidence artifacts. The owner alone knows the new password. No production-code
change, new automated test or broad regression run was needed for these checks.
Earlier invalid-link evidence remains valid; genuinely expired action links are
**NOT TESTED**. Analyst acceptance is recorded separately below.

## Dedicated Audio Analyst acceptance (Chapter 6)

The same verified test account was promoted from Healthcare Staff to Audio Analyst
through the real Administrator Users interface. The two established core Google
accounts retained their original Admin/Staff roles. All rows below use
**PRODUCTION + REAL FIREBASE; verified live** evidence. Only existing synthetic
audio was used.

| Requirement / concern | Observation |
| --- | --- |
| Role assignment and auditability | Existing Administrator's confirmed UI role update returned `200`; the dedicated account remained active/verified and became `audio_analyst`. Backend refresh retained the role. `account.changed` audit `0b13b5a9679e4f01b5458f02eac3ea26` recorded the actor and target. |
| Administrative isolation | Analyst Admin Users/audit requests returned `403`; role and status PATCH requests returned `403`; direct Admin Users navigation redirected to `/403`. UI visibility was not the security boundary. |
| R03/R11 pre-assignment isolation | Both Admin-owned Recording A and Staff-owned Recording B metadata/original media/download returned `403`. Analyst status alone did not provide private-audio access. |
| Scoped assignment | Owner's normal recording UI granted `review` on A's exact original-audio resource (`201`, assignment `21de67f12ba9474892fcd2b3618aa492`). No global/whole-recording/sibling grant was created. A metadata/media/download became `200`; B remained `403`. |
| Review and provenance | Assigned-review UI loaded authorized original media; Analyst saved and updated accepted, non-diagnostic synthetic notes (`PUT 200`). Review persisted after refresh, used the correct reviewer ID and produced two `review.updated` audit events. Owner/Admin could not update the Analyst's review (`403`). |
| Revocation and history | Owner UI revoked the grant (`204`); `grant.revoked` audit `c501ae9900d34c18af318ac74c0ecf2e` exists. A metadata/media/download/review GET/review PUT became `403`; B remained denied; assignments/authorized-recording lists became empty. Historical review and revoked-grant records were retained. |
| Direct private-media boundary | Anonymous media/download returned `401`; authenticated direct A URLs after revocation returned `403`. Knowing resource identifiers did not bypass the backend. |
| Role after a new login | UI logout returned to login with tokenless identity `401`. After owner-entered new-password sign-in, the same verified UID remained active `audio_analyst`; refresh preserved it, `/api/auth/me` returned `200`, Admin Users remained `403`, active assignments remained empty, and the dashboard loaded. |

Synthetic recording identifiers are A `3c366aef758643f29c6a1d280792313d` and B
`9f0e232e80e84a798cdc8f5b9a109e83`; their original-audio resource identifiers are
`b5204c691b7c47a9b133e1ddf759f9be` and `c815f69a3613491b9329698227870daa`.
These identify bounded fixtures, not participant data. No generated result,
heart/lung output, waveform, spectrogram or job exists for these fixtures: related
acceptance is **NOT AVAILABLE / NOT TESTED**, not inferred from original media.
No production defect, code fix, new automated test, broad suite run or redeployment
was required. Existing disabled/revoked Firebase-account rejection remains
**MOCK ONLY**; no real identity was disabled/revoked for these checks.

Post-acceptance public health and SPA returned `200`; StethoFuse web/API and
Axora containers remained healthy. No deployed code/configuration was changed.

## Backup and recovery (Chapters 4, 5, 6)

Client-encrypted Restic uses the private B2 EU Central bucket via S3. The first
production snapshot covers SQLite, private synthetic files, runtime configuration
and SHA-256 manifest only (five files, 145.326 KiB). Backup credentials, developer
ADC, source/build caches and Axora data are excluded. Separate root-only secrets
are delivered through systemd credentials; the encryption password has a tested
independent offline paper copy.

The daily timer starts at 03:15 Asia/Kuala_Lumpur with up to 45 minutes jitter.
The consistent backup briefly stops/restarts only StethoFuse, so a short nightly
maintenance outage is expected. Retention target remains 7 daily / 4 weekly /
6 monthly. **Destructive pruning is disabled.** Earlier synthetic remote restore
verified SQLite integrity, SHA-256/file sets/bytes; independent paper-password
recovery also passed. The first production snapshot was completed/listed, not
subjected to another full restore. Do not conflate these evidence scopes.

Rollback stops the dedicated tunnel and timer, then only this Compose project,
preserving data and encrypted snapshots. There is no previous production release.
Only the newly created StethoFuse DNS/tunnel/domain additions may be reversed;
Axora remains out of scope. Exact IDs, paths, image IDs and commands are in the
implementation repository's `deploy/PRODUCTION_2026-09-27.md`.

## Still planned or not tested

- The registration click and original verification-email delivery are
  owner-reported; the verified Firebase state and live email/password/recovery
  results are bounded above. Verification transition and genuinely expired
  action-link behavior were not observed. The bounded email/password and Analyst
  acceptance sequence above is complete, including post-promotion new login.
- Live disabled/revoked-account mutation was not performed. Earlier share/revoke
  evidence remains REAL FIREBASE + LOCAL BACKEND; the separately documented
  Analyst assignment/revocation above is PRODUCTION + REAL FIREBASE.
- Ensemble/expert execution, derived outputs, durable worker, device capture and
  GPU integration remain planned; health honestly reports ensemble unavailable.
- This is not clinical validation, target-user evaluation, security certification
  or a measured availability/performance result. Post-deployment feedback is
  still planned and must follow actual deployment/use, not be attributed to FYP1.
- Submitted `report/Submission/` is unchanged. The academic title and original
  literature/survey findings are unchanged.
