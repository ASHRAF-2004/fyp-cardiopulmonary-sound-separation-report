# Research Protocol

## Project Title

Machine Learning-Based System for Cardiopulmonary Sound Separation

## Phase 1 Status

This protocol prepares the literature review tracking system before collecting more papers. The folder already contains 20 local PDF files in `papers/pdfs/`; these papers still need to be audited, deduplicated, screened, and extracted. No new paper search, restricted PDF download, or publisher login is part of Phase 1.

## Research Objective

The objective of this literature review is to identify, screen, and synthesize academic evidence that supports the design of a machine learning-based proof-of-concept system for separating heart and lung audio from cardiopulmonary sound recordings.

The review focuses on methods, datasets, preprocessing steps, feature or signal representations, model implementation choices, and evaluation metrics that can be realistically adapted for a Python-based Final Year Project prototype.

## Research Questions

1. What machine learning and signal processing methods have been used for heart sound, lung sound, chest sound, or cardiopulmonary sound separation?
2. What public or reusable datasets are commonly used for cardiopulmonary, heart, lung, respiratory, or chest sound research?
3. What preprocessing and feature extraction techniques are used before heart and lung sound separation?
4. What model architectures or algorithms are suitable for a student-level Python implementation and software engineering prototype?
5. What evaluation metrics are used to measure source separation quality and audio reconstruction quality?
6. What research gaps justify building an application-based proof of concept rather than a disease detection system?

## Search Keywords

### Main Concepts

- Cardiopulmonary sound separation
- Heart and lung sound separation
- Chest sound separation
- Respiratory and cardiac sound separation
- Machine learning audio source separation
- Deep learning heart lung sound separation
- Single-channel source separation
- Blind source separation
- Non-negative matrix factorization
- Variational mode decomposition
- Denoising autoencoder
- U-Net audio separation
- NeoSSNet
- Public heart sound dataset
- Public lung sound dataset
- ICBHI respiratory sound dataset
- PhysioNet heart sound dataset

### Example Boolean Search Strings

```text
("heart sound" OR "lung sound" OR "cardiopulmonary sound" OR "chest sound")
AND ("separation" OR "source separation" OR "blind source separation")
AND ("machine learning" OR "deep learning" OR "neural network")
```

```text
("heart-lung sound separation" OR "heart and lung sound separation")
AND ("dataset" OR "public dataset" OR "evaluation metrics")
```

```text
("cardiopulmonary sound" OR "respiratory sound" OR "phonocardiogram")
AND ("preprocessing" OR "feature extraction" OR "time-frequency")
AND ("separation" OR "denoising")
```

### Boundary Terms To Avoid As Main Focus

- Disease detection
- Disease classification
- Diagnosis-only classification
- Heart failure detection
- Respiratory disease classification

These terms may appear in background papers, but papers focused only on diagnosis or classification should be excluded unless they provide reusable preprocessing, dataset, feature, or separation evidence.

<!-- Year range rule starts -->

## Publication Year Range Rule

Only studies published from 2022 to 2026 are included in the review. Papers published before 2022 are retained in the tracking files for PRISMA transparency but are excluded from Include/Maybe decisions with the reason: Outside publication year range: before 2022. Papers after 2026 are excluded unless they are clearly valid online-first 2026 records.

<!-- Year range rule ends -->

## Inclusion Criteria

- Publication year must be from 2022 to 2026 inclusive.

- The study is relevant to heart sound, lung sound, chest sound, respiratory sound, or cardiopulmonary sound processing.
- The study includes audio separation, denoising, source separation, signal decomposition, or a closely related method useful for separation.
- The study describes machine learning, deep learning, signal processing, or hybrid methods that can inform implementation.
- The study includes enough detail about preprocessing, feature extraction, model architecture, training, or evaluation.
- The study uses public datasets, reusable datasets, clearly described datasets, or provides transferable method evidence.
- The study reports evaluation metrics relevant to source separation, audio quality, reconstruction, or signal quality.
- The study is academically credible: peer-reviewed article, conference paper, thesis, reputable preprint, or technical report.
- The paper is written in English or has reliable English metadata and enough readable content for screening.

## Exclusion Criteria

- Exclude papers published before 2022 with the reason: Outside publication year range: before 2022.

- The study is only about disease detection, diagnosis, or classification with no useful separation, preprocessing, feature, dataset, or model evidence.
- The study is unrelated to cardiopulmonary, heart, lung, respiratory, chest, or audio source separation.
- The study does not describe a usable method, dataset, or evaluation approach.
- The full text is unavailable through open/public/legal access or the user's existing local files.
- The record is a duplicate by DOI, title, or local PDF.
- The source is not academically credible or has insufficient bibliographic metadata.
- The paper is hardware-only or clinical-only without transferable software, signal processing, or machine learning relevance.

