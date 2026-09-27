# Ensemble design and planned evaluation — ADR E01

## Current own-model direction — 28 September 2026

See [ADR T01: own separator training design](MODEL_TRAINING_DESIGN.md).
The owner superseded waiting for NeoSSNet rights/native reproduction for our
own compact fixed-label Conv-TasNet, trained from scratch with a licensed
library and CC-BY-4.0 data. **DESIGNED, not yet trained/evaluated.** NeoSSNet
stays research-only. The50/50 ensemble below is preserved/frozen, not replaced,
tuned or integrated. New ensemble choices must earn their place on validation
before final-test access. Older author-contact next steps are historical.

## Superseding reproduction diagnosis — 27 September 2026

**DEVELOPMENT DIAGNOSTIC / NOT FINAL; Outcome D for current target expert
qualification.** Native NeoSSNet reproduction is blocked, not proven successful
or disproved. The implemented equal-weight fusion stays frozen, but its conditional
NeoSSNet membership must be revisited before training, final evaluation or
application wiring. Production and all held-out audio remain untouched.

Chapter 2 interpretation: Poh et al. (2024), Table VII, labels16.00/14.46 dB as
heart/lung SI-SDR;14.76 is lung SDR. The
[author notebook](https://github.com/yangyipoh/Neonatal-Chest-Sound-Separation-using-Deep-Learning/blob/d97886b93bd2e71fd019c6b5073bb2dce2854ade/results.ipynb)
displays that exact baseline row using **improvement columns**, with category
medians averaged across three noise groups. Its released evaluator also calls
the permutation-optimising `fast_bss_eval.si_sdr`; `return_perm=False` does not
disable reassignment. These differences and the neonatal/manikin populations
preclude direct comparison to our mean fixed-label absolute scores. This is a
documented source discrepancy requiring clarification, not a silent correction
of the paper or a reason to adopt reference-oracle evaluation.

Chapters 4–6 evidence: strict released weights load (8,422,144 parameters,
132 finite state entries, no missing/unexpected keys), eval mode and exact
repeat/direct-call parity passed. One local positional-encoding edit had changed
the second mask branch's shared input. Restoring author behavior changed the six
lung means only−13.84→−13.81 dB; it did not repair separation. The evaluator now
preserves float64 caller arrays and rejects undefined silent estimates rather
than awarding0 dB. Independent fixed-label SI-SDR agrees within1.57e−7 dB on18
diagnostic executions. Mean-removal differences are below5.42e−6 dB; correlation
peaks show zero lag throughout, so no timing correction was applied.

| Development cases / globally fixed mapping | Heart SI-SDR / SI-SDRi (dB) | Lung SI-SDR / SI-SDRi (dB) |
| --- | ---: | ---: |
| Original6, restored author forward, documented0H/1L | −3.48 / −3.47 | −13.81 / −13.79 |
| Same6, one global1H/0L alternative | −5.72 / −5.70 | +0.23 / +0.24 |
| Additional12 author-protocol **manikin surrogates**, documented0H/1L | −4.15 / −4.14 | −15.08 / −15.06 |
| Same12, one global1H/0L alternative | −6.85 / −6.84 | −0.19 / −0.18 |
| Native neonatal published-fold reproduction | NOT RUN | NOT RUN |

The12 additional cases use only the same two frozen development source pairs,
levels−10/0/+10 dB, and instantaneous/seeded three-tap convolutive NoNoise rules.
They are correlated protocol surrogates, not new subjects or native data. The
original six normalized inputs already match author mixing to7.16e−7 full scale.
The source archive is4 kHz; earlier acquisition/conversion provenance remains
unknown. “Projected” means reference-free magnitude masks applied to original
mixture phase, not a target-dependent oracle. It restores additivity, not labels.
The documented mapping is retained; neither global mapping qualifies both sources.

**Domain shift is plausible, not experimentally demonstrated. Fine-tuning is not
yet justified:** strong native performance has not been reproduced, so the
owner's first training gate is unmet. The public weights are not linked by a
manifest to the notebook's `all1` run or neonatal reference folds. A later
author application contains a different stochastic model, not drop-in corrected
weights; it was not downloaded/adopted. Complete code/weight reuse rights remain
**PENDING RIGHTS**. A clarification request is prepared but not sent.

Two new regression functions; focused8 passed; one nearby ML regression15 passed.
18/18 executions had no shape/nonfinite failures. No ensemble-weight tuning,
training, final FYP result, clinical claim, native reproduction or deployment
claim follows. Full contract, hashes, failure attribution, source links and next
Luna task: [implementation reproduction report](https://github.com/ASHRAF-2004/Machine-Learning-Based-System-for-Cardiopulmonary-Sound-Separation/blob/fyp2/application/docs/NEOSSNET_REPRODUCTION_DIAGNOSIS.md).
The older Phase-D and prospective material below remains historical context.

## Follow-up qualification status — 28 September 2026

**Author clarification: PREPARED / NOT SENT.** The contact in the original
NeoSSNet repository is verified as `Yang.Poh@monash.edu`. The question set now
covers code/checkpoint permissions, checkpoint-to-paper run identity, fixed
channel order, a small lawful native fixture, and the notebook's metric and
aggregation protocol. No email or permission request was sent.

Two licensed research candidates are recorded for later qualification, not
selected as replacement experts: (1) Torabi et al.'s periodicity-informed
NMF/LingoNMF, whose author repository declares MIT and whose work includes
clinical-manikin experiments; (2) Grooby et al.'s neonatal NMF/NMCF, whose
author code is GPL-3.0 and whose reference-data/deployment obligations remain
to be resolved. Neither has been tested here. Their reported metrics and
conditions are not directly comparable with our fixed-label SI-SDR/SI-SDRi
diagnostics. The 50/50 design remains frozen; membership and fine-tuning are
unresolved.

The local source manifest has 36 development, 9 validation and 5 test heart
tracks; and 36 development, 5 validation and 9 test lung tracks. The current
split is sound-family separated, not subject-level. Future model-selection and
remixing must stay within partitions; pairwise remixes are correlated reuse of
source files, not independent recordings. Existing held-out source IDs remain
locked. This is a planned data protocol, not training or final evaluation.
Detailed candidate caveats, frozen IDs and the draft email are in the workspace
handoff; no audio or patient data was added to this repository.

## Earlier design and Phase-D context

27 September 2026. **Designed and now implemented/tested offline through Phase D
on a small development-only qualification set; not integrated, deployed or finally
evaluated.** This is not a new participant study, clinical claim or supervisor
approval. StethoFuse's deployed application is unchanged; user-facing separation
execution remains unavailable. The later offline evidence below supersedes the
earlier prospective wording retained for context.

The owner-supplied current academic title is **Development of a Machine
Learning-Based System for Cardiopulmonary Sound Separation**. Earlier submitted
title variants remain historical evidence; reconcile exact registration wording
before final submission without editing `report/Submission/`.

## Chapter 2 — targeted literature and implementation correspondence

NeoSSNet supplies a learned waveform separator (Poh et al., 2024). The candidate
local NMF uses generic multiplicative factorisation (Lee & Seung, 2000) with a
project-specific frequency-centroid labelling rule. It is **not** the neonatal
NMF/NMCF of Grooby et al. (2023), periodicity-based NMF, or the complete
DAE–NMF–VMD of Sun et al. (2024). Standalone VMD (Dragomiretskiy & Zosso, 2014)
is a baseline, not evidence of that hybrid. These distinctions constrain naming
and the research claims made in FYP2.

The author NeoSSNet repository's released weight/config/model-definition Git blobs
match local copies at upstream revision `d97886b93bd2e71fd019c6b5073bb2dce2854ade`.
No source/weight license was found in the inspected tree; GitHub reports no
declared license. Offline CPU loadability is now verified, while code/weight
redistribution and deployment permission remain blocked. Full-paper experimental
reproduction and neonatal-to-manikin generalisation are not established.

Detailed source/version/hash/license/input-output findings are maintained in the
implementation repository's [`docs/ENSEMBLE_SOURCE_AUDIT.md`](https://github.com/ASHRAF-2004/Machine-Learning-Based-System-for-Cardiopulmonary-Sound-Separation/blob/fyp2/application/docs/ENSEMBLE_SOURCE_AUDIT.md).
New bibliography is isolated in [ensemble-references.bib](provenance/ensemble-references.bib);
submitted/older bibliography files were not rewritten.

## Chapters 3–4 — chosen design

**Selected ensemble: fixed equal-weight complementary time-frequency magnitude-mask
fusion. Conditional experts: released NeoSSNet and local unsupervised NMF.**
Each must qualify before execution is enabled. No normal-user method selector,
learned gate, fresh model training or Federated Learning. Fixed Filter and qualified
VMD are internal comparators. Fine-tuned NeoSSNet weights are missing; NMCF and
DAE–NMF–VMD full implementations are unavailable and excluded from this version.

After shared mono/4-kHz preprocessing, each expert produces labelled raw heart/lung
arrays. Convert their magnitudes on a common1024/256 STFT into complementary
source masks, pool the heart masks0.5/0.5, use `lung_mask=1-heart_mask`, and
reconstruct using the original mixture phase.10-s windows/8-s hop bound inference;
overlap-add preserves the complete recording. Single input gain, explicit padding,
no per-source peak normalisation, no oracle delay/permutation, and common export
gain prevent incompatible output scaling from masquerading as fusion.

Mixture consistency is a useful constraint (Wisdom et al., 2019), not evidence of
source correctness. The proposed mask method is a project adaptation, not a
reproduction of that learned speech model. It may discard useful neural phase
information and assigns all residual noise to the two outputs. Fixed equal weights
avoid fitting confidence/gates to currently unverified data splits. Improvement is
an evaluation question, not a promised requirement.

Waveform averaging was rejected because current gains/phase/clipping differ;
segment selection lacks validated reference-free quality scores; gating/stacking
need independently labelled calibration data and more scope; energy-based confidence
has not been validated. The complete comparative decision, equations and failure
policy are in [`docs/ENSEMBLE_DESIGN.md`](https://github.com/ASHRAF-2004/Machine-Learning-Based-System-for-Cardiopulmonary-Sound-Separation/blob/fyp2/application/docs/ENSEMBLE_DESIGN.md).

Application design reuses owner-only `POST /api/recordings/{id}/jobs`, `m1_jobs`,
`m1_results`, `m1_files`, `m1_result_files` and existing authorised resources.
A dedicated single ML worker claims persistent SQLite jobs, publishes complete
private artifacts/provenance atomically and fails interrupted/invalid runs explicitly.
No Redis requirement, duplicate database, public static audio or role-policy change.
Original grants do not automatically expose new derived resources. Provenance
captures code/model/config hashes, weights, preprocessing, device, timings,
failures and output IDs. No ground truth means no user-facing accuracy score.

## Chapter 5 — offline implementation; application integration planned

Luna phases: artifact/data qualification → canonical adapters → fixed fusion →
offline evaluation → durable jobs → protected result publication → existing UI
workflow → worker packaging/evidence. Exact files, acceptance checks and rollback
boundaries are in [`docs/ENSEMBLE_LUNA_HANDOFF.md`](https://github.com/ASHRAF-2004/Machine-Learning-Based-System-for-Cardiopulmonary-Sound-Separation/blob/fyp2/application/docs/ENSEMBLE_LUNA_HANDOFF.md).
The subsequent Phase A–D implementation added an offline-only engine with raw
NeoSSNet and generic-NMF adapters, shared-gain canonicalisation, 10-s/8-s-hop
overlap-add, fixed 0.5/0.5 complementary magnitude-mask fusion and failed-run
provenance. The historical STFT first-sample loss was reproduced and repaired
with centred padding/periodic Hann. There is **no API, worker, frontend or
Compose integration** for this ensemble; existing production remains unchanged.

## Chapter 6 — planned evaluation and actual audit evidence

HLS-CMDS is manikin data, not a patient study (Torabi et al., 2025). Publisher/creator
README text reports22,050Hz, but the downloaded official HS/LS/Mix ZIPs contain
535 mono 4-kHz PCM16 WAVs that match all535 local WAVs byte-for-byte by SHA-256.
No local 22.05→4-kHz conversion occurred for those copies; earlier acquisition/
conversion lineage is unknown. There are145 local mixed/source triples,
but distinct filenames are not proof of independent templates or synchronised
samplewise ground truth. Source-aware split manifests are absent; two historical
CSV-named split files are Excel ZIPs and the test split is empty. Do not overwrite them.

One bounded offline probe used a2-s synthetic signal and three existing manikin
triples. Fixed Filter/NMF returned finite, correctly sized arrays. Legacy STFT
round-trip lost an initial0.3-amplitude sample. Same-time two-gain fits on the three
recorded triples left residual norms approximately0.999989/0.999764/0.999507 relative
to the mixture. These are **contract diagnostics**, not separation scores; they
justify fixing STFT boundaries and not assuming recorded references are additive.
That statement describes the earlier design sprint. Since then, the pinned
released NeoSSNet checkpoint has loaded strictly with Torch `weights_only=True`
and returned two finite 10-s CPU outputs. GPU remains untested. VMD, model
training and full-dataset benchmarking were not performed.

**New six-mixture engineering qualification (not a held-out result):** the
source-family split precedes mixing (heart families 6/2/2 and lung 4/1/1 for
development/validation/test). Two development source pairs at −5/0/+5-dB ratios
formed exact additive digital mixtures, with source hashes/gains in an ignored
manifest. Six of six runs completed. Mean heart/lung SI-SDRi (dB), respectively:

| Method | Heart | Lung |
| --- | ---: | ---: |
| NeoSSNet raw | −3.47 | −13.83 |
| NeoSSNet projected control | −2.61 | −12.43 |
| Generic NMF raw | −4.71 | −10.17 |
| Generic NMF projected control | −4.62 | −9.88 |
| Fixed Filter | −2.49 | −6.49 |
| Fixed 50/50 ensemble | **−3.22** | **−10.20** |

Thus this small, non-independent development probe does **not** establish
ensemble improvement; it suggests performance/label applicability needs careful
qualification before a held-out study. Author code labels NeoSSNet channel0
heart/channel1 lung, but two selected manikin examples favour an opposite
reference assignment; other probes do not establish a stable swap. No oracle
permutation was used in scores or fusion. Initially five focused ensemble tests,
one boundary regression and two nearby baseline tests passed (8 focused);
one subsequent nearby ML regression pass was 12/12 with pinned `vmdpy` present.
A sixth ensemble test protects provenance without Git metadata; its addition
and the final portability fix passed two targeted executions. The broader suite
was not rerun for that metadata-only change. No strict no-fallback VMD
comparison is claimed. Exact artifacts, runtime, manifest limitations and
full per-source figures are in the implementation repository's
[`docs/ENSEMBLE_OFFLINE_QUALIFICATION.md`](https://github.com/ASHRAF-2004/Machine-Learning-Based-System-for-Cardiopulmonary-Sound-Separation/blob/fyp2/application/docs/ENSEMBLE_OFFLINE_QUALIFICATION.md).

Primary quantitative evaluation will use exactly summed, source-labelled digital
mixtures from provenance-checked isolated recordings. Group source families before
splitting/mixing/cropping; where template IDs are unavailable use conservative
sound-type families across sites/gender/modes and disclose limited independence.
Keep probe-exposed families out of a claimed untouched test set. Seeded60/20/20
development/validation/test allocation, fixed ratios(-5/0/+5dB), common source/mixture
gain, source hashes and exact counts are frozen before testing. No learned weights
or fine-tuning in v1. Test families may be too few for generalisation claims.

Recorded mixed audio remains a separate realism/qualitative set unless matched
time-aligned references are justified. No oracle reference alignment to rescue
test scores. The historical23-record/five-method CSV results lack sufficient
split/checkpoint provenance and used reference-optimised lag; preserve as historical
repository experiments, not comparable current FYP2 results. Submitted §4.5.2
explicitly deferred actual separation results to FYP2.

Evaluate raw single experts, their single-mask projections and the ensemble under
the same contract; retain mixture/Fixed Filter controls and strict VMD if qualified.
Heart and lung **SI-SDR/SI-SDRi separately** (Le Roux et al., 2019), paired differences,
mean/median/IQR, outliers, failures, runtime and memory. Reconstruction residual is
only a constraint check. Ratios/crops of the same source are not independent samples.
Use paired source-block bootstrap intervals only with enough independent blocks;
otherwise descriptive results with explicit small-data limitations. No automatic
PESQ/STOI/clinical metrics or p-value battery. A gain for heart cannot conceal a loss
for lung. Worse ensemble results must be reported honestly.

## Claims and approvals still absent

No ensemble improvement, production execution, real-time SLA, faithful published
method reproduction, clinical benefit, user evaluation or supervisor approval is
claimed. CPU loadability and released-file identity are verified; redistribution
permission, independent generalisation evidence, source-label applicability,
GPU/worker resource measurements and final held-out evaluation remain gates. This refinement
belongs in supervisor discussion; it was not validated by the original survey.

## References (APA 7)

Dragomiretskiy, K., & Zosso, D. (2014). Variational mode decomposition.
*IEEE Transactions on Signal Processing, 62*(3), 531–544.
https://doi.org/10.1109/TSP.2013.2288675

Grooby, E., Sitaula, C., Fattahi, D., Sameni, R., Tan, K., Zhou, L., King, A.,
Ramanathan, A., Malhotra, A., Dumont, G., & Marzbanrad, F. (2023). Noisy neonatal
chest sound separation for high-quality heart and lung sounds. *IEEE Journal of
Biomedical and Health Informatics, 27*(6), 2635–2646.
https://doi.org/10.1109/JBHI.2022.3215995

Lee, D. D., & Seung, H. S. (2000). Algorithms for non-negative matrix factorization.
In T. K. Leen, T. G. Dietterich, & V. Tresp (Eds.), *Advances in neural information
processing systems* (Vol. 13). MIT Press.
https://proceedings.neurips.cc/paper_files/paper/2000/hash/f9d1152547c0bde01830b7e8bd60024c-Abstract.html

Le Roux, J., Wisdom, S., Erdogan, H., & Hershey, J. R. (2019). SDR—Half-baked or
well done? In *2019 IEEE International Conference on Acoustics, Speech and Signal
Processing (ICASSP)* (pp. 626–630). IEEE. https://doi.org/10.1109/ICASSP.2019.8683855

Poh, Y. Y., Grooby, E., Tan, K., Zhou, L., King, A., Ramanathan, A., Malhotra, A.,
Harandi, M., & Marzbanrad, F. (2024). NeoSSNet: Real-time neonatal chest sound
separation using deep learning. *IEEE Open Journal of Engineering in Medicine
and Biology, 5*, 345–352. https://doi.org/10.1109/OJEMB.2024.3401571

Sun, W., Zhang, Y., & Chen, F. (2024). Research on heart and lung sound separation
method based on DAE–NMF–VMD. *EURASIP Journal on Advances in Signal Processing,
2024*, Article 59. https://doi.org/10.1186/s13634-024-01152-0

Torabi, Y., Shirani, S., & Reilly, J. P. (2025). Descriptor: Heart and lung sounds
dataset recorded from a clinical manikin using digital stethoscope (HLS-CMDS).
*IEEE Data Descriptions, 2*, 133–140. https://doi.org/10.1109/IEEEDATA.2025.3566012

Wisdom, S., Hershey, J. R., Wilson, K., Thorpe, J., Chinen, M., Patton, B., &
Saurous, R. A. (2019). Differentiable consistency constraints for improved deep
speech enhancement. In *2019 IEEE International Conference on Acoustics, Speech
and Signal Processing (ICASSP)* (pp. 900–904). IEEE.
https://doi.org/10.1109/ICASSP.2019.8682783
