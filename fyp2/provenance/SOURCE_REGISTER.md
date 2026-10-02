# FYP2 source register and unresolved guidance

M1 source synchronization dated 26 September 2026. Documentation sources below are repository-relative unless stated otherwise. This register identifies what each source can support; it does not promote a plan, contract or README into independent experimental evidence. See [M1 source audit](M1_SOURCE_AUDIT.md) for the fresh guideline/DOCX/PDF checks and [M1 evidence notes](../M1_IMPLEMENTATION_AND_TEST_NOTES.md) for evolving implementation status.

## Source hierarchy

1. Latest explicit user decisions govern the requested product direction and approvals.
2. Current applicable university/supervisor instructions govern academic scope and submission requirements; the local T2610 handbook and continuation pack confirm the application-based seven-chapter structure. Current FYP2 rubric/template/term instructions still need reconciliation.
3. Submitted revised PDF/DOCX establish what FYP1 actually contained.
4. Original questionnaire, literature records, primary papers and diagram sources establish their respective evidence.
5. Inspected code and dated test artifacts establish narrowly scoped implementation/test facts.
6. The architecture pack and this preparation describe planned changes, not completed integrations.

## Sources inspected

| ID | Source and locator | Use and boundary |
| --- | --- | --- |
| S01 | `report/Submission/1221303805_Arshad_Jamal_FYP1_Report.pdf`; 104 pages | Authoritative submitted PDF. Cover/title, contents vii-x, requirement tables pp. 28-30, use cases/design pp. 31-49 and implementation plan pp. 50-55 inspected by text extraction; contents page ix rendered and visually checked. This was not a full 104-page layout review. |
| S02 | `report/Submission/1221303805_Arshad_Jamal_FYP1_Revised_Copy.docx` | Authoritative editable revised submission. OOXML headings checked against PDF; 45 embedded media files counted. Read without rewriting/exporting. |
| S03 | `proposal/FYP-Proposal-Form.pdf`, page 1 | Proposal title includes “Development of a”; Application-Based / Software Engineering / Application Software / Prototype-Proof of Concept classification. No title change approved here. |
| S04 | `resources/guidelines/FYP Handbook T2610.pdf`, sections 2, 3.5, 4 and 5 | FYP2 application-based seven-chapter structure confirmed; preliminary material, logs, formatting/caption and APA guidance. All extracted text read, page 14 rendered and visually checked again for M1. The file is a 32-page April 2026 handbook. Reconcile specific internal inconsistencies and current eBwise requirements. |
| S05 | `README.md`, `report/quarto/README.md`, `_quarto.yml`, scripts | Explicit warning that Quarto is older/unsynchronized. Historical revision workflow is DOCX transformation followed by Word field update/export; generation scripts were inspected, not run. |
| S06 | `report/questionnaire/User Requirements Questionnaire for Machine Learning-Based Cardiopulmonary Sound Separation System.csv`; submitted 3.2.13 | CSV parsed read-only: 53 data rows, 25 columns. Existing report explicitly notes underrepresentation of target healthcare roles. No respondent data copied into new preparation files. |
| S07 | `literature-review/prisma/prisma_counts.json`, `chapter_2_synthesis_selection`; screening/metadata folders | Existing synthesis records 96 considered, 47 excluded, 49 eligible and 35 selected/cited. Nested historical counts refer to different phases; do not flatten them or change old totals as part of preparation. |
| S08 | `report/revisions/verified_references.bib`; `literature-review/references/references.bib` | Revised and broader bibliographies are distinct. Selected candidate entries compared with local primary-paper first pages. No blanket fresh metadata verification. |
| S09 | Local NeoSSNet, Torabi NMF, Grooby NMF/NMCF and Sun DAE-NMF-VMD PDFs | Narrow bibliographic/method-identification support; see [method register](METHOD_ATTRIBUTION.md). Full method reproduction, licenses/code/checkpoints and effectiveness remain open. |
| S10 | `diagrams/plantuml/*.puml`, `diagrams/mermaid/audio_processing_workflow.mmd`; report figure folders | Editable historical diagram sources exist. Inspected component/class/use-case sources already show staff/analyst and the legacy individual-strategy design. Preserve originals; future FYP2 diagrams must be separate and versioned. |
| S11 | `../planning/source-plans/StethoFuse_Architecture_and_Agreed_Plan/00_MASTER_PLAN.md` and numbered sections 01-12, especially 05,06,09,10 | Target architecture and earlier decision record. Some report section numbers and actor descriptions predate the submitted revision. Hostname and owl approval are superseded by newer conversation evidence. |
| S12 | Current user instructions and continuation pack; historical `../implementation/frontend/PAUSE_NOTES.md` | Firebase plus backend roles; own-server persistent accounts/audio; EL not FL; unchanged supplied academic title; owl approval “Animation is Done”; final hostname confirmed StethoFuse. Intended primary-admin email is not a UID/privilege rule. This is decision provenance, not a deployment test. |
| S13 | Pre-M1 `../implementation/frontend/src/data/adapters.ts`, `store.tsx`, pages and `FRONTEND_INTEGRATION.md` | Historical working demo UI; initial live auth/data methods unavailable, fictional metadata/synthetic audio/simulated jobs. Current M1 adapter evidence is tracked separately in M1 notes; client checks are not backend security. |
| S14 | Pre-M1 `../implementation/app/main.py`, `app/routers/{separation,results}.py`, `database/schema.sql`, ML/evaluation paths | Historical legacy workflow lacked account-scoped result/download/history/static protection. This is the migration baseline, not a timeless description of concurrently edited M1 routes. Current route inventory/test evidence is tracked in M1 notes. |
| S15 | `../implementation/frontend/evidence/reference-match/functional/README.md`, workflow/admin JSON; frontend checkpoints | Dated, scoped prior fixture tests. No suite rerun for this documentation task; no extrapolation to real auth, clinical quality or deployment. |
| S16 | [Official Quarto single-user tarball instructions](https://quarto.org/docs/download/tarball.html), [stable v1.10.18 release](https://github.com/quarto-dev/quarto-cli/releases/tag/v1.10.18), [official download manifest](https://quarto.org/docs/download/_download.json) and published checksum asset; inspected 2026-09-26 | Provenance for the separately authorized project-local portable tool setup. Supports tool version/download integrity, not academic report content. See [exact hashes, commands and HTML-only checks](QUARTO_SETUP.md). |
| S17 | `resources/guidelines/CPT6314 Teaching Plan T2610 v1.pdf`, all three pages | Explicitly Final Year Project 1/CPT6314; FYP1 schedule only. Internal/confidential source inspected locally, not externally published. Not FYP2 deadline/assessment authority. |
| S18 | `resources/guidelines/FYP1 Rubrics.pdf`, all extracted rubric text | FYP1 management, analysis/design, document and oral/prototype criteria. Does not replace a missing current FYP2 rubric. |
| S19 | `../planning/source-plans/StethoFuse_Continuation_Pack_2026-09-26/08_CODEX_CONTINUE_FROM_CHECKPOINT.md`, 00-07 and manifest, all read | Current M1 scope/decisions, 52 granular IDs, status vocabulary, seven-chapter structure, identity/bootstrap and deployment boundaries. Preserved source; not proof those requirements have been implemented. |
| S20 | `../implementation/docs/ACCESS_FOUNDATION*.md`, foundation tests and `../.local/workspace-preparation/access-and-database-tests.xml` | Pre-M1 harness and mock-SDK behavior, 38 cases plus 26 subtests passed in the retained run. Not route-level or real-provider evidence. |
| S21 | `../planning/M1_PROVIDER_AND_ROUTING_STATUS.md`, coordinator read-only M1 inventory | Selected Firebase project has no Web Apps and uninitialized Auth/Get started; CLI has no account. Providers/domains/actions are not configured/verified. Observed Caddy/cloudflared containers are unrelated Axora services, not a proven StethoFuse route. Protected configuration access is a later routing gate. |
| S22 | Current `../implementation/app/m1/`, protected `app/main.py`, `scripts/bootstrap_m1_admin.py`, M1 route audit/contract, API/foundation/operator-safety tests; `../.local/m1-tests/backend-final-junit.xml` | Inspected local implementation and final 86-case + 26-subtest run. Actual temporary storage/HTTP, injected identities and mocked official SDK; no real provider/admin mutation. Legacy aliases are retired and private static mount removed; legacy source on disk must not be remounted. |
| S23 | Current frontend runtime/Firebase/API/live-provider source and `tests/m1/`; `../implementation/frontend/output/playwright/m1/` final artifacts | 14 mocked-auth browser, seven actual-client/mock-transport and six actual-local-API/mock-identity checks passed; final build reported passed. Separate explicit-demo regression suites and 1,282-file preservation check passed. Source/artifacts inspected and two cross-layer screenshots visually reviewed; evidence does not establish real Firebase or production. See exact paths/dates and retained failed harness runs in [M1 notes](../M1_IMPLEMENTATION_AND_TEST_NOTES.md). |

## Reconciliation log

| Conflict | Preparation resolution |
| --- | --- |
| Pack10 describes single actor and maps storage to 4.5.3; submitted revision already has two roles and added algorithm section | Use submitted S01/S02 headings: storage 4.5.4; model-selection strategy 4.5.3.5. Keep pack unchanged as historical input. |
| Earlier pack says NF5 avoids server storage | Revised NF5 instead minimizes identifying information and limits file access to the local workflow. New private persistent storage is an extension; do not misquote submitted NF5. |
| Six chapters in FYP1 versus discussion of evaluation in Chapter 6 | S04/S19 confirm FYP2 Implementation / Testing / Conclusion as chapters 5/6/7. Structure is settled; current rubric/template remains to reconcile. |
| Restored Quarto versus submitted revision | Submitted DOCX/PDF control content. No automatic regeneration or overwrite from older QMD. |
| Pack owl-first pause versus later user approval | Gate satisfied by explicit user approval recorded in S12; preserve current owl. Prior rejected renderers' PASS logs do not supersede approval. |
| Older pack `hearme.ashraf-alsaloul.com` versus continuation `stethofuse.ashraf-alsaloul.com` | Resolved by S19: final target is StethoFuse. Older target remains historical. No production verification follows from that decision. |
| Demo persistence versus persistent own-server target | Browser fixture storage is demo behavior only. M1 now tests real local SQLite/private WAV persistence with fictional identities; genuine-provider accounts, actual server restart/recovery and deployment remain separate gates. |
| Baseline NMF/VMD and NeoSSNet adapter versus three verified ensemble experts | Preserve reusable code; do not assert paper correspondence, complete DAE-NMF-VMD or real fusion from class names. |
| Proposal title versus submitted cover title | S19 confirms unchanged title matching the submitted cover. Preserve the proposal wording historically; do not reopen the decision or substitute product brand. |

## Exact university guidance still needed

- Current CPT6324/FYP2 rubric, teaching plan, term and eBwise submission/deadline instructions. The seven-chapter structure is confirmed; the local separate rubric and teaching plan are FYP1-specific and are not relabeled FYP2.
- Current final-report template, page-size policy and final naming convention. The submitted PDF is Letter; the handbook PDF itself is A4, which alone does not prescribe report paper size. Its cover margin guidance and body margins differ; confirm intended layout before a new final export.
- Supervisor confirmation of formal objective/method/scope changes, including ensemble research and persistent multi-user functionality. Development instructions are not university approval.
- Current supervisor-name/cover field format and final submission identifiers; the supplied official academic title is already confirmed unchanged.
- Genuine FYP2 meeting logs and current similarity report. Local handbook section 3.5 specifies at least six logs and an overall similarity threshold of at most 20%; confirm current-term requirements rather than fabricate these artifacts.
- Appendix numbering/preliminary-page interpretation: the handbook repeats Appendix B and lists Abstract twice in its suggested order. Resolve with current template/supervisor; do not reproduce obvious ambiguity as a new final layout.
- Assessment-weight inconsistencies: handbook p.5 lists FYP2 poster presentation at 10%, while p.6 labels it 20% but lists parts totaling 10%. The FYP1 teaching plan also differs from the handbook on FYP1 weightings. The current FYP2 rubric must resolve these; no grading scheme is invented here.
- Appropriate approval, recruitment, consent/data-handling process for any new target-user consultation or human recordings. No new consultation, clinical workflow validation or ethics approval was established here.

## Technical and research source gaps

Final expert membership; upstream revisions/licenses/checkpoints; faithful NMF/NMCF method choice; complete DAE-NMF-VMD availability; dataset version/access/license and source-aware splits; validated metric/alignment conventions; fusion weights/failure policy; exact supported capture device; real Firebase project/provider/session policy; backend migration/legacy-data ownership policy; retention/capacity/backups; authorized domain/hosting configuration; actual end-to-end server evidence; and current measured performance/UAT results. These are open work items, not empty fields to fill with plausible values.

## Preservation and inspection limits

No submitted PDF/DOCX, historical bibliography/diagram/questionnaire file, application source, production setting or external service was modified by this documentation worker. M1 edits are confined to the delegated separate FYP2 working files; implementation workers may edit application code concurrently. Earlier authorized Quarto installation is unchanged and no new tool is installed. Source-page rendering uses ignored scratch output, and starter HTML stays under `fyp2/_build/`. No submission rebuild was attempted. The complete 217-original-file manifest, not only selected hashes or a whole-working-tree clean claim, is the integrity check.
