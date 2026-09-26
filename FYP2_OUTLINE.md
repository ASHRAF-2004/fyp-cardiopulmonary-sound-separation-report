# FYP2 report outline

Preparation version, 26 September 2026. This outline follows the application-based final-report structure in the local *FYP Handbook T2610*, section 3.5.1, page 14. Confirm its applicability to the student's FYP2 term, current rubric and supervisor instructions before freezing the report format. It is not a completed report.

Academic title carried forward from the submitted report: **Machine Learning-Based System for Cardiopulmonary Sound Separation**. The proposal's additional *Development of a* wording is recorded, not silently reconciled. **StethoFuse** is the application brand.

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
3.3 New target-user consultation, only if genuinely conducted  
3.4 Functional requirements and acceptance criteria  
3.5 Non-functional requirements and measurable thresholds  
3.6 Role-specific user requirements and access matrix  
3.7 Requirement-to-design-to-test traceability  
3.8 Summary

Retain F1-F15, NF1-NF8, UR1-UR8 and UC01-UC10 as historical identifiers. Link additions/supersessions to new IDs instead of silently renumbering history. Separate owner-only processing jobs from explicitly shared recording/result content. Administrator status alone grants neither private audio nor analyst review authority.

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
4.9 Authorized interaction sequences  
4.10 Role-aware interface and state design  
4.11 Summary

Produce new versioned diagrams under the FYP2 tree; preserve existing PlantUML/Mermaid sources. Design records must specify owner/grant checks, stable provider identity, immutable run configuration, revocation and protected media. Reusable existing strategy adapters are not discarded because the normal-user selector is removed.

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

For each module, identify source revision, inputs/outputs, reused code, additions, configuration and remaining gaps. At this preparation checkpoint the frontend is a working local demo and the legacy backend is a separate single-system research application. Live adapters currently report unavailable. New access-foundation preparation, if present, is not evidence of integrated protected routes. Avoid past-tense completion for future sections 5.3-5.8.

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
6.8 Target-user acceptance, if conducted with appropriate approval  
6.9 Findings against requirements and remaining defects

A screenshot or build success is not backend security evidence. Existing fixture browser runs may support the demo UI only and must keep their original dates/environment. Do not restate old individual-method scores as ensemble results, mix test-set tuning with evaluation, or present lack of references as zero error. Record negative findings and failed cases as well as passes.

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

1. Confirm current FYP2 handbook/rubric, registered title and supervisor scope decisions.
2. Reconcile bibliography, methodology and actual implementation evidence.
3. Establish versioned tests, dataset splits and output provenance before collecting final results.
4. Synchronize any reused text from the submitted revision, never the stale Quarto baseline by default.
5. Render and inspect the new report independently; prove all historical hashes unchanged.

See [change map](FYP1_TO_FYP2_CHANGE_MAP.md), [traceability](fyp2/TRACEABILITY.md), [build plan](fyp2/BUILD_PLAN.md) and [source gaps](fyp2/provenance/SOURCE_REGISTER.md).
