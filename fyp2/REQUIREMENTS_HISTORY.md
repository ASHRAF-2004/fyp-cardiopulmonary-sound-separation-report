# Requirements history and continuation identifiers

M1 version, 26 September 2026. The submitted revised report remains the source of F1-F15, NF1-NF8, UR1-UR8 and UC01-UC10. The initial FYP2 register's R01-R18 remain stable summary IDs. The continuation pack adds the granular IDs below; they refine those summaries rather than replacing or renumbering historical requirements.

The [change map](../FYP1_TO_FYP2_CHANGE_MAP.md) records exact submitted sections. Status and evidence belong in [traceability](TRACEABILITY.md) and [M1 notes](M1_IMPLEMENTATION_AND_TEST_NOTES.md); this history table describes requirement disposition, not completed implementation.

| Continuation IDs | Requirement intent | FYP1 continuity and initial FYP2 summary |
| --- | --- | --- |
| R-AUTH-01 | Email/password registration | New identity capability; R01 |
| R-AUTH-02 | Email/password sign-in | New identity capability; R01 |
| R-AUTH-03 | Google sign-in | New identity capability; R01 |
| R-AUTH-04 | Sign-out | New identity capability; R01 |
| R-AUTH-05 | Password-reset request | New identity capability; R01 |
| R-AUTH-06 | Backend verifies Firebase ID tokens | Extends NF5; R01-R02 |
| R-AUTH-07 | No public privileged-role selection | Extends staff/analyst actor policy; R01, R13 |
| R-OWN-01 | Exactly one application-account owner per persistent recording | Extends F1-F5, NF5; R02-R04 |
| R-OWN-02 | Owned records/history after later sign-in | Extends F14, UR8, NF7; R03, R06 |
| R-OWN-03 | Direct result/media/download object authorization | Extends F12-F13, UC07-08, NF5; R02, R11 |
| R-OWN-04 | Cross-account guessed-ID denial | Extends NF5; R02, R06, R11 |
| R-OWN-05 | Paths are not authorization | Extends NF5/storage design; R02-R03, R11 |
| R-ROLE-01 | Default public role healthcare_staff | Existing staff actor, new trusted assignment; R01, R13 |
| R-ROLE-02 | Admin-assigned audio_analyst | Existing analyst actor, new trusted assignment; R12-R13 |
| R-ROLE-03 | Trusted backend/admin privilege assignment | New administrator role; R13 |
| R-ROLE-04 | Last-active-admin guard | New administrator invariant; R13 |
| R-ROLE-05 | Admin metadata privilege is not private-audio privilege | Extends NF5; R02, R13 |
| R-SHARE-01 | Owner explicitly shares/assigns allowed records | Extends analyst workflow; R12 |
| R-SHARE-02 | Analyst sees active grants/assignments only | Extends actor access limits/NF5; R06, R12 |
| R-SHARE-03 | Revocation removes future access | New grant lifecycle; R12; distinguish one grant from all overlapping grants |
| R-SHARE-04 | Actor/record/result/time-linked review notes and status | New review provenance; R12 |
| R-REC-01 | Supported WAV upload | Retains F2, UR2, UC02, NF6; R04 |
| R-REC-02 | Header/sample validation and safe rejection | Retains/extends F3, UR2, UC02; R04 |
| R-REC-03 | Compatible connected-device capture when verified | New capture path; R05; no physical-device success inferred |
| R-REC-04 | Relevant recording metadata | Retains F1, UR1, UC01; R04 |
| R-REC-05 | Authorized recording saved to account history | Extends F4/F14; R03, R06 |
| R-PROC-01 | One normal-user separation request | Supersedes ordinary model choice in F7/UR4/UC04; R07; preserves internal comparisons |
| R-PROC-02 | Non-blocking UI | Retains/extends F8/F11, NF2-NF3; R10 |
| R-PROC-03 | Persist job/error/provenance state | Extends F11/F14; R03, R10 |
| R-PROC-04 | Exact run/ensemble version linked to outputs | Extends F9-F10/F14; R07, R11 |
| R-PROC-05 | No invented percent progress | Refines F11; R10 |
| R-ENS-01 | Versioned expert registry | Evolves modular strategy design; R07-R08 |
| R-ENS-02 | Participating expert versions recorded | New ensemble provenance; R07-R09 |
| R-ENS-03 | Fusion weights/method/version persisted | New ensemble provenance; R09 |
| R-ENS-04 | Individual methods remain benchmarkable | Retains baseline comparison intent; R08, R14 |
| R-ENS-05 | Quality claims require controlled evaluation | Retains/strengthens F15; R14 |
| R-ENS-06 | Explicit reproducible expert-failure policy | Extends reliability; R09-R10 |
| R-RES-01 | Authorized original/heart/lung review | Retains/extends F9-F12/UR7; R11 |
| R-RES-02 | Waveform/spectrogram when available | Extends output review; R11 |
| R-RES-03 | Authorized output download | Retains/extends F13/UC08; R11 |
| R-RES-04 | Reference-based metrics only with valid references | Retains/strengthens F15/UC10; R14 |
| R-RES-05 | Distinguishable historical runs | Retains/extends F14/UC09; R03, R10 |
| R-ADM-01 | Search/filter account metadata | New admin capability; R13 |
| R-ADM-02 | Protected approved role/status changes | New admin capability; R13 |
| R-ADM-03 | Safe audit events | Extends NF5/traceability; R13 |
| R-ADM-04 | Protected versioned ensemble configuration | New admin/research boundary; R07, R13 |
| R-ADM-05 | Backend privilege enforcement | Extends NF5; R02, R13 |
| R-DEP-01 | Confirmed stethofuse.ashraf-alsaloul.com hostname | Resolved target decision; R17; not a live deployment claim |
| R-DEP-02 | Public HTTPS | Extends deployment/NF5; R17 |
| R-DEP-03 | Controlled frontend/API production origins | Extends deployment/NF5; R17 |
| R-DEP-04 | No committed secrets | Extends NF5/reproducibility; R13, R17-R18 |
| R-DEP-05 | Document/test backup, restore and retention | Extends NF7/maintenance; R03, R17 |

R15 accessibility/usability, R16 approved-owl preservation and R18 academic integrity remain cross-cutting summaries in addition to these 52 continuation IDs. No new survey questions, respondents, literature counts, experiments or university approvals are created by this mapping.

## Decision chronology

- **Submitted FYP1:** two actors already exist; individual-strategy selection and local storage are described. The questionnaire has 53 genuine responses with target-user limitations.
- **Initial FYP2 preparation:** added R01-R18 summary register and separated persistent multi-user/ensemble plans from a simulated frontend and standalone policy harness. Historical hash manifest fixed at 217 original files.
- **M1 continuation:** adopted the 52 granular IDs, seven-state evidence vocabulary, confirmed seven-chapter application-based structure and final hostname. The supplied academic title is confirmed unchanged. Intended primary-admin account is identified in the continuation pack, but no UID or privilege follows from the email string. Current development may change code status only when evidence is linked.
- **Future deployment/feedback:** still `planned`; requirements resulting from later genuine feedback receive a dated revision and provenance. Do not relabel FYP1 elicitation.
