# FYP2 source register and unresolved guidance

Read-only source audit dated 26 September 2026. Documentation sources below are repository-relative unless stated otherwise. This register identifies what each source can support; it does not promote an assistant-authored plan or README into independent experimental evidence.

## Source hierarchy

1. Latest explicit user decisions govern the requested product direction and approvals.
2. Current applicable university/supervisor instructions govern academic scope and submission requirements; the local T2610 handbook is available but current-term applicability still needs confirmation.
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
| S04 | `resources/guidelines/FYP Handbook T2610.pdf`, sections 3.5 and 4, pp. 13-17 | FYP2 application-based seven-chapter structure, preliminary material, logs and formatting guidance. Page 14 rendered and visually checked. The file is a 32-page April 2026 handbook. Confirm term applicability and current eBwise requirements. |
| S05 | `README.md`, `report/quarto/README.md`, `_quarto.yml`, scripts | Explicit warning that Quarto is older/unsynchronized. Historical revision workflow is DOCX transformation followed by Word field update/export; generation scripts were inspected, not run. |
| S06 | `report/questionnaire/User Requirements Questionnaire for Machine Learning-Based Cardiopulmonary Sound Separation System.csv`; submitted 3.2.13 | CSV parsed read-only: 53 data rows, 25 columns. Existing report explicitly notes underrepresentation of target healthcare roles. No respondent data copied into new preparation files. |
| S07 | `literature-review/prisma/prisma_counts.json`, `chapter_2_synthesis_selection`; screening/metadata folders | Existing synthesis records 96 considered, 47 excluded, 49 eligible and 35 selected/cited. Nested historical counts refer to different phases; do not flatten them or change old totals as part of preparation. |
| S08 | `report/revisions/verified_references.bib`; `literature-review/references/references.bib` | Revised and broader bibliographies are distinct. Selected candidate entries compared with local primary-paper first pages. No blanket fresh metadata verification. |
| S09 | Local NeoSSNet, Torabi NMF, Grooby NMF/NMCF and Sun DAE-NMF-VMD PDFs | Narrow bibliographic/method-identification support; see [method register](METHOD_ATTRIBUTION.md). Full method reproduction, licenses/code/checkpoints and effectiveness remain open. |
| S10 | `diagrams/plantuml/*.puml`, `diagrams/mermaid/audio_processing_workflow.mmd`; report figure folders | Editable historical diagram sources exist. Inspected component/class/use-case sources already show staff/analyst and the legacy individual-strategy design. Preserve originals; future FYP2 diagrams must be separate and versioned. |
| S11 | `../planning/source-plans/StethoFuse_Architecture_and_Agreed_Plan/00_MASTER_PLAN.md` and numbered sections 01-12, especially 05,06,09,10 | Target architecture and earlier decision record. Some report section numbers and actor descriptions predate the submitted revision. Hostname and owl approval are superseded by newer conversation evidence. |
| S12 | Current user instructions, reflected in preparation task and `../implementation/frontend/PAUSE_NOTES.md` | Firebase plus backend roles; own-server persistent accounts/audio; EL not FL; preserve academic title; owl approval “Animation is Done”; latest hostname stated as StethoFuse. This is decision provenance, not a deployment test. |
| S13 | `../implementation/frontend/src/data/adapters.ts`, `store.tsx`, pages and `FRONTEND_INTEGRATION.md` | Working demo UI; live auth/data methods unavailable, local fictional metadata, synthetic audio and simulated jobs. Client checks are not backend security. |
| S14 | `../implementation/app/main.py`, `app/routers/{separation,results}.py`, `database/schema.sql`, ML/evaluation paths | Legacy FastAPI single-system workflow. Inspected schema lacks ownership/accounts/grants; result/download/history/static visualizations do not enforce the new account model. Not safe evidence of integrated multi-user operation. |
| S15 | `../implementation/frontend/evidence/reference-match/functional/README.md`, workflow/admin JSON; frontend checkpoints | Dated, scoped prior fixture tests. No suite rerun for this documentation task; no extrapolation to real auth, clinical quality or deployment. |
| S16 | [Official Quarto single-user tarball instructions](https://quarto.org/docs/download/tarball.html), [stable v1.10.18 release](https://github.com/quarto-dev/quarto-cli/releases/tag/v1.10.18), [official download manifest](https://quarto.org/docs/download/_download.json) and published checksum asset; inspected 2026-09-26 | Provenance for the separately authorized project-local portable tool setup. Supports tool version/download integrity, not academic report content. See [exact hashes, commands and HTML-only checks](QUARTO_SETUP.md). |

## Reconciliation log

| Conflict | Preparation resolution |
| --- | --- |
| Pack10 describes single actor and maps storage to 4.5.3; submitted revision already has two roles and added algorithm section | Use submitted S01/S02 headings: storage 4.5.4; model-selection strategy 4.5.3.5. Keep pack unchanged as historical input. |
| Earlier pack says NF5 avoids server storage | Revised NF5 instead minimizes identifying information and limits file access to the local workflow. New private persistent storage is an extension; do not misquote submitted NF5. |
| Six chapters in FYP1 versus discussion of evaluation in Chapter 6 | S04 recommends FYP2 Implementation / Testing / Conclusion as chapters 5/6/7. Seven-chapter outline is provisional on current-term confirmation. |
| Restored Quarto versus submitted revision | Submitted DOCX/PDF control content. No automatic regeneration or overwrite from older QMD. |
| Pack owl-first pause versus later user approval | Gate satisfied by explicit user approval recorded in S12; preserve current owl. Prior rejected renderers' PASS logs do not supersede approval. |
| Pack `hearme.ashraf-alsaloul.com` versus current `stethofuse.ashraf-alsaloul.com` | Record current stated target and historical conflict. No live endpoint, DNS or redirect configuration verified or changed. |
| Demo persistence versus persistent own-server target | Browser fixture storage is demo behavior only. Real account/audio persistence remains integration work. |
| Baseline NMF/VMD and NeoSSNet adapter versus three verified ensemble experts | Preserve reusable code; do not assert paper correspondence, complete DAE-NMF-VMD or real fusion from class names. |
| Proposal title versus submitted cover title | Preserve both source wordings and request the official registered wording for the FYP2 cover; never substitute product brand as academic title. |

## Exact university guidance still needed

- Confirmation that the supplied T2610 handbook is the applicable FYP2 edition/term, and the current FYP2 rubric, module/term code and eBwise submission/deadline instructions. The local rubric is named **FYP1 Rubrics.pdf**; it is not silently relabeled FYP2.
- Current final-report template, page-size policy and final naming convention. The submitted PDF is Letter; the handbook PDF itself is A4, which alone does not prescribe report paper size. Its cover margin guidance and body margins differ; confirm intended layout before a new final export.
- Supervisor confirmation of formal objective/method/scope changes, including ensemble research and persistent multi-user functionality. Development instructions are not university approval.
- Official registered title and supervisor-name format for the FYP2 cover; proposal and report wordings differ.
- Genuine FYP2 meeting logs and current similarity report. Local handbook section 3.5 specifies at least six logs and an overall similarity threshold of at most 20%; confirm current-term requirements rather than fabricate these artifacts.
- Appendix numbering/preliminary-page interpretation: the handbook repeats Appendix B and lists Abstract twice in its suggested order. Resolve with current template/supervisor; do not reproduce obvious ambiguity as a new final layout.
- Appropriate approval, recruitment, consent/data-handling process for any new target-user consultation or human recordings. No new consultation, clinical workflow validation or ethics approval was established here.

## Technical and research source gaps

Final expert membership; upstream revisions/licenses/checkpoints; faithful NMF/NMCF method choice; complete DAE-NMF-VMD availability; dataset version/access/license and source-aware splits; validated metric/alignment conventions; fusion weights/failure policy; exact supported capture device; real Firebase project/provider/session policy; backend migration/legacy-data ownership policy; retention/capacity/backups; authorized domain/hosting configuration; actual end-to-end server evidence; and current measured performance/UAT results. These are open work items, not empty fields to fill with plausible values.

## Preservation and inspection limits

No submitted PDF/DOCX, historical bibliography/diagram/questionnaire file, application source, production setting or external service was modified by this documentation preparation. Only new files in the delegated documentation paths were authored, plus the separately authorized project-local portable Quarto installation. Source-page rendering used scratch files outside the report tree; the new starter's HTML output stays under `fyp2/_build/`. No submission rebuild was attempted. The complete original tracked-file manifest, not only selected hashes, is the integrity check.
