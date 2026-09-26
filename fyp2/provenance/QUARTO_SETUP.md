# Project-local Quarto setup and starter-build provenance

Date: 26 September 2026. Scope: the new FYP2 preparation HTML only. This is not a rebuild of the submitted report or proof of final university formatting.

## Source and integrity

The [official Linux tarball instructions](https://quarto.org/docs/download/tarball.html) support a single-user portable installation. The [official stable release](https://github.com/quarto-dev/quarto-cli/releases/tag/v1.10.18), [GitHub latest-release API](https://api.github.com/repos/quarto-dev/quarto-cli/releases/latest) and [Quarto download manifest](https://quarto.org/docs/download/_download.json) agreed on stable **1.10.18**, published **2026-07-24T13:50:30Z**, not a prerelease. The release page links source revision `5d07f3e`.

| Download | Recorded value |
| --- | --- |
| Archive | [quarto-1.10.18-linux-amd64.tar.gz](https://github.com/quarto-dev/quarto-cli/releases/download/v1.10.18/quarto-1.10.18-linux-amd64.tar.gz) |
| Archive size | 147,010,003 bytes (about 140.2 MiB), below the authorized 350 MB download ceiling |
| Archive SHA256 | `afad071b5bd22c02f2d300695743189d3650e0537a53073e654b630cff2b0c73` |
| Published checksum asset | [quarto-1.10.18-checksums.txt](https://github.com/quarto-dev/quarto-cli/releases/download/v1.10.18/quarto-1.10.18-checksums.txt), 1,042 bytes |
| Checksum asset SHA256 | `b50e206a1acbf24cbaee02095ec4ec525b3b64b1c3073042cbb244dba4bd1823` |
| Verification | Downloaded bytes matched the official manifest; the archive hash also matched the downloaded published checksum line. No source/download/checksum retry was needed. These are HTTPS-published checksums, not a separately verified signature. |

The archive was inspected before extraction: 3,006 entries beneath `quarto-1.10.18`, no absolute/traversing paths or device/FIFO entries, one internal relative symlink (`share/extension-subtrees/julia-engine/CLAUDE.md` → `AGENTS.md`). Extraction used `--strip-components=1 --no-same-owner` into the previously absent explicit destination `/home/ashraf/Documents/StethoFuse/.local/tools/quarto`. The downloaded archive remains there for provenance; the directory is approximately 587 MiB including that archive and the expanded distribution. The download ceiling was not an expanded-install-size claim.

No sudo, global symlink, shell-profile/PATH change, TinyTeX, Chromium, VeraPDF, Jupyter, R or optional add-on installation occurred. Quarto's normal runtime cache is `/home/ashraf/.cache/quarto`; the binary installation remains project-local. An existing `/usr/bin/google-chrome` was reused for inspection. The bundled distribution includes Pandoc/Deno/Sass/Typst; none was separately installed.

## Commands and outcomes

Commands below were used; downloads completed on their first attempt. They are an audit record, not an instruction to overwrite an existing installation.

```sh
curl --fail --location --max-time 120 --output /tmp/stethofuse-quarto-1.10.18-checksums.txt https://github.com/quarto-dev/quarto-cli/releases/download/v1.10.18/quarto-1.10.18-checksums.txt
sha256sum /tmp/stethofuse-quarto-1.10.18-checksums.txt
curl --fail --location --max-time 180 --output /home/ashraf/Documents/StethoFuse/.local/tools/quarto/quarto-1.10.18-linux-amd64.tar.gz https://github.com/quarto-dev/quarto-cli/releases/download/v1.10.18/quarto-1.10.18-linux-amd64.tar.gz
sha256sum /home/ashraf/Documents/StethoFuse/.local/tools/quarto/quarto-1.10.18-linux-amd64.tar.gz
tar --extract --gzip --file /home/ashraf/Documents/StethoFuse/.local/tools/quarto/quarto-1.10.18-linux-amd64.tar.gz --directory /home/ashraf/Documents/StethoFuse/.local/tools/quarto --strip-components=1 --no-same-owner
/home/ashraf/Documents/StethoFuse/.local/tools/quarto/bin/quarto --version
/home/ashraf/Documents/StethoFuse/.local/tools/quarto/bin/quarto check
```

`--version` returned `1.10.18`. `check` exited 0, including its built-in basic Markdown self-check; dependencies reported Pandoc 3.10.0, Dart Sass 1.101.0, Deno 2.7.14 and Typst 0.15.1. It reported optional R/Jupyter/TeX unavailable; none is required for this starter. This command did not execute the historical report workflow.

From `/home/ashraf/Documents/StethoFuse/documentation/fyp2`:

```sh
/home/ashraf/Documents/StethoFuse/.local/tools/quarto/bin/quarto render paper.qmd --to html
```

Exit 0; output `fyp2/_build/fyp2-preparation.html`. Configuration disables code evaluation and includes only `paper.qmd`; no bibliography, chapter or revision script from the historical report is included. The generated HTML is ignored by the new project's `.gitignore`.

| Build artifact | SHA256 at this render |
| --- | --- |
| `fyp2/paper.qmd` | `7ea61c9b0e03aacf1c7be67ef96b8b659f4f04d481711122ee781204f425c918` |
| `fyp2/_quarto.yml` | `895cacf9f12f1ebe0b6f5cfbe21bad7dfc1c042ec30ef4aa635b3696f4ea5bc7` |
| `fyp2/_build/fyp2-preparation.html` | `d40b85bdffa87805e8ae76811879e4230d93becacd76997389d2ea56f5c8eb5d` |

## Automated and visual checks

From `/home/ashraf/Documents/StethoFuse/documentation`:

```sh
/home/ashraf/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node fyp2/verify-html.mjs
sha256sum --check fyp2/provenance/tracked-files-2026-09-26.sha256 --quiet
git diff --exit-code
```

All exited 0. The HTML smoke check used existing Playwright Core 1.63.0 and Google Chrome 151.0.7922.137, with fresh isolated contexts at 1440×1000 and 360×800. Automated results: all eight expected section headings present, no horizontal overflow, no console/page errors, no HTTP(S) requests. See [JSON evidence](../output/playwright/fyp2-html-check.json).

Visual inspection of [desktop](../output/playwright/fyp2-desktop.png) and [mobile](../output/playwright/fyp2-mobile.png) full-page screenshots found readable content, correct seven-chapter numbering plus unnumbered preparation references, and no obvious overlap or clipping. The desktop table of contents is visible; mobile uses the default single-column Quarto layout. These are preparation HTML checks only, not accessibility certification or approved report typography/pagination.

All **217 historical tracked files remain byte-identical** against the pre-work manifest. No historical report build, application test, model evaluation/training, deployment or provider change was performed.
