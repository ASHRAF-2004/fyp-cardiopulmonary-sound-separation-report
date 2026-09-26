# Implementation status and evidence conventions

M1 synchronization, 26 September 2026. These terms apply to the separate FYP2 working copy. They do not revise what the submitted FYP1 report claimed.

| Status | Meaning | Required boundary |
| --- | --- | --- |
| `implemented` | Code or configuration exists in an identified working version. | Name the files and revision; existence is not a successful execution. |
| `integrated` | The component is connected to the actual application path. | Identify entrypoint, caller, data flow and remaining unavailable capabilities. A standalone policy harness is not route integration. |
| `tested` | A named test was run and its result retained. | State date, environment, identity source, fixture/data, command, outcome and evidence. A failed test is still a test, not a pass. |
| `verified live` | The real named provider/server/environment was successfully exercised. | Specify local API with real provider versus deployed production. One does not prove the other. |
| `planned` | Intended but not implemented, or implementation evidence has not yet been accepted into this record. | State the next acceptance evidence; do not imply code absence where concurrent work is in progress. |
| `simulated` | A workflow uses fictional data or substituted identity/service behavior. | Label fixtures, injected verifiers, mocked SDKs and synthetic audio. Simulation may also be tested. |
| `blocked` | A specific external dependency or authorization prevents the next step. | Name the dependency and bounded action; unrelated work continues. |

Statuses are not one linear completion scale. For example, route code can be `implemented`, `integrated`, and `tested` with `simulated` identities while real-provider verification is `blocked`. “Approved” records a user/supervisor decision separately; it is not a test status. “Pending evidence” is a note, not an eighth status. Do not collapse these distinctions into “done”, “secure”, “live” or “production-ready”.

## Evidence record

Each feature claim links requirement ID, historical disposition, design section/artifact, source/config/migration paths, commit or working-file hashes, test name/command, UTC timestamp, environment and versions, identity source, input fixture or authorized dataset, expected and actual results, evidence path and limitations. Keep failure/retry history. Do not sum overlapping suites into a unique total.

Use these environment descriptions explicitly: offline mocked SDK; isolated policy-store tests; local API with injected fictional verifier; Firebase emulator; local API with real Firebase account; production hostname. No test below the last two proves genuine Firebase-provider operation. A successful homepage, build or local token-shaped string is not live-auth evidence.

Never retain passwords, ID/refresh tokens, action/reset links, MFA codes, service-account keys, participant identifiers or private audio in report evidence. An intended administrator email is contact/intent metadata, not a Firebase UID or authorization rule. Record only the minimal non-secret identity facts needed for an approved live check.

## Requirements chronology

1. Preserve the FYP1 requirement IDs, 53-response survey and its original questions/limitations.
2. Record FYP2 implementation-driven additions and supersessions separately, with decision sources.
3. Deploy only after the distinct deployment approval and checks.
4. Collect genuine authorized user feedback, then analyse it and record resulting changes.

Post-deployment feedback remains `planned`; it must not be backdated into initial elicitation or attributed to the original 53 respondents. See [requirements history](REQUIREMENTS_HISTORY.md) and [M1 evidence notes](M1_IMPLEMENTATION_AND_TEST_NOTES.md).
