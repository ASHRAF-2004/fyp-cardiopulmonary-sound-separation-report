# FYP1-main Tool Audit

Project title: **Machine Learning-Based System for Cardiopulmonary Sound Separation**

Audited folder: `resources/tools/FYP1-main/`

Current handbook used for comparison: `resources/guidelines/FYP Handbook T2610.pdf`

Audit date: 2026-05-11

## Resource Inventory

| Path | What Exists | Notes for Report Workflow |
|---|---|---|
| `resources/guidelines/FYP Handbook T2610.pdf` | Current FYP handbook, revised April 2026. | Source of truth for report order, chapter structure, formatting, references, appendices, and submission requirements. |
| `resources/guidelines/FYP1 Rubrics.pdf` | FYP1 rubric file. | Useful later for checking marking emphasis, but this audit used the handbook as the formatting source of truth. |
| `resources/guidelines/CPT6314 Teaching Plan T2610 v1.pdf` | Teaching plan. | Useful later for schedule and milestone planning. |
| `resources/templates/Sample.pdf` | Sample report PDF. | Useful as visual comparison after a future render. |
| `resources/templates/Template - Content.docx` | Word content template with copyright, declaration, acknowledgements, abstract, TOC/list placeholders, chapter headings, references, appendix, headers/footers, and Word styles. | Strong candidate for the future Quarto DOCX `reference-doc`. Needs style validation against T2610. |
| `resources/templates/Template - Cover Page and Title Page.docx` | Word cover/title page template matching handbook fields. | Useful source for cover/title layout. Quarto may need front matter QMD or post-processing to reproduce it. |
| `resources/tools/FYP1-main/` | Old Quarto/Typst report tool. | Useful reference, but not usable as-is for a Word-first T2610 workflow. |

## Old Tool Contents

| File or Folder | Purpose |
|---|---|
| `README.md` | Explains Quarto, Markdown, Typst, Pandoc, and says the tool renders an MMU FYP interim report PDF. |
| `paper.qmd` | Single-file Quarto report source with YAML metadata, FYP1 chapter skeleton, sample figure, sample table, sample citation, references block, and appendices. |
| `references.bib` | One sample BibTeX entry only. |
| `logo.png` | MMU logo image used by the Typst title page. |
| `handbookMarkDown.md` | Extracted/converted older handbook text. It shows an April 2025/T2510-era source, not the current T2610 handbook. |
| `FYP Handbook T2510.pdf` | Older handbook bundled with the tool. Not the current source of truth. |
| `_extensions/mmu-fyp/_extension.yml` | Quarto extension registration for a custom Typst format. Requires Quarto `>=1.8.0`. |
| `_extensions/mmu-fyp/typst-template.typ` | Custom Typst template for front matter, margins, page numbering, headers/footers, list of tables/figures, and main body styling. |
| `_extensions/mmu-fyp/typst-show.typ` | Pandoc/Typst variable mapping into the custom template. |
| `images/example.png` | Sample figure. |
| `showcase/showcase.gif` | Visual showcase for the old tool. |

## Capability Audit

