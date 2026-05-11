# FYP1 Report Generation Plan

Project title: **Machine Learning-Based System for Cardiopulmonary Sound Separation**

Main recommendation: **Use Quarto as the report authoring and automation workflow, generate DOCX as the primary university-compatible output, and generate PDF only as a checking/backup output.**

Do not use pure LaTeX as the main workflow. Do not manually format the final report in Word. Do not refactor the old tool until the next phase.

## Decision

| Option | Recommendation | Reason |
|---|---|---|
| Quarto + Markdown/QMD -> DOCX | Use as primary workflow. | Best fit for automated chapter writing, citations, figures/tables, and Word output. |
| Quarto + Typst -> PDF | Use as optional checking/backup output. | The old tool already has useful Typst logic, but PDF is not the main submission format. |
| Pure LaTeX | Do not use as main workflow. | The university expects MS Word format; LaTeX would add conversion friction. |
| Manual Word editing | Avoid. | It breaks repeatability and makes Codex automation harder. |

## Current Tool Situation

- `resources/tools/FYP1-main/` is useful but outdated.
- It uses Quarto and a custom Typst extension.
- It appears designed mainly for PDF output.
- It bundles an older `FYP Handbook T2510.pdf`, while the current source of truth is `resources/guidelines/FYP Handbook T2610.pdf`.
- It does not currently provide a DOCX-first workflow.
- Quarto is not installed or not available on PATH on this machine.

## Target Workflow

```mermaid
flowchart TD
  A[Codex writes QMD chapter files] --> B[Quarto assembles report/index.qmd]
  B --> C[Citations from literature-review/references/references.bib]
  B --> D[Figures, tables, diagrams, PRISMA assets]
  C --> E[Quarto citeproc with APA CSL]
  D --> F[Captioned cross-references]
  E --> G[DOCX render using FYP Word reference template]
  F --> G
  G --> H[report/generated/fyp1-report.docx]
  G --> I[Optional PDF check output]
  H --> J[Validation checklist: formatting, numbering, citations, captions]
```

## Proposed Final Source Structure

Reuse the existing `report/` folder and keep chapter ownership clear:

```text
report/
  _quarto.yml
  index.qmd
  metadata/
    project.yml
  frontmatter/
    00-cover-and-title.qmd
    01-copyright.qmd
    02-declaration.qmd
    03-acknowledgements.qmd
    04-abstract.qmd
    05-lists.qmd
  chapter-1-introduction/
    chapter.qmd
  chapter-2-literature-review/
    chapter.qmd
  chapter-3-methodology/
    chapter.qmd
  chapter-4-design-and-implementation/
    chapter.qmd
  chapter-5-testing-and-evaluation/
    chapter.qmd
  final-report/
    notes.md
  appendices/
    appendix-a-gantt-chart.qmd
    appendix-b-fyp1-meeting-logs.qmd
    appendix-c-turnitin-similarity.qmd
    appendix-d-technical-documentation.qmd
  assets/
    figures/
    tables/
    diagrams/
  templates/
    fyp-reference.docx
    fyp-cover-title-reference.docx
  styles/
    apa.csl
  scripts/
    render-report.ps1
    validate-report.ps1
  generated/
    fyp1-report.docx
    fyp1-report.pdf
```

Notes:

- The existing chapter folder names can remain.
- `chapter-3-methodology/` can hold the FYP1 "Requirements Analysis" source for now, or it can be renamed later if the user wants exact handbook naming.
- `chapter-4-design-and-implementation/` can hold the FYP1 "System Design" source for now, or it can be split later for FYP2.
- `generated/` should be ignored as output and should be the only destination for generated DOCX/PDF files.

## Files to Create Later

| File | Purpose |
|---|---|
| `report/_quarto.yml` | Quarto project configuration, bibliography path, output settings, cross-reference settings, and format definitions. |
| `report/index.qmd` | Main assembly file that includes front matter, chapters, references, and appendices in handbook order. |
| `report/metadata/project.yml` | Project ID, title, student name/ID, programme, supervisor, submission month/year, term, course code. |
| `report/frontmatter/*.qmd` | Editable front matter content. |
| `report/*/chapter.qmd` | Modular chapter source files. |
| `report/appendices/*.qmd` | Required FYP1 appendix sources. |
| `report/templates/fyp-reference.docx` | DOCX reference template derived from `resources/templates/Template - Content.docx`. |
| `report/templates/fyp-cover-title-reference.docx` | Cover/title reference derived from `resources/templates/Template - Cover Page and Title Page.docx` if needed. |
| `report/styles/apa.csl` | APA citation style file for DOCX output. |
| `report/scripts/render-report.ps1` | Repeatable render command. |
| `report/scripts/validate-report.ps1` | Formatting/citation/output checklist. |

