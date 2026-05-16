$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptDir "..\..\..")
$paper = Join-Path $repoRoot "report\quarto\paper.qmd"
$bib = Join-Path $repoRoot "literature-review\references\references.bib"
$docx = Join-Path $repoRoot "report\generated\paper.docx"
$pdf = Join-Path $repoRoot "report\generated\paper.pdf"
$chapter1 = Join-Path $repoRoot "report\quarto\chapters\chapter-1.qmd"
$chapter2 = Join-Path $repoRoot "report\quarto\chapters\chapter-2.qmd"
$chapter3 = Join-Path $repoRoot "report\quarto\chapters\chapter-3.qmd"
$postProcess = Join-Path $repoRoot "report\quarto\scripts\fix-docx-format.py"

$checks = @(
  @{ Name = "paper.qmd exists"; Pass = Test-Path $paper },
  @{ Name = "chapter-1.qmd exists"; Pass = Test-Path $chapter1 },
  @{ Name = "chapter-2.qmd exists"; Pass = Test-Path $chapter2 },
  @{ Name = "chapter-3.qmd exists"; Pass = Test-Path $chapter3 },
  @{ Name = "literature-review references.bib exists"; Pass = Test-Path $bib },
  @{ Name = "DOCX post-processing script exists"; Pass = Test-Path $postProcess },
  @{ Name = "Quarto available on PATH"; Pass = [bool](Get-Command quarto -ErrorAction SilentlyContinue) },
  @{ Name = "DOCX output exists"; Pass = Test-Path $docx }
)

foreach ($check in $checks) {
  if ($check.Pass) {
    Write-Host "PASS: $($check.Name)"
  } else {
    Write-Host "FAIL: $($check.Name)"
  }
}

if ((Test-Path $docx) -and (Get-Command python -ErrorAction SilentlyContinue)) {
  $pythonCheck = @"
import re
import sys
import zipfile
from pathlib import Path
from lxml import etree

docx = Path(r"$docx")
with zipfile.ZipFile(docx) as zf:
    document = zf.read("word/document.xml").decode("utf-8", errors="ignore")
    settings = zf.read("word/settings.xml").decode("utf-8", errors="ignore")
    styles = zf.read("word/styles.xml").decode("utf-8", errors="ignore")
    header = zf.read("word/header1.xml").decode("utf-8", errors="ignore")
    footer = zf.read("word/footer1.xml").decode("utf-8", errors="ignore")
    plain = re.sub(r"<[^>]+>", " ", document)
    plain = " ".join(plain.split())
    styles_root = etree.fromstring(styles.encode("utf-8"))
    header_root = etree.fromstring(header.encode("utf-8"))
    footer_root = etree.fromstring(footer.encode("utf-8"))

ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
def heading_has_no_numpr(style_id):
    result = styles_root.xpath(f".//w:style[@w:styleId='{style_id}']/w:pPr/w:numPr", namespaces=ns)
    return len(result) == 0

def visible_text_runs_have_size(root, expected):
    runs = root.xpath(".//w:r[w:t]", namespaces=ns)
    if not runs:
        return False
    for run in runs:
        size = run.find("w:rPr/w:sz", namespaces=ns)
        complex_size = run.find("w:rPr/w:szCs", namespaces=ns)
        if size is None or size.get(f"{{{ns['w']}}}val") != expected:
            return False
        if complex_size is None or complex_size.get(f"{{{ns['w']}}}val") != expected:
            return False
    return True

checks = {
    "cover appears before table of contents": plain.find("FINAL YEAR PROJECT INTERIM REPORT") != -1 and plain.find("Table of Contents") != -1 and plain.find("FINAL YEAR PROJECT INTERIM REPORT") < plain.find("Table of Contents"),
    "chapter 1 appears after front matter": plain.find("Chapter 1: Introduction") > plain.find("List of Appendices"),
    "no obvious repeated subsection numbering": not re.search(r"\\b(\\d+\\.\\d+)\\s+\\1\\b", plain),
    "Word fields update on open": "updateFields" in settings,
    "at least three section properties": document.count("<w:sectPr") >= 3,
    "Heading styles do not add their own numbering": heading_has_no_numpr("Heading1") and heading_has_no_numpr("Heading2") and heading_has_no_numpr("Heading3"),
    "header font size is 10 pt": visible_text_runs_have_size(header_root, "20"),
    "footer font size is 8 pt": visible_text_runs_have_size(footer_root, "16"),
}
for name, ok in checks.items():
    print(("PASS" if ok else "FAIL") + ": " + name)
"@
  $pythonCheck | python -
}

Write-Host ""
if (Test-Path $pdf) {
  Write-Host "INFO: Optional PDF output exists"
} else {
  Write-Host "INFO: Optional PDF output was not generated"
}
Write-Host "Manual DOCX checks still required: Word field update/refresh, exact page-number display, margins, fonts, table/figure lists, captions, APA references, and appendices."
