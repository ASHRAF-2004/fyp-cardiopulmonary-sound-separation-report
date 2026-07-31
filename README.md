# FYP1 Report: Cardiopulmonary Sound Separation

## Project Information

| Item | Details |
|---|---|
| Project title | Machine Learning-Based System for Cardiopulmonary Sound Separation |
| Student | AL-SALOUL, ASHRAF ALI HUSSEIN |
| Student ID | 1221303805 |
| Supervisor | Arshad Jamal |
| Project ID | 985 |
| Programme | Bachelor of Computer Science (Hons.) / Software Engineering |
| Project type | Application-Based FYP1 |
| Contribution | Prototype / Proof of Concept |
| Term | 2610 |

This repository contains the FYP1 interim report, its revised submission copy,
supporting literature-review evidence, questionnaire evidence, system-design
diagrams, and the restored report-generation workflow.

The project is limited to separating a mixed cardiopulmonary recording into
heart-sound and lung-sound outputs. It does not perform disease diagnosis,
clinical decision-making, or treatment recommendation.

## Final Revised Submission

The final PDF prepared for eBwise submission is:

```text
report/Submission/1221303805_Arshad_Jamal_FYP1_Report.pdf
```

The editable revised Word document used to produce that PDF is:

```text
report/Submission/1221303805_Arshad_Jamal_FYP1_Revised_Copy.docx
```

The submission PDF was exported from Microsoft Word in print-quality mode and
verified as follows:

| Check | Result |
|---|---:|
| Total pages | 104 |
| Embedded images present | 45 |
| PDF navigation bookmarks | 104 |
| PDF encryption | None |
| Required filename | Correct |

The earlier report under `report/1221303805_Arshad_Jamal_FYP1_Report.docx` is
retained as the pre-revision baseline. It is not the revised submission copy.

## Supervisor Feedback Addressed

The revised report addresses the received supervisor and moderator comments:

| Feedback area | Revision made |
|---|---|
| Abstract | Expanded to summarize the problem, literature, requirements, design, implementation plan, findings, and limitations. |
| Existing tools and applications | Chapter 2 now compares Eko, 3M Littmann CORE, Thinklabs Wave, and StethAid. |
| Feature selection | Chapter 2 identifies retained, conditional, and additional application features. |
| User roles | Healthcare Staff and Audio Analyst replace the previous unspecified user. |
| Functional requirements | Added audio attributes, file listing, validation, model selection, status, history, preview, download, and evaluation functions. |
| Use-case documentation | Chapter 4 contains ten use cases and ten corresponding description tables. |
| Algorithm placement | Fixed Filter, NMF, VMD, and NeoSSNet-style strategy details are documented in Chapter 4. |
| FYP2 planning | Chapter 5 briefly describes planned development, integration, testing, deployment, and maintenance activities. |
| References | References were revised to APA 7th edition presentation with hanging indents and DOI/URL details where available. |
| Formatting | Body text is justified and table/figure captions use chapter-based numbering such as Table 3.1 and Figure 4.2. |
| Application focus | The report now defines a role-based audio-record workflow for a clinic- or laboratory-oriented prototype. |

## Why the Project Is Application-Based

The report treats sound separation as one service within a larger software
application. The proposed workflow is:

```text
enter audio attributes -> upload recording -> validate input -> list records
-> select a model -> preprocess and separate -> show processing status
-> preview/download outputs -> retain processing history and metrics
```

Application evidence in the revised report includes:

- two concrete actors: Healthcare Staff and Audio Analyst;
- 15 functional requirements;
- 8 non-functional requirements;
- 8 user requirements;
- 10 documented use cases;
- context, use-case, activity, class, component, and sequence diagrams;
- interface, storage, validation, history, and output-management design; and
- interchangeable separation strategies behind a common application workflow.

The report remains honest about implementation status. It specifies and plans
the FYP2 prototype but does not claim completed clinical validation, model
performance, system testing, or deployment.

## Chapter Status

| Chapter | Status |
|---|---|
| Chapter 1: Introduction | Revised and complete for FYP1 |
| Chapter 2: Literature Review | Expanded with existing-tool comparison and feature decisions |
| Chapter 3: Requirements Analysis | Updated using 53 real questionnaire responses and revised application requirements |
| Chapter 4: System Design | Expanded with role-based diagrams, use-case tables, storage design, and algorithms |
| Chapter 5: Implementation Plan | Refocused on activities planned for FYP2 |
| Chapter 6: Conclusion | Revised to state the contribution, limitations, and future work accurately |
| References | Reformatted for APA 7th edition presentation |
| Appendices | Gantt chart, meeting logs, similarity page, matrices, diagrams, test plan, and questionnaire included |

## Questionnaire Limitation

Chapter 3 uses 53 genuine Google Form responses. Most respondents were students
or respondents with academic and technical backgrounds. These responses help
identify general feature and usability preferences, but they do not validate a
hospital workflow. The revised report states this limitation and identifies
targeted follow-up with healthcare staff and audio analysts as future work.

No healthcare responses, percentages, implementation results, test results, or
model scores were fabricated.

## Repository Structure

```text
diagrams/                     Editable Mermaid and PlantUML diagram sources
literature-review/            Screening records, PRISMA evidence, and references
proposal/                     Original FYP proposal files
report/Submission/            Final revised submission artifacts
report/quarto/                Restored Quarto baseline workflow
report/questionnaire/         Questionnaire, responses, charts, and exports
report/requirements/          Questionnaire design and Google Form guide
report/revisions/             Reproducible supervisor-feedback revision script
resources/                    Handbook, rubric, templates, and source diagrams
supervisor-updates/           FYP1 meeting logs
```

## Report Workflows

### Final Supervisor-Feedback Revision

The final submission was produced from the original DOCX with:

```powershell
python report/revisions/revise_supervisor_feedback.py
```

This script applies the supervisor-feedback revisions, inserts the updated
application design, formats the references, updates report formatting, and
writes the revised DOCX under `report/Submission/`.

Microsoft Word is then used to update document fields, repaginate, and export
the final submission PDF.

### Restored Quarto Baseline

The deleted Quarto workflow has been restored under `report/quarto/` together
with its chapter sources, figures, templates, validation script, and rendering
script:

```powershell
powershell -ExecutionPolicy Bypass -File report/quarto/scripts/validate-report.ps1
powershell -ExecutionPolicy Bypass -File report/quarto/scripts/render-report.ps1
```

Important: the restored Quarto chapters are an earlier baseline and are not
fully synchronized with the final supervisor-feedback revision. In particular,
the Quarto Chapter 3 source still contains the pre-response questionnaire
template. The revised DOCX and PDF in `report/Submission/` are the authoritative
submission artifacts.

## Supporting Evidence

Key evidence folders are:

```text
literature-review/references/
literature-review/prisma/
literature-review/screening/
report/questionnaire/
supervisor-updates/
resources/guidelines/
```

PRISMA tracking records 96 considered records, 49 eligible records, and 35
studies used in the report. The questionnaire evidence contains the original
CSV export and charts used for the 53-response Chapter 3 analysis.

## Submission Naming

The required submission naming convention is:

```text
studentID_supervisorName_FYP1_Report.pdf
```

The final file follows that convention:

```text
1221303805_Arshad_Jamal_FYP1_Report.pdf
```

## Author

**AL-SALOUL, ASHRAF ALI HUSSEIN**

Student ID: 1221303805

Software Engineering Specialisation

Multimedia University, Malaysia
