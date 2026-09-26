# FYP1 to FYP2 change map

M1 synchronization, 26 September 2026. This is a controlled FYP2 change record, not a replacement for the submitted FYP1 report or a claim that the target system is complete. The revised DOCX and PDF in `report/Submission/` are the historical authority. The 217 original tracked files are preserved; their baseline hashes are in `fyp2/provenance/tracked-files-2026-09-26.sha256`. The separate FYP2 files may evolve after coordinator checkpoint `47c10af`.

## Basis and corrections to earlier mappings

The submitted PDF's contents pages vii-x and body were checked against the revised DOCX heading styles. Its Chapter 3 already contains **Healthcare Staff and Audio Analyst**, 53 questionnaire responses, 15 functional requirements, eight non-functional requirements and eight user requirements. The architecture pack's description of a single unspecified actor therefore describes an earlier baseline, not the submitted revision.

Important section corrections:

- `4.5.3` is **Separation Algorithm Design and Mathematical Formulation**.
- `4.5.3.5` is **Model Selection Strategy**, not `5.1.3.5`.
- `4.5.4` is **Database and Storage Design**, not `4.5.3`.
- Submitted NF5 is **Security and Privacy**: minimize identifying information and restrict access to the local application workflow. Do not attribute the older phrase about avoiding server storage to the revised submission.
- Submitted Chapter 5 is **Implementation Plan** and Chapter 6 is **Conclusion**. The local *FYP Handbook T2610*, section 3.5.1, page 14, gives application-based FYP2 chapters 5 **Implementation**, 6 **Testing**, and 7 **Conclusion**. The continuation pack confirms this seven-chapter structure; it does not pretend FYP1 Chapter 6 was already a testing/evaluation chapter. The separate teaching plan and rubric in the known directory are FYP1-specific.
- `report/quarto/chapters/` is an explicitly unsynchronized earlier source tree, including pre-response questionnaire placeholders. It is not a safe source for a verbatim FYP2 carry-forward.

## Current decisions and their scope

The application brand is **StethoFuse**. The continuation pack confirms the unchanged official academic title **Machine Learning-Based System for Cardiopulmonary Sound Separation**. The proposal's *Development of a* prefix is retained as historical source wording, not a reason to amend either original or reopen the confirmed title.

The latest user direction is a full application with Firebase identity, backend-managed roles and object permissions, accounts and audio persistent on the user's own server, and **Ensemble Learning, not Federated Learning**. Ordinary users request one ensemble run; experts remain internal implementation/evaluation choices. Firebase does not replace backend authorization or become the audio store by implication.

The user explicitly approved the owl with “Animation is Done. Now resume the front-end work”; `../implementation/frontend/PAUSE_NOTES.md` records this. The old owl-first hold in the architecture pack is historical. The pre-M1 frontend is a fictional local demonstration. M1 now adds implemented/integrated adapter and protected API paths tested locally with mocked identities, without making synthetic audio, simulated jobs, physical capture or ensemble inference real. Current code/test claims and pending live gates are recorded in [M1 notes](fyp2/M1_IMPLEMENTATION_AND_TEST_NOTES.md), using the [seven-state vocabulary](fyp2/STATUS_AND_EVIDENCE.md).

The final hostname is confirmed as `stethofuse.ashraf-alsaloul.com`; the earlier `hearme.ashraf-alsaloul.com` target is superseded for current planning. Confirmation is not deployment. This documentation work changes no DNS, certificates, provider configuration or services. The intended primary-admin email in the continuation pack is neither a Firebase UID nor a privilege rule; real sign-in, backend verification and explicit trusted-bootstrap approval remain separate gates.

## Section mapping from the actual submitted report

Page numbers below are printed report pages, not PDF file indices. For the main body, printed page 1 is PDF page 14.

