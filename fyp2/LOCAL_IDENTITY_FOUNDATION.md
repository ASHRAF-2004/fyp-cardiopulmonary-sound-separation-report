# Frost Studio — LOCAL identity foundation, 1 October 2026

**IMPLEMENTED / TESTED LOCALLY — READY FOR OWNER REVIEW. NOT DEPLOYED.**
The owner approved the integrated core/feedback interface (“looks good. go to
next step”) and asked continuation to the next reviewable slice. This covers LOCAL
L0 metadata and profile/core connections, not the complete handoff or production.

## Chapter 5 — actual implementation

The existing M1 store/API gains additive migration003/version3: immutable public
USR/REC/JOB/RES/MED/GRT/ASN references, canonical safe generated handles, one
self-service rename count/timestamp. Internal keys and Firebase UID remain the
authority. References are allocated transactionally, not fabricated/truncated in
the frontend; existing result/assignment entities are reused. Case-insensitive
uniqueness and the one-change rule are backend enforced. Display name stays editable.
PATCH `/api/auth/me` rejects client UID/role/public-ID/count mutation. There is no
new login alias, handle directory/resolver or authorization policy.

Approved Frost profile/settings composition connects actual server data, an explicit
handle confirmation/used state and subtle permanent reference. Library REC search,
shell identity and detail references are real; internal deep links/private-source
checks remain. Appearance/audio and existing provider security actions are retained.
An older API gives an honest unavailable identity state. Legacy sharing still uses
the internal recipient ID, available under Account details. No avatar/export/delete/
notification simulation is presented as a service.

Backend source `ebedc053e16b21e39aad9d056d1874c2fae101e1`; final implementation
checkpoint in root PAUSE. Detailed execution:
`implementation/docs/LOCAL_IDENTITY_FOUNDATION.md`.

## Chapter 6 — evidence and boundary

New isolated persistent review:127.0.0.1:4197 → API8197,
`implementation/.local/identity-review/`. A read-only-source SQLite backup preserves
the original4196/8196 review DB/schema2; only the new copy becomes schema3.
Four recordings, ten files, three jobs/results and six result-file links remain;
all ten copied audio hashes match and foreign-key check passes. Existing frozen
worker/checkpoint/inference is reused; no new processing pipeline or model run.

Identity alone uses the existing fixed fictional verifier/Firebase SDK stand-in,
not live Firebase or an emulator. API, SQLite and private artifacts are real; no
recording/profile/media responses are mocked. The separate fictional test reviewer
uses one rename; the owner-review identity's change remains available. Review audio
is unchanged eligible raw non-test HLS-CMDS Mix/M0001, not procedural listening tones,
patient material or T9. Tiny HTTP fixtures test policy, not separation performance.

| Evidence | Actual result |
|---|---|
| Backend identity/API/AF/migration regression |109 passed +26 subtests, exit0 |
| Browser/client focused checks |6 groups:5 real UI/API +1 client validation, exit0 |
| Read-only layout/legacy-API follow-up |3 groups, exit0 |
| Normal app TypeScript/Vite build |Standalone exit0 |
| Isolated design-preview build |Separate finite exit0 |

Checks include stable/missing-only metadata, collision/rollback/concurrency, strict
profile mutation, unchanged owner/exact-grant/Admin privacy, persistent rename/name
across refresh/new session, REC search,3-source authorized playback,100/150/200 gain,
1440×900/390×844/1024px, Frost/Midnight, focus/reduced motion, legacy query-section
unsaved protection and API2 compatibility. Images were inspected visually.

Ignored evidence: `frontend/output/playwright/identity-foundation/v3/` and
`final-layout-v1/`; respective receipt SHA-256:
37c62f3c41d5804c56dcd0d041747f4c5392b69d90d835be65a5b496a1f7a2f4 /
7f9b1732f433b43a25e66f1473e83bfb3037fe9000e12baca15db74853be66a7.
Earlier harness422 and missing client409 copy are recorded in the implementation
evidence. Six SDK-test environment failures were resolved by using the already
installed app/verifier environment, without reinstalling/upgrading dependencies.

## Limits and next gate

This is local technical evidence, not production identity migration, real-provider
qualification, clinical validation or final owner usability acceptance. Core UI
approval is complete; owner review of the new identity/profile flow is pending.
Frozen ML and T9 results remain unchanged. No training, T9 reuse, production/Axora
change or data deletion. Physical-stethoscope qualification remains separate.
Pending: avatar backend, handle sharing/login, export/delete/unlink, notifications,
global Insights and genuine owl flight (**ASSET-GATED — NOT IMPLEMENTED**).
STOP for owner hands-on review; no automatic next milestone or deployment.
