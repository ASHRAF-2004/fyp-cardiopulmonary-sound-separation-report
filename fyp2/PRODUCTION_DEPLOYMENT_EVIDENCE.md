# Production deployment evidence — 27 September 2026

Status: **implemented, integrated, tested, verified live** only for the bounded
checks below. Application release `921c40d0e5a9672d3917d98aea6d8802ec1d1b92` is
deployed at https://stethofuse.ashraf-alsaloul.com . This supersedes earlier
planned/blocked production snapshots, without rewriting FYP1 or old test results.

## Design actually deployed (Chapters 4–5)

Normal browser → Cloudflare HTTPS → dedicated `stethofuse-production` Tunnel →
loopback Caddy `127.0.0.1:8088` → static React SPA / same-origin FastAPI `/api`.
FastAPI port `8000` is internal to the isolated Compose network. SQLite and private
media are separate protected bind mounts, not web assets. Axora uses its unchanged
separate tunnel/network/services.

A final transport check initially found plain HTTP serving the SPA. A Cloudflare
Single Redirect scoped only to the StethoFuse hostname now sends HTTP to the same
HTTPS path/query with 308. Zone-wide settings and Axora are unchanged. The
implementation deployment receipt records the exact rule and rollback identifiers.

FastAPI verifies the Firebase JWT signature/claims using public certificates,
then presents the same token to Firebase Auth REST `accounts:lookup`. It validates
the matching UID, enabled/verified state and `iat >= validSince` (seconds), then
uses trusted local account/status/role/owner/grant records. A missing false
`disabled` boolean is permitted; explicit malformed values fail closed. The
server key is restricted to Identity Toolkit. No production ADC, service-account
key, Cloud Run, Artifact Registry, IAM role or Google billing change is involved.
Cloud Run remains a **superseded-before-deployment** design, not a deployed feature.

Firebase's authorized-domain list was extended only with the production hostname;
existing authDomain, Google provider and callback/sign-in configuration remain
unchanged. The two previously verified local accounts/roles and two explicitly
synthetic fixtures were copied using a consistent SQLite backup and private-file
copy. No repeated bootstrap, legacy migration, patient data or participant study.

## Bounded verification (Chapter 6)

| Requirement / concern | Observation | Evidence classification |
| --- | --- | --- |
| R01/R02/R13 identity and backend role | Real Google Admin: `/api/auth/me` 200 with matching Firebase UID/local admin; Admin Users 200. Real Staff: own identity 200/local healthcare_staff; Admin Users 403 and direct UI route denied. | PRODUCTION + REAL FIREBASE; verified live |
| R03/R11 ownership and private media | Owner metadata/media/download 200; downloaded synthetic bytes match SHA-256. Staff denied another owner's metadata/media/download (403). Admin likewise denied Staff-owned private content (403). Anonymous media and invalid token 401. | PRODUCTION + REAL FIREBASE / PRODUCTION; verified live |
| R03/R17 persistence | Controlled API restart preserved both users/roles, recordings/owners and two file hashes; SQLite integrity `ok`; service healthy. | PRODUCTION; tested |
| R17 ingress/isolation | Public HTTPS/TLS and SPA refresh work; health 200; API not host-published; web container has no private mount. Axora public HTTPS 200, original tunnel version/route and healthy services unchanged. | PRODUCTION; verified live |
| R17 backup operations | Restic snapshot `e0772dc0f83823e7d04b692ab0f54031f3fd8731bba811340de964383dca1df4`, 12:50 +08, completed and was listed remotely in encrypted B2. Services resumed healthy. | REAL B2 + PRODUCTION DATA; backup completion verified live |
| Error/revocation boundaries | Existing focused MOCK tests cover disabled/revoked and malformed/upstream failures. The optional-boolean parser correction passed 13 focused cases. | MOCK; tested, not live mutation of a real account |

Production acceptance used the two designated real Google identities through
normal external Chrome. Tokens/Authorization headers/key values were not included
in evidence; a bounded runtime-log scan found none. No broad regression suite was
repeated, and no new automated test functions were created during deployment.
Operational HTTP/browser/backup checks are not a new theoretical test campaign.

## Additional bounded action-link evidence (Chapter 6)

A continuation check on 27 September 2026 exercised the deployed missing-reset
link and deliberately invalid reset/verification links in separate tabs of normal
external Chrome, preserving the Admin session. Real Firebase returned HTTP400
`INVALID_OOB_CODE` for both invalid codes. The frontend removed the query, showed
the invalid-link state without displaying the code, and did not expose a reset
form or claim success. No email-send request occurred. Invalid-code rejection is
**PRODUCTION + REAL FIREBASE; verified live**; missing-code handling is
**PRODUCTION UI; tested**. This does not establish genuine expired-link behavior,
successful password registration/login/reset, email delivery, or verification.
No new automated test functions, account changes or broad suite reruns.

The remaining mailbox-dependent checks require one owner-designated test email,
not either established Google account. The owner types secrets and opens emails
personally. After verification, that account may serve as the designated Analyst
identity for later backend-enforced promotion/assignment acceptance.

## Backup and recovery (Chapters 4, 5, 6)

Client-encrypted Restic uses the private B2 EU Central bucket via S3. The first
production snapshot covers SQLite, private synthetic files, runtime configuration
and SHA-256 manifest only (five files, 145.326 KiB). Backup credentials, developer
ADC, source/build caches and Axora data are excluded. Separate root-only secrets
are delivered through systemd credentials; the encryption password has a tested
independent offline paper copy.

The daily timer starts at 03:15 Asia/Kuala_Lumpur with up to 45 minutes jitter.
The consistent backup briefly stops/restarts only StethoFuse, so a short nightly
maintenance outage is expected. Retention target remains 7 daily / 4 weekly /
6 monthly. **Destructive pruning is disabled.** Earlier synthetic remote restore
verified SQLite integrity, SHA-256/file sets/bytes; independent paper-password
recovery also passed. The first production snapshot was completed/listed, not
subjected to another full restore. Do not conflate these evidence scopes.

Rollback stops the dedicated tunnel and timer, then only this Compose project,
preserving data and encrypted snapshots. There is no previous production release.
Only the newly created StethoFuse DNS/tunnel/domain additions may be reversed;
Axora remains out of scope. Exact IDs, paths, image IDs and commands are in the
implementation repository's `deploy/PRODUCTION_2026-09-27.md`.

## Still planned or not tested

- Real email/password registration, verification/recovery emails and Analyst
  acceptance require designated accounts; no such result is claimed.
- Live disabled/revoked-account mutation was not performed. Share/revoke evidence
  remains the earlier REAL FIREBASE + LOCAL BACKEND result, not a repeated
  production test.
- Ensemble/expert execution, derived outputs, durable worker, device capture and
  GPU integration remain planned; health honestly reports ensemble unavailable.
- This is not clinical validation, target-user evaluation, security certification
  or a measured availability/performance result. Post-deployment feedback is
  still planned and must follow actual deployment/use, not be attributed to FYP1.
- Submitted `report/Submission/` is unchanged. The academic title and original
  literature/survey findings are unchanged.
