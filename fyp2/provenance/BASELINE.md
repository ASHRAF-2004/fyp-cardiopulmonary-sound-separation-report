# Preparation baseline and preservation checks

Initial audit and M1 continuation date: 26 September 2026. Repository: `/home/ashraf/Documents/StethoFuse/documentation`. The table records the initial preservation baseline; separate FYP2 working documents now evolve after the coordinator's checkpoint.

| Item | Recorded state |
| --- | --- |
| Branch | `codex/fyp2-documentation` |
| Initial HEAD | `21e64101820522b2c2a2af22721a1b278e38190e` |
| HEAD date and subject | 2026-09-10, `panic-sync: save the report before it escapes` |
| Initial working tree | Clean (`git status --short` empty) |
| Original tracked files | 217 |
| Clone configuration | The coordinator cloned the full-history partial repository and switched `main` to `codex/fyp2-documentation` before the initial audit. Promisor remote configured (`remote.origin.promisor=true`); existing working-tree files were readable and hashed. Coordinator later created preparation checkpoint `47c10af9527ccc1425f7a8904210c55a72db10b7`. No original FYP1 tracked-file edits or history rewrite occurred; this documentation worker makes no commits/pushes. |
| Authoring scope | Only new `FYP1_TO_FYP2_CHANGE_MAP.md`, `FYP2_OUTLINE.md` and `fyp2/` files; authorized follow-up portable tool installation limited to sibling project `.local/tools/quarto` |
| Historical preservation | All 217 SHA256 checks passed after authoring; tracked-file `git diff --exit-code` passed |

## Authoritative artifact hashes

| Artifact | SHA256 |
| --- | --- |
| Submitted PDF | `6d7e442f031880ba7d4c35c87218eb708b8efafcf9dac1abc1c29737fd53623d` |
| Revised submission DOCX | `1d9ba76c6a61738ec4a2a5b93da2966e46d4d90fde94af8d54a07ba694c0759f` |
| Handbook T2610 PDF | `8daa0d54e4ba8c7ad17f34e10decb0e66a7df815f512b8be60517927813c859c` |
| Original questionnaire CSV | `702f351c546f2c2cf24faa8cf9a8447a0f728c97921cee50d5b4eec0a91cba7c` |
| Revised bibliography | `71b012e71495af0a2a9b69e43abc5b6ef785486b1af5c02a3ec07a1473995a8d` |

Full relative paths and hashes are in [the complete original-file manifest](tracked-files-2026-09-26.sha256). Its SHA256 is `e0f61e43386f48dce66684bcf01ea569ce1f3140620dfa0b7a93e81bcad91849`. The manifest covers all originally tracked files, not just the five prominent artifacts above. It intentionally excludes new preparation files.

From the documentation repository:

```sh
sha256sum --check fyp2/provenance/tracked-files-2026-09-26.sha256
git diff --exit-code -- . ':!fyp2' ':!FYP1_TO_FYP2_CHANGE_MAP.md' ':!FYP2_OUTLINE.md'
git status --short
```

Initial preparation added new untracked documents; the coordinator checkpoint now tracks them. M1 may modify only the separate FYP2 working files and add new evidence there. A whole-repository clean diff is no longer expected during M1. The scoped diff and original 217-file hashes must still pass. Do not restore/reset or overwrite unrelated work if a later check differs; investigate the exact changed file.

## Implementation snapshot limits

Implementation baseline HEAD inspected: `559ddba2f1e553f1266f4c1810ed1f75244aa210`. Its working frontend was an untracked `frontend/` tree relative to that repository at inspection. A commit hash alone therefore does not identify the frontend evidence. Selected inspected frontend, legacy backend and planning-source bytes are recorded in `inspected-workspace-sources-2026-09-26.sha256`, with paths relative to this documentation repository.

The coordinator established `codex/fyp2-application-rebuild` and delegated new access-foundation preparation separately. That work may be concurrent and is not certified by this snapshot. The coordinator also prepended a new preparation checkpoint to `frontend/PAUSE_NOTES.md`, preserving its prior content and taking a scoped backup. Its entry in the selected-source manifest is the **before-coordinator-update inspection snapshot**, not a claim that its current hash remains unchanged. The source/evidence register describes inspected legacy routes and the demo frontend, not an assertion that the parallel scaffold is integrated or that the entire implementation repository is immutable. Only the separate 217-file documentation manifest is used for the unchanged historical-report claim.

Before M1 integration the coordinator checkpointed implementation at `c6818398d8e545834535afb08441f17eac3c2c6d`, preserving the previously local frontend and access foundation. Later M1 working changes are recorded in [M1 implementation and test notes](../M1_IMPLEMENTATION_AND_TEST_NOTES.md), not retroactively inserted into the initial manifest.

## Verification scope

Submitted report metadata: 104 pages, Letter size, not encrypted, Microsoft Word producer. Revised DOCX: 45 embedded media files; actual heading hierarchy inspected. Original questionnaire: 53 data rows. Two relevant PDF pages were rendered and visually inspected; no blanket full-report layout certification is claimed.

No historical report render, Word field update, application test rerun, model evaluation/training, deployment, provider change or external configuration was performed. After the initial read-only audit, an explicitly authorized follow-up installed checksum-verified portable Quarto 1.10.18 in the project-local tool folder and rendered only the new QMD starter. Its desktop/mobile HTML was checked using existing Chrome and Playwright Core. No system package, extra browser, TinyTeX or add-on was installed. All 217 historical hashes and tracked-file diff checks still passed after rendering. See [tool and build provenance](QUARTO_SETUP.md).

M1 documentation continuation repeats relevant local guideline/PDF/DOCX inspection and reuses the existing isolated HTML toolchain; no historical report build or new installation. Its [source audit](M1_SOURCE_AUDIT.md) and M1 notes separate newly inspected evidence from the initial snapshot. Application workers may run M1 tests independently; their results are not described as runs by this documentation worker.
