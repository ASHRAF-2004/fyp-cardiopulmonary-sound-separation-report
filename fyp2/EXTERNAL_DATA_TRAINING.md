# External-data training programme

**DATASET QUALIFIED · EXTERNAL PILOT COMPLETED / ADOPTION GATE FAILED · HLS-ONLY FINAL REFIT COMPLETE · REPLACEMENT T8 FROZEN · T9 SEALED · NOT DEPLOYED**

This FYP2 record preserves the predeclared protocol and reports its completed
non-test pilot below. External pretraining did **not** improve HLS held-out-family
transfer enough to pass adoption. Strategy C, the qualified HLS-only fallback,
is selected; its fixed-budget all-non-test refit completed as recorded below.
Submitted FYP1 and the original T8 artifacts remain unchanged. Replacement T8
metadata are frozen in version 2. No held-out T9 result exists.

## Rationale and selected data

The pre-test diagnosis supported insufficient independent source diversity as
the leading explanation for the approximately +3 dB validation SI-SDRi plateau.
Repeated HLS remixes are not new patients or sound families. External data must
therefore add traceable populations, not merely more correlated files.

The official-source audit considered paired/simultaneous recordings before
heart- and lung-labelled corpora. No acquired external dataset qualified as
Tier A isolated heart/lung references. The bounded pilot selects:

