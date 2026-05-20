# FYP Report: Cardiopulmonary Sound Separation

## Project Title

**Machine Learning-Based System for Cardiopulmonary Sound Separation**

## Repository Purpose

This repository documents and tracks the progress of my Final Year Project (FYP1) report.

The repository focuses on the complete report workflow, including:

- FYP proposal documentation
- Literature review collection and screening
- PRISMA-based search and screening documentation
- Literature review matrix preparation
- Reference and citation management
- Chapter-by-chapter report writing
- Methodology and system design documentation
- System diagrams
- Quarto-based DOCX report generation
- Supervisor meeting logs and progress tracking
- Final FYP1 report preparation

This repository is intended to show clear academic progress and provide an organized record of the FYP1 report development process.

---

## Project Overview

Cardiopulmonary sounds include heart and lung sounds that are commonly recorded together using a stethoscope. These sounds may overlap in time and frequency, making separation difficult using traditional signal processing methods.

This project focuses on a **machine learning-based software system** for separating mixed cardiopulmonary audio signals into two outputs:

1. Heart sound signal
2. Lung sound signal

The project is developed as a **Software Engineering application-based prototype/proof of concept**. The focus is sound separation only, not disease detection or medical diagnosis.

---

## Project Scope

The project focuses on:

- Cardiopulmonary sound separation
- Heart and lung sound separation
- Machine learning-based audio separation
- Audio preprocessing
- Feature extraction / input representation
- Public datasets
- System design and implementation planning
- Evaluation metrics for audio separation
- FYP1 report documentation and formatting

The project does **not** focus on disease detection, clinical diagnosis, or medical decision-making.

---

## FYP Objectives

The objectives of this project are:

1. To study and apply suitable preprocessing techniques to reduce noise and improve the quality of cardiopulmonary sound recordings.
2. To design and implement a machine learning-based approach for separating mixed cardiopulmonary recordings into heart and lung sound outputs.
3. To develop a reusable software prototype and evaluate its separation performance using public datasets and suitable performance metrics.

---

## Current Report Status

The repository has progressed beyond the initial literature review setup. The current status is:

| Area | Status |
|---|---|
| Repository structure | Completed |
| Literature review tracking files | Completed |
| Paper screening | Completed |
| PRISMA tracking | Completed |
| PRISMA diagram | Professional PRISMA 2020 version prepared |
| Literature review matrix | Completed |
| Chapter 1: Introduction | Completed |
| Chapter 2: Literature Review | Completed |
| Chapter 3: Methodology | Completed |
| Chapter 4: Design and Implementation | Completed for FYP1 report |
| Chapter 5: Testing and Evaluation | Completed for FYP1 report |
| Quarto DOCX workflow | Working |
| Generated Word report | Available in `report/generated/paper.docx` |
| Final formatting | Ongoing manual checking and refinement |

---

## Literature Review Progress

The literature review process includes systematic search, screening, classification, and synthesis.

Current literature review summary:

| Item | Count |
|---|---:|
| Records considered | 96 |
| Records excluded | 47 |
| Eligible records after screening | 49 |
| Papers selected and used in Chapter 2 / Appendix A | 35 |
| Core cardiopulmonary / heart-lung / chest sound separation studies | 18 |
| Background / supplementary studies | 17 |
| Eligible backup records not cited in the current report | 14 |
| Excluded papers cited | 0 |

The 35 selected papers are used in Chapter 2 or Appendix A. The selected papers include core sound separation studies and supporting studies related to datasets, preprocessing, machine learning methods, evaluation metrics, and background context.

---

## PRISMA Tracking

The PRISMA workflow documents the paper search and screening process.

PRISMA files are stored in:

```text
literature-review/prisma/
```

The professional PRISMA figure used in the report is stored in:

```text
report/quarto/figures/prisma/
```

The report uses a professional PRISMA 2020-style diagram instead of a Mermaid-based diagram.

---

## Literature Review Matrix

The report contains:

1. A concise literature review matrix in Chapter 2.
2. A full literature review matrix in Appendix A.

