# FYP2 report outline

M1 working version, 26 September 2026. This outline follows the confirmed application-based seven-chapter structure in the local *FYP Handbook T2610*, section 3.5.1, page 14, and the continuation pack. The current FYP2 rubric, final template and term/submission instructions still need reconciliation; the local teaching plan/rubric are FYP1-specific. It is not a completed report.

Confirmed unchanged academic title: **Machine Learning-Based System for Cardiopulmonary Sound Separation**. The proposal's additional *Development of a* wording remains historical provenance. **StethoFuse** is the application brand; `stethofuse.ashraf-alsaloul.com` is the confirmed production target, not a claimed live deployment.

## Preliminary material

Cover and title page; copyright; declaration; acknowledgements; abstract; table of contents; lists of tables, figures, abbreviations/symbols and appendices. Use current approved university wording and actual submission date. Do not reuse the FYP1 declaration date, term or signature as FYP2 evidence. Write the abstract after implementation/testing evidence is settled.

## Chapter 1 Introduction

1.1 Background and application context  
1.2 Problem statement  
1.3 Objectives and traceable changes from FYP1  
1.4 Scope of the multi-user separation application  
1.5 Limitations and non-diagnostic boundary  
1.6 Development and evaluation methodology  
1.7 Intended roles and stakeholders  
1.8 Report organization and summary

Explain why recording management, persistent ownership and authorized review belong to the application contribution. Treat improved ensemble separation as a question to investigate. Firebase identity, backend roles, private server storage and EL rather than FL are the current direction, not automatically completed features.

## Chapter 2 Literature Review

2.1 Overview  
2.2 Original search and transparently logged later updates  
2.3 Cardiopulmonary sound characteristics and recording limitations  
2.4 Individual separation methods and baseline roles  
2.5 Ensemble and fusion rationale  
2.6 Datasets, domain suitability and access  
2.7 Evaluation measures and reference requirements  
2.8 Existing tools and application workflow comparison  
2.9 Updated evidence matrix  
2.10 Gaps, method selection rationale and summary

Carry forward the submitted literature provenance, not all available PDFs indiscriminately. Candidate NeoSSNet, NMF/NMCF and DAE-NMF-VMD entries remain provisional until their papers, implementation revisions, licenses, checkpoints and adaptations are reconciled. The local paper title pages establish limited bibliographic facts, not reproduction fidelity. Fixed source-specific fusion is not adaptive fusion.

## Chapter 3 Requirements Analysis

3.1 Sources and versioning of requirements  
3.2 Original questionnaire and the 53-response limitations  
3.3 Implementation-driven FYP2 requirement revisions  
3.4 Functional requirements and acceptance criteria  
3.5 Non-functional requirements and measurable thresholds  
3.6 Role-specific user requirements and access matrix  
3.7 Requirement-to-design-to-test traceability  
3.8 Post-deployment feedback plan and later revisions  
3.9 Summary

Retain F1-F15, NF1-NF8, UR1-UR8 and UC01-UC10 as historical identifiers. Use [requirements history](fyp2/REQUIREMENTS_HISTORY.md) to connect the 52 continuation IDs and initial R01-R18 summaries. Separate initial elicitation from FYP2 revisions and future post-deployment feedback. No new consultation, deployment or feedback results are claimed. Separate owner-only processing jobs from explicitly shared recording/result content. Administrator status alone grants neither private audio nor analyst review authority.

## Chapter 4 System Design

4.1 Design scope and constraints  
4.2 System context and trust boundaries  
4.3 Use cases and descriptions  
4.4 Activity and job lifecycle  
4.5 Domain/class model  
4.6 Component architecture and identity/authorization boundary  
4.7 Ensemble Separation Engine and mathematical design  
4.7.1 Input validation, preprocessing and scale preservation  
4.7.2 Verified expert contracts and source correspondence  
4.7.3 Alignment, residual handling and representation choice  
4.7.4 Versioned orchestration, fixed fusion and optional adaptive research  
4.7.5 Failure, partial-output and retry policy  
4.8 Database migrations and private file storage  
4.9 Authentication, authorization and permitted interaction sequences  
4.10 Role-aware interface and state design  
4.11 Deployment and infrastructure design  
4.12 Summary

