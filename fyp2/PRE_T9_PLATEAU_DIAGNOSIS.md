# Pre-test generalization diagnosis and one planned intervention

28 September 2026. **DIAGNOSTIC RESULT / INTERVENTION DESIGNED, NOT EXECUTED /
T9 SEALED / NOT DEPLOYED.** The owner authorized one final challenge to training
assumptions before final evaluation. Existing T8 checkpoint/specification bytes
remain unchanged; final-test execution is on hold for review. No clinical or
final FYP performance conclusion is added. Submitted FYP1 and production are
unchanged.

## Diagnosis: data-limited, medium confidence

The selected171,313-parameter fixed-label Conv-TasNet retains validation H/L
SI-SDRi3.101/3.130dB. The earlier~12dB T4 result is a different model run fitting
two fixed development crops, not a measured9dB train–validation gap for the
selected checkpoint. Its online training SI-SDR at best epoch8 averaged3.910dB;
changing8s training batches and full15s validation are not directly matched.

The strongest supported explanation is limited learned source-pattern diversity
and pair-specific ambiguity, amplified by heavy remix reuse and narrow model-
selection coverage. It is not a proven allocation of every lost dB. Findings:

| Diagnostic | Evidence and interpretation |
| --- | --- |
| Independent information | Development36H/36L files,6H/4L families,18min total; non-test45H/41L,8H/5L families,21.5min. Manikin/source-family groups, not verified subjects. |
| Reuse | At best8:4,608draws,1,230/1,296file pairs,128appearances/source. Two random8s crops of15s overlap70.83% on average. More rows do not create physiology. |
| Similarity | Within-family PSD similarity exceeds between-family, but bounded±2s waveform correlations never reach0.8(max0.624). Correlated styles, not demonstrated duplicate audio or a calculable effective sample size. |
| Family distance | Development-standardized descriptors do not make Fine Crackles or Tachycardia broad outliers. Tachycardia envelope repetition proxy0.40s differs from development family medians0.84–0.88s. |
| Identifiability | Tachycardia×Fine Crackles normalized-PSD intersection0.462 vs0.327 for Late Diastolic Murmur×Fine Crackles. Supports harder overlap, not a proof of irreducible error. |
| Mixing | Crop-RMS multiplier10^(dB/20), common scaling and normalization are correct; maximum measured relative-level error4.90e−7dB. |
| Context | Exact interior convolutional support24,528samples/6.132s; global GroupNorm makes computational dependence full-window. Encoder8ms/hop4ms. No severe short-context defect shown. |
| Loss gradients | Three fixed development batches:5L1/SI gradient-norm ratios0.215–0.617, cosine0.593–0.804; H/L total-loss cosines0.345–0.818. No observed conflict justifies a loss change. |
| Consistency | Before trained equal-residual layer H/Li−7.079/−6.769; after3.101/3.130. Raw common mode is unsupervised; removing it is contraindicated. |
| Window distribution | Local RMS levels and tailpadding differ from training; regional replay does not show a universal tail failure. TailH/Li2.404/4.263 versus early3.243/2.606. No alternate inference rule tested. |
| Optimization | Continued loss improvement is79–82% SI-SDR-component improvement, but validation deteriorates. Both small-model optima precede LR reductions. More epochs alone are unsupported. |

Equal-residual consistency is part of training: `y_h=x/2+(z_h−z_l)/2`,
`y_l=x−y_h`. Adding the same waveform to both raw estimates cancels, so their
common mode is not separately supervised. Exactly additive references remain
feasible; this is not a mathematical recovery ceiling. It is distinct from the
previous, unselected magnitude-mask projection diagnostic.

At±10dB, the dominant source is hard to improve beyond its already~10dB mixture
baseline, while the weak source gains~5dB but has poor absolute separation.
Uniform training levels and discrete validation endpoints differ in emphasis;
there is no demonstrated10-versus20log error or justified new sampler. Recording
heterogeneity inside Fine Crackles is substantial. Both validation family pairs
share the same five lung recordings and are not independent groups. No IID-row
bootstrap, significance claim or clinical/patient generalization is warranted.

Seed20260929 remains confirmation only. Its higher aggregate redistributes
family/level performance rather than establishing robust superiority. No extra
seed, checkpoint averaging, projection or ensemble is selected.

## One planned intervention: family-qualified budget then non-test refit

Keep architecture, loss, mixture math/range, semantic outputs and inference
unchanged. Five fixed grouped folds each hold out one of the five non-test lung
families plus assigned heart families, covering all eight heart families once.
Use fresh seed20260928, AdamW LR0.001/decay1e−4/batch4/clip5 on pinnedCPU.
Each fold runs1,152updates, evaluating only576/864/1,152. No model sweep.

Aggregate eight held-out family-pair means equally, then Q=min(H,L), tie-break
balanced mean. Select the earliest budget with both Q and balanced mean within
0.10dB of the ranked best budget. This is a predeclared stability margin, not a
statistical confidence interval. Gate: both macro source SI-SDRi≥1dB, both
source means≥0 in every held-out family pair, zero failures. Do not relax the
gate or try a runner-up after results.

If PASS, train exactly once from scratch on all45H/41L non-test sources with
seed20260928, constantLR0.001 and the selected fixed update count. The endpoint
checkpoint is the sole candidate; no absorbed-validation early stopping or
checkpoint selection. If FAIL, retain T8 and stop for review. No alternative
intervention is preauthorized.

This CV qualifies broader family transfer and a budget; it cannot directly
demonstrate improvement over oldT8 because its held-out population differs and
many fold sources were original training data. The final refit has no new clean
validation score. Benefit is plausible, not promised. Expected later compute
~20–30minCV plus2–5minrefit on existingCPU; no GPU/environment changes.

All exact folds, recipes, hashes, update/LR/selection rules, failure gates and
P0–P7 tasks are in the implementation
[diagnosis](https://github.com/ASHRAF-2004/Machine-Learning-Based-System-for-Cardiopulmonary-Sound-Separation/blob/fyp2/application/docs/PRE_T9_PLATEAU_DIAGNOSIS.md),
[Luna handoff](https://github.com/ASHRAF-2004/Machine-Learning-Based-System-for-Cardiopulmonary-Sound-Separation/blob/fyp2/application/docs/PRE_T9_LUNA_HANDOFF.md)
and versioned JSON plan. Only analytical scripts/source statistics/current-model
replays and no-step gradients ran during this sprint. Model bytes and T8 spec
are unchanged. **No intervention training, CV, refit, T9 or production work.**

If later approved and qualified: refit →replacementT8 integrity freeze →STOP
for separate T9 approval. Ensemble decision and original final-test policy
remain unchanged. No test-driven retuning is allowed. Existing APA references
to Luo and Mesgarani's Conv-TasNet and Wisdom et al.'s consistency work remain;
new conclusions above are explicitly local diagnostic evidence/inference.
