# FYP1 Quarto Report Workflow

Project title: **Machine Learning-Based System for Cardiopulmonary Sound Separation**

This is the active report-generation workflow for the FYP1 interim report. It follows the current `resources/guidelines/FYP Handbook T2610.pdf` requirements and uses Quarto Markdown as the source format.

## Main Output

The primary output is MS Word DOCX:

```powershell
quarto render report/quarto/paper.qmd --to docx --output-dir report/generated
```

Expected file:

```text
report/generated/paper.docx
```

## Optional PDF Output

PDF is secondary and should be used only for checking or backup:

```powershell
quarto render report/quarto/paper.qmd --to typst --output-dir report/generated
```

## Current Source Files

| File | Purpose |
|---|---|
| `paper.qmd` | Main FYP1 report source in handbook order; includes the drafted chapter files. |
| `chapters/chapter-1.qmd` | Imported Chapter 1 introduction draft. |
| `chapters/chapter-2.qmd` | Imported Chapter 2 literature review draft. |
| `chapters/chapter-3.qmd` | Imported Chapter 3 methodology draft. |
| `_quarto.yml` | Quarto configuration for DOCX and optional Typst/PDF rendering. |
| `templates/fyp-reference.docx` | DOCX style reference copied from the current resource template. |
| `styles/apa.csl` | Local APA-like CSL fallback for render testing. Replace with official APA CSL before final submission if exact APA formatting is required. |
| `assets/figures/` | Placeholder figures and copied neutral assets used by the report source. |
| `scripts/render-report.ps1` | Repeatable render helper. |
| `scripts/validate-report.ps1` | Local validation helper. |

## Dependencies

Quarto must be installed and available on PATH.

Install steps for Windows:

1. Download Quarto from `https://quarto.org/docs/get-started/`.
2. Install the Windows MSI.
3. Close and reopen PowerShell.
4. Run:

```powershell
quarto --version
```

## Literature Review References

The workflow uses the existing bibliography directly:

```text
literature-review/references/references.bib
```

Do not copy, regenerate, or edit the literature-review bibliography from this workflow.

## Manual Checks Still Required

After a successful DOCX render, open the DOCX and verify:

- cover/title page layout
- top-right page numbering
- Roman preliminary page numbering
- Arabic numbering from Chapter 1
- body margins and title-page margins
- Arial or Calibri 11 pt body text
- heading sizes
- table captions above tables
- figure captions below figures
- table of contents
- list of figures
- list of tables
- APA reference formatting
- appendices and meeting-log placeholders