Produce new versioned diagrams under the FYP2 tree; preserve existing PlantUML/Mermaid sources. Design records must specify owner/grant checks, stable provider identity, immutable run configuration, revocation and protected media. The [M1 Mermaid sequence](fyp2/design/m1-auth-sequence.mmd) is illustrative design only. Explain trusted UID bootstrap outside public registration; intended administrator email is not a privilege rule. Reusable existing strategy adapters are not discarded because the normal-user selector is removed.

## Chapter 5 Implementation

5.1 Baseline, tools and reproducible environment  
5.2 Working frontend and approved animation  
5.3 Firebase identity integration and backend user resolution  
5.4 Persistent recording intake, account isolation and media delivery  
5.5 Background execution and expert integration  
5.6 Versioned ensemble fusion implementation  
5.7 Sharing, analyst review, settings and administration  
5.8 Own-server deployment and configuration  
5.9 Maintenance, backup and reproducibility  
5.10 Implementation status and limitations

For each module, identify source revision, inputs/outputs, reused code, additions, configuration and remaining gaps. Use `implemented`, `integrated`, `tested`, `verified live`, `planned`, `simulated` and `blocked` as defined in [status conventions](fyp2/STATUS_AND_EVIDENCE.md). The pre-M1 frontend/demo, legacy backend and standalone access scaffold are distinct foundations. Current M1 changes and accepted evidence belong in [M1 implementation notes](fyp2/M1_IMPLEMENTATION_AND_TEST_NOTES.md); do not treat concurrent work or mocked token tests as genuine provider integration. Sections 5.5-5.6 and deployment remain evidence-dependent.

## Chapter 6 Testing

6.1 Test strategy, environments and evidence conventions  
6.2 Unit tests and input/output contracts  
6.3 API, identity and object-authorization integration tests  
6.4 End-to-end persistent multi-account workflows  
6.5 Frontend, accessibility, responsive and animation tests  
6.6 Comparative separation evaluation  
6.6.1 Dataset manifest and leakage-controlled splits  
6.6.2 Baselines, verified experts and ensemble configurations  
6.6.3 Heart/lung metrics, runtime and failure reporting  
6.6.4 Ablation, uncertainty, domain limitations and interpretation  
6.7 Deployment, recovery, storage and reliability checks  
6.8 User acceptance and post-deployment feedback, only when genuinely conducted  
6.9 Findings against requirements and remaining defects

A screenshot or build success is not backend security evidence. Explicitly separate offline mocks, local API with injected identities, Firebase emulator, real-provider/local API and production. Existing fixture browser runs may support the demo UI only and must keep their original dates/environment. Post-deployment feedback remains planned until real deployment/evaluation occurs. Do not restate old individual-method scores as ensemble results, mix test-set tuning with evaluation, or present lack of references as zero error. Record negative findings and failed cases as well as passes.

## Chapter 7 Conclusion

7.1 Project summary  
7.2 Achieved objectives and application contribution  
7.3 Supported experimental findings  
7.4 Limitations  
7.5 Future work  
7.6 Summary

Derive conclusions from Chapter 6 evidence. Distinguish demonstrated prototype behavior from deployment readiness, clinical validity and research questions still open.

## References and appendices

Use verified citations and the required university style. Proposed appendix subjects are updated Gantt; genuine FYP2 meeting logs; current similarity evidence; traceability/use cases; versioned diagrams; test and evaluation manifests; data/method provenance; authorized deployment/recovery notes; and any genuine follow-up instruments/results. Confirm appendix lettering because the handbook repeats Appendix B, and confirm final naming/submission instructions from the current term's source.

## Preparation gates

1. Reconcile current FYP2 rubric/template/term instructions and supervisor scope decisions; the seven-chapter structure, academic title and target hostname are already confirmed.
2. Reconcile bibliography, methodology and actual implementation evidence.
3. Establish versioned tests, dataset splits and output provenance before collecting final results.
4. Synchronize any reused text from the submitted revision, never the stale Quarto baseline by default.
5. Render and inspect the new report independently; prove all historical hashes unchanged.

See [change map](FYP1_TO_FYP2_CHANGE_MAP.md), [traceability](fyp2/TRACEABILITY.md), [build plan](fyp2/BUILD_PLAN.md) and [source gaps](fyp2/provenance/SOURCE_REGISTER.md).
