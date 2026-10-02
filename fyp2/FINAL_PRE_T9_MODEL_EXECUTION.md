# Final pre-T9 model comparison — results

29 September 2026. **COMPARISON COMPLETE · HLS-ONLY T8 V2 RETAINED · T9 SEALED · NOT DEPLOYED.** The two frozen treatments were executed exactly under the predeclared grouped-family protocol. Neither passed the conjunctive adoption gate. No rescue variant, final refit, or T9 run was performed.

## Protocol and provenance

The planning config SHA-256 is `6776e53c1d53c66d39c8882169b6de729bc05358f337e26a91257fd74dce8103`. The matched saved control was verified and reused, not retrained. Five folds, eight held-out family-pair groups, and the same 1,775 correlated conditions were evaluated. Both treatments used seed 20260928, exact synthetic HLS recipes, fresh fold initialization, 576 updates, batch 4, AdamW LR 0.001, weight decay 0.0001, gradient clip 5, constant LR, and endpoint-only scoring. CPU environment: Python 3.14.4, torch/torchaudio 2.11.0+cpu. No T9 or external/native training data was used.

Implementation commit for all scored runs: `7d18f010b6ac247aab9f6b36b9daa379d2485536`. The implementation decision JSON `research/evidence/final_model_comparison_decision_v1.json` has SHA-256 `09890e6bfd714fef5583280318fde13d51bd0228310685bd9051f04c5e09428e` and binds the per-run hashes, metrics, gates and decision. Run outputs/checkpoints are ignored local artifacts, not committed.

## Treatment A — complex-mask TF U-Net

The exact 390,450-parameter frozen architecture passed its two-pair development capacity gate at update 180 in 13.957 s (peak RSS 620.47 MiB). Every case/source reached at least +10 dB SI-SDRi and at least 50% normalized waveform L1 reduction:

| Development pair | Heart SI-SDRi / L1 reduction | Lung SI-SDRi / L1 reduction |
|---|---:|---:|
| F_AF_A / F_N_LLA | +10.782 dB / 68.58% | +10.785 dB / 68.63% |
| F_ESM_LLSB / F_PR_LLA | +10.011 dB / 68.02% | +10.035 dB / 67.72% |

Capacity weights were not used for grouped folds. Five focused checks passed.

## Grouped-family metrics

All source scores below are equal-weight family-pair macro means. Q is the weaker source macro; balanced mean is the average of heart and lung SI-SDRi. The 1,775 conditions are correlated and are not IID subjects.

| Arm | Heart SI-SDR | Heart SI-SDRi | Lung SI-SDR | Lung SI-SDRi | Q | Balanced | Failures |
|---|---:|---:|---:|---:|---:|---:|---:|
| Control | 2.021 | 2.013 | 1.922 | 1.913 | 1.913 | 1.963 | 0 |
| A | 2.513 | 2.504 | 2.408 | 2.399 | 2.399 | 2.452 | 0 |
| B | 2.090 | 2.082 | 2.026 | 2.017 | 2.017 | 2.049 | 0 |

| Arm | ΔH | ΔL | ΔQ | Δbalanced | Pair balanced gains | Fold Q gains | Worst pair/source Δ | Negative-rate Δ H/L |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A | +0.492 | +0.485 | +0.485 | +0.489 | 8/8 | 5/5 | +0.114 | −5.13/−4.73 pp |
| B | +0.069 | +0.104 | +0.104 | +0.086 | 5/8 | 4/5 | −0.109 | −1.75/−1.30 pp |

Treatment-minus-control pair-level heart/lung SI-SDRi:

| Family pair | Control H/L | A H/L | B H/L |
|---|---:|---:|---:|
| Atrial Fibrillation × Wheezing | 2.984 / 2.739 | 3.623 / 2.858 | 2.875 / 2.639 |
| Early Systolic Murmur × Rhonchi | 1.246 / 0.807 | 1.599 / 1.041 | 1.336 / 0.883 |
| Late Diastolic Murmur × Fine Crackles | 2.836 / 2.609 | 3.180 / 3.570 | 3.022 / 2.965 |
| Late Systolic Murmur × Wheezing | 0.476 / 0.985 | 1.535 / 1.610 | 0.371 / 0.945 |
| Mid Systolic Murmur × Normal | 1.890 / 1.436 | 2.113 / 1.587 | 1.899 / 1.446 |
| Normal × Pleural Rub | 1.220 / 1.444 | 2.142 / 2.224 | 1.504 / 1.589 |
| S3 × Fine Crackles | 3.539 / 3.528 | 3.707 / 4.428 | 3.774 / 3.975 |
| Tachycardia × Rhonchi | 1.909 / 1.759 | 2.134 / 1.873 | 1.870 / 1.696 |

Fold Q deltas (f1 through f5): A `+0.151,+0.923,+0.174,+0.504,+0.375 dB`; B `+0.011,+0.284,+0.006,−0.107,+0.330 dB`. All arms scored all conditions; there were zero failures. Detailed per-fold endpoint hashes, runtimes, condition-level median/IQR and other provenance are in the JSON decision receipt. No IID uncertainty/significance claim is made.

## Frozen adoption decision

The gate required all twelve frozen conditions, including ΔQ and Δbalanced each at least +0.50 dB, both source gains at least +0.25 dB, balanced gains in at least 6/8 pairs, Q gains in at least 4/5 folds, no pair/source decline over 0.50 dB, negative-rate increases no more than 5 percentage points per source, zero failures, source macro floors of +1 dB and nonnegative means for every pair/source.

- **A: FAIL.** All clauses except the two aggregate margins passed. ΔQ is +0.4855 dB and Δbalanced +0.4886 dB. Do not round these into a pass or weaken the frozen gate.
- **B: FAIL.** ΔH +0.069, ΔL +0.104, ΔQ +0.104, Δbalanced +0.086 dB, and only 5/8 pair-balanced gains. Its other clauses passed.

The exact winner rule selects **CONTROL / HLS-only T8 v2** when neither passes. No all-non-test refit was authorized or performed; no v3 was created. The active specification remains `research/configs/final_separator_v2.json`, SHA `2573ae06b11aafc595a4cdb179e3ab0c9f7fbe37859863dcd36a5d8c70210b1b`; its checkpoint SHA is `1f7e549ba53240bc085221e4eed1f935bb7c330e9a66cfab4c183c8f096c2658`. Treatment A folds took 635.059 s total, B 525.005 s total; combined scored training 1,160.064 CPU seconds (19.33 minutes). Peak RSS was 943.266 MiB for A and 1,044.559 MiB for B.

T9 audio was not accessed and no test data/results were generated. Production, frontend, and Axora were untouched. This result is grouped non-test evidence, not a final held-out performance claim. **Ready for T9 with HLS-only T8 v2, subject to separate owner authorization. Stop.**
