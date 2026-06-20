# FYP Report: Cardiopulmonary Sound Separation

## Project Title

**Machine Learning-Based System for Cardiopulmonary Sound Separation**

## Repository Purpose

This repository documents and tracks the progress of my Final Year Project 1 report.

The project is an **Application-Based FYP1 report** for a Software Engineering prototype / proof of concept. The repository contains the report sources, literature review records, PRISMA files, diagrams, generated Word report, supervisor update files, and validation/rendering scripts.

The current report follows the FYP Handbook T2610 application-based structure:

1. Introduction
2. Literature Review
3. Requirements Analysis
4. System Design
5. Implementation Plan
6. Conclusion

The project focus is **cardiopulmonary sound separation only**. It does not claim disease diagnosis, clinical decision-making, completed model scores, completed implementation results, or completed user survey findings.

---

## Project Overview

Cardiopulmonary recordings may contain heart sounds, lung sounds, breathing artefacts, body movement, sensor noise, and environmental noise in the same audio signal. Heart and lung components may also overlap in time and frequency, making clean separation difficult using simple filtering alone.

This project proposes a **machine learning-based software prototype** that separates a mixed cardiopulmonary audio recording into:

1. Heart sound output
2. Lung sound output

The intended contribution is a reusable software workflow for upload, validation, preprocessing, separation, output generation, result viewing, download, and planned evaluation using public datasets and suitable separation metrics.

---

## FYP Objectives

The current report uses these three project objectives:

1. To study and apply suitable preprocessing techniques to reduce noise and improve the quality of cardiopulmonary sound recordings.
2. To design and implement a machine learning-based approach for separating mixed cardiopulmonary recordings into heart and lung sound outputs.
3. To develop a reusable software prototype and evaluate its separation performance using public datasets and suitable performance metrics.

---

## Current Report Status

Latest local state: the report has been refactored to the application-based FYP1 structure, regenerated as DOCX, and validated through the repository scripts.

| Area | Current status | Notes |
|---|---|---|
| Repository structure | Available | Main report workflow is under `report/quarto/`. |
| Chapter 1: Introduction | Completed for FYP1 | Contains exactly 3 expanded cited problem statements and exactly 3 objectives. |
| Chapter 2: Literature Review | Completed for FYP1 | Uses verified PRISMA counts, selected studies, concise matrix, and citations. |
| Chapter 3: Requirements Analysis | Completed for FYP1 | Replaces the old Methodology chapter. Survey response analysis is still pending because no real responses are in the repo. |
| Chapter 4: System Design | Completed for FYP1 | Includes context, use case, activity, class, sequence, and interface design sections. |
| Chapter 5: Implementation Plan | Completed for FYP1 | Replaces the old Testing and Evaluation chapter. Testing is presented as planned work only. |
| Chapter 6: Conclusion | Added | Summarizes FYP1 work, contributions, limitations, and future work. |
| PRISMA figure | Generated | Uses the filled DOCX source converted to PDF then PNG. Mermaid is not used for PRISMA. |
| Literature review matrix | Completed | Concise matrix in Chapter 2 and full matrix in Appendix D. |
| PlantUML diagrams | Generated | Editable `.puml` sources and rendered PNG/SVG files are available. |
| Table/Figure numbering | Updated | Captions are continuous: Table 1, Table 2, Figure 1, Figure 2, etc. |
| Generated Word report | Available | `report/generated/paper.docx` |
| Validation | Passed | `report/quarto/scripts/validate-report.ps1` passed after regeneration. |
| Render workflow | Passed | `report/quarto/scripts/render-report.ps1` regenerated the DOCX successfully. |
| Manual submission checks | Still required | Word field refresh, cover spacing, Gantt chart, meeting logs, Turnitin page, and supervisor confirmation. |

---

## Literature Review Progress

The literature review process includes systematic search, screening, classification, synthesis, and matrix preparation.

| Item | Count |
|---|---:|
| Records considered | 96 |
| Records excluded | 47 |
| Eligible records after screening | 49 |
| Studies selected and used in Chapter 2 / Appendix D | 35 |
| Core cardiopulmonary / heart-lung / chest sound separation studies | 18 |
| Background / supplementary studies | 17 |
| Eligible backup records not cited in the current report | 14 |
| Excluded papers cited | 0 |
| Missing citation keys | 0 |

The 35 selected papers are used in the Chapter 2 narrative, Chapter 2 summary matrix, or Appendix D full matrix. No new papers were added during the application-based refactor.

---

## PRISMA Tracking

PRISMA files are stored in:

```text
literature-review/prisma/
```

Current PRISMA outputs:

```text
literature-review/prisma/prisma_flow_diagram_filled.docx
literature-review/prisma/prisma_flow_diagram_filled.pdf
literature-review/prisma/prisma_flow_diagram_filled.png
report/quarto/figures/prisma/prisma_flow_diagram.png
```

The report uses the professional DOCX-based PRISMA figure, not a Mermaid-generated PRISMA diagram.

---

## Report Sources and Output

The report source is located in:

