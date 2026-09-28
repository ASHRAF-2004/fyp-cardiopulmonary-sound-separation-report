# HLS native-triplet audit and pilot result

**FORENSIC AUDIT COMPLETE · ROLE A QUALIFIED SUBSET · PILOT COMPLETE / ADOPTION GATE FAILED · T8 V2 RETAINED · T9 SEALED · NOT DEPLOYED**

This record follows the HLS synthetic baseline, bounded Conv-TasNet tuning,
external clinical-data negative-transfer experiment, and HLS-only fixed-budget
refit. It preserves those results and reports one completed native-treatment
pilot below. The qualified waveform targets did **not** improve grouped-family
transfer under the frozen adoption gate. The native and external branches are
closed; the 171,313-parameter HLS-only T8 v2 remains selected. Submitted FYP1,
frontend and production remain unchanged. No final-test result exists.

## Why native triplets were reconsidered

The data-limited diagnosis motivated checking whether HLS-CMDS's corresponding
mixture/heart/lung files contain supervision omitted from standalone synthetic
training. Nonadditivity alone does not establish that all triplets are useless.
Conversely, a dataset's correspondence label does not establish waveform truth.
The audit therefore tests timing, amplitude, filter-domain correspondence,
reference reuse and leakage before any neural treatment.

The [official author repository](https://github.com/Torabiy/HLS-CMDS) distinguishes
the earlier 210-file/110-mixture release from Dataset.v2 with **535 WAVs**:
50 standalone heart, 50 standalone lung, and 145 mixture/heart/lung triplets.
The local archive inventory agrees with the latter. The verified eligible WAV
contract is mono PCM16, 4 kHz, 15 seconds; the paper's stated 22,050 Hz does not
match these release headers. No undocumented conversion history is inferred.

The original publication describes CAE Juno/Maestro repeated playback recorded
using Littmann CORE/Eko. Mixtures enable both sources; isolated references are
recorded separately without moving the stethoscope. Reported modes differ:
heart/Bell, lung/Diaphragm, mixture/Midrange. Playback repetition is not proof of
sample synchronization. Per-file gain, phase reset, processing coefficients and
actual filter state are undisclosed (Torabi et al., 2025).

## Measured evidence and qualified population

Frozen family metadata excludes **45 triplets before audio access**. The
remaining 100 triplets cover eight heart and five lung families, all 40 permitted
family pairs. No test signal was decoded or fingerprinted. The measured release
has two distinct regimes:

| Eligible population | Correspondence finding | Decision |
|---|---|---|
| 73 earlier-numbered triplets | Median raw residual/mixture RMS 1.706; alignment/two-gain correction 1.036; fixed global FIR 1.035 on untouched temporal support. | Waveform supervision not qualified. |
| 27 later-numbered triplets | Same-time `M ≈ g(H+L)` with one positive gain calibrated on 6–9 s. Both untouched flanks pass the fixed residual limit; worst residual is 0.004798 times weaker-source RMS. | High-confidence waveform correspondence after shared amplitude calibration. |
| One full duplicate among those 27 | M0126 duplicates M0111's mixture and both references. | Retain M0111 only: **26 training triplets**. |

These are signal-quality exclusions, not selections using model scores. The
qualified subgroup requires no FIR, time warp or target-residual redistribution.
Use original released mixture input and targets `gH`, `gL`; references are needed
only for offline target preparation, never inference.

The qualified files happen to be above ID110, but the selection rule is measured
correspondence, not ID. Their common-gain structure and full-scale peak behavior
are consistent with normalized digital addition. **Their generation history is
not documented.** The paper, official README and repository history do not
explain a separate construction procedure for the appended files. Do not call
this evidence of newly captured real acoustic mixtures, or extend the finding
to the eight excluded later-numbered triplets.

The 26 retained triplets span **19 family pairs**, with 23 unique heart and
22 unique lung reference hashes. Thirteen heart and thirteen lung files are
absent from the standalone 86-source non-test pool. Thus they add **26 observed
reference files, zero new family categories and no established new patients**.
Many other references are exact standalone copies. A cross-class duplicate
labels the same bytes as Fine Crackles lung and Late Systolic Murmur heart in
three earlier records; all are unqualified and excluded, not silently relabelled.

## Why global transfer failure does not reject the subgroup

Global PSD fitting used 74 triplets/32 family pairs, with 26 triplets/eight pairs
held out. Correct references were compared with deterministic wrong-heart,
wrong-lung, both-wrong and same-family alternatives; alternatives came only from
the fitting partition and were selected by metadata/hash, not signal scores.
Correct-reference Hellinger error was lower in respectively 13, 15, 16 and
8 of 26 held-out conditions. This weak pooled discrimination does not qualify
general spectral targets for the nonadditive records.

The pooled global map worsened held-out macro Hellinger distance from 0.323 to
0.430. However, reusing the same outputs without refitting shows raw late-subset
PSD shape error only **0.0295**, versus **0.3805** for earlier held-out records.
Variable common gains explain much of the late absolute PSD mismatch. Therefore
the failed pooled map must not override near-exact waveform closure in the
restricted subgroup. Pair holdout is not independent-reference validation:
reference hashes cross those diagnostic groups. Neural evaluation uses stronger
family-heldout folds instead.

## Frozen matched pilot — preserved historical protocol

**ROLE A: direct waveform supervision of the qualified additive release subset.**
The [implementation audit and protocol](https://github.com/ASHRAF-2004/Machine-Learning-Based-System-for-Cardiopulmonary-Sound-Separation/blob/fyp2/application/docs/HLS_NATIVE_TRIPLET_AUDIT.md)
contain exact manifests, hashes and settings.

- Both arms use fresh seed20260928, existing small Conv-TasNet, CPU, AdamW
  LR0.001/weight decay0.0001, gradient clip5, exactly576updates and endpoint only.
- Keep each control synthetic batch4 unchanged. Treatment adds native batch4
  using `Lsynthetic + 0.25 Lnative`; both use the existing fixed-label negative
  SI-SDR +5×RMS-normalized L1. Extra compute is disclosed; no weight search.
- Native sampling balances available heart family, then lung family, then
  triplet and aligned8s crop. Shared scaling preserves released relative levels;
  synthetic −10…+10 dB mixing remains unchanged.
- Both native families must belong to a fold's training population. Reuse the
  verified matched HLS-only control, identical synthetic recipes, and existing
  five folds/eight held-out family pairs/1,775 correlated synthetic conditions.
  The old narrow approximately3.1dB score is not the matched control.

Adoption requires **all** predeclared guards: macro Q and balanced mean gains
≥0.50dB; heart/lung each≥0.25dB; balanced mean improves in≥6/8pairs and Q in≥4/5folds;
no pair/source regression>0.50dB; zero failures; no source's negative-condition
rate increase>5percentage points. Absolute utility also requires each source's
macro SI-SDRi≥1dB and every pair/source mean≥0dB. This engineering margin exceeds
twice the previously observed approximately0.227dB seed-Q gap; it is not a
statistical-significance claim or an IID-condition inference.

If FAIL, retain v2 and stop—no rescue loss, weight, role, seed or larger model.
If PASS, train once fresh on all45heart/41lung non-test sources plus26qualified
triplets with the same576-update constant-LR endpoint rule, then freeze v3 while
preserving v1/v2. No absorbed-validation or test checkpoint selection is allowed.

## Observed pilot result and decision

**FAIL: retain HLS-only T8 v2. No native final refit or v3 is produced.**
The preceding criteria were fixed before treatment, not revised from its result.
All five treatment runs used clean implementation commit
`ff2f09e85f3bf67587015971d0ef20fcffdbb5f8`, protocol SHA-256
`434506c52494d4473c8a1cf6664db67e211075e255f6f26ee893bdafa0954272`,
seed20260928 and exactly576updates each. Receipts verify identical fresh
initialization, all2,304 synthetic examples and validation condition IDs against
each matched control. No initializer checkpoint was loaded. One treatment was
evaluated across five grouped folds—not five tuning variants or independent
patient studies.

The five CPU runs took **815.510 seconds** in total, with maximum peak RSS
**1,096.527 MiB**. The decision receipt,
`implementation/research/evidence/hls_native_pilot_decision_v1.json`, preserves
per-fold run manifests, endpoint checkpoint hashes, recipe/history/evaluation
hashes and every gate result. Numerical failures were zero in both arms.

Aggregate equally over eight family-pair means, not over unequal fold sizes or
the1,775 correlated conditions. Q is the weaker macro source SI-SDRi; M is their
balanced mean. Values below are dB.

| Arm at576updates | Heart SI-SDR | Heart SI-SDRi | Lung SI-SDR | Lung SI-SDRi | Q | M |
|---|---:|---:|---:|---:|---:|---:|
| HLS synthetic-only control | 2.021 | 2.013 | 1.922 | 1.913 | 1.913 | 1.963 |
| Synthetic + qualified native treatment | 2.059 | 2.050 | 0.840 | 0.832 | 0.832 | 1.441 |
| Treatment minus control | +0.038 | +0.038 | −1.082 | −1.082 | −1.082 | −0.522 |

| Held-out family pair | Δ heart SI-SDRi | Δ lung SI-SDRi | Δ M |
|---|---:|---:|---:|
| Atrial Fibrillation × Wheezing | −0.022 | −0.111 | −0.066 |
| Early Systolic Murmur × Rhonchi | +0.158 | +0.026 | +0.092 |
| Late Diastolic Murmur × Fine Crackles | −0.396 | −3.074 | −1.735 |
| Late Systolic Murmur × Wheezing | +0.142 | +0.098 | +0.120 |
| Mid Systolic Murmur × Normal | +0.087 | −0.137 | −0.025 |
| Normal × Pleural Rub | +0.888 | −0.028 | +0.430 |
| S3 × Fine Crackles | −0.502 | −5.075 | −2.789 |
| Tachycardia × Rhonchi | −0.053 | −0.353 | −0.203 |

Only **3/8 pairs** improved M and **2/5 folds** improved Q. The largest losses
were in the Fine Crackles holdout fold: treatment lung SI-SDRi became −0.465dB
for Late Diastolic Murmur and −1.547dB for S3. Macro lung SI-SDRi also fell below
the1dB absolute-utility floor. Pooled negative-condition rates changed from
24.789%→19.944% for heart and28.732%→35.662% for lung; the lung increase of
6.930percentage points exceeds the5-point guard. These rates are descriptive,
not independent binomial observations. Every adoption guard except zero new
numerical failures failed; a small heart aggregate gain cannot override lung
regression or the frozen weaker-source policy.

**Interpretation:** this is valid negative transfer under the tested additional-
supervision policy, not failure to establish the subset's mathematical
additivity. More file hashes did not create new family categories or establish
independent physiological diversity. Restricted reference coverage, retained
native level relationships and the added objective can plausibly alter the
learned source prior, but this single matched experiment does not isolate which
mechanism caused the lung regression. Five folds share training families and
are not independent patients. No causal, statistical-superiority or clinical
claim follows. No additional role, weight, loss, seed, capacity or rescue run is
performed.

## Retained final separator and stop checkpoint

The active final separator remains **HLS-only T8 v2**, small Conv-TasNet
N64/B32/H64,171,313parameters, seed20260928, its existing576-update all-non-test
refit endpoint. Unchanged frozen specification:
`implementation/research/configs/final_separator_v2.json`, SHA-256
`2573ae06b11aafc595a4cdb179e3ab0c9f7fbe37859863dcd36a5d8c70210b1b`.
Unchanged checkpoint SHA-256:
`1f7e549ba53240bc085221e4eed1f935bb7c330e9a66cfab4c183c8f096c2658`.
V1/v2 history, native forensic data and rejected pilot artifacts are preserved;
there is no v3 and no native all-non-test final training.

**READY FOR T9 WITH HLS-ONLY T8 V2.** This is a readiness statement, not permission
to execute the test. T9 remains completely unopened and its predeclared protocol
unchanged. Production, frontend, FYP1 and application integration remain
untouched. The UX decision remains **NO DEMOGRAPHIC INPUT REQUIRED**. Stop for
separate owner authorization before any T9 execution.

## References

Torabi, Y., Shirani, S., & Reilly, J. P. (2025). Descriptor: Heart and lung sounds
dataset recorded from a clinical manikin using digital stethoscope (HLS-CMDS).
*IEEE Data Descriptions, 2*, 133–140. https://doi.org/10.1109/IEEEDATA.2025.3566012

Torabi, Y. (n.d.). *HLS-CMDS* [Data set and repository; commit
ad9a5b08c05f31a61096fec4ab4fde6b0ff1f45c]. GitHub.
https://github.com/Torabiy/HLS-CMDS
