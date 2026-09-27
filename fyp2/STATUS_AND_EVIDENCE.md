# Implementation status and evidence conventions

## Ensemble architecture checkpoint — 27 September 2026

**Designed; not yet implemented/evaluated:** [fixed 50/50 complementary TF-mask
ensemble](ENSEMBLE_DESIGN_AND_EVALUATION.md), conditional released NeoSSNet + local
NMF membership. No gate training. Source hashes match the author model release;
reuse permission and loadability still require qualification. One offline NumPy
probe established finite NMF/Fixed Filter output and a legacy STFT endpoint defect;
three manikin source triples are not usable as-is additive targets. This is not a
benchmark or new separation result. Zero automated tests added; no broad suite,
model training, production access, dependency installation or deployment occurred.
The next authorised implementation should begin with Luna Phase A qualification.
All live security/backup evidence below remains unchanged; ensemble execution is
still unavailable. Historical results are not upgraded to current FYP2 evidence.

## Current production checkpoint — 27 September 2026

The isolated M1 application is deployed. Public Google Admin 200/Staff 403,
private-media isolation, HTTPS/SPA/API and restart persistence are **verified
live** within the scope in [production deployment evidence](PRODUCTION_DEPLOYMENT_EVIDENCE.md).
The first encrypted production B2 snapshot completed; daily backups are enabled,
pruning disabled. The active Firebase path is self-hosted JWT + REST lookup;
Cloud Run/billing remain unused. The dated evidence supersedes all older
not-deployed/not-installed/pending-real-REST statements below. Those older
sections are historical snapshots, not current setup instructions.

The dedicated password-provider account now supplies **verified live** login,
session, recovery/password-rotation and default-Staff evidence. Its verified state
was confirmed against Firebase; signup and original verification-email delivery
are owner-reported, while the actual verification transition was not observed.
Production Analyst promotion/audit, refresh/new-login persistence, Admin denial,
exact-original-audio assignment/review, unrelated-record isolation, and revocation
also passed. No production defect or code change was needed. Expired links remain
NOT TESTED, disabled/revoked provider cases remain MOCK ONLY, and nonexistent
generated outputs are NOT AVAILABLE / NOT TESTED. See the bounded evidence above;
do not upgrade historical local/mock results or claim participant evaluation.

## Superseding Firebase production-auth decision — 27 September 2026

Cloud Run was stopped before deployment because Google Cloud billing requires
an unavailable MYR 120 prepayment. Billing remains disabled; no Cloud Run,
Artifact Registry, service account or custom role was created. The active planned production boundary is local FastAPI Firebase
JWT verification followed by HTTPS Firebase Auth REST `accounts:lookup` with a
server Web API key restricted only to Identity Toolkit. The implementation
checks UID match, disabled/email verification state and the `validSince`
revocation boundary, then continues into trusted local StethoFuse authorization.
The focused auth/M1 regression passed 113 tests and 26 subtests (one
non-failing pre-existing Starlette deprecation warning). The restricted key
passed a harmless invalid-token reachability check. Real Admin/Staff REST
lookup is pending, so this path
is not yet `verified live`. No production deployment/routing changed. The prior
Cloud Run discussion is superseded and retained only as decision history.

## Latest backup evidence — 27 September 2026

This update supersedes earlier statements in this file that B2/Restic remote
setup or restore was blocked; it does not change the status of Firebase verifier
deployment or submitted FYP1. The owner-created private bucket
`stethofuse-prod-backup-927f5b7d` is in EU Central at
`s3.eu-central-003.backblazeb2.com`. Restic `0.18.1` initialized its encrypted
repository. A synthetic-only remote snapshot was checked and restored into an
isolated temporary path; `restic check` reported no errors, SQLite
`integrity_check` was `ok`, and manifest SHA-256, exact file-set and byte checks
passed. Evidence is recorded in the implementation backup runbook. This is
`tested` remote recovery for synthetic data only—not a production application
backup, scheduled job, or live deployment. On 27 September 2026 the owner
independently entered the offline paper-copy Restic password; it unlocked the
repository and restored the known synthetic file with its expected SHA-256. The
installed password credential was not used, and temporary recovery files were
removed. Offline password escrow recovery is **verified**. The 7/4/6 retention
policy is prepared; pruning and the systemd
timer remain disabled. No production DNS, Cloud Run/IAM, Firebase domain, Caddy,
or application-service changes occurred.

## Security sprint checkpoint — 27 September 2026