```text
report/quarto/
```

Main wrapper file:

```text
report/quarto/paper.qmd
```

Chapter sources:

```text
report/quarto/chapters/
```

Generated Word report:

```text
report/generated/paper.docx
```

The generated DOCX is the main university-compatible output. The Quarto sources and post-processing scripts are the source of truth; the generated DOCX should not be manually edited as the primary source.

---

## Report Chapters and Appendices

| Section | Title | Current status |
|---|---|---|
| Chapter 1 | Introduction | Completed for FYP1 |
| Chapter 2 | Literature Review | Completed for FYP1 |
| Chapter 3 | Requirements Analysis | Completed for FYP1; survey response analysis pending if required |
| Chapter 4 | System Design | Completed for FYP1 |
| Chapter 5 | Implementation Plan | Completed for FYP1 |
| Chapter 6 | Conclusion | Completed for FYP1 |
| References | Cited sources used in the report | Completed |
| Appendix A | Gantt Chart | Placeholder; insert final chart manually when ready |
| Appendix B | FYP1 Meeting Logs | Placeholder/check item; insert if required |
| Appendix C | Turnitin Similarity Index Page | Placeholder; insert after Turnitin report is available |
| Appendix D | Full Literature Review Matrix | Completed; landscape formatting |
| Appendix E | PRISMA Screening Summary | Completed |
| Appendix F | System Design Diagrams | Completed |
| Appendix G | Planned Test Cases and Evaluation Metrics | Completed as planned FYP2 checks |

---

## Diagrams

Editable PlantUML sources are stored in:

```text
diagrams/plantuml/
```

Rendered report figures are stored in:

```text
report/quarto/figures/plantuml/
```

Current PlantUML diagram set:

- Context diagram
- Use case diagram
- Activity diagram
- Class diagram
- Sequence diagram

The local PlantUML wrapper is:

```text
tools/plantuml.cmd
```

---

## Validation and Rendering

Validate the report:

```powershell
powershell -ExecutionPolicy Bypass -File report\quarto\scripts\validate-report.ps1
```

Regenerate the Word report:

```powershell
powershell -ExecutionPolicy Bypass -File report\quarto\scripts\render-report.ps1
```

The render script uses Quarto and then applies the DOCX post-processing script:

```text
report/quarto/scripts/fix-docx-format.py
```

The post-processing script handles Word-specific formatting such as navigation lists, header/footer sizing, appendix landscape formatting, and continuous table/figure caption numbering.

---

## Repository Structure

```text
proposal/
  FYP proposal form and related documents

report/
  final-report/
    Final report review notes
  generated/
    Generated DOCX and generated figure copies
  quarto/
    Quarto source, chapters, figures, scripts, styles, and templates

literature-review/
  metadata/
  screening/
  prisma/
  references/
  notes/
  papers/

diagrams/
  plantuml/
  mermaid/
  prisma/
  system-architecture/
  uml/
  workflow/

supervisor-updates/
  Meeting logs and supervisor-related documents

resources/
  guidelines/
  templates/
  tools/

tools/
  Local helper tools such as the PlantUML wrapper/JAR
```

---

## Reference Management

The active bibliography is:

```text
literature-review/references/references.bib
```

The Quarto report uses this BibTeX file for citations and references. Zotero is not required for the current local rendering workflow.

---

## Tools and Technologies

| Purpose | Tool / Technology |
|---|---|
| Report authoring | Quarto / Markdown |
| Final report output | Microsoft Word DOCX |
| DOCX post-processing | Python |
| Citation source | BibTeX |
| PRISMA figure | Filled Word document converted to PDF/PNG |
| UML diagrams | PlantUML |
| Graph rendering support | Graphviz |
| Version control | Git |
| Planned prototype backend direction | Python / FastAPI |
| Planned storage direction | SQLite or lightweight local storage |
| Planned ML implementation | Python-based machine learning workflow |

---

## Manual Items Before Submission

The generated report exists, but final manual checking is still required before submission:

- Open `report/generated/paper.docx` in Microsoft Word and update all fields.
- Check cover page and title page spacing.
- Confirm Table of Contents, List of Tables, List of Figures, and List of Appendices after Word field update.
- Check page numbering and page breaks.
- Confirm Appendix D landscape formatting and matrix readability.
- Insert the Gantt chart when ready.
- Insert or attach FYP1 meeting logs if required.
- Insert the Turnitin similarity index page after it is available.
- Get supervisor confirmation on final scope, dataset direction, and implementation plan.
- Update Chapter 3 only after real survey responses are collected, if the supervisor requires response analysis.

---

## Disclaimer

This project is developed for academic purposes as part of a Final Year Project.

The proposed system is a prototype / proof of concept for cardiopulmonary sound separation. It is not intended for clinical diagnosis, treatment recommendation, or medical decision-making.

---

## Author

**AL-SALOUL, ASHRAF ALI HUSSEIN**  
Student ID: 1221303805  
Bachelor of Computer Science (Hons.)  
Software Engineering Specialization  
Multimedia University, Malaysia
