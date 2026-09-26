# Candidate method attribution and verification gaps

Prepared 26 September 2026 from local primary-paper title/abstract pages, the revised bibliography and inspected code paths. This is not a new systematic search or a reproduction audit. No web metadata was substituted for the local sources, and no paper performance numbers are presented as StethoFuse results.

## Locally checked identities

| Candidate or relevant work | Local source checked | What is established here | What remains unverified |
| --- | --- | --- | --- |
| NeoSSNet | `literature-review/papers/pdfs/Poh et al. - 2024 - NeoSSNet Real-Time Neonatal Chest Sound Separation Using Deep Learning.pdf`, first page, printed p. 345; revised BibTeX key `poh2024neossnet` | Title, nine named authors beginning Yang Yi Poh, publication year 2024 and DOI `10.1109/OJEMB.2024.3401571` agree with the local bibliography. The paper describes neonatal heart/lung separation and a learned encoder/mask/decoder architecture. | Full implementation-to-paper audit; upstream revision/license; exact checkpoint origin/hash/training configuration; input/output conventions; domain suitability for proposed data; whether local adaptation changes architecture, normalization or training. Existing adapter presence is not fidelity proof. |
| Periodicity-based NMF | `Torabi et al. - 2023 - A New Non-Negative Matrix Factorization Approach for Blind Source Separation of Cardiovascular and R.pdf`, first page; key `torabi2023negative2` | First page names Yasaman Torabi, Shahram Shirani and James P. Reilly and the periodicity-based NMF title. It describes a modified affine NMF with multilayer units. The revised bibliography records arXiv preprint DOI `10.48550/arXiv.2305.01889`; the first page alone does not independently verify that identifier/year. | Exact paper version/publication status; method/repository/license; correspondence to a proposed expert. Do not call generic NumPy NMF a faithful implementation or equate it with NMCF. |
| Neonatal NMF/NMCF | `Grooby et al. - 2023 - Noisy Neonatal Chest Sound Separation for High-Quality Heart and Lung Sounds.pdf`, first page, printed p. 2635; key `grooby2023noisyneonatal` | Authors begin Ethan Grooby and Chiranjibi Sitaula; IEEE JBHI volume 27, issue 6, June 2023; DOI `10.1109/JBHI.2022.3215995`. The abstract explicitly distinguishes NMF and NMCF. The first page prints a code-repository link, but it was not fetched here. | Which of these distinct methods is intended by the NMF/NMCF candidate; full source/version/license/dependency/parameter audit; adaptation and independent reproducibility. Not interchangeable attribution with the Torabi work. |
| DAE-NMF-VMD | `Sun et al. - 2024 - Research on heart and lung sound separation method based on DAE–NMF–VMD.pdf`, first page; key `sun2024daenmfvmd` | Wenhui Sun, Yipeng Zhang and Fuming Chen; EURASIP Journal on Advances in Signal Processing, 2024:59; DOI `10.1186/s13634-024-01152-0`. Local abstract describes DAE feature extraction, NMF clustering and VMD denoising stages. | Full pipeline availability, data/checkpoints, code/license and reproduction effort. Existing standalone NMF and VMD baselines do not establish this hybrid. Two similarly named local PDFs exist; do not count filenames as independent studies. |

All local PDF paths in the table are under `literature-review/papers/pdfs/` in the documentation repository. Full bibliographic entries remain in the original `report/revisions/verified_references.bib`; the filename “verified” is not blanket verification of every implementation claim. `literature-review/references/references.bib` is the older broader literature collection, including excluded candidates and differing entry types.

## Code boundaries checked

The legacy implementation has `app/ml/strategies/fixed_filter_strategy.py`, `nmf_strategy.py`, `vmd_strategy.py`, `app/ml/neossnet_strategy.py`, factory/service integration, dataset/evaluation utilities and tests. Its README describes NMF and VMD as decomposition baselines, not trained models. The current separation route chooses an individual method/model; the new frontend's ensemble action is a simulation. No candidate-combination inference or fitted fusion result was verified in this preparation.

Each adopted expert needs a record containing full paper identity, local/upstream source URL, commit, license, environment, input/output shapes and source order, sample-rate/scale/length behavior, checkpoint/configuration hashes, training data and split, modifications, known failures, and reproducible smoke/evaluation commands. Literature methods that are unavailable or infeasible should be documented as considered but not adopted.

## Evaluation safeguards for the outline

- Keep the unprocessed mixture and usable fixed-filter/NMF/VMD baselines separate from verified candidate experts and ensembles.
- Freeze source-aware train/validation/test membership before fitting weights. Record patient/source/mixture relationships where available to prevent segment leakage.
- Resolve time alignment, channel correspondence, scale preservation and residual noise explicitly; do not assume compatible masks or blindly peak-normalize every estimate.
- Inspect existing metric alignment and reference lookup before adoption. `evaluation_service.py` searches reference pairs using identifiers derived from filenames and includes reference-based alignment choices. Document and test the evaluation convention; it is not an inference-time oracle available for ordinary uploads.
- Fixed per-source weights are not adaptive; adaptive inference requires observable, validated predictors. Numeric weights and final membership are still undecided.
- Report heart and lung separately, plus runtime/resources, failures and uncertainty. A worse result remains a result. No clinical benefit, universal superiority or reference-dependent quality for unpaired uploads may be inferred.

The next bounded research task is an expert-by-expert provenance/reproducibility audit, not training or a claim that all three candidates already work.