## Files to Keep

- Keep `resources/tools/FYP1-main/` unchanged as a reference copy.
- Keep `resources/guidelines/FYP Handbook T2610.pdf` as the source of truth.
- Keep `resources/templates/*.docx` as Word-template references.
- Keep all `literature-review/` data untouched.
- Keep existing `report/` chapter folders unless the user approves a rename.

## Files Not to Replace Yet

- Do not replace `resources/tools/FYP1-main/paper.qmd`.
- Do not replace `resources/tools/FYP1-main/_extensions/mmu-fyp/*`.
- Do not replace `literature-review/references/references.bib`.
- Do not generate `report/generated/*.docx` or `report/generated/*.pdf` in this planning phase.

## Quarto Configuration Direction

The future `report/index.qmd` should be a single assembly document using includes, rather than relying on Quarto book output. This keeps DOCX output simpler and more predictable:

```markdown
{{< include frontmatter/01-copyright.qmd >}}
{{< include frontmatter/02-declaration.qmd >}}
{{< include chapter-1-introduction/chapter.qmd >}}
{{< include chapter-2-literature-review/chapter.qmd >}}
```

The future Quarto configuration should use:

```yaml
bibliography: ../literature-review/references/references.bib
csl: styles/apa.csl
format:
  docx:
    reference-doc: templates/fyp-reference.docx
    toc: true
```

PDF should be a secondary format:

```yaml
format:
  typst:
    toc: true
```

If the old Typst extension is reused, copy it into `report/_extensions/` later and update it against T2610 before rendering.

## How Codex Should Write Chapters

Codex should write one chapter source file at a time, using the handbook structure:

- Chapter 1: Introduction
  - Overview
  - Problem Statement
  - Project Objectives
  - Project Scope
  - Project Limitations
  - Methodology
  - Target Audience
  - Summary
- Chapter 2: Literature Review
  - Use the audited literature-review records and `references.bib`.
  - Focus on cardiopulmonary sound separation, heart-lung sound separation, biomedical audio source separation, preprocessing, models, datasets, metrics, and research gaps.
- Chapter 3: Requirements Analysis
  - Use application-based project requirements, functional requirements, non-functional requirements, and user requirements.
- Chapter 4: System Design
  - Include context diagram, use case diagram, use case descriptions, activity diagram, class diagram, sequence diagram, and interface design.
- Chapter 5: Implementation Plan
  - Development phase, testing phase, deployment phase if applicable.
- Chapter 6: Conclusion
  - Achievements so far, remaining FYP2 work, issues encountered.

## Citation Workflow

Use:

```text
literature-review/references/references.bib
```

Rules:

- Do not copy or regenerate the bibliography unless the literature-review phase asks for it.
- Cite in QMD using Pandoc citation syntax, for example `[@citationKey]`.
- Use APA CSL for DOCX.
- Validate that every citation key used in chapters exists in `references.bib`.
- Validate that generated references are APA-style and use hanging indents/double spacing in DOCX.

## Figures, Tables, Captions, and Diagrams

Use Quarto cross-reference syntax:

```markdown
![System architecture](assets/diagrams/system-architecture.png){#fig-system-architecture}
```

Refer to figures in text:

```markdown
As shown in @fig-system-architecture, ...
```

Tables should use captions above the table where DOCX permits it. This must be validated after the first render because DOCX caption placement can differ from PDF/Typst behavior.

Diagram sources:

- Keep Mermaid or PlantUML source files in `diagrams/` or `report/assets/diagrams/`.
- Render DOCX-friendly images, preferably PNG, before including them.
- Include `literature-review/prisma/prisma_flow_diagram.png` directly or copy it into `report/generated/assets/` at render time. Do not modify the literature-review PRISMA source during report generation.

## Appendices

Required FYP1 appendices:

- Appendix A: Gantt Chart
- Appendix B: FYP I Meeting Logs
- Appendix C: Turnitin Similarity Index Page
- Appendix D: Technical documentation, if needed

Implementation notes:

- Appendices must be referenced from the body text.
- Meeting logs and Turnitin PDF pages may need conversion to images for DOCX insertion.
- Raw LaTeX `\includepdf` comments from the old tool should not be used for DOCX.

