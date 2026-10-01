# Frost Studio — LOCAL owner feedback and Analyst role purpose

Interface/adapter/dev-review/evidence source checkpoint:
7cfe92e764f82948157d79d617df1f4c42155b88 (fyp2/application, existing PR9).

2 October 2026. **IMPLEMENTED / TESTED LOCALLY — NEW OWNER REVIEW PENDING.
NOT DEPLOYED.** The owner approved the earlier Shared & assigned / saved notes
(“ok working and good”) and requested continuation and an assessment of role
differences. Approved Frost design and frozen ML/production evidence are preserved.

## Chapter 5 — actual bounded implementation

Recording owners can now read saved technical feedback/current assignments through
GET `/api/recordings/{id}/reviews`, protected by existing active/verified actor and
recording-owner checks before SELECT. Parameterized SQLite, one read snapshot,
default3/maximum20 rows and actual total. No schema/migration, new role, broad grant
or second ML pipeline. Backend commit d9d9200ddffc552525ad637feb978469b1f9ba53.

The approved recording detail shows Analyst feedback, actual reviewer name/@handle,
exact source, outcome, time and assignment state. Three rows / See more / See less;
long notes / Read more notes / Read less. Request review opens the existing exact
@handle sharing flow, not a new granting policy. Save review explicitly publishes
observations to the owner; unsaved drafts are not shared. Revocation ends future
reviewer access, but does not erase saved owner feedback/audit. Latest saved
version per assignment, not a complete version-history service.

Analyst Overview prioritizes current pending-first assigned work and Open assigned
reviews; own New recording remains secondary. Staff remains recording-first.
AssignmentRows is reused with the queue. Activity counts cover current active
assignments, not all historical work. Both roles share frozen separation/player/
technical-analysis capabilities: role is not a clinical credential, extra model
or automatic private access. Result-only assignment still denies sibling audio.

## Chapter 6 — real local evidence, not production/clinical qualification

| Check | Actual result |
|---|---|
| New owner-reader tests + current review/API/sharing | 78 passed, exit0 |
| API-client unit checks with mock token-source/transport | 8 passed, exit0; explicitly not Firebase evidence |
| Real owner UI assign → Analyst save → owner read/refresh/new session | PASS within6 real local groups |
| Bounded/long-note keyboard disclosure, role priority and exact-resource/revocation checks | PASS within same6 groups |
| Separately labelled transport-fault check | PASS; private rows cleared, no fake results |
| Final read-only recording/review/grant layout checks | PASS exit0;8 inspected captures |
| Normal application build | npm run build, separate finite command, exit0 |
| Isolated design-preview build | npx --no-install vite build --config ux-preview.vite.config.ts, separate, exit0 |

Anonymous/unrelated Staff/nonowner Admin/reviewer owner-feedback reads deny.
Revoked/expired reviewer read/write deny; owner annotations remain. Saved script
text is rendered as text, never HTML. Existing copied manual notes/assignments,
accounts and result provenance were compared/preserved. Four functional-run grants
were revoked; clearly labelled workflow-test annotations/audit retained. No new
inference or performance evaluation. Listening data was the eligible RAW non-test
HLS-CMDS M0001 source, not generated tones, patient data or T9.

The first UI run exposed a strict-client pagination adapter mismatch; typed numeric
parameters resolved it without allowing arbitrary query/URL/token paths. A later
test expected incorrect denial copy and was corrected, not the authorization.
Visual review fixed reviewer-name contrast and compact mobile/tablet controls.
Final Midnight capture waits for settled actual control colour; mid-transition
images/partial overbroad-animation-wait captures are retained as earlier evidence.
No theme-token redesign. Five-axis review has no outstanding Critical/Important
finding; not a complete accessibility audit or clinical effectiveness claim.

Final artifacts: implementation/frontend/output/playwright/review-feedback/
final-layout-v6/, at1440×900/390×844/820×1000, Frost/Midnight;8 personally inspected
screens, no overflow/JS errors, reduced motion/focus/mobile clearance preserved.
Functional receipt SHA256:
b02970dbea213e387352e4cd6d0da6c2ef8d87765cecdbc7f493348743d66d2f.
Client receipt:6b03b77fb0f12b08cade28c574a77ed7604425ebc7af8aba64cdc95653305d96.
Final layout receipt:751aaec17ff8556908ad4c0fe66754150411dc30e600c164f3bcd26607ce6430.

## Owner review / boundary

New4200/API8200 namespace retains earlier4196–4199 data/windows. TWO dedicated
headed fictional Staff/Analyst sessions use the established fixed SDK/TestVerifier
ONLY for identity, not Firebase/emulator verification. Never enter real credentials.
SQLite/private files/API/frozen worker are real, loopback-only; worker loaded the
verified unchanged endpoint once0.318182s. Guarded stop/restart preserves data.
The owner can review both role views and saved feedback now; approval is pending.

The role distinction is meaningful for this non-clinical collaboration workflow:
owner requests/receives feedback, Analyst reviews assigned resources/publishes
observations. Common audio tools are appropriate, not duplicated-role failure.
No different algorithm or blanket access is needed merely to differentiate roles.

No production/Axora/Firebase-provider/ML/checkpoint/DSP/T9 change or deployment.
Historical T9 values stay frozen; physical-stethoscope qualification is separate.
Pending: full review-history/version UI, notifications, avatar/account-data/export/
delete/unlink, secure handle login, global Insights and asset-gated owl flight.
