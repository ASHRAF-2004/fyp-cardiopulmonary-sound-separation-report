# Final pre-T9 model representation/objective review — design record

29 September 2026. This file preserves the **pre-execution design**. The two
authorized treatments have since run and neither passed the frozen adoption
gate. See [the execution record](FINAL_PRE_T9_MODEL_EXECUTION.md). The result
is **HLS-only T8 V2 retained / T9 sealed / not deployed**.

Implementation planning/probe commit:
`c582159e80540a83197ba57071f1468b276f721b`.
Authoritative decision and exact Luna phases R0–R11:
`implementation/docs/FINAL_PRE_T9_MODEL_DECISION.md`.
Machine protocol `research/configs/final_pre_t9_model_plan_v1.json`, SHA-256
`6776e53c1d53c66d39c8882169b6de729bc05358f337e26a91257fd74dce8103`.

## Diagnosis and scope

The rejected external clinical-data and native-triplet treatments remain valid
negative-transfer evidence. They do not prove that useful independent data are
now sufficient: external purity/domain mismatch and native reuse/no new families
remain limitations. Representation efficiency is a plausible remaining
hypothesis, not an established primary cause. Prior numerical mixing, loss,
semantics, context and mixture-consistency audits are not reopened.

T4's two-example approximately12dB demonstrates capacity, not a directly
comparable generalization score. Current matched five-fold family-pair macro
control at576updates is H/L SI-SDRi **2.012519/1.913416dB**, Q1.913416 and
balanced mean1.962968; the old two-pair~3.1dB validation is not its control.
Repeated family reuse prevents IID condition/patient significance claims.

## Two predeclared treatments, not results

**A: compact complex-mask STFT U-Net**,390,450parameters. One256-sample periodic
Hann STFT at4kHz,64-sample hop,centered constant-zero padding,all129bins.
64mswindow/16mshop/15.625Hzgrid. Four mixture-derived inputs: log1p magnitude,
real/imaginary normalized phase components and absolute frequency coordinate.
Encoder8/16/32/64,bottleneck96,mirrored skip decoder; GroupNorm/SiLU,one dilated
bottleneck convolution. Complex masks Mh=.5+u+iv,Ml=1−Mh; no bounded magnitude
restriction. ISTFT and existing equal-residual consistency. Existing waveform
loss only. Nominal mask-path context6.640–6.896s; normalization adds full-window
dependence, not proof of learned physiological understanding.

The simpler real-mask representation was an analytical comparison only, not a
third trained treatment. Reference-assisted reconstruction on the two fixed
development examples yielded~8.1–9.2dB improvement. This is neither deployable
performance nor a strict SI-SDR upper bound. Complex masks avoid unnecessarily
forcing mixture phase; phase-estimation variance remains a risk.

**B: unchanged171,313-parameter Conv-TasNet + one spectral auxiliary loss.**
L = existing loss +6Lsp. For each source, rho=targetRMS+1e−6 and
A(z)=|STFT(z/rho)|/sqrt(96); Lsp is mean absolute log1p(Aestimate)−log1p(Atarget)
over batch,source,frequency,time. Same256/64 STFT; no PIT or predicted-RMS
normalization. Lambda6 follows a frozen initial-gradient calibration rule,
not validation scores. Weighted spectral gradients were19.7–20.2% of existing
loss norms, cosines0.850–0.949 on three fixed development batches. This supports
a modest compatible emphasis, not correction of demonstrated loss conflict.

Both retain exact synthetic HLS supervision only, source semantics, inference
windowing, target-free consistency and CPU environment. No native/external
training, extra seeds, model combination, UI or production work.

## Luna execution boundary

At most two treatment protocols, five folds each; seed20260928,batch4,exactly
576updates,AdamW.001,decay.0001,clip5,constantLR,endpoint evaluation only.
Reuse verified historical control recipes/evidence. A necessarily has different
initial weights and parameter count; B matches the control's fresh-state hash.
Thus A is a representation-package comparison, not a perfectly capacity-matched
causal ablation. No control rerun or duration search.

Before A CV, its fixed two-example capacity gate must pass EVERY case/source
SI-SDRi≥10dB and normalized-L1 reduction≥50%,within400updates/600seconds.
Fresh gate initialization; never reuse gate weights. A gateFAIL rejects A;
B stays eligible. No alternate mask/architecture/loss weight after results.

Adoption independently requires all: ΔQ/Δbalancedmean≥.5dB, both source gains
≥.25dB,6/8 pair means and4/5 foldQ improve, no pair/source regression>.5dB,
negative-condition-rate increase≤5pp,zero failures,source macro means≥1dB
and each pair/source≥0dB. This is an engineering gate, not a significance test.

If both pass: Q, then balanced mean, then pair/fold consistency; exact remaining
tie chooses B for smaller unchanged inference. If neither passes: retainv2 and
**end model development**. Only a valid winner may receive one fresh final
45heart/41lung non-test refit at576updates,seed20260928,constant.001 and sole
endpoint selection. Then preservev1/v2 and freezev3. Always STOP beforeT9.

## Evidence actually produced

All configured MCP/auth checks passed; no login/environment changes. Probes
performed **zero optimizer updates**, no validation replay and no T9 audio.
Four original-development files supported gradient/representation calculations;
synthetic inputs verified lengths, finite gradients, zero behavior and consistency.
Selected A count390,450 and B count171,313 verified; model states unchanged.
No capacity gate or full treatment has been trained. No model improvement claimed.

Forward/backward timing suggests roughly20–35CPUminutes for both protocols,
plus the bounded gate and a conditional final refit; full-run timing is unmeasured.
T8v2/checkpoint hashes remain unchanged. Production/frontend/demographics/FYP1
are untouched. The full one-shot T9 remains separately authorized and sealed.

Original method sources and APA metadata are recorded in the implementation
decision: Jansson et al.(2017),Erdogan et al.(2015),Yamamoto et al.(2019),and
official PyTorch2.11 STFT/ISTFT documentation. These motivate designs, not a
cardiopulmonary performance claim or a reproduced published system.
