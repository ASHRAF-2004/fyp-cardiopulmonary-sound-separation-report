# Final Report Review Notes

Report title: Machine Learning-Based System for Cardiopulmonary Sound Separation

Main output: `report/generated/paper.docx`

## Completed Sections

- Front matter updated with cover/title information, copyright, declaration, acknowledgements, abstract, table of contents placeholder, list of tables, list of figures, abbreviations, and appendices.
- Chapter 1 completed as the official Introduction chapter with 3 numbered problem statements and 3 numbered objectives.
- Chapter 2 completed as the official Literature Review chapter with PRISMA explanation, PRISMA diagram, summary literature review matrix, and full Appendix A matrix.
- Chapter 3 completed as the official Methodology chapter.
- Chapter 4 completed and included as Design and Implementation.
- Chapter 5 completed and included as Testing and Evaluation.
- Appendix A retained as the full literature review matrix.
- Appendix B added as the PRISMA screening summary.
- Appendix C added as the system design diagram summary.
- Appendix D added as planned test cases and evaluation checks.
- References compile through the active bibliography.

## Literature Review Verification

| Item | Count |
|---|---:|
| Selected papers | 35 |
| Actually cited or used in Chapter 2 or Appendix A | 35 |
| Selected but not cited or used | 0 |
| Excluded papers cited | 0 |
| Missing citation keys | 0 |

The 35 selected papers are treated as final for the current Chapter 2 synthesis: 18 core separation studies and 17 background/supplementary studies.

## Formatting Checks Completed

- DOCX render succeeded.
- Output regenerated at `report/generated/paper.docx`.
- Header font size remains 10 pt.
- Footer font size remains 8 pt.
- Appendix A is landscape only.
- Other sections remain portrait.
- Appendix A matrix uses 8 pt text, borders, and repeated header row.
- Chapter headings do not show repeated numbering.
- Chapter 4 and Chapter 5 are included in the generated DOCX.
- Report-facing text does not contain internal workflow file names or tool names.
- References section appears in the generated DOCX.
- DOCX package is readable and contains embedded figure media.

## PlantUML Rendering Status

PlantUML source files were created:

- `diagrams/plantuml/use_case_diagram.puml`
- `diagrams/plantuml/component_diagram.puml`
- `diagrams/plantuml/sequence_diagram.puml`

Rendered images were created and inserted into the report:

- `report/quarto/figures/plantuml/use_case_diagram.png`
- `report/quarto/figures/plantuml/component_diagram.png`
- `report/quarto/figures/plantuml/sequence_diagram.png`

The diagrams were rendered through the Kroki PlantUML endpoint because a local `plantuml` command was not available. Render command pattern:

```powershell
curl.exe -s -S -X POST https://kroki.io/plantuml/png -H "Content-Type: text/plain" --data-binary "@diagrams\plantuml\use_case_diagram.puml" -o report\quarto\figures\plantuml\use_case_diagram.png
```

The Mermaid workflow source and rendered image were also created:

- `diagrams/mermaid/audio_processing_workflow.mmd`
- `report/quarto/figures/mermaid/audio_processing_workflow.png`

The local Mermaid CLI timed out during rendering, so the workflow image was rendered through Kroki.

## Known Limitations

- The report presents FYP1 design, methodology, and planned testing. It does not report final separation scores because the full prototype evaluation has not been completed.
- Chapter 4 describes the designed implementation honestly at module level. Endpoint names, final database schema, and exact class names should be confirmed during implementation.
- Chapter 5 contains planned test cases and metrics. Actual results should be added only after the prototype has been tested.
- HLS-CMDS is treated as the main public dataset candidate, but final dataset download, preparation, and experiment subset selection still need to be completed.

## Items Needing Supervisor Confirmation

- Confirm that the 5-chapter FYP1 structure is acceptable for the submission format.
- Confirm that HLS-CMDS is acceptable as the primary public dataset candidate.
- Confirm the final model direction before implementation begins.
- Confirm whether the optional appendices for meeting logs, Turnitin page, or Gantt chart must be inserted into the same DOCX or submitted separately.

## Remaining Manual Corrections Before Submission

- Open the DOCX in Microsoft Word and update the Table of Contents field.
- Review the cover/title page against the latest faculty template and adjust spacing if required.
- Review the List of Tables and List of Figures after updating Word fields.
- Insert meeting logs if the supervisor or faculty requires them inside the report package.
- Insert the Turnitin similarity page if required by the submission checklist.
- Perform a final manual proofread for page breaks, figure placement, table readability, and reference formatting.

## Next Actions

1. Open `report/generated/paper.docx` in Word.
2. Update all fields in Word.
3. Check cover page, page numbering, table and figure lists, and appendix placement.
4. Add any required faculty attachments such as meeting logs or Turnitin page.
5. Get supervisor confirmation on dataset, model direction, and FYP2 implementation plan.
