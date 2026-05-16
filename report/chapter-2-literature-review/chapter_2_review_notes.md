# Chapter 2 Review Notes

Review date: 2026-05-16

Scope: reviewed and improved `chapter_2_draft.md` only. No new papers were added, no searches were performed, and `references.bib` was not changed.

## Main Improvements

1. Strengthened academic flow by changing the chapter from a coverage-style draft into a clearer thematic synthesis.
2. Added stronger comparison between method families: NMF/decomposition, blind filtering/SSA, hybrid neural methods, U-Net-style models, attention/transformer methods, and pretrained-model reprogramming.
3. Tightened the connection to the FYP scope by repeatedly framing the project as an audio source-separation software prototype, not a diagnosis or disease-classification system.
4. Made the research gap explicit and FYP-aligned: dataset reproducibility, feasible method selection, separation-appropriate evaluation, and software-system integration.
5. Reduced repetition around "not diagnosis" by keeping that point mainly in the introduction, dataset/evaluation discussion, and research gap.
6. Repositioned classification and diagnosis-oriented papers as background or context only.
7. Kept unsupported claims cautious by avoiding numerical performance claims not already present in the draft evidence.
8. Preserved the recommended 35-paper evidence set and kept citations in Pandoc-style citation-key format.

## Section-Level Review

| Section | Main revision |
|---|---|
| 2.1 Introduction | Clarified the chapter purpose and contrasted classical versus learning-based separation work. |
| 2.2 Cardiopulmonary Sound Characteristics | Improved explanation of overlap, temporal structure, signal quality, and preprocessing relevance. |
| 2.3 Heart and Lung Sound Separation Problem | Made the single-channel, noisy, underdetermined nature of the task clearer. |
| 2.4 Traditional Signal Processing Methods | Reorganized methods into NMF, hybrid NMF, VMD, blind filtering, SSA, and respiratory preprocessing groups. |
| 2.5 Machine Learning and Deep Learning Methods | Compared feasible deep models with more complex attention, transformer, and reprogramming approaches. |
| 2.6 Datasets | Emphasized HLS-CMDS as the primary separation-relevant dataset and separated it from classification datasets. |
| 2.7 Evaluation Metrics | Clarified that separation metrics should be prioritized over classification accuracy. |
| 2.8 Existing Systems and Prototype Relevance | Connected literature to the planned software workflow: input, preprocessing, separation, storage, metrics, and interface. |
| 2.9 Research Gaps | Rewritten into four explicit FYP-aligned gaps plus a clear gap statement. |
| 2.10 Summary | Updated to match the revised argument and transition toward methodology. |

## Citation and Scope Checks

- The revised draft still uses the recommended Chapter 2 writing set only.
- Citation keys were kept in the same Pandoc-style format used in the first draft.
- No excluded papers were intentionally cited as supporting evidence.
- No new citation keys were introduced.
- Disease classification papers are used only as dataset, benchmark, or downstream-context evidence.
- The chapter remains suitable for FYP1 because it focuses on rationale, comparison, feasibility, and research gap rather than final implementation claims.

## Remaining Work Before Final Report Formatting

1. Once the final separation method is chosen, align Sections 2.4, 2.5, and 2.9 more tightly with that exact methodology.
2. Add a small comparison table later if the final report format allows it, especially for method family, dataset type, strengths, and limitations.
3. Convert citations and headings into the final report or Quarto format only after the chapter content is approved.
