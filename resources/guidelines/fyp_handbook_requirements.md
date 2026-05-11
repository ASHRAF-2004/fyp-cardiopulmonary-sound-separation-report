# FYP Handbook T2610 Report Requirements

Project title: **Machine Learning-Based System for Cardiopulmonary Sound Separation**

Source of truth: `resources/guidelines/FYP Handbook T2610.pdf`

Handbook revision shown in PDF: April 2026

Scope of this extraction: FYP1 interim report requirements, with application-based project structure as the primary target for this project.

Status legend:

- `supported`: already supported by the old `FYP1-main` tool or by the proposed Quarto workflow with only normal configuration.
- `needs refactor`: partially supported, but the old tool or proposed workflow needs changes before it should be used.
- `missing`: not currently supported by the old tool.
- `unclear`: handbook text does not fully define the implementation detail, so this must be confirmed or validated.

| Requirement | Handbook Source | Implication for Report Tool | Status |
|---|---|---|---|
| The report must be an individual report, even for group projects. | Section 3.3, p. 7 | Report metadata and generated front matter must represent the student's individual project scope. | supported |
| FYP1 report is submitted as a soft copy in eBwise and to the moderator by the deadline. | Section 3.2, p. 7; Section 3.4, p. 7 | The workflow should produce a clean submission file, with DOCX as the primary target because the university expects MS Word format. | needs refactor |
| FYP1 submission must include the interim report, at least six meeting logs, and Turnitin Similarity Index Report with overall similarity index <= 20%. | Section 3.4, p. 7; Appendix B, p. 32 | Appendices must include meeting logs and Turnitin page placeholders or inserted pages. The tool should keep these as required appendix slots. | needs refactor |
| Meeting logs must be attached as an appendix to the report. | Section 3.4, p. 7; Appendix B, p. 32 | Appendix handling must support attached/generated meeting-log pages. PDF appendices may need conversion to images for DOCX. | needs refactor |
| Interim report should contain Declaration, Acknowledgements, Abstract, Table of Contents, Chapters 1-6, References, and Appendices. | Section 3.4.1, pp. 8-9 | The report scaffold must include these front matter, chapter, reference, and appendix files. | supported |
| Declaration page must include a student declaration with signature/date area. | Section 3.4.1, p. 8; Figure 4, p. 22 | Front matter template must generate the declaration page and leave signature/date area. | needs refactor |
| Acknowledgements should thank supervisor, parents, friends, and others involved in the study. | Section 3.4.1, p. 8 | Front matter should provide an editable acknowledgements source file. | supported |
| Abstract should summarize the project in one page and not more than two pages. | Section 3.4.1, p. 8 | Abstract source should be separate and validated by length/page estimate before submission. | supported |
| Table of Contents must list preliminary pages, chapter headings, bibliography, and appendices; page numbers must be consistently placed at the top-right corner. | Section 3.4.1, p. 8 | DOCX workflow must generate or insert a Word TOC field and maintain top-right page numbers. | needs refactor |
| Suggested FYP1 order: cover, title page, copyright, declaration, acknowledgements, abstract, TOC, list of tables, list of figures, list of abbreviations/symbols, list of appendices, chapters, references, appendices. | Section 3.4.2, p. 10 | `report/index.qmd` must assemble files in this order. | needs refactor |
| For application-based FYP1 projects, Chapter 1 should include overview, problem statement, objectives, scope, limitations, methodology, target audience, and summary. | Section 3.4.2, p. 11 | Chapter 1 source file should use these headings. | supported |
| For application-based FYP1 projects, Chapter 2 should be Literature Review with overview, topic sections, and summary. | Section 3.4.2, p. 11 | Chapter 2 should be generated from the existing literature-review evidence and cite `literature-review/references/references.bib`. | supported |
| For application-based FYP1 projects, Chapter 3 should be Requirements Analysis with fact-finding techniques, justification, questionnaire/interview/observation analysis if used, functional requirements, non-functional requirements, and user requirements. | Section 3.4.2, p. 11 | Chapter 3 scaffold must reflect requirements analysis, not research-only theory. | needs refactor |
| For application-based FYP1 projects, Chapter 4 should be System Design with context diagram, use case diagram and descriptions, activity diagram, class diagram, sequence diagram, interface design, and summary. | Section 3.4.2, p. 12 | Existing diagram folders can feed this chapter. Old tool should be updated from "Rich Picture Diagram" to "Context Diagram". | needs refactor |
| For application-based FYP1 projects, Chapter 5 can be Data Analysis Plan or Implementation Plan. Implementation Plan includes development phase, testing phase, and deployment phase if applicable. | Section 3.4.2, p. 12 | For this software prototype, use Implementation Plan. | supported |
| Chapter 6 should summarize what has been achieved against objectives, what remains for next phase, and issues encountered. | Section 3.4.1, p. 9; Section 3.4.2, p. 12 | Chapter 6 should stay concise and progress-focused for FYP1. | supported |
| FYP1 references must include all materials referred to in the report and all cited sources must be cited at appropriate places. APA style is compulsory. | Section 3.4.1, p. 9; Section 5, p. 23 | Quarto must use citeproc with `literature-review/references/references.bib` and an APA CSL/style. Citation validation should check missing references and uncited entries. | needs refactor |
| Appendices may include technical details, specifications, design documents, prototype code listings, meeting logs, Turnitin page, and Gantt chart. | Section 3.4.1, p. 9; Section 3.4.2, p. 12 | Appendix files should be explicit and referenced from body text. | supported |
| Typical interim report length is 9,000 to 12,000 words, approximately 40 pages, excluding preliminary pages and appendices. | Section 4, p. 14 | Add a future word-count validation step for body chapters only. | missing |
| Cover and title page must contain project ID and title, student ID and name, programme of study, university name, and month/year of submission. | Section 4, p. 14; Figure 1, p. 19; Figure 2, p. 20 | Metadata file must drive cover/title pages. Missing personal/project fields should fail validation before final render. | needs refactor |
| Cover and title page margins are 25.4 mm on all sides. | Section 4, p. 14 | DOCX template or post-processing must apply separate first-section margins. | needs refactor |
| Body font: normal text should be Arial or Calibri, 11-point, not bold or narrow, justified. | Section 4, pp. 14-15 | DOCX reference template must set Normal style to Arial/Calibri 11 pt justified. Old Typst template uses Arial 12 pt and must be corrected if reused. | needs refactor |
| Chapter heading: Arial or Calibri, 14 pt, bold. | Section 4, p. 14 | Heading 1 style must match. | needs refactor |
| Sub-heading: Arial or Calibri, 12 pt, bold. | Section 4, p. 14 | Heading 2 style must match. | needs refactor |
| Sub-sub-heading: Arial or Calibri, 11 pt, bold. | Section 4, p. 15 | Heading 3 style must match. | needs refactor |
| Line spacing should be one-and-a-half spacing; next paragraph should use double spacing and paragraph indent of 12.7 mm. Tables or charts should use single spacing. | Section 4, p. 14 | DOCX paragraph styles must be tuned. Tables need a separate table text style. | needs refactor |
| Main report margins: left 38 mm, right 28 mm, top 28 mm, bottom 28 mm. | Section 4, p. 15 | DOCX sections and optional PDF template must apply these margins after title pages. | needs refactor |
| Page numbers must be at the top-right corner. Every page except cover and title page must be numbered. Preliminary pages use lower-case Roman numerals; main text starts at Arabic page 1 from Introduction and continues consecutively. | Section 4, p. 15 | DOCX must use section breaks and header page-number fields. This is a key validation item. | needs refactor |
| Copyright page, declaration, acknowledgements, abstract, TOC, list of tables, list of figures, list of abbreviations/symbols, and list of appendices use lower-case Roman numerals. | Section 4, p. 15 | Front matter section numbering must be validated in DOCX. | needs refactor |
| Chapter body, references, and appendices use Arabic numerals and continue consecutively. | Section 4, p. 15 | Main body and appendix sections must not restart numbering after Chapter 1. | needs refactor |
| Illustrations should be readable, may be colour or black-and-white, and must respect the 38 mm left margin. | Section 4, p. 16 | Diagrams and screenshots should be exported at report-ready resolution and checked for fit. | supported |
| All tables, charts, figures, and graphs must be numbered and titled. Figure captions go below figures; table captions go above tables. | Section 4, pp. 16-17 | Quarto cross-references must be used for every figure/table. DOCX caption placement must be validated. | needs refactor |
| Figures and tables should appear after first mention in the text and be referred to by number. | Section 4, p. 16 | Chapter writing workflow must require a text reference before each figure/table include. | supported |
| Figure and table numbering should include chapter number followed by sequential number, e.g. Figure 1.2 and Table 1.1. | Section 4, pp. 16-17 | Quarto/Pandoc cross-reference configuration or post-processing must support chapter-based numbering. | unclear |
| Long tables/figures that span more than one page should show the number and "continued" on each additional page. | Section 4, p. 17 | This likely requires manual table splitting or Word-specific handling. | unclear |
| Diagrams must be numbered, titled, easy to understand, and referred to/elaborated in the text. Graphs need clear units, data points, and legends where applicable. | Section 4, pp. 17-18 | Mermaid/UML/system diagrams should be rendered as high-resolution images and included with proper captions. | supported |
| Project ID follows the format `CCCCC-SS-TTTTT-NNNN`, e.g. `FYP01-IS-T2530-0001`; specialisation code includes `SE` for Software Engineering. | Section 4, p. 18 | Project metadata should include `project_id` and validate format when known. | supported |
| APA citation style is mandatory. | Section 5, p. 23; Appendix A, pp. 24-31 | Use APA CSL for DOCX and validate author-date in-text citations. | needs refactor |
| Reference list should be double-spaced and use hanging indents. | Section 5, p. 23 | DOCX reference style must set spacing and hanging indent. | needs refactor |
| Every quoted/cited reference must appear in the reference list. | Section 5, p. 23 | Add citation compilation and missing-reference checks. | supported |
| Statements beyond common knowledge should be cited. | Section 5, p. 23 | Codex chapter writing should add citations for technical claims, datasets, methods, and metrics. | supported |
| Short quotations, long quotations, paraphrases, and summaries must be cited according to APA guidance. | Appendix A, pp. 24-25 | The workflow should prefer paraphrase/synthesis over long quotation and keep any direct quotes properly cited. | supported |
| Appendices must be useful, referred to in the text, and contain supplementary material that would distract from the body. | Section 6 / Appendices, p. 24 | Appendix includes must be referenced from chapters and not used as a dumping ground. | supported |
| The handbook says soft-copy submission, but does not explicitly state `.docx` as the required file extension. | Section 3.2, p. 7; Section 3.4, p. 7 | Because the university expectation is MS Word, the project workflow should still target DOCX first, with PDF only as a checking/backup output. | unclear |

## Immediate Tool Implications

1. The report workflow should be Word-first: `.qmd` sources should render to `.docx` using a Word reference template.
2. The old `FYP1-main` Typst extension can be reused only as an optional PDF path after updating font size, chapter details, and T2610 wording.
3. The old tool must not be used as-is because it is based on the older T2510 handbook source and only targets PDF through Typst.
4. The current Word templates in `resources/templates/` are important starting points for DOCX styling and front matter.
5. The final validation checklist must check DOCX page numbering, margins, font, line spacing, captions, APA citations, generated references, and appendix order.