The local split identity boundary is **implemented, integrated and tested**:
`google-auth` verifies Firebase RS256 signatures and required project/issuer/time/UID
claims without ADC; the Cloud Run component uses Firebase Admin revocation/current-user
checks; local SQLite remains the authority for roles and private resources. The proposed
native service identity has only `firebaseauth.users.get` in a custom role. Production
emulator configuration is rejected; transport failure, untrusted responses and identity
mismatches fail closed. Email/verification fields are returned only for local identity
sync. Account-promotion target verification uses stored provider provenance; every target
request must still pass a current live identity check. No arbitrary target-UID API exists.

Validation: **42 focused tests passed** (verifier, JWT boundary, manifest), followed by
**91 access/M1/operator tests plus 26 subtests passed**. The first regression attempt
had 22 failures: the temporary environment lacked the already-locked upload parser,
and the bootstrap dry-run test patched the pre-split function name. After installing
the lockfile dependency and correcting that test reference, the rerun passed. A known
Starlette TestClient deprecation warning remains. Two new test functions were added in
this sprint (four executions); 18 pre-existing uncommitted test functions were retained.
Existing error-path checks now also assert that token/header/SDK diagnostic markers are
absent from application logs/output. These are **MOCK / LOCAL BACKEND / local cryptographic**
results; no new REAL FIREBASE or PRODUCTION evidence is claimed.

The verifier image builds. A credential-free API image with networking disabled passed
health 200, protected-route 401 and malformed-token 401 checks. The previously ambiguous
container-smoke output is superseded by this successful recorded check.

B2/Restic preparation includes systemd-loaded separate key/password credentials,
7/4/6 retention grouped by host/tags, and an executable synthetic remote restore drill
checking SQLite integrity, SHA-256 and byte equality. S3 key scope includes one bucket's
file operations and read-only bucket metadata; no bucket/account mutation authority.
Scripts pass shell syntax checks; remote execution remains **blocked** by owner account,
bucket/key setup and encrypted-repository initialization. Restic is not yet installed on
the host. Cloud Run/IAM/Artifact Registry and B2 resources are not created; no production
DNS, tunnel, Caddy, Firebase-domain, service or Axora changes were made.

Next: owner B2 setup and credential placement, then execute the prepared synthetic drill;
obtain approval for the exact Cloud Run/IAM and final isolated deployment changes before
any such write. Submitted FYP1 remains unchanged. No further broad test campaign is
required unless subsequent implementation or configuration changes warrant one.

## Current production identity and backup status — 27 September 2026

This addendum supersedes the prior production prerequisite snapshot below without
changing submitted FYP1 or historical M1 results. The owner approved a split
identity design: local, ADC-free Firebase RS256/claim validation in FastAPI; a
minimal, unprovisioned Cloud Run service with a dedicated native identity performs
Firebase revocation/current-user checks; StethoFuse's backend/database remains
the authority for roles, status, ownership, grants, assignments and audit. The
Cloud Run runtime permission required by the inspected SDK calls is
`firebaseauth.users.get`; a proposed project custom role with only that supported
permission is not yet created. No GCP IAM/service resource or production write exists.

Verifier changes and injected-boundary tests are `implemented` and `tested` locally
with simulated provider behavior only. The real Firebase/local backend acceptance
reported earlier predates this path and is not Cloud Run acceptance evidence. The
remote verifier is not `integrated live` or `verified live`; production remains
`planned` and must fail closed until deployed and checked with valid, revoked,
disabled and unverified identities.

The owner approved Backblaze B2 with Restic's S3-compatible backend. EU Central is
the prepared region recommendation because B2 offers no Asia region. Client-side
encryption, private bucket, bucket-scoped file list/read/write/delete application
key, separately escrowed Restic password and root-only systemd delivery are
required. Retention is 7 daily / 4 weekly / 6 monthly, but pruning is gated on a
successful remote restore drill. Script/template work is local only: no B2 account,
bucket, key, remote repository, encrypted backup or restore evidence exists. Do not
call the same-host archive test an off-host recovery test. No production deployment
or public routing change occurred.

