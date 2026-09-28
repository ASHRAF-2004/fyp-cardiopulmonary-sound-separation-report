# Final validation-only ensemble reconsideration

28 September 2026. **DECISION COMPLETE; T8 FREEZE PREPARED; FINAL TEST SEALED;
NOT DEPLOYED.** Application-Based FYP2 design/validation evidence only. Submitted
FYP1 and production remain unchanged.

## Chapters 4–6 — decision and bounded evidence

**Decision B: retain the selected small Conv-TasNet standalone**, with its
existing learned waveform output and target-free equal-residual consistency.
Use N64/B32/H64, 171,313 parameters, seed 20260928 best epoch 8. Checkpoint:
`89f8d66134c0a49aa2a05971720cdffbdd1e501ebce99bb83119e6683d58ac93`.
No ensemble weights, source-specific weighting, learned gate, confidence
routing, or extra mixture-phase postprocessing are selected.

One diagnostic pass compared the existing Fixed Filter and Generic NMF against
that selected checkpoint on the same frozen 225 validation conditions. Only
two family-pair groups exist; these correlated manikin remixes do not provide
225 independent observations. All methods used fixed heart/lung labels, the
same shared gain, 4-kHz samples, 10-second/8-second-hop inference and audited
SI-SDR. Results are equal-family macro means in dB:

| Method | Heart SI-SDR / SI-SDRi | Lung SI-SDR / SI-SDRi | Weaker-source Q |
| --- | ---: | ---: | ---: |
| Selected TCN waveform | 3.097 / 3.101 | 3.126 / 3.130 | 3.101 |
| TCN magnitude-mask projection (diagnostic) | 3.347 / 3.351 | 3.367 / 3.371 | 3.351 |
| Fixed Filter | −0.826 / −0.822 | −2.757 / −2.753 | −2.753 |
| Generic NMF | −3.429 / −3.425 | −3.615 / −3.611 | −3.611 |

There were zero execution/metric failures and no excluded conditions. The TCN
control replay matched saved T7 scores within 6.20e−14 dB. NMF reused its frozen
6-component/80-iteration/seed-42 per-input factorization; no new trained bases,
model parameters, neural training, or seeds were introduced.

| Family pair | TCN H / L SI-SDRi | Fixed Filter H / L | NMF H / L |
| --- | ---: | ---: | ---: |
| Late Diastolic Murmur × Fine Crackles | 3.702 / 3.664 | −2.397 / −3.913 | −5.551 / −4.728 |
| Tachycardia × Fine Crackles | 2.501 / 2.596 | 0.752 / −1.592 | −1.299 / −2.493 |

The filter wins 21/225 heart and 17/225 lung conditions; NMF wins 9/225 each.
All filter heart wins and every NMF win are in Tachycardia, concentrated in
`F_T_RC`. Among conditions where the TCN has negative improvement, the filter
outperforms it in 11/24 heart and 2/33 lung comparisons; NMF wins 8/24 and 0/33.
These counts do not imply the secondary output reaches positive improvement.
Secondary residuals are strongly positively correlated with TCN residuals
(median 0.764 filter, 0.729 NMF), and their median error energy is about
2.52×/2.61× larger. Correlation is descriptive;
it does not mathematically rule out every beneficial convex combination.

**ORACLE UPPER BOUND — NOT DEPLOYABLE:** choosing the higher reference score
per condition and per source yields Q 3.332 with the filter (+0.231 dB) or Q 3.174
with NMF (+0.073 dB). This is only a hard-routing upper bound, not a bound on all
waveform fusions. It uses ground truth and may violate paired additivity. Filter
oracle H/L gains are 0.000/0.019 dB in the first family and 0.463/0.505 dB in
Tachycardia. This narrow, concentrated opportunity gives insufficient support
for selecting another validation-driven fusion experiment or routing rule.

Projection onto complementary magnitude masks and mixture phase improves TCN
macro H/L SI-SDRi by 0.250/0.241 dB. It therefore did **not** discard an aggregate
advantage on these data. However, 53 heart and 62 lung conditions worsen, and
the result supplies no evidence of information from a second expert. This
permitted representation diagnostic is not automatically promoted into an
additional tuned final-system variant. Preserve the previously selected
waveform contract. No new projection experiment is proposed.

On ten predeclared validation conditions, both TCN representations have zero
cross-correlation peak delay for all sources, with no sign inversion. Secondary
heart peaks occasionally differ by 1–2 samples; there is no common fixed delay
to correct. No reference-guided shift or sign change was applied. Maximum
samplewise mixture reconstruction error is 1.19e−7 for TCN/projection/filter,
2.44e−5 for NMF because its epsilon masks are slightly noncomplementary.

Waveform convex fusion is technically feasible for aligned additive outputs;
TF-mask fusion is also feasible. Neither has a sufficiently credible secondary
expert here. Different heart/lung weights add selection freedom and break
additivity without correction; confidence routing lacks a validated
target-free quality feature. VMD retains its strict no-fallback qualification
gap. NeoSSNet and the larger TCN were excluded as final ensemble experts. No
new algorithm or weight sweep was run.

CPU method calls took 4.447 s for TCN, 0.821 s for filter, 3.311 s for NMF across 225
15-second records; the projection including TCN took 5.683 s. The full diagnostic
took 15.01 s, peak RSS 455.6 MiB. These are local observations excluding model-load
and deployment overhead. Standalone selection adds no second-expert cost.

## Limits and final-system freeze

This is insufficient evidence for a useful ensemble in this milestone, not
proof that all ensembles are inferior. The one predeclared confirmation seed
was not loaded or rescored for selection; its existing T7 robustness status
remains **UNCERTAIN**. No final-test data, labels, recipes, audio or metrics
were inspected for this decision. No neural training, optimizer updates,
production changes or broad tests occurred. One synthetic numerical/shape smoke
check and the control replay protected diagnostic correctness.

The original 50/50 NeoSSNet+NMF ensemble remains **implemented offline / research
comparison only / not qualified / not deployed**. Preserve its poor six-probe
development evidence separately; do not compare incompatible pipelines as
held-out results. Ensemble Learning remains part of the investigated research
component; the chosen application separator does not falsely advertise ensemble
inference. No final Chapter 6 quality, clinical or broad generalization claim is
supported by this record.

Next is metadata-only T8 freeze completion: confirm the selected checkpoint,
architecture, all preprocessing/window/consistency/label rules, exact metric
source, pinned environment and the declared mixture/Fixed Filter/NMF comparator
identities. There are no ensemble experts or weights to tune. The prepared
freeze record lists hashes without opening test sources. Only after complete
system freeze and explicit owner T9 approval should a test-only evaluator run
the held-out protocol once. A disappointing test result cannot restart tuning.
No final test or deployment is authorized by this document.

Exact protocol, per-level results, oracle limitations, hashes and T8 checklist:
[implementation decision](https://github.com/ASHRAF-2004/Machine-Learning-Based-System-for-Cardiopulmonary-Sound-Separation/blob/fyp2/application/docs/FINAL_ENSEMBLE_RECONSIDERATION.md).
Diagnostic clean source commit: `656a79e677bed198b119abbf008e21392d14ef92`.
Summary SHA-256: `eb3f20ea83b401b86cb7c74c623255f6802eab138de4e13044f46f63e9ff3039`.
Existing Luo and Mesgarani (2019) and Wisdom et al. (2019) references remain in
`provenance/ensemble-references.bib`; those speech studies motivate the
representation/consistency discussion, not target-domain performance claims.
