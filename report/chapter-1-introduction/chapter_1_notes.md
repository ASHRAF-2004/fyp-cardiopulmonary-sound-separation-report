# Chapter 1 Notes

Draft date: 2026-05-16

## Alignment With Proposal

The Chapter 1 draft follows the approved proposal content extracted from `proposal/FYP-Proposal-Form.pdf`.

| Proposal item | How it is reflected in Chapter 1 |
|---|---|
| Project title: Development of a Machine Learning-Based System for Cardiopulmonary Sound Separation | The chapter uses the corrected report title: `Machine Learning-Based System for Cardiopulmonary Sound Separation`. |
| Project type: Application-Based | The chapter frames the work as a Software Engineering application prototype. |
| Project category: Application Software | The scope and expected output describe a software system rather than hardware or clinical deployment. |
| Focus/contribution: Prototype/Proof of Concept | The aim, significance, and expected output describe a functional proof-of-concept prototype. |
| Background: heart and lung sounds recorded together and overlapping | Section 1.1 explains mixed cardiopulmonary audio and the source separation problem. |
| Problem statement: overlap, noise, and existing solutions focusing on diagnosis rather than reusable software | Section 1.2 states the overlap/noise problem and avoids disease-diagnosis framing. |
| Methodology: Python, preprocessing, feature extraction, ML models, public datasets | Sections 1.4 and 1.5 include Python-based processing, preprocessing, ML separation, datasets, and evaluation. |
| Expected output: two separate audio outputs | Sections 1.5 and 1.7 explicitly state separated heart sound and lung sound outputs. |
| Limitation: sound separation only, no disease detection | Section 1.5 excludes diagnosis, disease detection, and clinical decision-making. |

## Supervisor Review Needed

The following points should be confirmed with the supervisor:

1. Whether the Chapter 1 headings should exactly follow the user's requested structure or the handbook's application-based headings, which also mention methodology, target audience, limitations, and summary.
2. Whether "Project Aim" should remain as one broad aim or be merged with the objectives in the final report format.
3. Whether the expected evaluation metrics should be named in Chapter 1 or left general until Chapter 3.
4. Whether HLS-CMDS should be named in Chapter 1 as the main dataset candidate or introduced mainly in Chapter 2 and Chapter 3.
5. Whether Chapter 5 should be described as "Testing and Evaluation" or "Implementation Plan" to match the final FYP1 structure required by the handbook.

## Assumptions Made

1. The corrected project title provided by the user is the report title, even though the proposal form title begins with "Development of".
2. The project remains a one-student Software Engineering application software project.
3. The system will be developed as a software prototype/proof of concept rather than a production medical tool.
4. Python will be the main implementation language, consistent with the proposal.
5. Public or accessible datasets will be used, and HLS-CMDS is treated as the strongest current dataset candidate because it includes mixed and source heart/lung recordings.
6. The machine learning method has not yet been finalized, so Chapter 1 describes it generally and leaves model-selection detail for Chapter 3.
7. Citations are used sparingly in Chapter 1 and only for technical background, dataset support, and literature-grounded problem framing.
8. No new references were added and `references.bib` was not edited.

## Citation Use

The draft uses existing citation keys from `literature-review/references/references.bib` only. Citations are included where Chapter 1 makes technical claims about separation methods, datasets, and recent literature. Detailed comparison of studies is intentionally left for Chapter 2.