| Question | Finding | Match Against T2610 / Current Need |
|---|---|---|
| What language/tool does it use? | Quarto `.qmd`, Markdown, Pandoc, and a custom Typst format. | Good base for Markdown-first writing. |
| How is it run? | README says open `paper.qmd` and use Quarto preview, or run `quarto preview paper.qmd`; output is expected as `paper.pdf`. | Run path is PDF-oriented and writes beside source. New workflow should render into `report/generated/`. |
| Is it Quarto-based? | Yes. `paper.qmd` declares `format: mmu-fyp-typst`, and `_extension.yml` contributes a Typst format. | Useful, but only for the optional PDF path. |
| Does it output PDF? | Yes, through Typst. README describes PDF output. | Useful as an optional checking/backup output after T2610 refactor. |
| Does it output DOCX? | No DOCX format is configured. No Word reference template is used. | Missing for the university Word-first requirement. |
| Does it support references? | Partially. It has a sample `references.bib`, sample citation `@sample2024`, and raw Typst bibliography command with APA style. | Needs refactor to use `literature-review/references/references.bib` and a DOCX-compatible APA CSL/style. |
| Does it support figures/tables/captions? | Partially. It includes a sample image, sample table, and Typst rules that place table captions above tables and image captions below images. | Good conceptually. Must validate DOCX output and chapter-based numbering. |
| Does it support List of Figures and List of Tables? | Typst template creates outlines for tables and figures. | Useful for PDF. DOCX list generation remains missing/needs refactor. |
| Does it support appendices? | Partially. `paper.qmd` includes Appendix A-D placeholders. Some comments use LaTeX-style `\includepdf`, which is not a DOCX solution and may not work in Typst as written. | Needs refactor for DOCX appendices and meeting-log/Turnitin handling. |
| Does it use a Word reference template? | No. | Missing. The repo's `resources/templates/*.docx` should be used later to build a Quarto `reference-doc`. |
| Does it match the current T2610 handbook? | Partially. It contains many same FYP1 front matter and chapter ideas, but it bundles `FYP Handbook T2510.pdf` and `handbookMarkDown.md` from an older handbook. | Needs refactor against T2610. |
| Does it match current font rules? | No. Typst template sets body text to Arial 12 pt, while T2610 requires Arial or Calibri 11 pt for normal body text. | Needs refactor. |
| Does it match current margins? | Partially. Typst template uses title-page margins of 25.4 mm and main margins of left 38 mm, right/top/bottom 28 mm. | Good for PDF; DOCX still needs validation. |
| Does it match current page numbering? | Partially. Typst template uses unnumbered cover/title, Roman preliminary pages, and Arabic main body pages. | Good for PDF; DOCX needs section/header configuration. |
| Does it match current application-based chapter structure? | Mostly. It has Chapters 1-6 and the same broad FYP1 structure. Chapter 4 uses "Rich Picture Diagram" while T2610 application-based structure asks for a Context Diagram. | Needs refactor. |
| Does it support modular chapter authoring? | No. Everything is in one large `paper.qmd`. | Needs refactor so Codex can edit chapters independently. |
| Does it isolate generated files? | No. README expects `paper.pdf` beside `paper.qmd`. | Needs refactor to `report/generated/`. |

## Quarto Availability Check

Command checked:

```powershell
quarto --version
```

Result:

```text
quarto : The term 'quarto' is not recognized as the name of a cmdlet, function, script file, or operable program.
```

Implication: Quarto is not currently available on PATH. No render test was run because the user requested no proof-of-concept generation in this phase.

## Recommendation

Do not use `resources/tools/FYP1-main/` as-is.

Use it as a reference and refactor its useful ideas into a new Word-first Quarto workflow under `report/`:

- Reuse the idea of Markdown/Quarto source files.
- Reuse the FYP front matter logic and optional Typst/PDF styling only after updating it for T2610.
- Use the current handbook, not the bundled T2510 PDF/Markdown, as the rule source.
- Use `resources/templates/Template - Content.docx` and `resources/templates/Template - Cover Page and Title Page.docx` as the basis for DOCX styling and front matter.
- Link citations to `literature-review/references/references.bib`.
- Keep the old tool untouched until a separate refactor phase is approved.

## Refactor Risk Notes

1. DOCX is the hardest part, not Markdown authoring. Margins, Roman/Arabic page numbering, TOC/list fields, and caption lists must be validated in the generated Word file.
2. Quarto/Pandoc can handle citations and references well, but APA output requires a CSL/style path for DOCX.
3. PDF appendices, meeting logs, and Turnitin pages may need a conversion step for DOCX.
4. The old Typst extension is helpful for PDF, but it does not solve the university Word-format requirement.
5. The old tool's sample `references.bib` should not replace the real literature-review bibliography.
