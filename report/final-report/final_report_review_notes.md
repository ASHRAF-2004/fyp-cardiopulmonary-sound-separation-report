# Final Report Review Notes

Report title: Machine Learning-Based System for Cardiopulmonary Sound Separation

Main output: `report/generated/paper.docx`

## Refactor Status

- Report refactored to the FYP Handbook T2610 Application-Based Project structure.
- Chapter 1 is Introduction with expanded cited problem statements and exactly 3 project objectives.
- Chapter 2 is Literature Review with PRISMA, concise matrix, verified synthesis, and references.
- Chapter 3 is Requirements Analysis, not Methodology.
- Chapter 3 now uses a questionnaire-based requirements analysis template.
- The questionnaire is required, not optional.
- Chapter 4 is System Design.
- Chapter 5 is Implementation Plan.
- Chapter 6 Conclusion is added.
- Appendices are ordered as:
  - Appendix A: Gantt Chart
  - Appendix B: FYP1 Meeting Logs
  - Appendix C: Turnitin Similarity Index Page
  - Appendix D: Full Literature Review Matrix
  - Appendix E: PRISMA Screening Summary
  - Appendix F: System Design Diagrams
  - Appendix G: Planned Test Cases and Evaluation Metrics
  - Appendix H: Full User Requirements Questionnaire

## Literature Review Verification

| Item | Count |
|---|---:|
| Records considered | 96 |
| Records excluded | 47 |
| Eligible records after screening | 49 |
| Studies selected and used in the current review or Appendix D | 35 |
| Core separation studies | 18 |
| Background/supplementary studies | 17 |
| Eligible backup records not cited | 14 |
| Excluded papers cited | 0 |
| Missing citation keys | 0 |

The 35 selected papers remain unchanged. No new papers were collected and no literature review decisions were changed.

## Formatting and Generation Checks

- DOCX render succeeded.
- Output regenerated at `report/generated/paper.docx`.
- Chapter titles are post-processed as centered uppercase headings in the format `CHAPTER X: TITLE`.
- PRISMA was converted from `literature-review/prisma/prisma_flow_diagram_filled.docx` to PDF, then PNG.
- Report PRISMA figure uses `report/quarto/figures/prisma/prisma_flow_diagram.png`.
- Mermaid is not used for the PRISMA figure.
- Table captions use continuous numbering: Table 1, Table 2, Table 3, and so on.
- Figure captions use continuous numbering: Figure 1, Figure 2, Figure 3, and so on.
- List of Tables, List of Figures, and List of Appendices use internal hyperlinks and PAGEREF fields.
- Header font size remains 10 pt.
- Footer font size remains 8 pt.
- Appendix D is landscape and uses compact matrix formatting.
- Report-facing body text avoids internal workflow file names and tool names.

## Questionnaire Guide and Template Status

- Google Form creation PDF guide has been created at `report/requirements/questionnaire_google_form_step_by_step.pdf`.
- Google Form guide source has been created at `report/requirements/questionnaire_design_google_form.md`.
- Editable DOCX guide copy has been created at `report/requirements/questionnaire_google_form_step_by_step.docx`.
- Chapter 3 now presents the questionnaire as a required fact-finding method for Requirements Analysis.
- Chapter 3 uses a text-only respondent background summary for Section A.
- Chapter 3 uses one main chart per questionnaire analysis item.
- Only 10 main requirement-focused charts are used in Chapter 3.
- The full 24-question questionnaire is intended for Appendix H.
- Placeholder figures were inserted for the 10 main questionnaire analysis items.
- Google Form response collection is still pending.
- Response collection and real analysis are pending.
- After collecting Google Form responses, replace the placeholder figures with real charts and update the pending findings.

## PlantUML Rendering Status

Editable PlantUML sources:

- `diagrams/plantuml/context_diagram.puml`
- `diagrams/plantuml/use_case_diagram.puml`
- `diagrams/plantuml/activity_diagram.puml`
- `diagrams/plantuml/class_diagram.puml`
- `diagrams/plantuml/sequence_diagram.puml`

Rendered report images:

- `report/quarto/figures/plantuml/context_diagram.png`
- `report/quarto/figures/plantuml/use_case_diagram.png`
- `report/quarto/figures/plantuml/activity_diagram.png`
- `report/quarto/figures/plantuml/class_diagram.png`
- `report/quarto/figures/plantuml/sequence_diagram.png`

The diagrams were rendered through the local PlantUML wrapper at `tools/plantuml.cmd`.

## Completed Chapters

- Chapter 1: Introduction
- Chapter 2: Literature Review
- Chapter 3: Requirements Analysis
- Chapter 4: System Design
- Chapter 5: Implementation Plan
- Chapter 6: Conclusion

## Known Limitations

- The report is still an FYP1 report, so it does not claim completed prototype implementation results.
- No final model scores, API endpoints, database tables, screenshots, implementation results, or testing results are reported.
- Chapter 3 includes the required questionnaire design and analysis template. Actual Google Form response analysis is pending until real responses are collected.
- Public dataset selection and experiment subset preparation still need supervisor confirmation before FYP2 implementation.
- The PRISMA counts and selected literature set were preserved from the existing review records.

## Remaining Manual Items

- Manually create the Google Form using `report/requirements/questionnaire_google_form_step_by_step.pdf`.
- Distribute the Google Form to target respondents after supervisor approval.
- Collect Google Form responses.
- Replace Q1-Q10 placeholder figures with real charts generated from actual responses.
- Update Chapter 3 pending findings after collecting real responses.
- Check cover page spacing in Microsoft Word.
- Insert or check FYP1 meeting logs.
- Insert the Turnitin similarity index page.
- Insert the Gantt chart.
- Get supervisor confirmation on final scope, dataset direction, and implementation plan.
- Open the DOCX in Word and update all fields before final submission.

## Latest Validation

- Validation script passed after regeneration.
- Render script passed after regeneration.
- Manual Word review is still required for final displayed page numbers, field refresh, page breaks, and submission attachments.
