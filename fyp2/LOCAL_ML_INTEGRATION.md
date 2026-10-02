# Local application integration of the frozen final separator

29 September 2026. **IMPLEMENTED LOCALLY / TESTED LOCALLY / FINAL ML EVALUATION
COMPLETE / PRODUCTION ML INTEGRATION NOT YET DEPLOYED.** Earlier “worker not
connected” statements are superseded for the local branch only. Production M1
and submitted FYP1 remain unchanged.

## Chapter 5 — implementation

The implemented flow is record/upload → metadata review → **Separate** → durable
job → one CPU worker → private heart/lung WAVs → persisted provenance → authorized
review. Existing owl/theme/typography/navigation are retained. There is no user
algorithm selector, demographic input, diagnostic interpretation or fabricated
per-record quality score. Browser AudioWorklet capture previews PCM16 WAV before
using the same authenticated upload path; physical stethoscope qualification
remains pending because acceptance used a fake microphone.

The model is unchanged HLS-only T8v2: Conv-TasNet N64/B32/H64,171313 parameters,
historical fresh seed20260928,576 updates on45 heart/41 lung non-test sources.
Checkpoint SHA-256:
`1f7e549ba53240bc085221e4eed1f935bb7c330e9a66cfab4c183c8f096c2658`;
specification SHA-256:
`2573ae06b11aafc595a4cdb179e3ab0c9f7fbe37859863dcd36a5d8c70210b1b`.
The worker verifies these and frozen source/environment identities, loads once
strictly and invokes unchanged4-kHz mono inference with10s windows,8s hop,2s
overlap and equal-residual consistency. No projection, permutation, ensemble,
training or new preprocessing is used.

Existing SQLite jobs/results/files/resources/grants are reused with additive
migration002. Owner request returns202; HTTP never waits for inference. A
recording/model uniqueness constraint, exclusive worker lock and transactional
claims prevent duplicate execution. One interrupted attempt may retry on restart;
a second interruption fails. Normal inference/storage errors fail visibly, not
through another algorithm. Both private4-kHz float32 WAVs are verified/fsynced
before one transaction publishes their result/provenance. Originals are preserved.

Firebase UID/current-account verification and application role/status/owner/grant
rules are unchanged. Admin has no blanket audio access. Result review grants do
not imply sibling audio: outputs need explicit read grants or deliberate whole-
recording access. Revocation blocks subsequent requests, not recall of downloads.
Provenance includes model/checkpoint/spec/code identities, input/output hashes,
canonicalization/inference contract, environment, worker version/attempt and times.

Application/clean acceptance commit:
`58be00a4a972b77680edfd93a758e8a36e391184`; image-context correction:
`2b6b3c0b461cff0bb8e865a11cf43f9db394d1e2`. Exact routes, tests, artifacts and
deployment review requirements:
[implementation evidence](https://github.com/ASHRAF-2004/Machine-Learning-Based-System-for-Cardiopulmonary-Sound-Separation/blob/fyp2/application/docs/LOCAL_ML_INTEGRATION.md).

## Chapter 6 — separate evaluation populations

| Evidence | Population / interpretation | Result |
| --- | --- | --- |
| Tiny capacity | Two fixed development mixtures; memorization, not transfer | Approximately+12dB SI-SDRi |
| Narrow validation | Two family pairs/225 correlated conditions | Approximately3.1dB; not the grouped control |
| Grouped non-test selection | Five folds/eight family pairs/1775 correlated conditions | Control Heart/Lung SI-SDRi2.013/1.913dB |
| Final T9 | Frozen all-non-test v2 endpoint,225 conditions/two family pairs | Heart/Lung SI-SDRi1.849/2.333dB; zero failures |
| Local application acceptance | Synthetic PCM/fake microphone, fictional identity, real API/worker/model | Workflow/security/durability only; no separation-quality score |

Unchanged [T9 evidence](T9_FINAL_HELDOUT_EVALUATION.md), family-pair macro dB:

| Method | Heart SI-SDR | Heart SI-SDRi | Lung SI-SDR | Lung SI-SDRi | Failures |
| --- | ---: | ---: | ---: | ---: | ---: |
| Original mixture |−0.037 |0.000 |−0.037 |0.000 |0 |
| Fixed Filter |0.325 |0.362 |−2.484 |−2.447 |0 |
| Generic NMF |−2.503 |−2.466 |−3.444 |−3.407 |0 |
| Final Conv-TasNet v2 |1.813 |1.849 |2.296 |2.333 |0 |

Under the frozen225-condition HLS-CMDS held-out protocol, the final Conv-TasNet
produced positive SI-SDR improvement for both sources and outperformed these
Fixed Filter and Generic NMF comparators. This does not imply clinical or
patient-level effectiveness, state of the art or general superiority. T9 is
consumed and was not reused for integration.

Five focused API/worker tests and five real-local browser groups passed. They
cover owner/outsider access, queue/claim/output/result persistence, explicit
analyst assignment/revocation, hashes/strict load, finite correct-length outputs,
API restart/new session, exclusive worker, bounded recovery, missing/corrupt
artifact and inference/partial-storage failures. One broader campaign resolved
137 cases+26 subtests passing;14 mock browser groups passed. Initial test-only
environment/harness failures and targeted corrections are preserved in the
implementation record. TypeScript/Vite build passed. Do not add overlapping
run counts as independent coverage or call fictional-provider tests live Firebase.

For one15-second generated example: startup1.061s, model-loader setup0.502s,
inference0.035s, whole job0.048s, startup+job CPU0.909s and peak process
RSS560.914MiB (includes test/API overhead). These are local engineering
observations, not a production SLA or model-performance estimate.

## Chapter 7 — conclusion and limitations

Research-to-application separation is implemented and tested locally, without
post-test model development. The history remains visible: external clinical
pretraining had negative transfer; native direct supervision substantially
regressed lung transfer; more epochs were unsupported; TreatmentB failed.
TreatmentA TF U-Net remains promising non-test research: Heart2.504, Lung2.399,
Q2.399, balanced2.452dB;8/8 pair means and5/5 foldQ improved. It missed the
predeclared+0.50dB gates by about0.0145dB Q/0.0114dB mean. No post-hoc relaxation
occurred. It is not selected/deployed/T9-evaluated; future research needs fresh
independent evaluation.

HLS-CMDS manikin acoustics, limited independent family diversity, synthetic
mixture reliance and modest absolute improvement limit interpretation. T9's
hardest pair was AV Block × Coarse Crackles (balanced0.947dB), compared with
S4 × Coarse Crackles (3.235dB). Heart−1.744dB SI-SDRi at−10dB and Lung−1.374dB
at+10dB illustrate extreme-level weaknesses. These descriptive observations
did not change the model. No patient-level clinical validation or stakeholder
UAT has been established.

Owner review must separately approve model provisioning/permissions, schema
migration/rollback, worker activation and live protected-output acceptance.
Existing data/private backup scope covers outputs; model-bundle encrypted
off-host retention and all-writer quiescence are release prerequisites. No
production database/provider/routing/backup, Axora or FYP1 change occurred.

**LOCAL ML INTEGRATION COMPLETE — READY FOR PRODUCTION DEPLOYMENT REVIEW.**