| Submitted source | FYP2 destination | Required change and evidence boundary |
| --- | --- | --- |
| Cover, title page, abstract; pp. i-vi | Preliminary pages | Preserve academic identity. Rewrite abstract last around actual implementation and results; no completed integration or improvement claims now. |
| 1.1-1.2 Overview and Problem Statement; pp. 1-2 | 1.1-1.2 | Explain account-specific recording/review workflow and the research question about combining estimates. Do not promise superior separation. |
| 1.3 Project Objectives; p. 2 | 1.3 | Retain original objective provenance; show objective-to-requirement mapping. Record any material revision and supervisor decision rather than silently rewriting the original objectives. |
| 1.4-1.5 Scope and Limitations; p. 3 | 1.4-1.5 | Add authenticated ownership, persistence, sharing/review, administration and ensemble scope. Retain separation-only/non-diagnostic boundary, dataset/device limits and absence of clinical validation. |
| 1.6-1.7 Methodology and Target Audience; p. 4 | 1.6-1.7 | Incremental application integration plus controlled individual-versus-fusion evaluation. Extend existing staff/analyst roles with Administrator; role names are not verified professional credentials. |
| 2.2 Literature Search and Screening; pp. 6-7 | 2.2 | Preserve original 96 considered / 49 eligible / 35 selected synthesis record. Any later search needs its own dated search/screening log and revised totals, not retroactive edits. |
| 2.4 Separation Techniques; p. 8 | 2.4 and 2.5 | Distinguish baseline algorithms from faithful paper implementations. Add justified fusion literature only after verification. See method attribution register. |
| 2.5 Datasets and 2.6 Metrics; p. 9 | 2.6 and 2.7 | Identify actual dataset version, license/access, subject/source grouping, train/validation/test split, reference availability, metric definitions and evaluation conventions. No metric for an upload lacking the required references. |
| 2.7-2.9 Systems, Matrix and Gaps; pp. 10-13 | 2.8-2.10 | Retain existing-tool comparison, review features and extend application/fusion rationale with sources. Do not repurpose classification fusion as verified separation fusion. |
| 3.2 Questionnaire; pp. 14-28 | 3.2-3.3 | Preserve 53-response data and respondent limitations. A new targeted consultation is separate evidence; no invented healthcare interviews or claims that the original survey asked about Google login or ensembles. |
| 3.3 Functional Requirements; pp. 28-29 | 3.4 | Version F1-F15 rather than erase their history. Add identity, ownership, review/grants, administration, persistent storage and ensemble provenance requirements. |
| 3.4 Non-Functional Requirements; p. 29 | 3.5 | Strengthen NF5 to enforced private server access; extend reliability, responsiveness, accessibility, retention/deletion, backup/restore and traceability. Define measurable acceptance thresholds before testing. |
| 3.5 User Requirements; pp. 29-30 | 3.6 | Own workspace for each role; explicit analyst access; safe admin metadata. Update UR4/UR5 normal-user model choice to one ensemble action. |
| 4.2 Context and 4.3 Use Cases; pp. 31-37 | 4.2-4.3 | Retain two existing actors and add admin/provider/device boundaries. Supersede UC04 model selection in ordinary operation; add account, ownership, sharing/review and admin cases without conflating them with original use cases. |
| 4.4 Activity Diagram; pp. 37-38 | 4.4 | Upload/capture, validation/save, non-blocking job, expert/fusion/result stages; error, partial/failure, retry and optional review branches. |
| 4.5 Class Diagram and 4.5.1 Components; pp. 38-40 | 4.5-4.6 | Extend reusable strategy/service boundaries with users, ownership, provider verification, grants/reviews, immutable run versions and safe audit events. New class names are design proposals until mapped to code. |
| 4.5.2 Algorithm and Model Selection Design; pp. 41-42 | 4.7 | Retitle as Ensemble Separation Engine Design. Ordinary users no longer choose an individual strategy; internal registry and baseline evaluation remain. |
| 4.5.3 Algorithm Formulation; pp. 42-46 | 4.7 | Reconcile actual preprocessing and scaling, output ordering, alignment, residual handling, fusion weights and failure policy. Keep fixed-filter/NMF/VMD as documented baselines unless evidence establishes paper equivalence. |
| 4.5.3.5 Model Selection Strategy; p. 46 | 4.7.4 | Replace normal-user strategy selection with versioned ensemble orchestration. Distinguish fixed source-specific weights from per-recording adaptive weights. No weights are approved or measured yet. |
| 4.5.4 Database and Storage; pp. 46-47 | 4.8 | Migrate legacy metadata/files into explicit ownership, protected media, separate historical runs, grants, retention and recovery. Do not treat path naming as authorization. |
| 4.6 Sequence Diagram; pp. 47-48 | 4.9 | Include identity verification and object authorization for upload, processing, result/media retrieval, sharing, revocation and review. |
| 4.7 Interface Design; pp. 48-49 | 4.10 | Link working route/state inventory, approved owl and responsive screenshots to dated builds. Show the demo/live boundary on relevant figures. |
| 5.1.1-5.1.4 Development; pp. 50-52 | 5.1-5.7 | Write implementation facts with code paths and revision/configuration evidence. Separate the legacy backend, completed demo UI, M1 local adapter/API implementation and pending genuine-provider acceptance. |
| 5.2.1-5.2.4 Testing; pp. 53-54 | Chapter 6 | Expand planned tests into actual reproducible unit/integration/system/UAT results when run. Keep frontend fixture tests distinct from backend identity, server persistence and genuine separation tests. |
| 5.3 Deployment; pp. 54-55 | 5.8 and 6.7 | Own-server deployment and configurable target origin are plans. Document rollout, protected storage, provider configuration and restore proof only when authorized and tested. |
| 5.4 Documentation and Maintenance; p. 55 | 5.9 | Reproduction instructions, versioned evidence, migrations, provenance, backup/restore and maintenance boundaries. |
| Chapter 6 Conclusion; pp. 56-57 | Chapter 7 | Summarize achieved objectives and measured limitations, not the original expected contributions as if fulfilled. |
| References; pp. 58-63 | References | Start reconciliation from the submitted references and revised bibliography; validate every new citation and preserve original files. |
| Appendices A-H; pp. 64 onward | New FYP2 appendices | Add updated Gantt, genuine FYP2 logs, current similarity evidence, traceability and test/evaluation manifests. Do not relabel old FYP1 logs, diagrams or test plans as new completed work. |

