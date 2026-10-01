# Frost Studio — concise details and handle sharing, 1 October 2026

**IMPLEMENTED / TESTED LOCALLY — READY FOR OWNER REVIEW. NOT DEPLOYED.**
The owner requested key recording facts first, expandable full provenance and
sharing by @handle rather than an internal recipient identifier. This is a bounded
follow-up to the existing local identity foundation, not a redesign or auth change.

## Chapter 5 — implemented delta

Recording detail now presents six applicable facts, with all unchanged references,
hashes and provenance behind keyboard-operable **See more / See less**. Sharing
uses an exact handle lookup, actual display-name/handle confirmation and explicit
permission/resource scope. Three active permissions are shown initially; additional
permissions and revoked/expired history are disclosed on demand. No active grants
means an honest private-recording state, not a list of historical recipients.

The owner-only POST `/api/recordings/{id}/sharing-recipient` returns only current
display name, handle and public user reference. It has no directory, prefix search,
email or Firebase-UID disclosure. Safe audit events bound lookup per owner across
recordings/restarts. Existing grant creation confirms the handle and immutable
public reference in the same transaction, then reuses the original grant policy.
Existing verified status, ownership, role, read/review, exact-resource, revocation
and Admin privacy rules remain authoritative. Legacy recipient-ID clients remain
compatible; no schema change, migration, dependency or new processing pipeline.

Backend source: `5b819c57e95e16b637c5177d4344e8578cfaf5d8`.
Full source/evidence paths and final interface checkpoint are in
`implementation/docs/LOCAL_SHARING_REFINEMENT.md` and root `PAUSE_NOTES.md`.

## Chapter 6 — actual evidence

| Check | Result |
|---|---|
| Focused sharing + existing API/authorization regression | 99 passed + 26 subtests; exit 0 |
| Existing identity regression | 18 passed; exit 0 |
| Real local browser/API acceptance | 4 groups; exit 0 |
| Delayed actual-response transport check | 1 separately identified group; exit 0 |
| Read-only final disclosure/layout checks | 2 groups; exit 0 |
| Normal app and isolated-preview builds | Separate finite commands; both exit 0 |

Actual Heart-only grants permit protected Heart playback but deny Original, Lung,
result metadata and nonowner recipient lookup. Owner revocation persists, is
audited and blocks subsequent recipient requests. Four temporary grants per
browser run were revoked; audit/history remains. Confirmed references prevent
stale/reassigned handles from redirecting access. Owner/recipient identity choices
and stored recording/result receipts were not reset or rewritten.

Screens inspected at 1440×900, 390×844, 820×1000 and Frost/Midnight:
`implementation/frontend/output/playwright/handle-sharing/v5/` and
`final-layout-v2/`. Earlier failed harness/accessible-name checks are retained and
described in the implementation record; no policy was weakened to make tests pass.
Functional receipt SHA-256:
`0054d1b2a64255f042ed85f1108b87c7cbcfbb363c9eeb99164ac7a355d46e20`.
Final read-only check receipt SHA-256:
`60b346dd42f11f63732fcfd28e4a996e478b28f0114c6bf413047f06f60bb049`.

## Review and boundaries

The dedicated visible local review uses loopback frontend 4198/API 8198 and a
separate persistent `.local/handle-sharing-review/` SQLite/private-file namespace,
copied without modifying the existing 4196/4197 sessions. Both copies retain four
recordings, ten correctly hashed private artifacts and three jobs/results, with
no unfinished job or foreign-key error. The frozen CPU worker loads unchanged
verified weights; no new inference or training was run in this follow-up.

Only identity uses the existing fixed fictional verifier/SDK: **not live Firebase
verification or an emulator**. Media, grants, API, database and private files are
real. Listening uses eligible raw non-test HLS-CMDS manikin Mix/M0001.wav, not
procedural tones, patient recordings or T9. Owner @dragonfighter and fictional
recipient @review.owl27 are current local stored handles, not preview fallbacks.

Production/Axora, Firebase provider/account settings, ML weights/spec/inference,
consumed T9 and approved visual assets are unchanged. Handle login, avatar/data
services, notifications/global Insights and genuine owl flight remain pending;
flight is **ASSET-GATED — NOT IMPLEMENTED**. Owner acceptance of this follow-up is
pending. No clinical or physical-stethoscope validation is claimed. Stop for
owner review; no automatic next milestone or production deployment.
