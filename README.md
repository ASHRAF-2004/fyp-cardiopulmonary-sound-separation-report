# FYP Report: Cardiopulmonary Sound Separation

## Project Title

**Machine Learning-Based System for Cardiopulmonary Sound Separation**

## Repository Purpose

This repository now keeps the cleaned local submission package and supporting evidence for my Final Year Project 1 report.

The project is an **Application-Based FYP1 report** for a Software Engineering prototype / proof of concept. The report focuses on cardiopulmonary sound separation only. It does not claim disease diagnosis, clinical decision-making, completed model scores, completed implementation results, or completed user acceptance findings.

The previous Quarto source/build workflow and local tool folders have been removed from this working copy. The repository should now be treated mainly as a final report package, literature review evidence store, questionnaire evidence store, and supervisor update archive.

---

## Current Main Report File

The current main report file is:

```text
report/1221303805_Arshad_Jamal_FYP1_Report.docx
```

The latest editable/report-generation sources are no longer present in this working copy. To regenerate the report from Quarto, restore the removed source folders from Git history or a backup first.

---

## Current Report Status

| Area | Current status |
|---|---|
| Report type | Application-Based FYP1 report |
| Main submission format | Microsoft Word DOCX |
| Chapter 1 | Introduction completed for FYP1 |
| Chapter 2 | Literature Review completed for FYP1 |
| Chapter 3 | Requirements Analysis updated using 53 Google Form responses |
| Chapter 4 | System Design completed for FYP1 prototype scope |
| Chapter 5 | Implementation Plan completed for planned FYP2 work |
| Chapter 6 | Conclusion completed for FYP1 |
| Questionnaire evidence | Preserved under `report/questionnaire/` |
| Literature review evidence | Preserved under `literature-review/` |
| Meeting logs | Preserved under `supervisor-updates/` |

---

## Project Overview

Cardiopulmonary recordings may contain heart sounds, lung sounds, breathing artefacts, body movement, sensor noise, and environmental noise in the same audio signal. Heart and lung components may also overlap in time and frequency, so simple filtering alone may not separate the signals cleanly.

This project proposes a **machine learning-based software prototype** that separates a mixed cardiopulmonary audio recording into:

1. Heart sound output
2. Lung sound output

The intended contribution is a reusable software workflow for upload, validation, preprocessing, model selection, separation, output generation, result viewing, download, and planned evaluation using public datasets and suitable separation metrics.

---

## FYP Objectives

1. To study and apply suitable preprocessing techniques to reduce noise and improve the quality of cardiopulmonary sound recordings.
2. To design and implement a machine learning-based approach for separating mixed cardiopulmonary recordings into heart and lung sound outputs.
3. To develop a reusable software prototype and evaluate its separation performance using public datasets and suitable performance metrics.

---

## Preserved Evidence and Supporting Files

### Literature Review

The literature review evidence is preserved in:

```text
literature-review/
```

Important files include:

```text
literature-review/references/references.bib
literature-review/references/references_apa.md
literature-review/prisma/prisma_counts.json
literature-review/prisma/prisma_diagram_notes.md
literature-review/prisma/prisma_flow_diagram_filled.docx
literature-review/prisma/prisma_flow_diagram_filled.pdf
literature-review/prisma/prisma_flow_diagram_filled.png
literature-review/screening/
literature-review/metadata/
literature-review/papers/pdfs/
```

PRISMA tracking used these counts:

| Item | Count |
|---|---:|
| Records considered | 96 |
| Records excluded | 47 |
| Eligible records after screening | 49 |
| Studies selected and used in the report | 35 |
| Core separation studies | 18 |
| Background / supplementary studies | 17 |
| Eligible backup records not cited in the report | 14 |
| Excluded papers cited | 0 |

### Questionnaire

The questionnaire evidence is preserved in:

```text
report/questionnaire/
```

Important files include:

```text
report/questionnaire/User Requirements Questionnaire for Machine Learning-Based Cardiopulmonary Sound Separation System.csv
report/questionnaire/Results/Results.docx
report/questionnaire/Results/User Requirements Questionnaire for Machine Learning-Based Cardiopulmonary Sound Separation System.pdf
report/questionnaire/Results/Figures/
report/questionnaire/Questions/
```

The report uses 53 real Google Form responses. Chapter 3 summarizes Section A in text and uses selected requirement-focused charts from Sections B to E.

### Supervisor Updates

The supervisor update folder is:

```text
supervisor-updates/
```

It contains the FYP1 meeting log template and Meeting Logs 1 to 6:

```text
Meeting-Log-1.pdf
Meeting-Log-2.pdf
Meeting-Log-3.pdf
Meeting-Log-4.pdf
Meeting-Log-5.pdf
Meeting-Log-6.pdf
```

### Guidelines and Templates

The preserved guideline/template files are:

```text
resources/guidelines/FYP Handbook T2610.pdf
resources/guidelines/FYP1 Rubrics.pdf
resources/guidelines/CPT6314 Teaching Plan T2610 v1.pdf
resources/templates/
```


---

## Manual Items Before Submission

Before submitting, check the final DOCX manually in Microsoft Word:

- Open `report/1221303805_Arshad_Jamal_FYP1_Report.docx`.
- Update all Word fields if needed.
- Check the cover page and title page spacing.
- Confirm the submission month/year is correct.
- Confirm Table of Contents, List of Tables, List of Figures, and List of Appendices.
- Check page numbering and page breaks.
- Confirm Gantt chart, questionnaire charts, PRISMA figure, tables, and appendices are readable.
- Confirm Meeting Logs 1 to 6 are inserted or submitted as required.
- Insert or submit the Turnitin similarity index page according to the FYP instructions.
- Get supervisor confirmation before final submission.

---

## Author

**AL-SALOUL, ASHRAF ALI HUSSEIN**  
Student ID: 1221303805  
Bachelor of Computer Science (Hons.)  
Software Engineering Specialization  
Multimedia University, Malaysia
