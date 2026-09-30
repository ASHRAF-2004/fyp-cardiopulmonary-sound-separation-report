# FYP2 requirements design code and evidence register

## Current UX design trace — local proof, 30 September 2026

| Requirement | Design → implementation | Evidence and boundary |
| --- | --- | --- |
| R15/R16 usability/visual identity | Seven laws → Frost Studio tokens/reusable shell → four isolated React screens | Seven final desktop/mobile/Midnight screenshots inspected, twelve focused UI groups and build pass; owner visual approval pending, not stakeholder feedback |
| R04/R05 low-friction capture | One New recording action → existing capture/upload contract in prepared handoff | Choice/layout designed; no new microphone/upload route or physical-device qualification claimed |
| R03/R11 privacy | Automatic protected media + abort/revoke + explicit scopes | Local401/403 presentation tests; existing backend/live private-media semantics unchanged; no new live qualification |
| R02/R12/R13 identity/access | Internal Firebase UID retained; local handle/public-ID/share prototypes | Actual server migration/handle resolver not implemented; exact grants/analyst/Admin privacy preserved |
| R07–R14 separation/evaluation | Frozen Conv-TasNet v2 and consumed T9 remain final | No model change, training, test reuse or fabricated per-recording accuracy |
| R17 deployment/recovery | Existing completed production release retained | Redesign not deployed; worker/private storage/backups/Axora untouched |
| R18 evidence integrity | Spec/law audit/visual references/five-axis review/compact hashes/Luna phases | Local proof and future service work distinguished; FYP1/history unchanged |

See [design review](UX_DESIGN_REVIEW.md) and the preserved production acceptance
addendum. This local design checkpoint does not reverse the completed production
deployment, and does not upgrade mock UI checks to live authorization evidence.

## Current final-model and local application trace — 29 September 2026

This supersedes proposed-ensemble and integration-pending rows for the local
branch. Historical requirements/negative results remain below; no FYP1 or
questionnaire record is rewritten.

| Requirement | Design → implementation | Actual evidence / remaining boundary |
| --- | --- | --- |
| R07/R08/R09 one request/method/failure | Frozen v2 → `app/m1/frozen_model.py`, unchanged inference | Exact hashes/171313 parameters/strict load; no substitute model; T9 separately complete |
| R10 nonblocking durability | Existing jobs/results+migration002 → `processing_store.py`, `worker.py` |202, transactional claim, uniqueness, exclusive lock, bounded recovery; local pass |
| R03/R11 private persistent outputs | Existing files/resources+protected media | Two finite60000-sample outputs, provenance, owner access/anonymous401/outsider403, restart/session persistence |
| R02/R12/R13 grants/review/admin privacy | Existing UID/status/role/owner/exact-grant policy | Explicit analyst metadata/audio pass; non-assigned/revoked denied; admin not privileged for private audio |
| R04/R05 record/upload | PCM validation+AudioWorklet→same API | Synthetic upload/fake microphone pass; physical hardware unverified |
| R14 valid evaluation | Pre-test choice→one-shot T9→immutable record | Heart/Lung SI-SDRi1.849/2.333dB,225 conditions, zero failures; no reuse/tuning |
| R15/R16 usability/visual identity | Existing components+live status/players | Five real-local browser groups and14 mock regression groups; owl/CSS/art unchanged; no clinical UAT |
| R17 deployment/resource/recovery | One CPU worker+opt-in Compose/runbook | Local15s inference0.035s, peak process560.914MiB; deployment NOT performed |
| R18 evidence integrity | Source/artifact hashes→chapter5/6/7 records | Training, non-test selection, final T9 and app acceptance separated; FYP1 preserved |

See [local integration](LOCAL_ML_INTEGRATION.md), [T9](T9_FINAL_HELDOUT_EVALUATION.md)
and [final model comparison](FINAL_PRE_T9_MODEL_EXECUTION.md).

## Historical representation/objective design — 29 September 2026

- R08/R09:390450-parameter complex-mask TF candidate and171313-parameter
  TCN+spectral objective defined; neither trained/selected as final. V2 preserved.
