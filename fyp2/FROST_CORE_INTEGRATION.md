# Frost Studio — owner-approved core integration, 30 September 2026

**IMPLEMENTED LOCALLY / INTEGRATED / TESTED LOCALLY / READY FOR OWNER REVIEW.
NEW INTERFACE NOT DEPLOYED.** The owner explicitly approved polish-v1, closing
the design decision and authorizing only this core milestone. The existing
production ML deployment/acceptance/backup remains unchanged and complete.

## Chapter 5 implementation evidence

Fixture-free adaptations of the approved Frost Studio shell, glass tokens,
editorial/operational typography, Library, audio players/charts and perched owl
now connect to the existing LiveAppProvider and authenticated API client.
Source commit: `8174d54e723ae6fa878f83c935556ea1775db3cc` in implementation.
No backend runtime, schema migration, authorization rule or second processing
pipeline was needed. Existing upload/AudioWorklet capture, durable SQLite jobs,
private storage and frozen CPU worker are reused.

Core routes: `/app/overview`, `/app/library`, `/app/recordings/new[/upload|/record]`,
`/app/recordings/{id}`. API: GET/POST `/api/recordings`, GET/PATCH recording detail,
POST `/api/recordings/{id}/jobs`, GET `/api/jobs/{id}`, GET `/api/results/{id}`,
GET/HEAD `/api/media/{id}`. The Library joins three complete authorized collections,
not repeated per-row requests; counts/pagination describe their actual scope.
Stages are queued/processing/succeeded/failed, never invented percentages.
The authenticated logo goes to Overview. Existing recording/job/result links
preserve identity; direct result/audio views do not require an owner-only job.
Working Shared/review/settings/profile/Help/Admin functions remain available.

Every displayed waveform/metric is derived from loaded authorized WAV samples.
RMS/peak/crest/clipping, source-dependent waveform and bounded spectrogram use
unboosted stored-rate samples; device playback resampling does not relabel the
artifact. Silence/missing/denied data is explicit. No separation accuracy,
confidence, SI-SDR or diagnosis is assigned to ordinary uploads. Playback remains
0–200% with the accepted GainNode/compressor; downloaded files remain unchanged.

No fake handles/public IDs were added. Missing identity fields are honest; real
internal keys stay in technical details and existing advanced sharing controls.
Global Insights and fake notifications are not presented as completed features.

## Chapter 6 acceptance boundary and result

The existing test-only verifier/browser SDK identity seam was used with fictional
accounts. This is **not live Firebase or an auth emulator**, and no bypass was
added to application runtime. The API, loopback proxy, SQLite DB/private files
and hash-verified frozen worker were real and isolated under implementation's
ignored `.local/frost-core-runtime/`; no production data/path/provider was used.
Synthetic input was `M0001.wav`,15s/4kHz/mono/60,000 samples, not patient/T9 audio.

Seventeen real-local groups passed: upload→Library→Separate→queued→processing→
ready, repeated-job reuse, refresh/new test-authenticated session, automatic
Original/Heart/Lung, seek/source/gain100/150/200, unchanged-download hashes,
actual finite outputs, real collection search/filter/sort/pagination, old links,
anonymous/unrelated denial, exact Heart-only sibling/analysis isolation, separate
result grants, revocation clearing audio/plots, sign-out URL cleanup, failed-job
persistence and truthful API-unavailable presentation. No page exceptions or
unexpected external requests. An induced failure uses the existing **test-only**
observation barrier, not a model change. Capture uses a **fake microphone** with
the real AudioWorklet/PCM upload path; physical stethoscope qualification remains
uncompleted and is not inferred.

Separately,14 existing SDK/API **mock** account-workflow regression groups passed,
including profile/settings/review/role/session/recovery guards. They are not real
backend/provider evidence. Both finite builds exited0 (`npm run build`; isolated
`npx --no-install vite build --config ux-preview.vite.config.ts`). No historical
ML/backend campaign or Lighthouse audit was repeated.

Integrated desktop1440×900, mobile390×844, tablet900px, Frost/Midnight, long titles,
empty/unavailable/failed states were rendered and visually inspected against
polish-v1. One legacy img clamp shrank the mobile branch; a scoped override
restored the approved geometry. Two focused final real-local layout checks passed;
desktop/mobile close-ups confirm planted claws. Renderer/iris/asset/flight policy
is unchanged. Earlier harness wait/RIFF/teardown/configuration assumptions remain
documented rather than hidden. Worker provenance honestly reports the pre-commit
base SHA plus dirty worktree; no clean-code attribution is fabricated.

Detailed ignored receipts/screenshots and hashes are indexed in implementation's
`docs/FROST_CORE_EVIDENCE.json` and `docs/FROST_CORE_INTEGRATION.md`. The full real
receipt SHA-256 is `255a201842e4c6c299080a71e2138a526f3cf9b10434ede389cab25c71288fee`;
the separate mock regression receipt is
`93f3a1f6b1c6c5819c5d1bf5548dbafa76bde7bd12dcdf9f081fb3c258e9f7c7`.

## Privacy, limits and next gate

Each protected source is independently authorized; visible result metadata never
implies sibling permission. Obsolete requests abort, private object URLs/audio
nodes clear, and access revalidation removes denied plots/bytes. Revocation blocks
subsequent requests but cannot recall already downloaded bytes. The backend
remains authoritative; administrator status gives no blanket private access.

No model/checkpoint/specification/inference change, training, T9 reuse, production
mutation or Axora change occurred. Final T9 results remain exactly as recorded in
[the frozen evaluation](T9_FINAL_HELDOUT_EVALUATION.md). This is local technical
acceptance, not stakeholder usability, clinical or physical-device validation.

Pending, not cancelled: handles/public-ID backfill, username login, handle-sharing
services, avatar/profile backend extensions, export/unlink/delete, global Insights
and genuine owl flight (**ASSET-GATED — NOT IMPLEMENTED**). Existing production
functionality is distinct from this newly integrated local interface. STOP for
owner review; deployment and next account/identity/data milestone need separate
authorization.