## DOCX Output Plan

Primary command after Quarto is installed and the scaffold exists:

```powershell
quarto render report/index.qmd --to docx --output-dir report/generated
```

Expected output:

```text
report/generated/fyp1-report.docx
```

DOCX validation must check:

- Cover and title page layout.
- Body margins: left 38 mm, right 28 mm, top 28 mm, bottom 28 mm.
- Cover/title margins: 25.4 mm all sides.
- Normal text: Arial or Calibri, 11 pt, justified.
- Heading sizes: 14 pt bold for chapter heading, 12 pt bold for sub-heading, 11 pt bold for sub-sub-heading.
- Line spacing and paragraph indentation.
- Top-right page numbers.
- Roman preliminary page numbering.
- Arabic body numbering starting at Chapter 1.
- TOC, List of Tables, List of Figures, List of Abbreviations/Symbols, List of Appendices.
- Figure captions below figures.
- Table captions above tables.
- APA citations and reference list formatting.

## PDF Output Plan

PDF is optional and secondary.

Preferred options, in order:

1. Generate PDF from the validated DOCX using Word or LibreOffice headless, so the PDF mirrors the actual submission file.
2. Reuse the old Quarto Typst extension as an optional PDF renderer after updating it to T2610.

Do not make PDF the source of truth.

## Old FYP1-main Refactor Plan

If approved in a later phase, refactor by copying useful parts rather than editing the old folder in place.

Target folder:

```text
report/_extensions/mmu-fyp-typst/
```

Files to keep or reuse:

- `resources/tools/FYP1-main/logo.png`
- Concept from `_extensions/mmu-fyp/typst-template.typ`
- Concept from `_extensions/mmu-fyp/typst-show.typ`
- Chapter skeleton ideas from `paper.qmd`

Files to avoid copying as active sources:

- `resources/tools/FYP1-main/FYP Handbook T2510.pdf`
- `resources/tools/FYP1-main/handbookMarkDown.md`
- `resources/tools/FYP1-main/references.bib`
- `resources/tools/FYP1-main/images/example.png`
- `resources/tools/FYP1-main/showcase/showcase.gif`

Files to update during refactor:

- Change body font from Arial 12 pt to Arial/Calibri 11 pt.
- Update chapter structure to T2610 application-based wording.
- Replace "Rich Picture Diagram" with "Context Diagram".
- Link bibliography to `../literature-review/references/references.bib`.
- Add DOCX output configuration.
- Add output directory `report/generated/`.
- Add APA CSL for DOCX.
- Add Word reference template support.

How to include diagrams and PRISMA:

- Reference stable image paths from `report/assets/diagrams/`.
- Use `literature-review/prisma/prisma_flow_diagram.png` as a read-only source.
- Add a render step that can copy generated diagram assets into `report/generated/assets/` without changing the literature-review folder.

How to generate List of Figures and List of Tables:

- For PDF/Typst, reuse or update the old Typst outline logic.
- For DOCX, use Word fields or a post-processing step if Quarto/Pandoc output does not generate complete lists automatically.
- Validate the generated DOCX in Word before submission.

## Quarto Installation Steps

Current check:

```powershell
quarto --version
```

Current result: Quarto is not recognized on PATH.

Install steps for Windows:

1. Download the Windows installer from `https://quarto.org/docs/get-started/`.
2. Install Quarto using the MSI installer.
3. Close and reopen PowerShell.
4. Run:

```powershell
quarto --version
```

5. If reusing the old Typst extension, make sure the installed Quarto version satisfies the extension requirement `>=1.8.0`, or update the extension after checking current Quarto compatibility.
6. Optional: install the Quarto VS Code extension for preview while editing.

## Future Verification Commands

Do not run these until the report scaffold/refactor phase is approved.

```powershell
quarto --version
quarto render report/index.qmd --to docx --output-dir report/generated
quarto render report/index.qmd --to typst --output-dir report/generated
```

Expected checks after render:

- `report/generated/fyp1-report.docx` exists.
- Optional `report/generated/fyp1-report.pdf` exists if PDF generation is enabled.
- Citations compile without missing keys.
- References render from `literature-review/references/references.bib`.
- Figure and table captions appear in the correct positions.
- Generated files are placed only in `report/generated/`.

## Phase Boundary

This phase created planning and audit documents only.

No full report chapters were written.
No DOCX or PDF was generated.
No proof-of-concept was created.
No `literature-review/` tracking data was modified.
