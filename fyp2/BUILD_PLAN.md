# Separate FYP2 authoring and build plan

This preparation does not rebuild or modify the submitted FYP1 report. The editable starter in this directory is a small, separately configured QMD outline; it is not synchronized report text and is not a verified final Word/PDF artifact.

## Inspected existing workflows

| Workflow | Inputs and actual outputs | Preparation decision |
| --- | --- | --- |
| Authoritative supervisor revision | `report/revisions/revise_supervisor_feedback.py` reads the historical report DOCX (prefers a Submission source if present), copies to **`report/Submission/1221303805_Arshad_Jamal_FYP1_Revised_Copy.docx`**, changes content/formatting/figures and creates `_apa_work` intermediates. It invokes `quarto pandoc` for references. Word then updates fields and exports the submission PDF. | Do not execute the script as-is: its fixed output overwrites an authoritative artifact. Do not change the tracked script merely to make this preparation run. |
| Restored Quarto baseline | `report/quarto/paper.qmd`, six included chapters, reference DOCX and older bibliography; `render-report.ps1` writes `report/generated/paper.docx`, then runs `fix-docx-format.py` in place. Optional Typst PDF is not the submitted Word export. | Do not use as a current report content source without deliberate reconciliation. No historical render in this task. |
| Existing validation helper | `validate-report.ps1` checks old baseline paths, placeholders, tool presence and generated output. | It does not verify synchronization with the revised report or constitute FYP2 acceptance. Do not treat placeholder presence as current questionnaire completeness. |
| New FYP2 starter | `fyp2/paper.qmd`, independent `_quarto.yml`; HTML output limited to `fyp2/_build/`. No automatic inclusion of old chapters or bibliography. | Rendered successfully with project-local Quarto 1.10.18 on 26 September 2026. Desktop/mobile HTML inspected. HTML is for preparation review, not university submission formatting. |

## Tools checked on this host

Initially available: Poppler `pdftotext`, `pdfinfo`, `pdftoppm`; `unzip`; Graphviz `dot`; workspace-bundled Python with `python-docx 1.2.0` and `lxml 6.1.1`. Quarto, Pandoc, PowerShell `pwsh` and PlantUML were not initially found on PATH. Microsoft Word final field/export capability was not exercised.

An explicitly authorized follow-up installed the official stable Linux amd64 **Quarto 1.10.18** portable distribution only at `/home/ashraf/Documents/StethoFuse/.local/tools/quarto`. Its 147,010,003-byte archive matched the official manifest and published SHA256 checksum. No sudo, system package, PATH/profile change, TinyTeX, Chromium or add-on installation was performed. `quarto check` exited 0: bundled Pandoc 3.10.0, Dart Sass 1.101.0, Deno 2.7.14 and Typst 0.15.1 checked successfully. Existing system Chrome was detected; R/Jupyter/TeX are not available or required for this non-executable HTML starter. See [installation and build provenance](provenance/QUARTO_SETUP.md).

Workspace dependency loader resolved Python to:

```text
/home/ashraf/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3
```

No bundled LibreOffice path was returned by that loader invocation; no installed desktop LibreOffice was used. A later DOCX build must resolve the managed renderer/runtime before attempting a render. Do not assume a local `soffice` is the approved renderer.

## Checks performed now

