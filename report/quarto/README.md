# Restored FYP1 Quarto Workflow

Project title: **Machine Learning-Based System for Cardiopulmonary Sound Separation**

This folder contains the restored Quarto source and build workflow for the FYP1
report. It includes six chapter sources, report templates, figures, validation,
DOCX rendering, and DOCX post-processing.

## Important Status

This is a restored baseline workflow. It is not fully synchronized with the
final supervisor-feedback revision in `report/Submission/`.

In particular, the restored Chapter 3 source still contains the questionnaire
template and placeholder figures from before the 53 responses were analyzed.
The authoritative revised submission files are:

```text
report/Submission/1221303805_Arshad_Jamal_FYP1_Revised_Copy.docx
report/Submission/1221303805_Arshad_Jamal_FYP1_Report.pdf
```

Do not replace the final submission with a fresh Quarto render unless the
Quarto chapters have first been synchronized with the revised DOCX.

## Source Structure

| File | Purpose |
|---|---|
| `paper.qmd` | Main report source and appendices |
| `chapters/chapter-1.qmd` | Introduction |
| `chapters/chapter-2.qmd` | Literature Review |
| `chapters/chapter-3.qmd` | Requirements Analysis baseline |
| `chapters/chapter-4.qmd` | System Design |
| `chapters/chapter-5.qmd` | Implementation Plan |
| `chapters/chapter-6.qmd` | Conclusion |
| `_quarto.yml` | DOCX render configuration |
| `templates/` | Word reference and report templates |
| `figures/` | PRISMA, questionnaire, workflow, and system-design figures |
| `scripts/validate-report.ps1` | Source validation helper |
| `scripts/render-report.ps1` | DOCX rendering helper |
| `scripts/fix-docx-format.py` | Word formatting and field post-processor |

## Dependencies

- Quarto
- Python 3
- Pandoc supplied by Quarto
- Microsoft Word for final field updates and PDF export
- Graphviz and PlantUML when diagrams must be regenerated
- Mermaid CLI only when Mermaid figures must be regenerated

## Validate the Baseline

Run from the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File report/quarto/scripts/validate-report.ps1
```

## Render the Baseline

```powershell
powershell -ExecutionPolicy Bypass -File report/quarto/scripts/render-report.ps1
```

Expected output:

```text
report/generated/paper.docx
```

The generated DOCX is intentionally ignored by Git. Open it in Microsoft Word
to update fields and inspect the cover, page numbering, navigation lists,
captions, references, figures, tables, and appendices.

## Bibliography

The Quarto workflow reads:

```text
literature-review/references/references.bib
```

Literature-review decisions and PRISMA counts must not be changed as part of a
routine report render.
