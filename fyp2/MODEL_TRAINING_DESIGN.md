# Own separator training design — ADR T01

28 September 2026. **DESIGNED / PLANNED / NOT YET TRAINED / NOT YET EVALUATED.**
This is Application-Based FYP2 design/methodology, not Chapter5/6 training or
separation results. Production and submitted FYP1 remain unchanged. The full
[implementation training plan](https://github.com/ASHRAF-2004/Machine-Learning-Based-System-for-Cardiopulmonary-Sound-Separation/blob/fyp2/application/docs/STETHOFUSE_MODEL_TRAINING_PLAN.md)
contains exact equations, baseline YAML, source manifest and Luna phases.

## Chapter 2 — Architecture decision and provenance

Select **StethoFuse-ConvTasNet-4k-v1**: compact non-causal waveform separation,
trained from scratch, fixed output0=heart/output1=lung. It uses torchaudio2.11.0
ConvTasNet (BSD-2-Clause), our target-free mixture-consistency wrapper, and our
training process/weights. No NeoSSNet code/weights in this production path.

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

## Chapters 5–6 — Planned training/evaluation methodology

The T0–T4 data/model/objective and capped overfit runner are implemented offline.
The **full baseline trainer/run (T5) is not implemented or started**. Its
approved baseline configuration remains:

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
- At most two diagnosed single-factor variants and one optional seed-sensitivity
  run after baseline. No broad sweep or test feedback.

Validation:45 pairs ×five levels(−10,−5,0,5,10)=225 **correlated conditions**,
full15 s, no random crop. Score each source using the same mixture and reference.
Macro-average SI-SDRi across family-pair groups equally; call these H and L.
**Select Q=min(H,L)**, tie-break by(H+L)/2 then earlier epoch. This protects the
weaker source. Also show pooled mean/median/IQR, each level/family, runtime and
failures. Only two validation family-pair groups exist; do not overstate support.

Test IDs/hashes and the same45-pair/five-level/full15-s recipe are frozen now,
but test waveforms remain unopened. Freeze code/model/config/preprocessing/
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
tests passed. Full baseline training
and model selection remain **NOT STARTED**; there are no model results yet.
Detailed run receipt is in the implementation's
`docs/T0_T4_EXECUTION.md`.

### Bounded feasibility evidence — design-only probe, not trained results

Actual server: Ryzen5 9600X6-core/12-thread CPU,29 GiB RAM; Radeon RX9060XT16
GiB exists, but Torch/torchaudio2.11.0 are CPU-only. No driver/dependency changes.
Synthetic sizing probes only: final retained probe measured645,681 parameters,
0.343 s batch4×8-s forward/loss/backward,0.0194 s warmed10-s inference and1155
MiB process peak RSS at2 threads. Shapes/finite gradients/repeatability passed;
weights unchanged, **zero optimizer steps**. Not quality/throughput guarantees.

Estimate1.5–4 h for a CPU80-epoch baseline; replace with measured timing after3
epochs. Stop/checkpoint above8-h projection or4-GiB memory. A single resource
fallback uses the same TCN at N64/B32/H64(170,545 parameters), subject to the
same capacity gate. No automatic paid compute, GPU setup or model search.

## Handoff and requirements traceability

T0–T4 are complete and checkpointed. **Next, owner review is required before
T5 baseline training.** The full plan defines baseline, validation, bounded
tuning, final freeze and one-shot test. No broad application regression was
run; production and application behavior were not changed.

Own artifacts belong in ignored `.local/training/stethofuse-tcn-v1/<run-id>/`
with immutable config/manifest, recipes/RNG/version/device provenance, all
validation metrics, state dictionaries and SHA-256. No large audio/weights in
Git. Future packaging must verify our artifact hash and preserve license/data
notices; this document is not deployment approval.

The50/50 NeoSSNet+NMF candidate stays **implemented offline / frozen /
unqualified / not deployed / no demonstrated advantage**. Any new ensemble
choice must use validation **before** the final test; after that, a newly tuned
ensemble needs untouched evaluation data. Ensemble requirement/default choice
remains a later owner/FYP decision. Authentication, roles, jobs, storage,
frontend, backups and production routing are unchanged. No clinical or
superiority claim is made. Sources are recorded in
[`provenance/ensemble-references.bib`](provenance/ensemble-references.bib).
