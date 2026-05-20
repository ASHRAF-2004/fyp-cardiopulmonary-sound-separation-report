# PRISMA Diagram Notes

Project title: **Machine Learning-Based System for Cardiopulmonary Sound Separation**

## Source Files

- `literature-review/prisma/prisma_counts.json`
- `literature-review/metadata/papers_master.csv`
- `literature-review/metadata/duplicate_check.csv`
- `literature-review/metadata/exclusion_reasons.csv`
- `literature-review/screening/title_abstract_screening.csv`
- `literature-review/screening/full_text_screening.csv`

## Count Mapping

- Records identified from existing local PDF set: `20`.
- Public database/metadata candidates seen: `121`. This combines `76` added records and `45` duplicate candidates skipped before adding.
- Duplicate candidates skipped before adding: `45` (`15` in Phase 3 and `30` in Phase 7).
- Records retained in `papers_master.csv` and screened at title/abstract/metadata level: `96`.
- Records excluded in the final project decision state: `47`.
- Records retained for literature-review use: `49`.
- Studies selected and cited in the current Chapter 2 synthesis: `35`.
- Core separation studies in the current Chapter 2 synthesis: `18`.
- Background/supplementary studies in the current Chapter 2 synthesis: `17`.
- Eligible backup records not cited in the current Chapter 2 draft: `14`.
- Final decision count marked Include in the screening data: `18`.
- Final decision count marked Maybe/background in the screening data: `31`.
- Full-text/access screening rows documented: `71`.
- Reports assessed for eligibility from accessible full text or online full text: `38`.
- Full text unavailable / not retrieved in the full-text screening table: `33`.
- Phase 7 metadata-only records not yet represented in `full_text_screening.csv`: `25`.

## Interpretation Notes

- The report-facing PRISMA diagram now distinguishes screening decisions from the Chapter 2 synthesis selection.
- The current Chapter 2 draft cites `35` selected papers from the `49` eligible records.
- The `35` cited papers consist of `18` core separation studies and `17` background/supplementary studies.
- The remaining `14` eligible records are retained as backup/background evidence but are not cited in the current Chapter 2 draft.
- Excluded records are not used as supporting evidence in the report.
- The review tracking combines local PDF auditing, public metadata screening, year-range checks, duplicate handling, and manual access updates. Therefore, the diagram is a project-specific PRISMA-style mapping rather than a claim that every retained metadata record has a retrieved full text.
- No paper decisions were changed when generating this diagram.
- The Mermaid diagram remains as backup/source evidence, but the report figure uses the professionally rendered PRISMA 2020-style output.