- R14: exact STFT/loss/lambda/initialization,576-update five-fold control reuse,
  adoption/ranking rules and conditional sole-endpoint refit predeclared.
  Analytical probes only,zero optimizer updates; no final-test claims.
- R10 application integration and all production/frontend work remain excluded.
  T9 sealed. See [final bounded model review](FINAL_MODEL_REPRESENTATION_REVIEW.md).

## Native HLS audit and bounded transfer result — 29 September 2026

- R08 source/expert validity:535-file release and145triplet mapping verified;
  45triplets conservatively sealed/excluded,100assessed,26deduplicated affine-
  additive triplets qualified. Exact reuse and a rejected cross-class label
  contradiction prevent blanket clean/native-reference claims. No new families.
- R14 reproducibility: committed protocol, fixed seed20260928/576updates,
  unchanged synthetic stream plus0.25-weight native waveform loss, five matched
  family folds/eightpairmeans. GateFAIL: ΔQ−1.082dB, ΔM−0.522dB, zero numerical
  failures. Artifact/recipe/hash/family guards verified; no rescue rerun.
- R08/R09 final separator: retain existing171313-parameter HLS-onlyv2; no v3,
  projection, fusion or model-selection change. R10 integration remains separate
  and unexecuted. T9 remains sealed; no production/frontend/FYP1 mutation.

Evidence: [native audit and completed pilot](HLS_NATIVE_TRIPLETS.md).
This updates the current ML checkpoint without rewriting earlier decisions.

## Reproduction qualification gate — 27 September 2026

- R08 expert validity: strict released-checkpoint execution verified; one source
  compatibility line restored. Target heart/lung qualification **fails**; code/
  weight rights and native fold/run correspondence remain unresolved.
- R14 trustworthy evaluation: independent fixed-label metric audited; float64
  mutation/undefined-silence defects fixed. Six old +12 new correlated development
  cases only. No PIT/data-dependent relabelling, held-out inspection, tuning or
  final result. Published table/notebook metric discrepancy recorded explicitly.
- R09 fusion remains0.5/0.5, not re-evaluated/tuned in this sprint. R10/application
  wiring remains on hold pending expert qualification; fine-tuning is not yet
  justified without native reproduction. Existing M1 requirements unchanged.

Evidence and next gate: [reproduction section](ENSEMBLE_DESIGN_AND_EVALUATION.md).

## Ensemble Phase A–D trace — 27 September 2026 (supersedes planned-only rows below)

| Requirement | Offline implementation/evidence | Remaining gate |
| --- | --- | --- |
| R07/R08 required experts | `app/ml/ensemble_v1.py`: released NeoSSNet strict CPU load and generic NMF raw adapters; one10-s smoke for NeoSSNet | Code/weight redistribution permission and robust source-label applicability unresolved. No production expert availability claim. |
| R09 fusion and failure | Centred periodic-Hann1024/256 STFT; fixed50/50 complementary masks on original mixture phase; one legacy boundary regression and fail-closed/overlap-focused checks | No worker-level deadline/restart/error persistence yet. |
| R14 evaluation | Six exact additive development mixtures from two source-family-separated pairs; per-source SI-SDR/SI-SDRi, hashed source/gain manifest; ensemble heart −3.22 dB/lung −10.20 dB mean SI-SDRi | Small non-independent qualification only; no improvement claim, VMD comparator, untouched held-out study or clinical generalisation. |
| R10/R03/R11/R12/R17 application, private results and runtime | Existing production M1 security unchanged; offline engine has no API/worker/output publication | Durable worker, protected derived results, resource qualification and separately reviewed deployment still planned. |

See [offline design/evaluation evidence](ENSEMBLE_DESIGN_AND_EVALUATION.md).

## Ensemble design trace — 27 September 2026 (planned implementation)

This updates only ensemble design/evaluation requirements, not completed live M1 evidence.
The [design and research record](ENSEMBLE_DESIGN_AND_EVALUATION.md) is authoritative
for this refinement; implementation ADR E01 supplies exact equations and interfaces.

