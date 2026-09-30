# Implementation status and evidence conventions

## Current UX checkpoint — owner-approved core integration, 30 September 2026

**POLISH-V1 OWNER APPROVED / CORE IMPLEMENTED, INTEGRATED AND TESTED LOCALLY /
NEW INTERFACE NOT DEPLOYED / READY FOR OWNER REVIEW.**

[Core execution evidence](FROST_CORE_INTEGRATION.md) proves the real local
upload/capture→Library→durable Separate→private players→measured analysis path,
using the unchanged existing API/SQLite/storage/frozen CPU worker. Seventeen
real-local groups,14 separately labelled mocked account regressions and2 final
layout checks passed; both standalone builds exit0. Local identity uses the
existing test-only verifier/SDK seam, not a production bypass or live Firebase.
Owner approval closed the design; no remaining-service or deployment authority.

Existing production ML acceptance/backup and final consumed T9 evidence are
unchanged. This is a newly integrated LOCAL interface, not a new live release.
Handles/IDs/account services/global Insights/asset-gated flight remain pending.
STOP for owner review; physical-device/clinical qualification is still unclaimed.

## Historical UX checkpoint — local design proof, 30 September 2026

**FOUR REPRESENTATIVE SCREENS IMPLEMENTED LOCALLY / DESIGN INTERNALLY FROZEN /
OWNER VISUAL APPROVAL PENDING / REDESIGN NOT DEPLOYED.**

[Frost Studio design evidence](UX_DESIGN_REVIEW.md) proves Overview, consolidated
Library, ready detail with custom audio/actual signal analysis, and six-section
Profile & settings. Frost/Midnight/mobile screenshots, focused12-group checks
and normal build passed. Owner-directed green owl eyes, whole-page tracking and
leafy-perch contact are local only. Flight remains asset-gated; real identity/
privacy service migration and remaining app are not yet implemented.

The [completed production ML acceptance](PRODUCTION_DEPLOYMENT_EVIDENCE.md)
remains the live baseline: deployed integration, role/privacy acceptance and
encrypted post-acceptance backup were verified on29 September. The older local
“not yet deployed” statuses below are historical, not a reversal of deployment.
Frozen v2/T9/Firebase/private-resource authority/backups/Axora are unchanged.
No T9 reuse, training, production redesign or submitted FYP1 change occurred.

Owner screenshot approval is the next UX gate; Luna/full implementation and
deployment are not started automatically. Physical-device/clinical qualification
remain unclaimed.

## Current application checkpoint — local frozen-model integration, 29 September 2026

**IMPLEMENTED LOCALLY / TESTED LOCALLY / FINAL ML EVALUATION COMPLETE /
PRODUCTION ML INTEGRATION NOT YET DEPLOYED.**

[Local integration evidence](LOCAL_ML_INTEGRATION.md) connects record/upload,
one separation action, durable jobs, one hash-verified CPU worker, private
heart/lung WAVs, provenance and authorized review. Five focused tests/five
real-local browser groups passed; the broader campaign resolved137 cases and26
subtests passing, with14 mock browser groups passing. Harness corrections and
failed attempts remain recorded. Generated outputs follow owner/exact-grant
rules; admin has no blanket access. Capture used a fake microphone, not physical
stethoscope hardware. No new real-provider or production acceptance is claimed.

Frozen v2 and T9 evidence remain unchanged. Model selection is closed; T9 was
not reused. No training/tuning. Existing production M1, owl/theme and FYP1 remain
unchanged. Worker deployment/migration/provisioning require owner approval.
This supersedes only older local integration-pending statuses below.

## Completed ML checkpoint — T9 final held-out evaluation, 29 September 2026

**T9 HELD-OUT FINAL EVALUATION COMPLETE / FINAL MODEL HLS-ONLY T8 V2 /
MODEL SELECTION CLOSED / FINAL TEST CONSUMED / NOT YET INTEGRATED.**

[T9 final held-out results](T9_FINAL_HELDOUT_EVALUATION.md) evaluate the frozen
171,313-parameter HLS-only Conv-TasNet v2 on 225 prescribed conditions across
five heart and nine lung sources at five levels. The evaluation finished for
the exact four frozen methods with 900 rows and zero failures. Final model
Heart/Lung SI-SDRi was 1.849/2.333 dB (family-pair macro); Fixed Filter was
0.362/−2.447 dB and Generic NMF −2.466/−3.407 dB. These results describe this
controlled HLS-CMDS manikin/source-family test only; the test is consumed and
there is no post-test tuning or application integration in this checkpoint.