See the [current M1 note](M1_IMPLEMENTATION_AND_TEST_NOTES.md#current-production-identity-and-backup-design--27-september-2026),
[traceability](TRACEABILITY.md), and implementation [verifier runbook](../../implementation/deploy/auth-verifier/README.md).

## Superseding production prerequisite evidence — 27 September 2026

This addendum supplements earlier M1/runtime snapshots without revising submitted
FYP1 or reclassifying old mock/synthetic tests. Graphify was queryable, but its
implementation index was at historical `main` commit `559ddba2…`, not the current
M1/runtime branch; the exact Firebase source paths were inspected after that
coverage gap was identified.

The current backend `implemented` path verifies Firebase ID tokens with online
revocation checking (`check_revoked=True`) and reads current Firebase Auth user
records to require enabled and email-verified accounts for session/account sync
and Admin role changes. It contains no runtime Firebase user create/update/delete,
password/email-send or custom-claim operation. StethoFuse roles, status, ownership,
grants, assignments and audit are backend/database controlled. This is a code-path
inventory, not new live-provider acceptance or a production call log. Do not remove
the online revocation/current-account checks as an optimization: signature-only
verification would change the current disabled/revoked-session policy. Least
privilege production permission remains Firebase Authentication Viewer (`users.get`)
only; no IAM change has occurred.

Production ADC is `blocked`: read-only host discovery found no Google-native workload
identity or genuine external OIDC/SAML/X.509 issuer. True unattended keyless Firebase
ADC cannot be completed on this host until a supported external workload identity
source exists; the operator's browser/ADC and a service-account JSON key are not
acceptable replacements. Local ADC packaging checks do not prove production ADC.

Off-host recovery is also `blocked`: no configured remote target or StethoFuse
backup repository was found. The new `implementation/deploy/backup-restic.sh` is
prepared but not installed or tested against a remote. A private Backblaze B2 bucket
plus Restic S3 backend is the conditional recommendation, pending region/privacy and
cost approval. Same-host synthetic archive/restore evidence remains `tested` only
for local packaging; no encrypted off-host backup/restore has been `tested`. No
provider account, key, billing resource, real recording or production service was
created/touched. The workspace-level operational decision record is
`planning/PRODUCTION_IDENTITY_AND_BACKUP.md`; this separate report repository
keeps the verified status here so its GitHub copy does not depend on a sibling
checkout.

M1 synchronization, 26 September 2026. These terms apply to the separate FYP2 working copy. They do not revise what the submitted FYP1 report claimed.

| Status | Meaning | Required boundary |
| --- | --- | --- |
| `implemented` | Code or configuration exists in an identified working version. | Name the files and revision; existence is not a successful execution. |
| `integrated` | The component is connected to the actual application path. | Identify entrypoint, caller, data flow and remaining unavailable capabilities. A standalone policy harness is not route integration. |
| `tested` | A named test was run and its result retained. | State date, environment, identity source, fixture/data, command, outcome and evidence. A failed test is still a test, not a pass. |
| `verified live` | The real named provider/server/environment was successfully exercised. | Specify local API with real provider versus deployed production. One does not prove the other. |
| `planned` | Intended but not implemented, or implementation evidence has not yet been accepted into this record. | State the next acceptance evidence; do not imply code absence where concurrent work is in progress. |
| `simulated` | A workflow uses fictional data or substituted identity/service behavior. | Label fixtures, injected verifiers, mocked SDKs and synthetic audio. Simulation may also be tested. |
| `blocked` | A specific external dependency or authorization prevents the next step. | Name the dependency and bounded action; unrelated work continues. |

Statuses are not one linear completion scale. For example, route code can be `implemented`, `integrated`, and `tested` with `simulated` identities while real-provider verification is `blocked`. “Approved” records a user/supervisor decision separately; it is not a test status. “Pending evidence” is a note, not an eighth status. Do not collapse these distinctions into “done”, “secure”, “live” or “production-ready”.

## Evidence record

Each feature claim links requirement ID, historical disposition, design section/artifact, source/config/migration paths, commit or working-file hashes, test name/command, UTC timestamp, environment and versions, identity source, input fixture or authorized dataset, expected and actual results, evidence path and limitations. Keep failure/retry history. Do not sum overlapping suites into a unique total.

Use these environment descriptions explicitly: offline mocked SDK; isolated policy-store tests; local API with injected fictional verifier; Firebase emulator; local API with real Firebase account; production hostname. No test below the last two proves genuine Firebase-provider operation. A successful homepage, build or local token-shaped string is not live-auth evidence.

Never retain passwords, ID/refresh tokens, action/reset links, MFA codes, service-account keys, participant identifiers or private audio in report evidence. An intended administrator email is contact/intent metadata, not a Firebase UID or authorization rule. Record only the minimal non-secret identity facts needed for an approved live check.

## Requirements chronology

1. Preserve the FYP1 requirement IDs, 53-response survey and its original questions/limitations.
2. Record FYP2 implementation-driven additions and supersessions separately, with decision sources.
3. Deploy only after the distinct deployment approval and checks.
4. Collect genuine authorized user feedback, then analyse it and record resulting changes.

Post-deployment feedback remains `planned`; it must not be backdated into initial elicitation or attributed to the original 53 respondents. See [requirements history](REQUIREMENTS_HISTORY.md) and [M1 evidence notes](M1_IMPLEMENTATION_AND_TEST_NOTES.md).