| Requirement | Design → current/proposed code | Required evidence / present status |
| --- | --- | --- |
| R07 one ensemble request | Existing owner-only `app/m1/api.py` job POST → proposed two-expert engine | Designed; route still503, no runtime implementation. No user algorithm selector. |
| R08 expert provenance | Pinned original NeoSSNet + local NMF; new raw adapters reuse current DTOs | Code/artifact identity audited, NMF tiny execution only; permission/NeoSSNet loadability conditional. Missing fine-tune and complete literature hybrids excluded. |
| R09 compatible fusion/failure | Boundary-safe common STFT → fixed complementary masks → shared-gain exports | Designed; legacy first-sample loss observed offline. Round-trip/finite/label/length and two-expert failure checks belong to implementation. |
| R10 non-blocking processing | Existing `m1_jobs` + additive migration → single supervised worker | Planned; require atomic claim, interrupted-job state and API responsiveness. No duplicate legacy job database. |
| R03/R11/R12 protected results | Existing result/file/resource tables → staged atomic publication, exact grants | Existing original-media evidence remains valid; generated-output grant/revoke/restart checks not yet available. |
| R14 valid evaluation | Source-family split → controlled sums → same-pipeline per-source SI-SDR/SI-SDRi | Planned; local4k lineage/splits unresolved. Three recorded triples fail additive-reference probe; historical23-record scores not comparable evidence. |
| R17 resource/backup safety | Future isolated worker → existing runtime and backup quiescence | Planned; CPU RSS/time measurement and all-writer backup quiescence required before a separately approved release. Production unchanged. |

## Current production trace — 27 September 2026

R01/R02 → Firebase password-provider identity + application session onboarding →
live auth UI and `/api/auth/session`, `/api/auth/me` → same verified UID, default
Staff, refresh/logout/login, real recovery request, old-password denial and
owner-entered new-password success. Registration click and verification-email
delivery remain owner-reported; verified state is provider-confirmed.
R02/R12/R13 → confirmed Admin role update + exact-resource grant/review policy →
`/api/admin/users/{id}`, `/api/recordings/{id}/grants`, `/api/assignments/{id}/review`,
`/api/grants/{id}` → production Analyst promotion/audit, fresh-login persistence,
Admin403, scoped original-media/review200, unrelated-record403, revocation403 and
retained history. No generated result/derived-media acceptance is inferred.

R01/R02/R13 → JWT + Firebase REST current-account check → `app/m1/` identity and
trusted account/role policy → real public Admin 200 / Staff 403 and matching UIDs.
R03/R11 → private storage/owner-grant policy → recording/media API → public
owner 200 / cross-owner (including Admin) 403 / anonymous 401 and matching bytes.
R17 → isolated Compose/Tunnel + encrypted B2 → `implementation/deploy/` →
HTTPS/SPA/health, restart persistence, first production snapshot and healthy
unchanged Axora. Exact versions, boundaries and remaining gaps:
[production evidence](PRODUCTION_DEPLOYMENT_EVIDENCE.md). This supersedes older
pending-production/Cloud Run status below, without changing historical requirements
or reclassifying local/mock evidence as production.

## Production identity decision update — 27 September 2026

The Cloud Run verifier path was superseded before deployment because Google
Cloud billing requires an unavailable MYR 120 prepayment. Active planned
architecture: FastAPI local Firebase JWT verification, token-authenticated
Firebase Auth REST `accounts:lookup`, then trusted local role/ownership/grant
authorization. Focused local tests pass and a restricted Identity Toolkit key
reached the endpoint with a deliberately invalid token; real-account current
user/revocation checks remain pending. No Google Cloud billing or production
service was created. Do not treat historical Cloud Run notes below as current.

M1 synchronization: 26 September 2026. Paths beginning `implementation/` are relative to the parent StethoFuse workspace; source report paths are relative to the documentation repository. R01-R18 retain the initial FYP2 summary history, not replacements for submitted F1-F15 / NF1-NF8 / UR1-UR8 / UC01-UC10. All 52 continuation-pack requirement IDs and their summary/historical relationships are in [requirements history](REQUIREMENTS_HISTORY.md).

