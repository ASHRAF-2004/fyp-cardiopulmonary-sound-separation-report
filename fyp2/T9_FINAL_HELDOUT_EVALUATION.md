# T9 final held-out evaluation

29 September 2026. **T9 COMPLETE · FINAL MODEL HLS-ONLY T8 V2 · MODEL
SELECTION CLOSED · TEST CONSUMED · NOT YET INTEGRATED.** The one-shot frozen
evaluation covered all 225 conditions for the four authorized methods with no
failures. No model or method was changed after the first held-out waveform was
opened.

## Protocol and frozen model

Run `t9-final-heldout-v1`; implementation SHA at first waveform access:
`e343102692efa0187d1c2e0b75e53c318b579f85`. The implementation and
documentation worktrees were clean before access. Documentation starting SHA:
`944a646e09da466040d22b6de0af6e05fe3b0d77`. First waveform access was
`2026-09-28T21:42:52.641041+00:00`. Test-protocol SHA-256:
`c2c884211a2a7361aedcea7eaadb2ab752a853200b10e6ca244c4dee3692822c`;
source-manifest SHA-256:
`39d5456477b07772bdc24b86ee73dee17c44fd1e0837b62b96eab8c19a1b65e4`.

Frozen model: compact Conv-TasNet N64/B32/H64, 171,313 parameters, seed
20260928, 576 updates. Checkpoint SHA-256
`1f7e549ba53240bc085221e4eed1f935bb7c330e9a66cfab4c183c8f096c2658`;
separator-spec SHA-256
`2573ae06b11aafc595a4cdb179e3ab0c9f7fbe37859863dcd36a5d8c70210b1b`.
Strict loading and synthetic inference checks passed before access. Evaluation
used 5 heart × 9 lung sources × five levels (−10, −5, 0, +5, +10 dB), full
15-second inputs, and exactly these methods: mixture baseline, Fixed Filter,
Generic NMF, and final T8 v2. The final model retained 4-kHz mono input,
10-second windows, 8-second hop, fixed heart/lung order, and target-free
equal-residual mixture consistency. No projection or ensemble was used.

Metrics were the frozen zero-mean SI-SDR (epsilon 1e−8) and same-condition
mixture SI-SDRi. Aggregation averages conditions within each family pair and
then family pairs equally. The 225 conditions are correlated remixes, not 225
independent patients.

## Aggregate results

Scores are dB; mixture baseline SI-SDRi is zero by definition.

| Method | Heart SI-SDR | Heart SI-SDRi | Lung SI-SDR | Lung SI-SDRi | Failures | Runtime |
|---|---:|---:|---:|---:|---:|---:|
| Original mixture | −0.037 | 0.000 | −0.037 | 0.000 | 0 | 0.003 s |
| Fixed Filter | 0.325 | 0.362 | −2.484 | −2.447 | 0 | 1.077 s |
| Generic NMF | −2.503 | −2.466 | −3.444 | −3.407 | 0 | 4.180 s |
| Final T8 v2 Conv-TasNet | 1.813 | 1.849 | 2.296 | 2.333 | 0 | 11.140 s |

Final separator SI-SDRi median/IQR: Heart **2.146/3.332 dB**; Lung
**1.691/4.975 dB**. Both source macro improvements are positive. Relative to
Fixed Filter, v2 is higher by +1.487 dB Heart and +4.779 dB Lung; relative to
Generic NMF, +4.315 and +5.740 dB. The source macros are fairly close, but
level-specific weakness remains asymmetric.

## Family-pair and level detail

Only two heart×lung family-pair groups occur in this test partition:

| Family pair | Heart SI-SDR | Heart SI-SDRi | Lung SI-SDR | Lung SI-SDRi | Balanced SI-SDRi | Conditions | Failures |
|---|---:|---:|---:|---:|---:|---:|---:|
| AV Block × Coarse Crackles | 0.742 | 0.784 | 1.068 | 1.111 | 0.947 | 135 | 0 |
| S4 × Coarse Crackles | 2.884 | 2.915 | 3.523 | 3.555 | 3.235 | 90 | 0 |

S4 × Coarse Crackles was strongest by balanced SI-SDRi; AV Block × Coarse
Crackles was hardest.

| Lung-to-heart level | Heart SI-SDRi | Lung SI-SDRi | Balanced mean | Conditions |
|---:|---:|---:|---:|---:|
| −10 dB | −1.744 | 3.862 | 1.059 | 45 |
| −5 dB | 0.982 | 3.602 | 2.292 | 45 |
| 0 dB | 2.627 | 2.950 | 2.788 | 45 |
| +5 dB | 3.205 | 1.402 | 2.303 | 45 |
| +10 dB | 3.112 | −1.374 | 0.869 | 45 |

The hardest levels descriptively were −10 dB for Heart and +10 dB for Lung.
This pattern does not authorize further tuning on this consumed test.

## Interpretation and limits

Previous grouped non-test fold controls were Heart/Lung SI-SDRi
2.013/1.913 dB; final T9 v2 was 1.849/2.333 dB. The descriptive differences
(−0.163/+0.419 dB) are not a paired estimate of a common population: fold
endpoints and the all-non-test final endpoint differ, and T9 includes only two
family-pair groups. This is the first held-out result for the exact final v2
checkpoint; no significance claim is made.

The scope is controlled HLS-CMDS held-out-source separation on manikin
recordings. It does not establish clinical effectiveness, diagnostic accuracy,
patient-level/subject-independent generalization, or superiority outside this
protocol. Treatment A remains a promising non-test result but was not selected
for T9: its +0.4855 dB ΔQ and +0.4886 dB Δbalanced mean narrowly missed the
predeclared +0.50 dB gates, which were not relaxed. Treatment A was not tested
on T9.

Ignored raw evidence is under
`implementation/.local/training/stethofuse-tcn-v1/t9/t9-final-heldout-v1/`.
Recipe SHA-256 `1de947075c1feb73376f131c7a76284df9f5e945b02428e750bb88cc51c59f28`;
raw 900-row result SHA-256
`b4491f1443cff869353cfde0c798d6d50c8065f6714b927b77ec14ecef65749c`;
summary SHA-256 `c2f91be43ca607fd920477008179553377c10d4b2a2dd45577f49b5651966221`.
The compact implementation evidence receipt is
`research/evidence/t9_final_heldout_v1.json`. No raw audio or generated mixture
was committed. Production, frontend, and Axora remain untouched. **T9 VALID AND
COMPLETE — READY FOR OWNER REVIEW. STOP.**