Appendix A is formatted in landscape orientation for readability. The full matrix summarizes selected studies using details such as research title, authors, source, objective, method, dataset, findings, research gap, limitation, and relevance to this project.

---

## Report Generation Workflow

The report is written using a Quarto-based workflow.

The main report source is located in:

```text
report/quarto/
```

The generated Word report is located in:

```text
report/generated/paper.docx
```

The workflow is designed to generate a Microsoft Word `.docx` report as the main university-compatible output. Quarto is used only as the authoring and automation tool; the submitted file is the generated Word document.

---

## Report Chapters

| Chapter | Title | Status |
|---|---|---|
| Chapter 1 | Introduction | Completed |
| Chapter 2 | Literature Review | Completed |
| Chapter 3 | Methodology | Completed |
| Chapter 4 | Design and Implementation | Completed for FYP1 report |
| Chapter 5 | Testing and Evaluation | Completed for FYP1 report |
| References | Cited sources used in the report | Completed |
| Appendix A | Full Literature Review Matrix | Completed |
| Appendix B | PRISMA Screening Summary | Completed |
| Appendix C | System Design Diagrams | Completed |
| Appendix D | Planned Test Cases and Evaluation Metrics | Completed |

---

## Diagrams

The report includes diagrams for literature review and system design.

Diagram types used:

- PRISMA 2020 flow diagram
- PlantUML use case diagram
- PlantUML component diagram
- PlantUML sequence diagram
- Mermaid workflow diagram for simple process flow

PlantUML is preferred for UML-style diagrams, especially use case, component, and sequence diagrams.

---

## Repository Structure

```text
proposal/
  FYP proposal form and related documents

report/
  chapter-1-introduction/
  chapter-2-literature-review/
  chapter-3-methodology/
  chapter-4-design-and-implementation/
  chapter-5-testing-and-evaluation/
  final-report/
  generated/
  quarto/

literature-review/
  metadata/
  screening/
  prisma/
  references/
  notes/
  papers/

diagrams/
  erd/
  prisma/
  system-architecture/
  uml/
  workflow/
  plantuml/

supervisor-updates/
  Meeting logs and supervisor-related documents

resources/
  guidelines/
  templates/
  tools/
```

---

## Reference Management

References are managed using:

- Zotero
- BibTeX
- APA-style reference output where needed

Reference files are stored in:

```text
literature-review/references/
```

The Quarto report uses the bibliography from the literature review reference files to avoid reference duplication and maintain consistency.

---

## Tools and Technologies

| Purpose | Tool / Technology |
|---|---|
| Report authoring | Quarto / Markdown |
| Final report output | Microsoft Word DOCX |
| Citation management | Zotero, BibTeX |
| Literature tracking | CSV files |
| PRISMA diagram | PRISMA 2020 Word/PDF/PNG workflow |
| UML diagrams | PlantUML |
| Simple workflow diagrams | Mermaid |
| Version control | Git and GitHub |
| Planned backend / prototype direction | Python / FastAPI |
| Planned database | SQLite |
| Planned ML implementation | Python-based machine learning workflow |

---

## Progress Updates

Supervisor-related progress files are stored in:

```text
supervisor-updates/
```

This may include meeting logs, supervisor comments, progress notes, and other FYP administration files.

---

## Manual Items Before Submission

The generated report is available, but final manual checking is still required before submission.

Remaining checks include:

- Open the generated Word file and update all fields.
- Check the cover page and title page spacing.
- Confirm table of contents, list of tables, list of figures, and list of appendices are clickable.
- Check page numbering and section formatting.
- Confirm Appendix A landscape formatting.
- Add or attach meeting logs if required.
- Add Turnitin page if required.
- Review final formatting against the FYP handbook and faculty template.
- Get supervisor feedback and make corrections if needed.

---

## Disclaimer

This project is developed for academic purposes as part of a Final Year Project.

The proposed system is a prototype/proof of concept and is not intended for clinical diagnosis or medical decision-making.

---

## Author

**AL-SALOUL, ASHRAF ALI HUSSEIN**  
Bachelor of Computer Science (Hons.)  
Software Engineering Specialization  
Multimedia University, Malaysia