- `git status --short`, branch and HEAD checks before preparation.
- SHA256 of all 217 originally tracked files.
- `pdfinfo` on submitted report and handbook; selected text extraction and read-only DOCX OOXML heading/media inspection.
- Rendered/visually inspected submitted contents page ix and handbook page 14 using Poppler in a scratch directory.
- Parsed original questionnaire CSV count without reproducing respondent records.
- Checked all nine new Markdown files and 27 local links after tool setup: no broken local links or unexpected trailing whitespace (two-space Markdown hard breaks are intentional). An initial standalone YAML-parser check could not run because the bundled Python has no PyYAML; no Python package was installed. The subsequent successful Quarto render validated the configuration through the actual build tool.
- Rendered only the new starter to `fyp2/_build/fyp2-preparation.html`; command exited 0. The tool's installation self-check also rendered its own basic test document, not a historical report.
- Ran [the isolated HTML smoke check](verify-html.mjs) using existing Playwright Core 1.63.0 and Google Chrome 151.0.7922.137. At 1440×1000 and 360×800: eight expected section headings present, zero horizontal overflow, zero console/page errors and zero external HTTP(S) requests. Inspected both full-page screenshots: readable text and no visible clipping/overlap. [Machine-readable result](output/playwright/fyp2-html-check.json), [desktop](output/playwright/fyp2-desktop.png), [mobile](output/playwright/fyp2-mobile.png).
- Read historical scripts and selected bibliographic/diagram/code/test evidence without executing revision, application, training or evaluation workflows.

These are source/preparation and HTML-starter checks, not a finished academic report build, Word/PDF layout certification or fresh application test results.

## Safe commands for later work

From the documentation repository, verify historical bytes before and after every build:

```sh
sha256sum --check fyp2/provenance/tracked-files-2026-09-26.sha256
git diff --exit-code -- . ':!fyp2' ':!FYP1_TO_FYP2_CHANGE_MAP.md' ':!FYP2_OUTLINE.md'
git status --short
```

The following commands were executed successfully from the documentation repository (the render was run from `fyp2/`; the equivalent repository-root path is shown):

```sh
/home/ashraf/Documents/StethoFuse/.local/tools/quarto/bin/quarto --version
/home/ashraf/Documents/StethoFuse/.local/tools/quarto/bin/quarto check
/home/ashraf/Documents/StethoFuse/.local/tools/quarto/bin/quarto render fyp2/paper.qmd --to html
/home/ashraf/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node fyp2/verify-html.mjs
```

Confirmed output from its own configuration: `fyp2/_build/fyp2-preparation.html` (ignored generated output). Run only the new project, not `report/quarto/paper.qmd` or the historical revision script. The smoke-check script depends on the existing sibling frontend's Playwright Core package and the documented system Chrome path; it installs nothing and opens only the local HTML in fresh browser contexts. Screenshot evidence is stored separately under `fyp2/output/playwright/`.

## When the editable final report is authorized

1. Choose a deliberate working format with the student. The revised DOCX is the authoritative content baseline, while QMD is a possible future maintained source after reconciliation. Do not silently switch workflows.
2. Create a separately named copy under `fyp2/` or a dedicated scratch checkout with explicit new output paths. Never use a submitted path as a temporary output.
3. Reconcile source content chapter by chapter against S01/S02, especially the questionnaire and added algorithm formulation. Track citations, diagrams, equations, captions, cross-references and original requirement IDs.
4. Use the current university template after the open guidance items are resolved. Do not infer final pagination/margins from a generic template or the handbook PDF's own page size.
5. If reusing revision logic, isolate it in new FYP2 code with explicit input/output arguments and refusal to overwrite submitted or input files. Do not blindly rerun FYP1 replacements against an already revised DOCX.
6. Test the new pipeline on a small separate sample before a full report. Rendering/output paths must be outside `report/Submission/`. Record tool versions, source/output hashes, commands and exit status.
7. Render the new DOCX to page images using the managed document renderer; inspect every page, native equations, tables, captions, TOC/lists, Roman/Arabic numbering and bibliography. Word field update/export, if required, must be separately verified. A successful conversion alone is not visual QA.
8. Verify historical hashes again. New final DOCX/PDF names must not collide with FYP1 artifacts. No final export or submission without user review.

## Next dependencies and decisions

The isolated HTML route is now available; no additional dependency installation is needed for this preparation. A final DOCX route still needs the approved template, managed rendering and Word/export verification where applicable. Current FYP2 format/rubric confirmation and source reconciliation remain open; a successful starter render does not make the stale historical QMD baseline authoritative.