The preceding [pre-T9 model-comparison record](FINAL_PRE_T9_MODEL_EXECUTION.md)
remains the model-selection evidence: both treatments failed the unmodified
gate, so v2—not Treatment A—was frozen before T9.

[Frozen decision design and normative protocol](FINAL_MODEL_REPRESENTATION_REVIEW.md).

## Native HLS pilot complete, 29 September 2026 (preserved checkpoint)

**NATIVE FORENSICS COMPLETE / QUALIFIED WAVEFORM PILOT FAILED ADOPTION /
HLS-ONLY T8 V2 RETAINED / T9 SEALED / NOT DEPLOYED.**

[Native HLS audit and pilot](HLS_NATIVE_TRIPLETS.md) is the latest pre-test
checkpoint. Of145 triplets,45 were excluded without audio access. Of100
assessed,27 had strong same-time common-gain closure;26 remained after exact
deduplication. They add26 reference-file hashes, not new families or proven
patients. Their acquisition/generation process is not sufficiently documented
to claim new real-acoustic-mixture supervision. The other73 did not train.

One fixed-weight treatment completed five matched576-update family folds from
clean implementation `ff2f09e85f3bf67587015971d0ef20fcffdbb5f8`, seed20260928.
Heart/lung macro SI-SDRi was2.050/0.832dB versus2.013/1.913dB control;
Q fell1.082dB and balanced mean fell0.522dB. Only3/8pair means and2/5foldQ
scores improved; zero numerical failures. Severe Fine Crackles lung regressions
were finite negative transfer, not a demonstrated implementation defect.
All frozen gate clauses except numerical-failure protection failed.

No rescue tuning, native final refit, v3, additional seed or ensemble followed.
The existing v2 specification/checkpoint hashes below remain unchanged, with
v1 preserved. **READY FOR T9 WITH HLS-ONLY T8 V2**, pending separate owner
authorization. No T9 audio, recipes, metrics or results; no production,
application/frontend, demographic classifier or FYP1 changes.

## External-data pilot and HLS-only refit, 29 September 2026 (preserved checkpoint)

**EXTERNAL DATA QUALIFIED / EXTERNAL TRANSFER PILOT FAILED ADOPTION /
HLS-ONLY FINAL REFIT COMPLETE / REPLACEMENT T8 FROZEN /
T9 SEALED / NOT DEPLOYED.**

[External-data programme evidence](EXTERNAL_DATA_TRAINING.md) supersedes the
older next-step statements below. CirCor/SPRSound contributed qualified
imperfect Tier-B targets, not isolated clean references. The frozen pilot
trained for 2,304 updates and completed matched HLS non-test grouped-family
transfer evaluation. At the preselected 576-update HLS budget, macro heart/lung
SI-SDRi was 2.013/1.913 dB for HLS-only control versus 1.860/1.586 dB for external-
pretrained treatment; Q fell 0.328 dB. Only 3/8 family-pair balanced means and 1/5 fold
Q scores improved. The unchanged adoption gate failed despite zero numerical
failures. No full external scale-up, additional capacity variant or rescue
tuning was executed. Historical approximately 3.1 dB original-split performance
is not directly comparable to these broader held-out-family folds.

The qualified fallback then completed one fresh HLS-only refit on 45 heart/41 lung
non-test sources, seed 20260928, exactly 576 updates, 75.179 s, peak 1,012.695 MiB,
zero numerical failures. It started from clean implementation
`7eefa37100bb40d878d48b84b3811557ce98512b`; no external checkpoint or optimizer
state was loaded. Endpoint SHA-256:
`1f7e549ba53240bc085221e4eed1f935bb7c330e9a66cfab4c183c8f096c2658`.
This endpoint has not been assigned held-out performance or claimed superior
to original T8. The separate `final_separator_v2.json` anchors it and records
version 1 as superseded before T9, while preserving version 1 bytes, checkpoint
and provenance. New specification SHA-256:
`2573ae06b11aafc595a4cdb179e3ab0c9f7fbe37859863dcd36a5d8c70210b1b`.
Strict-load and synthetic-only shape/finite/consistency checks passed. The full
T9 protocol and inference behavior remain unchanged. READY FOR T9 WITH
ORIGINAL/HLS-ONLY T8 (version 2), pending separate execution authorization.

**T9 has not been opened or scored.** No application/frontend integration,
demographic input/classifier, production change or deployment occurred. FYP1
remains unchanged. Stop before T9 even after replacement-freeze completion.

## Pre-T9 diagnosis — 28 September 2026 (historical checkpoint)