## Requirements that change meaning

| Original identifiers | FYP2 treatment |
| --- | --- |
| F1-F3 / UC01-UC02 / UR1-UR2 | Retain metadata/upload/validation; add account ownership, private persistence and a separately verified capture path. |
| F4-F5 / UC03 / UR3 | Account-scoped list/search; explicitly shared items separate from owned recordings. |
| F6-F8 / UC04-UC05 / UR4-UR5 | Preprocessing and processing retained; normal-user selection superseded by one versioned ensemble request. Baseline selection remains evaluation/admin infrastructure. |
| F9-F10 / UC05 | Real heart/lung files must be linked to actual run provenance. Demo audio is not proof. |
| F11 / UC06 / UR6 / NF2-NF3 | Actual non-blocking job state, errors, retries and availability; no fabricated percentages or silent single-expert fallback presented as full ensemble success. |
| F12-F13 / UC07-UC08 / UR7 | Authorize preview/download for owner or active grant, including direct media and visualizations. |
| F14 / UC09 / UR8 / NF7 | Preserve original and every historical run; owner-only job detail is separate from explicitly shared recording/result content. |
| F15 / UC10 / UR8 | Valid evaluation information only. Research quality review is not a reference-based separation metric. |
| NF1, NF4, NF6, NF8 | Retain usable workflow/modularity/WAV support/extensibility; add measurable checks instead of retrospective success claims. |
| NF5 | Extend the submitted privacy requirement to enforced backend ownership, grants, revocation, protected storage and documented retention. No zero-knowledge claim. |

The [requirements history](fyp2/REQUIREMENTS_HISTORY.md) maps all 52 continuation IDs to original F/NF/UR/UC identifiers and the retained R01-R18 summary register. Requirements elicitation, implementation-driven revision and future post-deployment feedback are separate phases; no later feature is attributed to the original 53 respondents. Evidence gates are in [traceability](fyp2/TRACEABILITY.md). Formal scope/objective changes and the current FYP2 rubric/template remain confirmation items in [the source register](fyp2/provenance/SOURCE_REGISTER.md).
