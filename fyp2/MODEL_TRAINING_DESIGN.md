# Own separator training design — ADR T01

28 September 2026. **BASELINE AND ONE T7 WIDTH VARIANT TRAINED; ONE SEED
CONFIRMATION COMPLETED; VALIDATION EVIDENCE ONLY; FINAL TEST SEALED; NOT
DEPLOYED.** This is Application-Based FYP2 methodology and validation evidence,
not a held-out final result. Production and submitted FYP1 remain unchanged. The full
[implementation training plan](https://github.com/ASHRAF-2004/Machine-Learning-Based-System-for-Cardiopulmonary-Sound-Separation/blob/fyp2/application/docs/STETHOFUSE_MODEL_TRAINING_PLAN.md)
contains exact equations, baseline YAML, source manifest and Luna phases.

## Chapter 2 — Architecture decision and provenance

Select the **StethoFuse-ConvTasNet-4k** compact non-causal waveform-separation
family, trained from scratch with fixed output0=heart/output1=lung. It uses
torchaudio2.11.0 ConvTasNet (BSD-2-Clause), our target-free mixture-consistency
wrapper, and our training process/weights. The original 645,681-parameter
profile is the baseline control; the smaller 171,313-parameter profile narrowly
ranked first on the frozen validation selector and is the current research
candidate. Neither is deployed. No NeoSSNet code/weights are in this path.

Luo and Mesgarani (2019) support learned waveform encoding/decoding and dilated
depthwise temporal separation for speech, **not demonstrated cardiopulmonary
transfer**. The selected645,681-parameter configuration limits capacity and CPU
cost compared with an8.42M-parameter NeoSSNet-inspired network (Poh et al.,2024).
A TF U-Net is credible (Jansson et al.,2017; Ronneberger et al.,2015), but simple
magnitude masking retains mixture-phase constraints. Complex spectral mapping
would require further design. No architecture sweep or U-Net training occurred.

Scratch training avoids unverified fixed-semantic transfer from speech models
and unresolved NeoSSNet weights. The selected component's permission is the
**torchaudio release license**, not naplab's author code, which advertises
CC-BY-NC-SA3.0-US. Retain exact library notices and cite the architecture.
The [official HLS-CMDS API](https://zenodo.org/api/records/15376628) declares
CC-BY-4.0; preserve Torabi/Shirani/Reilly attribution and transformation records.
Software and data permissions are distinct.

NeoSSNet remains **research comparator only**. Its poor fixed-label manikin
diagnostics remain valid; native neonatal reproduction is unresolved, not
disproved. Published16.00/14.46 values retain the documented notebook SI-SDRi/
category-median/permutation caveat, not numerical targets for our fixed-label
means. The owner's own-training direction supersedes the author-email gate;
no email workflow continued and no NeoSSNet deployment permission was inferred.

## Chapters 3–4 — Data and model contract

The versioned CSV preserves100 standalone source IDs,100 unique hashes and
zero families spanning partitions. No existing test assignment was changed.

| Partition | Heart files / families | Lung files / families | Potential pairs |
| --- | ---: | ---: | ---: |
| Development/training | 36 / 6 | 36 / 4 | 1,296 |
| Validation | 9 / 2 | 5 / 1 | 45 |
| Locked test | 5 / 2 | 9 / 1 | 45 |

Source CSV SHA-256:
`39d5456477b07772bdc24b86ee73dee17c44fd1e0837b62b96eab8c19a1b65e4`.
Training contains9 minutes per source type. The1,296 pairings are correlated
remixes of72 source files, not independent subjects. Groups are sound families,
not verified subject/session/template identities. Test remains AV Block/S4
heart and Coarse Crackles lung; validation is Late Diastolic Murmur/Tachycardia
heart and Fine Crackles lung. No patient/device generalisation is established.

The released archive inspected for this project contains4 kHz WAV files.
Earlier acquisition/conversion provenance could not be established. Preserve
the conflicting22,050-Hz external description; do not invent resampling. Use
mono4-kHz PCM16→float32, with2-kHz Nyquist limitation. Recorded mixture/reference
triples are excluded from additive supervision because they were separately
recorded, not valid sample-aligned sums. Manikin filtering remains a confound.

Model: learned128-filter encoder/decoder, kernel32/stride16; bottleneck/skip64,
hidden128; kernel3 depthwise TCN,8 dilations repeated3 times; ReLU latent masks,
global normalization, no attention/BatchNorm/dropout. Train8-s crops; infer10-s
windows with8-s hop/2-s cosine overlap, deterministic padding and exact trim.
No PIT, oracle swapping, target-guided alignment or independent output gains.

For raw estimates `z_h,z_l`, add half the input residual to each:
`e=x−z_h−z_l; outputs=(z_h+e/2,z_l+e/2)` (Wisdom et al.,2019).
This is target-free and differentiable, ensuring additivity, not correctness.
It differs from the old ensemble's original-mixture-phase TF projection.
Learned waveform decoding can reconstruct phase. No third noise source is
modelled, so real background noise would be allocated to the two outputs.

### Mixture generation

Select independent valid8-s development crops and sample lung-to-heart level
uniformly in[−10,+10] dB. Scale lung by `RMS(h)/RMS(l) × 10^(level/20)`;
apply a shared gain keeping both contributions and their sum below0.95 peak;
sum. The mixture's peak then normalizes input and both targets together, and
inverse gain is retained. No quantization/clipping or inference-time oracle.

The envelope follows the original NeoSSNet mixing range, not a clinical ratio
distribution claim. Unequal measured development-source energies make raw1:1
amplitude an unjustified default. Augment only pairing, valid crop/relative
timing and relative level. No pitch/time distortion, arbitrary filtering,
unjustified noise or global gain subsequently cancelled by normalization.

An epoch is576 draws:24 instances of each24 family pairs with shuffled source
cycles balanced within each family; batch4 gives144 steps. Save source IDs/
hashes, seeds, starts, gains and generated-array hashes. Generate mixtures on
demand. No large redundant WAV corpus; crops do not increase independent N.

## Chapters 5–6 — Training/evaluation methodology and baseline evidence

The T0–T4 pipeline and T5 CPU baseline are implemented and executed offline.
The approved baseline configuration used was:

- Fixed-label mean negative SI-SDR plus **5×source-RMS-normalized waveform L1**.
  SI-SDR uses mean removal and the audited1e-8 energy epsilon; uncentered L1
  retains amplitude/DC. Weight5 is precommitted, not empirically optimal.
- Scratch seed20260928; AdamW LR0.001, betas0.9/0.999, eps1e-8, decay1e-4;
  clip gradient norm5.0. Batch4, fp32, CPU2 threads, loader workers0.
- Max80 epochs; ReduceLROnPlateau factor0.5/patience4/absolute0.1-dB threshold/
  minLR1e-5; early stop after12 epochs without significant0.1-dB improvement.
  Separate best, final and resumable checkpoints; never choose by test score.
- First intentionally overfit two fixed development mixtures: ≤400 updates/
  10 min; each source/case SI-SDRi≥10 dB and normalized L1 reduction≥50%.
  Failure blocks baseline. Discard those fitted weights and initialize afresh.
- T7 decision below selects one smaller-width variant and one predeclared
  seed-sensitivity run. No second variant, broad sweep or test feedback.

Validation:45 pairs ×five levels(−10,−5,0,5,10)=225 **correlated conditions**,
full15 s, no random crop. Score each source using the same mixture and reference.
Macro-average SI-SDRi across family-pair groups equally; call these H and L.
**Select Q=min(H,L)**, tie-break by(H+L)/2 then earlier epoch. This protects the
weaker source. Also show pooled mean/median/IQR, each level/family, runtime and
failures. Only two validation family-pair groups exist; do not overstate support.

Test IDs/hashes and the 45-pair/five-level/full15-s recipe specification are
frozen; no test recipes have been generated and test waveforms remain unopened.
Freeze code/model/config/preprocessing/
labels/comparator list before **one held-out final evaluation**. Never tune,
early-stop, cherry-pick or debug on test. Poor results do not authorize reuse;
only a disclosed genuine implementation defect may justify a corrected rerun.

Eventual baselines: mixture, Fixed Filter, generic NMF, own model; VMD only after
strict no-fallback qualification on development, and released NeoSSNet as a
research comparator where appropriate. Same windows/gain/labels/metrics; no
historical FYP1 values reused. Report separate heart/lung SI-SDR and SI-SDRi,
failures and runtime. Positive absolute scores and improvement for both sources
are gates, not promises. With45 remixed pairs and few held-out families, avoid
naïve225-independent-row significance claims; use descriptive paired evidence.

### T5/T6 baseline validation evidence — not final test

The fresh-seed CPU baseline completed **20 epochs** and stopped under the
configured 12-epoch early-stopping policy; best checkpoint was epoch8. Frozen
selection used 225 validation-only conditions in two family-pair groups. Best
family-pair macro results were Heart SI-SDR **3.031 dB**, SI-SDRi **3.035 dB**;
Lung SI-SDR **3.075 dB**, SI-SDRi **3.079 dB**. The weaker-source selector was
**3.035 dB**, tie-break mean **3.057 dB**; validation had zero failures. Both
source SI-SDRi values were positive and close, but condition-level spread was
substantial and only two family-pair groups contribute. These are limited
development/validation findings, not final test results, subject-independent
generalization, or a claim of clinical or comparative superiority.

Training loss declined from1.397 (epoch1) to−3.706 (epoch20), while the best
validation selector occurred at epoch8 and fluctuated afterward. LR followed
the configured plateau schedule. LR used for training was 0.001 in epochs 1–7,
0.0005 in 8–13, 0.00025 in 14–18, and 0.000125 in 19–20. This corrects the
earlier prose: logs record post-validation LR, so reductions after epochs
7/13/18 affect the next epoch. No numerical result or artifact changed.
Runtime was1,243.5s (20.72min), peak RSS
2,078MiB on CPU. No nonfinite loss/gradient and zero validation failures were
recorded. The run used fresh seed20260928 initialization; the T4 checkpoint was
not loaded. Six existing focused training-contract tests passed; no new test
campaign or application regression ran. Full run provenance and checkpoint
hash are in the implementation execution receipt.

**The final test partition remains sealed:** no test audio was decoded, no test
recipes were generated, and no test metrics were computed. The model is not
integrated or deployed. Owner review is required before any final freeze or
one-shot test.

### T7 width experiment and one seed confirmation — validation only

The baseline remains a valid control. The predeclared small-width profile was
evaluated offline after the bounded gate passed. This is validation evidence,
not a final-test result or a production model selection.

| Validation family pair | Conditions | Heart mean SI-SDRi | Lung mean SI-SDRi |
| --- | ---: | ---: | ---: |
| Late Diastolic Murmur × Fine Crackles | 150 | 3.847 dB | 3.713 dB |
| Tachycardia × Fine Crackles | 75 | 2.223 dB | 2.445 dB |

These two groups receive equal macro weight; 225 correlated conditions are
not 225 independent examples. Both group averages improve both sources, but
Tachycardia contains 23/28 negative heart-improvement conditions. Pooled H/L
SI-SDRi median is 2.973/2.848 dB, IQR 3.877/4.581 dB. At −10 dB lung/heart
level, macro heart improvement is −0.267 dB; at +10 dB, macro lung improvement
is −0.517 dB. The already-dominant source sometimes worsens while the quieter
source improves yet remains poor in absolute SI-SDR. Negative improvement is
not a runtime failure. No conditions were removed or reweighted.

Training gain draws cover the range approximately uniformly; no silent-crop
retries were recorded. All validation crops are fixed full 15 seconds. There
is no demonstrated gain-coverage defect justifying new augmentation/sampling.

From epoch 8 to 20, mean negative SI-SDR changes −4.313→−5.535 and unweighted
normalized L1 0.420→0.366. The 5×L1 contribution drops 2.098→1.829;
approximately 82% of the total-loss improvement comes from SI-SDR. Both
objectives improve while validation plateaus; this does not support reducing
the L1 coefficient. Scalar magnitudes are not gradient attribution, and no
per-component gradient or validation-L1 history was saved. Overfit/generalization
pressure is plausible, but excessive capacity is not established; narrow
validation coverage and family/level heterogeneity limit the causal conclusion.

The sole variant used the smaller N64/B32/H64 Conv-TasNet, scratch seed
**20260928**. Its actual pinned-library count is **171,313 parameters** (the
design estimate was 170,545); width alone changed. It passed the two-example
development gate and was then trained fresh for 17 epochs, selecting epoch 8.
Validation macro H/L SI-SDRi was **3.101/3.130 dB**, Q **3.101 dB**, balanced
mean **3.116 dB**, zero failures. The existing 645,681-parameter baseline
scored Q **3.035 dB** and mean **3.057 dB**. The small profile's margins
(+0.066 dB Q, +0.059 dB mean) are descriptive only given two family-pair
groups; they do not establish superiority. Both small-model sources improved
on average. Family-pair and relative-level details, runtime and checkpoint
hash are preserved in the linked implementation decision record.

Configuration selection occurred on seed 20260928 **before** one fresh
seed-20260929 robustness confirmation. That run selected epoch 4 (16 epochs),
with H/L SI-SDRi **3.332/3.328 dB**, Q **3.328 dB**, balanced mean **3.330 dB**,
zero failures. Its higher score does not replace the canonical seed-20260928
checkpoint. Across only two family-pair groups and correlated level conditions,
the family/level behavior differs enough that seed robustness is **UNCERTAIN**,
not established. No second variant or further seed was run. Variant 2 remains
**NONE**; the loss, optimizer, sampler and all other settings stayed frozen.

Exact evidence, deltas, hashes, future runner changes and stop criteria:
[T7 decision](https://github.com/ASHRAF-2004/Machine-Learning-Based-System-for-Cardiopulmonary-Sound-Separation/blob/fyp2/application/docs/T7_TUNING_DECISION.md)
and [Luna handoff](https://github.com/ASHRAF-2004/Machine-Learning-Based-System-for-Cardiopulmonary-Sound-Separation/blob/fyp2/application/docs/T7_LUNA_HANDOFF.md).
The small configuration is the selected validation candidate for subsequent
system-level validation work, not a final model. No superiority, clinical
performance, subject/device generalization, or deployment claim is supported.
The final test remains sealed.

### T0–T4 offline pipeline evidence — not trained-model results

The frozen T0–T4 pipeline is now **IMPLEMENTED OFFLINE** and the T4 capacity
gate **PASSED** on exactly two predeclared development mixtures after100 CPU
updates (13.90 seconds): every heart/lung case exceeded+10 dB SI-SDRi and
reduced source-normalized waveform L1 by at least74.4%. This demonstrates only
that the implementation can fit those two examples. It is **not** baseline
training, validation performance, held-out evidence, or a separation-quality
claim. The overfit checkpoint is excluded from future initialization.

The source manifest was re-audited at T0:100 distinct IDs/hashes, no sound
family crossing partitions, expected mono4-kHz PCM16/15-s headers. Development
and validation waveforms were finite; test waveforms remained locked and were
not decoded or scored. Deterministic training recipes (576 draws/epoch) and
225 validation-only recipes were written outside Git. The pinned model forward
and backward passed at645,681 parameters, with synthetic consistency error
below2.4e−7. The whole-record wrapper implements10-s windows/8-s hop and passed
a length/additivity check on synthetic input. Six focused training-contract
tests passed.
The T4 execution used the then-uncommitted working tree at its recorded base
HEAD; a clean source-tree snapshot was not captured. This reproducibility
limitation is recorded in the run receipt, so this remains bounded engineering
evidence rather than a clean-commit reproducibility result.
Detailed run receipt is in the implementation's
`docs/T0_T4_EXECUTION.md`.

### Bounded feasibility evidence — design-only probe, not trained results

Actual server: Ryzen5 9600X6-core/12-thread CPU,29 GiB RAM; Radeon RX9060XT16
GiB exists, but Torch/torchaudio2.11.0 are CPU-only. No driver/dependency changes.
Synthetic sizing probes only: final retained probe measured645,681 parameters,
0.343 s batch4×8-s forward/loss/backward,0.0194 s warmed10-s inference and1155
MiB process peak RSS at2 threads. Shapes/finite gradients/repeatability passed;
weights unchanged, **zero optimizer steps**. Not quality/throughput guarantees.

The first baseline took20.72min for20 epochs including per-epoch validation;
observed epoch duration was about60–63s and peak RSS2,078MiB. This is a measured
single-run observation, not a guarantee for another host. Stop/checkpoint above
8-h projection or4-GiB memory. A single resource
fallback uses the same TCN at N64/B32/H64(170,545 parameters), subject to the
same capacity gate. No automatic paid compute, GPU setup or model search.

## Handoff and requirements traceability

T0–T7 are complete and checkpointed. **Next, separately authorize the
validation-only ensemble reconsideration before freezing the complete
separation system and opening the held-out test once.** No ensemble was
evaluated during T7. No broad application regression was run; production and
application behavior were not changed.

Own artifacts belong in ignored `.local/training/stethofuse-tcn-v1/<run-id>/`
with immutable config/manifest, recipes/RNG/version/device provenance, all
validation metrics, state dictionaries and SHA-256. No large audio/weights in
Git. Future packaging must verify our artifact hash and preserve license/data
notices; this document is not deployment approval.

The50/50 NeoSSNet+NMF candidate stays **implemented offline / frozen /
unqualified / not deployed / no demonstrated advantage**. Any new ensemble
choice must use validation **before** the final test. Explicit future order:
baseline → bounded T7 → selected configuration → seed confirmation →
**validation-only ensemble decision (legacy T10 moved before T8/T9)** → freeze
the complete separation system → one owner-authorized held-out test. Do not
test the single model and then use that result to choose/tune an ensemble;
after testing, a newly tuned system needs untouched evaluation data. Ensemble requirement/default choice
remains a later owner/FYP decision. Authentication, roles, jobs, storage,
frontend, backups and production routing are unchanged. No clinical or
superiority claim is made. Sources are recorded in
[`provenance/ensemble-references.bib`](provenance/ensemble-references.bib).