**T8 PRESERVED / DIAGNOSIS COMPLETE / ONE INTERVENTION DESIGNED, NOT EXECUTED /
T9 SEALED / NOT DEPLOYED.** [Diagnosis and planned handoff](PRE_T9_PLATEAU_DIAGNOSIS.md)
supersede older next-step statements below. Data-limited generalization is the
most supported classification (medium confidence); no objective, dB scaling,
severe receptive-field or harmful-consistency defect was found. Family-held-out
budget qualification then one conditional all-non-test refit is planned, not run.
Zero optimizer updates this sprint; no test, application or production access.
T8 spec/checkpoint hashes remain unchanged. Stop for owner review before any
intervention and, separately, before T9. Historical findings remain preserved.

## Own-model training design — 28 September 2026 (historical design checkpoint)

**DESIGNED / NOT YET TRAINED / NOT YET EVALUATED.** The owner selected an
own-weight path independent of NeoSSNet author contact. [ADR T01](MODEL_TRAINING_DESIGN.md)
specifies compact fixed-label Conv-TasNet(645,681 parameters), scratch training,
CC-BY-4.0 HLS-CMDS sources, frozen family partitions, balanced additive mixtures,
loss/maximin-source validation selection, CPU settings and one locked final
evaluation. Only development-file statistics and tiny synthetic graph probes
ran, with **zero optimizer steps**. No validation/test audio access, new
automated tests or production changes. Graphify requested reauthentication;
known current files were read narrowly. Historical diagnostic/metric caveats
remain valid; the author-contact gate below is superseded **for our own model**,
not retrospectively satisfied. NeoSSNet stays research-only and50/50 stays
frozen/unqualified. Next: Luna T0–T4, then checkpoint.

## NeoSSNet reproducibility checkpoint — 27 September 2026

**DEVELOPMENT DIAGNOSTIC / NOT FINAL.** Current target-domain expert qualification
fails (Outcome D); native reproduction remains blocked by author data/run-artifact
availability. The table16.00/14.46 reference has a notebook improvement/aggregation
discrepancy and permutation-capable metric, not a matched absolute comparison.
Strict/eval/deterministic checkpoint checks pass; independent SI-SDR agrees.
Restored author positional encoding and fixed metric mutation/silence handling;
neither explains the large target deficit. Six rechecked +12 correlated manikin
protocol surrogates remain poor; no source swap, lag or gain change was adopted.
Two new tests, focused8/nearby regression15 passed. No training or application
integration. **Rights pending; native reproduction required before fine-tuning.**
See [current diagnosis](ENSEMBLE_DESIGN_AND_EVALUATION.md). This supersedes the
next-step guidance, not the historical scores or live M1 evidence, below.

**28 September follow-up:** author clarification remains **PREPARED / NOT SENT**.
Two research-only fallback candidates were identified (periodicity-informed
NMF/LingoNMF, MIT source; Grooby neonatal NMF/NMCF, GPL-3.0 source); neither is
selected or tested. Existing source-family split counts and locked test IDs are
documented; no audio was read and no training/evaluation was run. The detailed
status and risks are recorded in the implementation qualification note and the
workspace handoff.

## Ensemble Phase A–D offline checkpoint — 27 September 2026 (supersedes design-only status below)

**Implemented/tested offline, not integrated or deployed.** Released NeoSSNet
strict CPU checkpoint load and 10-s shape/finite inference passed; GPU untested.
All535 local HLS-CMDS WAVs match the official released 4-kHz PCM WAVs byte-for-byte;
the README's22.05-kHz description does not match the released files. A frozen
sound-type-family split and six exactly additive development mixtures were
manifested. Corrected centred STFT, raw expert adapters and fixed50/50 original-
mixture-phase fusion ran6/6 without shape/numerical failure. Focused tests:8
passed; one nearby ML regression pass:12 passed with pinned `vmdpy`. Mean SI-SDRi on the tiny development probe was
heart −3.22 dB, lung −10.20 dB for the ensemble: **no improvement shown**.
This is engineering qualification, not a held-out FYP finding. NeoSSNet license/
redistribution rights and its manikin source-label applicability remain unresolved.
Worker/API/frontend separation and final evaluation remain not implemented/not
evaluated. See [bounded evidence](ENSEMBLE_DESIGN_AND_EVALUATION.md) and the
implementation [offline qualification report](https://github.com/ASHRAF-2004/Machine-Learning-Based-System-for-Cardiopulmonary-Sound-Separation/blob/fyp2/application/docs/ENSEMBLE_OFFLINE_QUALIFICATION.md).
Production and submitted FYP1 remain unchanged.

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