| Source | Official release | Population/technical evidence | Pilot role |
|---|---|---|---|
| Heart | [CirCor DigiScope 1.0.3](https://physionet.org/content/circor-heart-sound/1.0.3/) | Public metadata contain 942 participant rows and 3,163 WAVs; Additional-ID links require merging before independent-subject counting. Native 4 kHz, Littmann 3200, Northeast Brazil; age category, sex, murmur status, recording site and cardiac-cycle annotations. | Tier B, heart-dominated clinical targets; only contiguous accepted annotation intervals of at least eight seconds. |
| Lung | [SPRSound](https://github.com/SJTU-YONGFU-RESEARCH-GRP/SPRSound), pinned commit `bca1e51422a42a042441010081519610ef3845d0`; BioCAS2022 training release for this pilot | Original paper: 292 participants, 2,683 recordings, approximately 8.2 hours; 8 kHz/16-bit, Yunting II, Shanghai Children's Medical Center. Released subject, age, sex, site and respiratory/event labels. | Tier B, lung-dominated clinical targets; exclude official Poor Quality recordings. |

The CirCor release uses ODC-By 1.0 and SPRSound uses CC BY 4.0; attribution and
source/version lineage remain attached to registry records. Article licences
are not substituted for dataset terms. HF_Lung_V1 remains secondary rather than
silently accepted: patient/session grouping and source purity need qualification.
ICBHI access/terms and other candidate limitations are retained in the
[implementation dataset audit](https://github.com/ASHRAF-2004/Machine-Learning-Based-System-for-Cardiopulmonary-Sound-Separation/blob/fyp2/application/docs/EXTERNAL_DATASET_AUDIT.md).
HLS mirrors and duplicated challenge-task exports are not independent data.

**Neither heart-labelled nor lung-labelled means physiologically pure.**
Clinical background, breathing/cardiac leakage, handling artifacts and device
transfer functions can remain. Annotation and technical screening plus bounded
spectrogram review support imperfect-source pretraining, not clean-reference
certification or clinician listening approval. Three deterministically selected
candidates and one excluded control per source were inspected in the initial
representative review. The HLS held-out-family transfer gate—not external
reconstruction quality—was the predeclared criterion for whether these imperfect
targets help. Its observed rejection is reported below.

## Frozen qualification evidence

The initial representative acquisition contained 40 groups per source, with at
most two recordings each. The pilot expanded once to 160 metadata-selected
groups per source, again at most two recordings; it did not replace difficult
cases after signal inspection. The actual candidate acquisition contained
613 recordings: 304 heart and 309 lung. After all filters, 398 records were
eligible and 215 had explicit exclusions.

| Frozen partition | Heart records / linked subject groups | Lung records / subjects | Eligible source-interval seconds |
|---|---:|---:|---:|
| Training | 115 / 74 | 240 / 133 | Heart 2,031.835; lung 2,666.496 |
| External validation | 12 / 8 | 31 / 16 | Heart 216.130; lung 365.568 |

These are recording and subject-group denominators, not synthetic-mixture
sample counts. Training coverage exceeds the predeclared minimum of 64 subjects
per source **after** technical/annotation exclusions, deduplication, shared-age
filtering and subject holdout.

Originals remain immutable and checksum-pinned. Derived arrays use mono float32
at 4 kHz, deterministic anti-aliased resampling where necessary, recorded
resampler settings and independent derived hashes. Qualification checks include
corruption, finite samples, silence, clipping, identity, duration and valid
contiguous crop intervals. An inconsistent SPRSound WAV block-align field is
corrected only in memory for the exact verified header pattern; originals are
not rewritten. One invalid CirCor annotation is excluded, not relabelled.

Exact original/canonical hashes found no duplicate cluster in this bounded
pilot. A predeclared spectral-fingerprint shortlist led to 5,429 normalized
waveform near-copy comparisons, with no flagged pair. This limited screen is
**not proof of global uniqueness**. Known duplication elsewhere in SPRSound
remains relevant if acquisition later scales up. Cross-subject duplicate
clusters would be excluded before partitioning.

CirCor Additional-ID components and SPRSound patient IDs are the grouping units.
External holdout uses the fixed hash of
`external-v1:<dataset_group>:<merged_subject_id>` modulo 10; zero is held out.
No person-group crosses train/external-validation partitions. All exclusions
remain auditable rather than disappearing from the denominator.

## Demographic and acquisition limitations

Shared training age domains are Infant, Child and Adolescent. SPRSound ages map
to Infant ≤1 year, Child >1 and <12, and Adolescent ≥12 and ≤18; unknown or
unshared domains are excluded from these age-compatible mixtures. CirCor's
released categories are preserved, not converted into fabricated exact ages.
The acquisition sample was not redrawn following correction of the age-12
pairing boundary. Original acquisition strata remain recorded.

Training contains heart age counts 10/58/47 and lung counts 26/196/18 across
Infant/Child/Adolescent respectively. Sampling balances domains and subjects;
the file counts must not imply equal independent demographic coverage. Sex,
pathology, site and device metadata are descriptive factors, not model inputs.
Murmur status is not equivalent to a disease diagnosis. A heart-only Littmann
domain versus a lung-only Yunting domain creates a source/device shortcut risk;
age effects cannot be disentangled confidently from device, site and pathology.

**UX DECISION A: NO DEMOGRAPHIC INPUT REQUIRED.** Train one robust separator.
No age/sex selector, demographic routing or automatic demographic classifier is
implemented or justified by this qualification evidence.

## Predeclared experiment (preserved historical protocol)

The pilot selected **strategy A: external pretraining → HLS target-domain fine-tuning**.
Strategy C, HLS-only training, is the matched control and fallback. Joint
multi-dataset training is not selected: it adds an external/HLS weighting choice
and may let the larger clinical population dominate the manikin target.

The existing small Conv-TasNet stays fixed at 171,313 parameters. Keep 4 kHz,
eight-second training crops, fixed heart/lung outputs, target-free equal-residual
mixture consistency and the objective `−mean SI-SDR + 5 × normalized L1`.
No projection, ensemble, architecture, augmentation or loss search is introduced.

1. **HLS control:** five non-test family folds, 1,152 updates each, snapshots at
   576/864/1,152. The already-frozen earliest-within-0.10-dB rule selects one
   common update budget before treatment. Eight family-pair means receive equal
   weight; neither 1,775 correlated conditions nor five unequal folds are IID.
2. **External pilot:** fresh seed 20260928, exactly 2,304 updates, batch four,
   AdamW LR 0.001/weight decay 0.0001, gradient clipping five, constant LR and
   endpoint checkpoint only. Hierarchical sampling chooses shared age domain,
   then dataset, released label, subject, recording and valid crop. Crop-RMS
   lung/heart gain remains uniform −10 to +10 dB with shared final scaling.
3. **External sanity:** 32 frozen subject-heldout conditions, recipe seed
   20260929, endpoint evaluation only—not another model seed or checkpoint
   selection surface. The 9,216 training draws and 32 sanity recipes passed a
   no-model/no-optimizer materialization check; maximum additivity discrepancy
   was approximately 1.19×10⁻⁷. Nine focused checks passed.
4. **Matched HLS treatment:** each fold starts from the same external endpoint,
   with fresh optimizer state and identical fold recipes/settings. Run exactly
   the control-selected budget. No held-out HLS family receives optimizer
   exposure; no treatment-specific duration/checkpoint selection is allowed.

### Adoption gate, frozen before treatment results

All conditions must hold against the matched HLS-only control:

- Family-pair macro weaker-source score Q and balanced mean each improve
  **≥0.50 dB**; macro heart and lung SI-SDRi each improve **≥0.25 dB**.
- Balanced mean improves in at least **6/8 family pairs**, and Q improves in
  at least **4/5 folds**; no family/source mean regresses by more than 0.50 dB.
- Zero new numerical failures; neither source's pooled negative-SI-SDRi rate
  rises by more than five percentage points.
- Absolute utility also passes: each source's macro SI-SDRi ≥1 dB, every
  family/source mean ≥0 dB and zero numerical failures.

These are conservative engineering guards, **not statistical significance**.
The 0.50-dB margin exceeds twice the previous observed 0.226-dB seed-Q gap,
but two seeds do not estimate seed variance reliably. Correlated held-out
families/conditions remain a limitation. Historical T8's approximately 3.1 dB
is context only: it trained on some new CV holdout families and is not a valid
matched control on those folds.

If the pilot fails, end external training and apply the frozen HLS-only
fallback gate. If it passes, qualify the full selected original pools, run one
fresh 9,216-update external pretraining and repeat the same HLS gate. There are
no capacity/tuning variants in this concrete protocol. Only a full-strategy
pass permits the final fixed-budget fine-tune on all 45 heart/41 lung HLS
non-test sources, seed 20260928, endpoint checkpoint only. No absorbed validation
data or T9 result may select that final checkpoint. CPU caps are 30 minutes
for the pilot, 120 minutes for full pretraining and 8 GiB peak RSS.

## Observed pilot result and decision

**SELECTED STRATEGY C: HLS-only grouped-family qualification and conditional
all-non-test refit. External strategy A is rejected under the unchanged gate.**
The statements above are the protocol frozen before treatment, not retrospective
criteria. No full external acquisition/pretraining, capacity comparison or other
tuning variant follows this failed pilot.

### Completed external pretraining

Run `pilot-pretrain-seed20260928` started fresh from clean implementation commit
`328b38c79e4261c0226067cb54403ace2442cedc`, seed 20260928, with the 171,313-parameter
model and no loaded checkpoint. It completed exactly **2,304 optimizer updates**
on CPU in **295.962 seconds**, with **1,022.844 MiB peak RSS** and zero numerical
failures. Environment: Python 3.14.4, PyTorch 2.11.0+cpu, torchaudio 2.11.0+cpu.
The endpoint SHA-256 is
`546e7ec4cbd0f246250f3c9d224eaafbd48034a32790b3c1694dd3f183467bce`.

The 32 external-heldout sanity conditions returned descriptive mean SI-SDRi
**8.771 dB heart / 9.636 dB lung**, with zero failures. These are reconstruction
scores against **imperfect Tier-B clinical-recording targets**, using eight-second
external sanity inference. They are not clean-source truth, HLS performance,
clinical effectiveness, or 32 independent subject observations. No checkpoint
was selected with this sanity result. Its high score did not override the target-
domain gate.

### Matched HLS held-out-family comparison

Both arms use five folds/eight family pairs and the same 1,775 correlated
conditions. Aggregate each family pair equally. Q is the weaker of the two
macro source SI-SDRi values; M is their balanced mean.

| Arm, at 576 HLS updates | Heart SI-SDR | Heart SI-SDRi | Lung SI-SDR | Lung SI-SDRi | Q | M |
|---|---:|---:|---:|---:|---:|---:|
| HLS-only control | 2.021 | 2.013 | 1.922 | 1.913 | 1.913 | 1.963 |
| External-pretrained treatment | 1.869 | 1.860 | 1.594 | 1.586 | 1.586 | 1.723 |
| Treatment minus control | −0.152 | −0.152 | −0.328 | −0.328 | −0.328 | −0.240 |

The control's ranked-best endpoint was 1,152 updates (Q 1.933, M 1.993), but
**576 updates** met the predeclared earliest-within-0.10-dB rule (Q 1.913416,
M 1.962968) and passed absolute utility. This budget was recorded before
treatment. The 864-update control scored Q 1.825 and M 1.942. Treatment folds
all used the selected 576-update endpoint; no later treatment checkpoint was
searched to rescue transfer.

| Held-out family pair | Δ heart SI-SDRi | Δ lung SI-SDRi | Δ M |
|---|---:|---:|---:|
| Atrial Fibrillation × Wheezing | −1.132 | +0.000 | −0.566 |
| Early Systolic Murmur × Rhonchi | +0.026 | +0.109 | +0.068 |
| Late Diastolic Murmur × Fine Crackles | −0.029 | −1.702 | −0.866 |
| Late Systolic Murmur × Wheezing | −0.601 | +0.448 | −0.076 |
| Mid Systolic Murmur × Normal | +0.274 | −0.085 | +0.095 |
| Normal × Pleural Rub | −0.395 | −0.006 | −0.200 |
| S3 × Fine Crackles | +0.621 | −1.451 | −0.415 |
| Tachycardia × Rhonchi | +0.015 | +0.064 | +0.039 |

Only **3/8 family-pair balanced means** improved, against the required six;
only **1/5 fold Q scores** improved, against the required four. Neither source
met the ≥0.25-dB macro improvement gate, and Q/M changes were negative rather
than ≥0.50 dB. Several source-family regressions exceeded 0.50 dB. Treatment
Late Systolic Murmur × Wheezing heart SI-SDRi was **−0.124370 dB**, also failing
the absolute requirement that every family/source mean be nonnegative.

Both arms had **zero numerical failures**. Pooled negative-condition SI-SDRi
rates were heart/lung **24.789% / 28.732%** for control versus
**26.986% / 31.211%** for treatment. These descriptive condition rates passed
the ≤5-percentage-point increase guard, but do not compensate for the other
failed criteria and do not treat correlated conditions as independent people.

The measured result supports **negative transfer under this specific bounded
strategy**. Clinical-to-manikin mismatch, device/source confounding and imperfect
target purity remain plausible explanations; this experiment does not isolate
their individual causal effects. It does not establish that every external
dataset or future pretraining design must fail. It does establish that scaling
this branch is not justified by the predeclared target-domain evidence.

### Completed HLS-only endpoint refit

The fallback control passes its absolute qualification gate. Therefore the
authorized fallback was executed as one **freshly initialized**, seed-20260928
HLS-only run on **45 non-test heart and 41 non-test lung sources**, stopping
after exactly **576 optimizer updates**. AdamW LR 0.001 remained constant, with
batch four, weight decay 0.0001, clipping five and the unchanged small-model
loss/inference contract. The endpoint—not a training-loss minimum—is the
candidate. **No external pretrained weights or optimizer state entered this
refit.** No absorbed HLS validation or T9 scoring chose its checkpoint.

Run `refit-all-nontest-seed20260928` began from clean commit
`7eefa37100bb40d878d48b84b3811557ce98512b`, completed in **75.179 seconds**, used
**1,012.695 MiB peak RSS** and recorded **zero numerical failures**. The manifest
records identical fresh-seeded/initialized state hashes, null initialization-
checkpoint fields and an empty initial optimizer state, supporting scratch
initialization rather than external-weight reuse. Endpoint SHA-256:
`1f7e549ba53240bc085221e4eed1f935bb7c330e9a66cfab4c183c8f096c2658`.

This endpoint has **not received a held-out performance evaluation**. Its
generalization is not assigned the CV scores of the separate fold models, and
it is not claimed better than the original approximately +3.1-dB candidate.
The predeclared grouped-family evidence justified the training strategy and
budget, not a fabricated endpoint result.

The replacement specification is `research/configs/final_separator_v2.json`,
for the HLS-only fixed endpoint. Its SHA-256 is
`2573ae06b11aafc595a4cdb179e3ab0c9f7fbe37859863dcd36a5d8c70210b1b`.
Strict checkpoint loading and synthetic-only inference passed: 171,313 parameters,
finite `[2,60001]` output, exact length, zero-input zeros and maximum mixture-sum
error 5.96×10⁻⁸. Configured heart/lung order was checked, not claimed as semantic
accuracy from synthetic data. No audio file was opened by this smoke.
Version 1 remains byte-for-byte preserved
with its original checkpoint and provenance. Supersession is recorded through
version 2 **before T9**, not by overwriting version 1 or retrospectively changing
its evidence. T9 remains unopened.

Evidence records are
[`external_hls_control_decision_v1.json`](https://github.com/ASHRAF-2004/Machine-Learning-Based-System-for-Cardiopulmonary-Sound-Separation/blob/fyp2/application/research/evidence/external_hls_control_decision_v1.json)
and
[`external_pilot_transfer_decision_v1.json`](https://github.com/ASHRAF-2004/Machine-Learning-Based-System-for-Cardiopulmonary-Sound-Separation/blob/fyp2/application/research/evidence/external_pilot_transfer_decision_v1.json).
The external run's detailed manifest remains in ignored local artifacts at
`.local/training/stethofuse-external-v1/pilot-pretrain-seed20260928/run_manifest.json`.

## Reproducibility anchors and stop boundary

| Artifact | SHA-256 / Git identity |
|---|---|
| Clean implementation milestone | `328b38c79e4261c0226067cb54403ace2442cedc` |
| Clean HLS final-refit start | `7eefa37100bb40d878d48b84b3811557ce98512b` |
| HLS-only final endpoint checkpoint | `1f7e549ba53240bc085221e4eed1f935bb7c330e9a66cfab4c183c8f096c2658` |
| `research/configs/final_separator_v2.json` | `2573ae06b11aafc595a4cdb179e3ab0c9f7fbe37859863dcd36a5d8c70210b1b` |
| `research/configs/external_pretraining_pilot_v1.json` | `dedc8fd654aa9a976b255ae0c8095e6d7a13ce6b1c9a7743f6e5a3585e95489e` |
| Ignored accepted pilot registry | `09b2aefca4c957ea0346039f7ca8d4d5c553f49bf109f6b0da02a390e733328d` |
| `research/manifests/external_pilot_registry_v1.json` | `c922d58bf1cf2b0daae0acdfc110199c55f70c5b1cf5120c2eb0dc04372ffae6` |
| Freeze summary | `a04e83b7c95079e1fa5db615e55808b2214faf0b91d64ae3464e0dedad453058` |

The implementation configuration and run manifests are normative. Checkpoints,
audio, caches and detailed runtime artifacts remain ignored; Git stores metadata,
code and evidence only. Any replacement T8 requires a valid non-test adoption
decision and complete checkpoint/specification hashes. Preserve original T8
provenance. **T9 remains completely sealed; stop before it.** No production,
application integration, frontend or clinical-effectiveness claim is part of
this programme. **READY FOR T9 WITH ORIGINAL/HLS-ONLY T8 — selected HLS-only
version 2.** Separate owner authorization remains required before execution.
The original 225-condition T9 policy, comparators, metrics, inference and bug/
rerun rules are unchanged; no actual test recipes or results were generated.

## References

Oliveira, J., Renna, F., Costa, P. D., Nogueira, M., Oliveira, C., Ferreira, C., Jorge, A., Mattos, S., Hatem, T., Tavares, T., Elola, A., Rad, A. B., Sameni, R., Clifford, G. D., & Coimbra, M. T. (2022). The CirCor DigiScope dataset: From murmur detection to murmur classification. *IEEE Journal of Biomedical and Health Informatics, 26*(6), 2524–2535. https://doi.org/10.1109/JBHI.2021.3137048

Oliveira, J., Renna, F., Costa, P., Nogueira, M., Oliveira, A. C., Elola, A., Ferreira, C., Jorge, A., Bahrami Rad, A., Reyna, M., Sameni, R., Clifford, G., & Coimbra, M. (2022). *The CirCor DigiScope phonocardiogram dataset* (Version 1.0.3) [Data set]. PhysioNet. https://doi.org/10.13026/tshs-mw03

Zhang, Q., Zhang, J., Yuan, J., Huang, H., Zhang, Y., Zhang, B., Lv, G., Lin, S., Wang, N., Liu, X., Tang, M., Wang, Y., Ma, H., Liu, L., Yuan, S., Zhou, H., Zhao, J., Li, Y., Yin, Y., … Lian, Y. (2022). SPRSound: Open-source SJTU paediatric respiratory sound database. *IEEE Transactions on Biomedical Circuits and Systems, 16*(5), 867–881. https://doi.org/10.1109/TBCAS.2022.3204910

SJTU-YONGFU-RESEARCH-GRP. (2026). *SPRSound* [Data set and repository; commit bca1e51422a42a042441010081519610ef3845d0]. GitHub. https://github.com/SJTU-YONGFU-RESEARCH-GRP/SPRSound/tree/bca1e51422a42a042441010081519610ef3845d0
