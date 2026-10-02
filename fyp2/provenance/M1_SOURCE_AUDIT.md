# M1 source and guidance audit

Read-only source inspection, 26 September 2026. This audit read continuation-pack 08 first, then 00-07 in order and the manifest; required workspace/access/checkpoint documents; the three actual guideline PDFs; and the authoritative submitted DOCX/PDF. Existing text extractions at `../.local/m1-reference/` were read in full. Relevant PDF pages were rendered and visually inspected in ignored `fyp2/.quarto/m1-source-review/`. No original was rewritten or re-exported.

## Confirmed sources

| Source | Verified use |
| --- | --- |
| `../planning/source-plans/StethoFuse_Continuation_Pack_2026-09-26/08_CODEX_CONTINUE_FROM_CHECKPOINT.md`, 00-07 and manifest | Current M1 instructions, final hostname, unchanged academic title, intended administrator identity process, 52 granular requirements and seven-state evidence vocabulary. A plan is not execution evidence. |
| `resources/guidelines/FYP Handbook T2610.pdf`, April 2026, 32 pages | Covers CPT6314 and CPT6324. Page 14 explicitly gives application-based FYP2 chapters Introduction, Literature Review, Requirements Analysis, System Design, Implementation, Testing, Conclusion. Page 13 requires at least six FYP2 logs and similarity at most 20%; eBwise controls deadlines. Pages 14-17 set formatting/caption guidance; section 5 requires APA. |
| `resources/guidelines/CPT6314 Teaching Plan T2610 v1.pdf`, three pages | Page 1 names Final Year Project 1 and CPT6314; page 2 is the FYP1 interim schedule. Not an FYP2 deadline/rubric source. Marked internal/confidential; no new external publication or full reproduction was made. |
| `resources/guidelines/FYP1 Rubrics.pdf` | Read rubric categories and prototype/planning criteria. It is the existing FYP1 rubric, not a newly discovered FYP2 rubric. |
| `report/Submission/1221303805_Arshad_Jamal_FYP1_Revised_Copy.docx` | Read OOXML heading hierarchy without editing. Confirms 4.5.3 mathematical formulation, 4.5.4 storage, Ch5 Implementation Plan and Ch6 Conclusion. |
| `report/Submission/1221303805_Arshad_Jamal_FYP1_Report.pdf` | Re-extracted content and visually inspected contents page ix (PDF page 9), consistent with the revised DOCX. Rechecked requirement/use-case labels: F1/UR1/UC01 are recording attributes; F2/UR2/UC02 are upload, with F3 validation in that workflow. Original 104-page report is not fully re-certified for layout. |

Teaching-plan SHA256: `877e3a971f401b8aa83542bfeb20466fde646adf792fbdf050b0605354a340de`. FYP1-rubric SHA256: `9de52e25da8f462432f41353a0dc5ce791733bb00b9ec9ff7f852784e4ec7cc1`. The handbook and both submitted artifacts retain their [previous baseline hashes](BASELINE.md). All 217 historical entries passed again before M1 documentation edits.

The [M1 input manifest](m1-inputs-2026-09-26.sha256) pins the full continuation pack, three guideline PDFs, two submitted artifacts and retained M0 test XML. Paths are relative to the documentation repository. Concurrent M1 code/provider notes are deliberately not certified by this immutable-input manifest; later implementation snapshots need their own revision/hash record.

The final M1 local implementation snapshot is coordinator commit `56ecc2d`; a separate [eight-result manifest](m1-final-test-evidence-2026-09-26.sha256) pins the final backend and frontend test artifacts. Environment/mocking limits and exact result counts remain in the M1 ledger. All 217 original report-file hashes and all 16 immutable M1-input entries passed again at documentation freeze; no original-file diff was present.

## Resolved versus open guidance

**Resolved:** application-based seven-chapter structure is confirmed for this working copy; final target is `stethofuse.ashraf-alsaloul.com`; supplied official academic title remains unchanged. The earlier `hearme` target and proposal title prefix remain historical provenance, not current questions that block M1.

**Still required before final submission:** the current CPT6324/FYP2 rubric and teaching plan, applicable term/deadlines/naming/template/page-size instructions, supervisor approval of material objective/scope changes, genuine FYP2 meeting logs, current similarity report and any approval/consent process for new human recordings or consultation. The known directory contains no separate current FYP2 rubric. Do not infer one from a file named FYP1.

Specific inconsistencies to reconcile with the current university source:

- Handbook page 5 assigns FYP2 poster presentation 10%; page 6 labels that subsection 20%, while its listed parts total 10%. Do not silently choose a new grading scheme.
- Handbook page 14 repeats Appendix B; page 13 lists Abstract twice. Use the approved current template for final order/lettering.
- Handbook typography section says interim report while appearing under general report preparation; the submitted PDF is Letter, while the handbook PDF's A4 page size is not itself a report-paper prescription.
- The FYP1 teaching plan and handbook differ on FYP1 structure/oral-presentation weightings. Neither disagreement establishes FYP2 assessment weights.
- Preserve the submitted APA 7 approach requested in the continuation pack; reconcile any older-looking handbook citation examples with the actual current instruction rather than copying examples blindly.

## Evidence limits

No new literature search, questionnaire, participant/patient data, model experiment, deployment, provider mutation or administrator assignment was performed by this documentation worker. M1 source and result claims are synchronized separately in [implementation and test notes](../M1_IMPLEMENTATION_AND_TEST_NOTES.md). Original requirements and respondent history remain intact.