## Databases and Sources

Use these sources for future phases only. Do not log in or use university credentials through Codex.

- Google Scholar: broad discovery and citation chaining, manual use only.
- Semantic Scholar: metadata, abstracts, related papers, citation context.
- PubMed / PubMed Central: biomedical and cardiopulmonary sound literature.
- arXiv: machine learning and signal processing preprints.
- IEEE Xplore: metadata and abstracts only unless the user already has legal access outside Codex.
- ScienceDirect: metadata and abstracts only unless open access or already available.
- SpringerLink: metadata and abstracts only unless open access or already available.
- ACM Digital Library: software engineering and audio ML references where relevant.
- MDPI, Frontiers, Nature, Elsevier, Wiley, and other publisher pages: open-access records only.
- Public dataset sources: PhysioNet, ICBHI challenge pages, Kaggle only for openly reusable datasets, Zenodo, Figshare, GitHub repositories linked by papers.

## Screening Process

1. Assign each candidate paper a stable `paper_id` in `metadata/papers_master.csv`.
2. Record where each paper came from using `record_source`, `search_id`, `source_record_id`, DOI, URL, and local PDF path where available.
3. Run duplicate checks by DOI first, then normalized title, then local file name similarity.
4. Record duplicate decisions in `metadata/duplicate_check.csv`.
5. Screen titles and abstracts in `screening/title_abstract_screening.csv`.
6. Apply exclusion reasons from `metadata/exclusion_reasons.csv`.
7. Screen full texts in `screening/full_text_screening.csv` using only local PDFs or open/public/legal full texts.
8. Extract accepted evidence into `screening/extraction_matrix.csv`.
9. Add accepted references to `references/references.bib` and `references/references_apa.md`.
10. Update `prisma/prisma_counts.json` and `prisma/prisma_flow_diagram.mmd` after each screening stage.

## PRISMA Tracking Method

The PRISMA workflow will track four stages:

1. Identification: records from database searches, existing local PDFs, and other public sources.
2. Deduplication: duplicates removed by DOI, title, or file-level similarity.
3. Screening: title and abstract review against the inclusion and exclusion criteria.
4. Eligibility and inclusion: full-text screening and final included studies for Chapter 2.

The current Phase 1 PRISMA baseline is:

- Existing local PDFs pending audit: 20
- New searches performed in Phase 1: 0
- Duplicates removed: 0
- Records screened: 0
- Studies included: 0

Update counts only after actual audit decisions are made.

## Zotero and Manual PDF Download Workflow

Use Zotero as an optional reference manager, not as a credential store.

1. Search sources manually in a normal browser where needed.
2. Do not provide Codex with university login credentials.
3. Do not ask Codex to log in to IEEE, ScienceDirect, Springer, ResearchGate, or university portals.
4. If a paper is open access, download it manually or save it through Zotero.
5. If a paper is restricted, record metadata only and mark full text unavailable unless the user already has the PDF legally.
6. Store legal local PDFs in `papers/pdfs/`.
7. Use Zotero citation keys or manual BibTeX keys in `metadata/papers_master.csv`.
8. Use `references/references.bib` for included papers after screening.
9. Use `references/references_apa.md` for final APA references after inclusion decisions.

## Local PDF Audit Workflow

The 20 PDFs currently in `papers/pdfs/` should be audited before any new collection.

1. List all local PDFs.
2. Assign `paper_id` values.
3. Extract visible title, authors, year, DOI, and abstract when available.
4. Populate `metadata/papers_master.csv`.
5. Check for duplicates.
6. Screen title and abstract.
7. Screen full text.
8. Extract Chapter 2 evidence.

Use PDF extraction only on local files that already exist in the repository. Do not download restricted PDFs.

## Audit Notes

- Keep disease detection outside the main review unless it contributes reusable preprocessing, dataset, model, or evaluation evidence.
- Prefer methods that are explainable in a viva and realistic for a student FYP prototype.
- Keep evidence traceable from every Chapter 2 claim back to `paper_id`, BibTeX key, and source PDF or URL.

<!-- Manual access restrictions starts -->

## Manual Full-Text Access Notes

- SSRN records that are removed or under review are excluded as full text unavailable.
- Records unavailable through university access are excluded at the full-text retrieval/access stage and retained for PRISMA tracking.
- Avoid IOP Science as a future priority source due to access limitations.
- Avoid ASTM Digital Library as a future priority source due to access limitations.
- Papers readable online but not downloadable as PDF may remain Include/Maybe if the online full text is sufficient for screening and extraction.

<!-- Manual access restrictions ends -->