Use only the feature-status vocabulary **implemented**, **integrated**, **tested**, **verified live**, **planned**, **simulated**, **blocked**, with definitions in [status conventions](STATUS_AND_EVIDENCE.md). Prior “code present”, “demo” and “recorded test” wording below describes the preserved M0 snapshot; it maps respectively to implemented, simulated and tested-with-original-date, not live acceptance. Approval is a separate decision, and unverified means missing evidence rather than an extra completion status.

The table preserves the **pre-M1 baseline** so route migrations do not erase their reason or history. The current M1 design/code/configuration/version/test/environment/evidence record is [M1 implementation and test notes](M1_IMPLEMENTATION_AND_TEST_NOTES.md). Where a baseline says a route was unscoped or an adapter unavailable, it is not a claim about later concurrent M1 code. No M1 integration is accepted solely because a worker or contract file says it is planned.

## Current M1 changes, separate from the baseline

| Summary requirements | Current code/design evidence | Accepted test boundary |
| --- | --- | --- |
| R01-R04, R06, R11-R13 | Protected `app/main.py` / `app/m1/`, trusted bootstrap CLI and canonical live frontend Firebase/API/provider path `implemented` and `integrated`; legacy private aliases retired | Historical local tests: 86 backend cases + 26 subtests, 14 mocked-auth browser checks, seven client checks and six real-local-API cross-layer checks. Identity seams in those tests remain `simulated`; subsequent genuine provider/operator progress is recorded separately below. No privileged email rule or implicit admin media access. |
| R01, R13; R-AUTH-06, R-ROLE-01,03-04 | Restricted keyless backend ADC completed/read-tested; user-reported Google app login corroborated by official provider lookup and existing matching verified local default-staff account; authorized first-admin CLI applied | `verified live` only for the stated ADC/provider-read/trusted-bootstrap operations: independent provider/store admin check, unchanged retry, one active admin and one bootstrap audit event. No real application-user token extracted; post-promotion browser/API and wider real-provider cases remain pending. Separate focused local rerun: coordinator reports 22 cases + 21 subtests passed, 64 deselected, existing Starlette warning; not added to prior totals. See [bounded evidence](M1_IMPLEMENTATION_AND_TEST_NOTES.md#primary-admin-operation-and-bounded-live-evidence--26-september-2026). |
| R13; R-ROLE-03-05, R-ADM-01-03,05 | Historical commit `3d95270` used current-provider exact-target lookups. Superseding design in the current `fyp2/application` worktree removes the arbitrary UID lookup API: only an existing locally provider-verified target may be promoted, and each target's later API use still requires its own live token to pass the Cloud Run revocation/current-user verifier. Local role/status/audit updates remain transactional and last-active-admin protection remains. | Historical full backend run `tested` with simulated identity/provider outcomes: **99 cases + 26 subtests passed** (artifact and limits remain recorded below); that run does not test the new Cloud Run boundary. New verifier/role tests are `simulated`/controlled-local and must be rerun after the current work stabilizes. Live deployment/provider verification remains `planned`. |
| R05, R07-R10, R14 | Capture hardware, ensemble/expert fidelity, persistent executor and measured evaluation remain `planned`; processing/benchmark unavailability is explicit | A tested 503 or demo synthetic output does not implement separation. Physical-device, method, dataset and quality evidence is still required. |
| R15-R16 | Approved styling/owl preserved; explicit demo kept separate from live-default runtime | Separate `tested` regressions: 16 simulated workflows, five actual public-homepage and six owl checks; 1,282 selected protected files match the pre-M1 checkpoint. Not target-user UAT or blanket visual/accessibility approval. |
| R17-R18 | Confirmed StethoFuse hostname, seven-chapter report structure, requirement history and separate evidence provenance | The isolated Compose runtime remains locally tested historically. Current production identity design is a self-hosted API with local Firebase JWT checks plus an unprovisioned minimal Cloud Run current-user/revocation service; no production IAM/service write occurred. Backblaze B2 + Restic S3 is approved but no account/bucket/key/repository exists and no remote restore has been tested. Production is `planned`; no DNS/tunnel/Caddy/Firebase-domain/service deployment. 217 original report files remain the preservation baseline; current university term/rubric/template and feedback evidence remain open. See [production identity/backup decision](../../planning/PRODUCTION_IDENTITY_AND_BACKUP.md). |

### Current production ML continuation — 29 September 2026

The dated 27 September production/M1 baseline above remains historical. Its
production status statements are superseded only for the already-authorized
frozen ML continuation by
[production ML acceptance evidence](PRODUCTION_DEPLOYMENT_EVIDENCE.md#production-ml-deployment-and-focused-acceptance--29-september-2026):
the unchanged final T8 v2 maps to the M1 durable job/result/resource tables;
the owner-only request creates/reuses a persisted job; one CPU worker verifies
and loads the frozen checkpoint, writes private Heart/Lung resources and records
provenance; protected endpoints use the existing owner/exact-grant semantics.
The acceptance recording was synthetic and non-patient. Owner, anonymous,
assigned Analyst, exact Heart scope, post-revocation Analyst, and Admin-without-
grant outcomes were observed through production Firebase sessions. A mistyped
recipient ID caused the initial correct `403`; the verified recipient ID then
created the exact Heart grant. No code/policy change was needed. Post-acceptance
Restic/B2 snapshot and isolated restore checks passed, including SQLite
integrity and both model artifact hashes. This closes the production separation
and backup acceptance trace for the deployed system; it does not establish
clinical effectiveness, patient-level generalization or physical-device
qualification. Axora's existing public root remained `200` and its services
were untouched.

### Confirmed account provisioning and use-case actors

The user confirmed that an existing admin may promote accounts. R-AUTH-07 and R-ROLE-01 therefore remain unchanged: public verified onboarding creates `healthcare_staff`, never a self-selected analyst/admin. R-ROLE-02 permits admin-assigned `audio_analyst`. R-ROLE-03 distinguishes the trusted first-admin bootstrap from subsequent authenticated, confirmed and audited admin promotion. Sign-in uses the shared Firebase flow and retrieves the persisted role; it does not confer a new privileged role. This agrees with the current backend/API and live admin UI, so no operator-only restriction is asserted.

The latest R-ROLE/R-ADM clarification requires backend enforcement, audit, existing verified target accounts and last-active-admin protection for promotion/demotion. Earlier current-provider exact-target checks and their transactional local verified-target test remain historical. The current design does not call Cloud Run with an arbitrary target UID: it requires an existing locally provider-verified account; future API use of that account independently verifies its own live ID token, revocation and provider state before local permissions are applied. Cloud Run itself has no app-role authority. The earlier 99-case/26-subtest run used simulated provider outcomes and does not test the new verifier boundary. Genuine live promotion and verifier deployment acceptance remain gaps. See the [roles and account-provisioning guide](../../implementation/docs/ROLES_AND_ACCOUNT_PROVISIONING.md) and the [dated M1 identity/backup addendum](M1_IMPLEMENTATION_AND_TEST_NOTES.md#current-production-identity-and-backup-design--27-september-2026).

Application human actors are **Healthcare Staff**, **Audio Analyst** and **Administrator**. Staff manage their own authorized workspace; analysts additionally review exact active assignments; admins manage permitted account/operational metadata without automatic private-audio or analyst-review access. Firebase is a supporting external identity actor; the trusted developer/operator is an operational setup/bootstrap actor, not a public fourth role. A signed-out visitor is an authentication state. See [the role/use-case mapping](M1_IMPLEMENTATION_AND_TEST_NOTES.md#confirmed-signup-sign-in-and-actor-policy). Preserve the submitted FYP1 staff/analyst actors and original use-case identifiers; these explicit administration/provider/operator boundaries are a dated FYP2 refinement, not a rewrite of FYP1.

Self-management policy is now explicit: the current admin is read-only in User
Management (`403` for self role/status changes), while another verified account may be
promoted/demoted under audit and last-active-admin protection. The UI compares each row
with the backend-authoritative Firebase UID and refreshes `/me` and the user list after
changes. See the editable [role/use-case diagram source](design/role-use-cases.mmd).
The FYP2 design set also includes the current M1 [system architecture](design/m1-system-architecture.mmd)
and [deployment topology](design/deployment-topology.mmd), which labels observed Axora routing
separately from the unconfigured StethoFuse production route.

Latest real-provider acceptance (27 September 2026): existing verified Google sessions for
the primary Administrator and ordinary Healthcare Staff resolved through Firebase and
FastAPI to their authoritative backend roles. Admin Users returned `200` to Administrator
and `403` to Staff. A synthetic silent WAV was owner-readable; direct recording metadata,
media and download returned `403` to Staff without a grant, `200` after a single-resource
read grant, and `403` again after revocation. In the reverse direction, Admin received
`403` for Staff-owned synthetic recording metadata/media/download, and the item was absent
from Admin's recording list. This was **REAL FIREBASE + LOCAL BACKEND**, not production.
The Staff session also received `403` for a forged role-change request and
`401` after logout when calling `/api/auth/me` without a token. Email/password, recovery,
live analyst review, results/derived-artifact media, and production access remain untested.

## Preserved pre-M1 baseline

| ID and source | Requirement and design location | Baseline code or artifact | Pre-M1 evidence and continuing acceptance gate |
| --- | --- | --- | --- |
| R01 Identity; latest user / pack D07-D08, AC01-03 | Firebase email/password and Google identity; backend resolves stable UID to local user/status/role. Outline 3.4, 4.6, 5.3. | `implementation/frontend/src/data/adapters.ts`; auth forms in `src/pages/PublicPages.tsx` | Demo/unavailable provider adapter, not live auth. Prove sign-in, sign-out, linking, recovery/verification, expired/replayed action states and disabled-user handling with authorized test accounts. No public privileged-role assignment. |
| R02 Server authorization; pack D09-D11, AC04,09,11 | Every list/detail/media/mutation checks identity, role, owner or active grant. Outline 3.6, 4.6, 6.3. | Demo `src/data/store.tsx:canAccess`; legacy `app/routers/results.py`, `database/schema.sql` | Client scoping exists; legacy API has no account-aware enforcement. Backend access preparation may be added separately but is not integrated evidence. Prove direct API/URL denial for Staff B, analyst and admin without grants, not merely hidden controls. |
| R03 Persistent originals and outputs; F2,F14,NF7 / AC05,08 | Own-server SQLite metadata and private files survive sessions/restart; original preserved, each retry/reprocess gets a distinct run. Outline 4.8, 5.4, 6.4. | `app/services/storage_service.py`, legacy `separation_service.py`; demo metadata in `localStorage` | Legacy file/metadata code present; no owner model in inspected schema. Demonstrate cross-browser sign-in and process restart with unchanged original hashes and retrievable authorized outputs. Retention/deletion/restore policy must be agreed. |
| R04 Recording context and WAV validation; F1-F3 / UC01-02 / AC13 | Validate type/header/readability/size/audio attributes before saving/processing. Outline 3.4, 4.4, 5.4. | `src/pages/WorkspacePages.tsx`; `app/services/audio_validation.py`; `tests/test_upload.py` | Local UI validation recorded in demo workflows. Backend tests exist but were not run here. Add malformed/truncated/oversize cases and server-side validation with real owner attachment. |
| R05 Physical capture; pack D12 / AC13 | Compatible laptop-connected digital stethoscope capture joins the same intake path. Outline 4.4, 5.4. | `WorkspacePages.tsx:DeviceRecording` | Demo simulator only. Hardware/browser/OS and permissions remain unselected/unverified. Prove source selection, start/stop, disconnection, silence and saved WAV integrity on named actual equipment. |
| R06 Own list and shared list; F4-F5 / UC03 / AC04 | Search/filter only scoped own records; separately show explicitly shared/assigned items. Outline 3.4, 4.3. | `WorkspacePages.tsx:RecordingList,Shared`; legacy `/history` | Demo and recorded fixture isolation tests. Legacy history is global. API must scope before pagination/search and resist guessed IDs; verify totals do not leak other accounts' data. |
| R07 One ensemble request; F7-F8,UR4-UR5,UC04-05 superseded / D04-06,AC06 | Ordinary users request the configured ensemble, not a method chooser; internal baselines retained. Outline 4.7, 5.5-5.6. | Demo `store.tsx:startJob`; legacy `app/routers/separation.py` and `app/ml/strategy_factory.py` | Demo timer and legacy individual-strategy path are separate; neither establishes ensemble inference. Verify request contract, immutable version/membership and actual expert/fusion execution. FL excluded. |
| R08 Expert provenance; F6-F10 / pack06 | Include only verified, compatible expert adapters. Outline 2.4-2.5, 4.7. | `app/ml/neossnet_strategy.py`, `app/ml/strategies/{fixed_filter,nmf,vmd}_strategy.py`; [method register](provenance/METHOD_ATTRIBUTION.md) | Code present; checkpoint identity, paper fidelity and proposed NMF/NMCF/DAE-NMF-VMD correspondence unverified. Approve code/license/checkpoint/config hashes and deviations before reporting a named reproduction. |
| R09 Fusion and failure; pack06 / AC15 | Resolve timing, source order, sample rate, length, scale, residual and missing-expert policy. Outline 4.7.3-4.7.5. | Proposed architecture and frontend run metadata contracts | Planned. First evaluate fixed weights chosen on training/validation only. Do not silently label a single-expert fallback full ensemble success. Adaptive weights require inference-time features and separate validation. |
| R10 Non-blocking job state; F11,NF2-NF3 / UC06 / AC07-08 | Stages and errors reflect service truth; navigation does not cancel work; retry preserves history. Outline 4.4, 5.5, 6.4. | `app/routers/separation.py` background option; `app/services/separation_service.py`; demo job state | Legacy background-task code present; persistent worker/restart behavior unverified. Prove failure/retry/cancellation, restart recovery and honest partial states. No made-up progress percentage. |
| R11 Audio/result access; F9-F13 / UC07-08 / AC14 | Authorized originals and correct run outputs, waveform/spectrogram/download. Outline 4.9, 5.4. | `src/components/AudioWorkbench.tsx`; `app/routers/results.py`; `/visualizations` mount in `app/main.py` | Browser audio is synthetic demo; legacy downloads/static visualizations are not account-protected. Test permission checks on every artifact, range/download path and post-revocation request. |
| R12 Sharing and review; latest user / D11 / AC09 | Explicit owner grant, analyst-only review within active assignment, revocation and retained authorship/history. Outline 4.3, 4.8-4.9, 5.7. | `WorkspacePages.tsx:AssignForm,Shared,AnalystList,ReviewWorkspace`; demo store | Demo and recorded browser grant/revoke/reassignment tests. Prove backend transaction semantics, stale links, wrong recipient, role changes and author preservation. Shared recording/result access must not expose owner-only processing jobs. |
| R13 Safe administration; D09 / AC10-11 | User ID search and audited role/status changes; no implicit audio access, passwords, reset codes or impersonation. Outline 3.6, 4.6, 5.7. | `src/pages/AccountPages.tsx`; demo store | Recorded admin fixture checks, not production enforcement. Prove privileged endpoint denial, last-active-admin safeguards, audit payload minimization and no private-media escalation. |
| R14 Valid evaluation; F15 / UC10 / AC15-16 | Separate heart/lung reference-based measurements from qualitative review and operational metadata. Outline 2.7, 6.6. | `app/services/evaluation_service.py`; `tests/test_evaluation_service.py`; evaluation scripts | Existing reference/metric code present; no new evaluation run. Verify reference-pair identity, split, alignment convention, metric definitions and run manifest before using any scores. Missing reference means unavailable, not inferred accuracy. |
| R15 Usability and accessibility; NF1-NF2 / AC12,18 | Responsive/keyboard/reduced-motion routes, honest unavailable provider states and usable feedback. Outline 4.10, 6.5. | `src/components/ui.tsx`, pages, `frontend/tests/`; route map | Prior isolated Chrome fixture results inspected. These are not physical-device tests, a full accessibility certification or UAT with target professionals. Record named conditions and defects. |
| R16 Approved owl; latest user / AC17-18 | Preserve the approved animation; its acceptance is not a new gate blocking other preparation. Outline 5.2, 6.5. | `frontend/PAUSE_NOTES.md`, owl component/renderers and preserved evidence | User approval explicitly recorded; focused prior animation evidence exists. Do not change owl assets/controller here or confuse earlier rejected candidates' test results with final visual approval. |
| R17 Deployment and recovery; latest user / D14,AC05 | Own server, protected audio, same-origin `/api` plan, safe origin/provider configuration and backup/restore. Outline 4.11, 5.8-5.9, 6.7. | Continuation pack05; `implementation/deploy/` runtime; `planning/PRODUCTION_RUNTIME_PROPOSAL.md`; `implementation/deploy/BACKUP_B2_RUNBOOK.md` | Local production-like package `implemented` and `tested` (27 Sep 2026): Compose frontend/API, same-origin proxy, isolated SQLite/private mounts, tokenless 401 and restart persistence. `tested`: real encrypted B2/Restic synthetic remote snapshot/restore on 27 Sep 2026; Restic check clean, restored SQLite integrity `ok`, manifest/file-set/byte comparisons passed. Independent offline-paper-password recovery unlocked the same repository and restored a known synthetic file with matching SHA-256; escrow recovery is verified. This does not prove scheduled or live-application backup. Production remains `planned`: isolated StethoFuse tunnel preferred; no production DNS/tunnel/Caddy/Firebase-domain/service write. Cloud Run verifier/IAM remain unprovisioned; production service identity, live HTTPS/provider checks, first application-data backup, scheduled retention rollout and deployment rollback proof remain outstanding. Submitted FYP1 remains unchanged. |
| R18 Academic and evidence integrity; AC19-20 | Registered title preserved; original survey/submission unchanged; implementation, measurement and approval kept distinct. Outline all chapters. | Baseline manifest; revised DOCX/PDF; source register | 217-file historical baseline recorded. Verify SHA256 manifest after each preparation pass. Obtain current-term rubric/scope decisions and genuine FYP2 meeting/similarity records before submission. |

## Existing evidence that may be cited with limits

`implementation/frontend/evidence/reference-match/functional/README.md` reports 69 passed, zero failed checks on 24 September 2026 in isolated, fictional headless Chrome contexts. The workflow JSON contains 16 named passes and no failures; the admin JSON records individual checks. These artifacts were read in this preparation, not rerun. The report distinguishes a mobile visual issue and the later five-case rerun. Do not add these counts to overlapping older suites as a unique grand total.

`frontend/PAUSE_NOTES.md` records subsequent public/authentication and homepage work through 25 September. Figures must identify the relevant build/checkpoint and route/persona, not imply all captures came from one synchronized final release. Repository tests being present is not a pass result.

No backend tests, provider calls, physical recording, training, ensemble benchmark, DNS change or deployment were performed by this documentation task.

The separately inspected 26 September M0 foundation run contains 38 testcase elements plus 26 subtests (JUnit aggregate 64), zero failures/errors. It proves the isolated policy/SDK-mock and database-smoke conditions only. The [M1 ledger](M1_IMPLEMENTATION_AND_TEST_NOTES.md) separates that prior evidence from new API/client tests, real Firebase and production checks. No new user study or post-deployment feedback has occurred.

## Minimum evidence record for each new claim

Record requirement ID; implemented scope and deviations; code commit plus hashes for untracked work; command/test case; UTC date; environment/browser/device; input fixture or authorized dataset manifest; expected and actual outcome; pass/fail/blocked status; artifact path; reviewer/approval where relevant. Never include credentials, recovery links, patient identifiers or private audio in report evidence.

For model results, also record dataset version/license, split/group membership, reference mapping, preprocessing and alignment, seed, exact method/checkpoint/configuration hashes, fusion weights and where fitted, heart/lung metrics separately, runtime/hardware, failures/exclusions and limitations. A missing item stays a gap rather than being filled from assumption.
