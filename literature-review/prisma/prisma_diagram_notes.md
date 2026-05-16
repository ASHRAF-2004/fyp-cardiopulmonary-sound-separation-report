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
- Studies included in the literature review: `18`.
- Maybe/background or supplementary records retained: `31`.
- Full-text/access screening rows documented: `71`.
- Reports assessed for eligibility from accessible full text or online full text: `38`.
- Full text unavailable / not retrieved in the full-text screening table: `33`.
- Phase 7 metadata-only records not yet represented in `full_text_screening.csv`: `25`.

## Interpretation Notes

- The final included count is `18`. Maybe/background records are not counted as final included studies.
- The `31` maybe/background records are shown separately because they are retained for context, datasets, preprocessing, metrics, or later review.
- The review tracking combines local PDF auditing, public metadata screening, year-range checks, duplicate handling, and manual access updates. Therefore, the diagram is a project-specific PRISMA-style mapping rather than a claim that every retained metadata record has a retrieved full text.
- No paper decisions were changed when generating this diagram.
- The Mermaid diagram remains as backup/source evidence, but the report figure uses the professionally rendered PRISMA 2020-style output.
