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

body_root = etree.fromstring(document.encode("utf-8"))
body = body_root.find("w:body", namespaces=ns)
paragraphs = body.findall("w:p", namespaces=ns)

def para_text(p):
    return "".join(p.xpath(".//w:t/text()", namespaces=ns)).strip()

def find_para(needle):
    for i, p in enumerate(paragraphs):
        if needle in para_text(p):
            return i, p
    return -1, None

def section_orientations():
    result = []
    for sect in body_root.xpath(".//w:sectPr", namespaces=ns):
        pg = sect.find("w:pgSz", namespaces=ns)
        if pg is not None:
            result.append(pg.get(f"{{{ns['w']}}}orient", "portrait"))
    return result

def body_child_index(target):
    for i, child in enumerate(list(body)):
        if child is target:
            return i
    return -1

def appendix_matrix_table():
    a_idx, a_para = find_para("Appendix A: Full Literature Review Matrix")
    b_idx, b_para = find_para("Appendix B: Gantt Chart")
    if a_para is None or b_para is None:
        return None
    start = body_child_index(a_para)
    end = body_child_index(b_para)
    if start < 0 or end <= start:
        return None
    for child in list(body)[start:end]:
        if child.tag == f"{{{ns['w']}}}tbl":
            return child
    return None

matrix_tbl = appendix_matrix_table()
matrix_rows = matrix_tbl.findall("w:tr", namespaces=ns) if matrix_tbl is not None else []
matrix_runs = matrix_tbl.xpath(".//w:r[w:t]", namespaces=ns) if matrix_tbl is not None else []
matrix_run_sizes_ok = bool(matrix_runs) and all(
    (run.find("w:rPr/w:sz", namespaces=ns) is not None and run.find("w:rPr/w:sz", namespaces=ns).get(f"{{{ns['w']}}}val") == "16")
    for run in matrix_runs
)
matrix_header_repeats = bool(matrix_rows) and matrix_rows[0].find("w:trPr/w:tblHeader", namespaces=ns) is not None
orientations = section_orientations()

checks = {
    "cover appears before table of contents": plain.find("FINAL YEAR PROJECT INTERIM REPORT") != -1 and plain.find("Table of Contents") != -1 and plain.find("FINAL YEAR PROJECT INTERIM REPORT") < plain.find("Table of Contents"),
    "chapter 1 appears after front matter": plain.find("Chapter 1: Introduction") > plain.find("List of Appendices"),
    "no obvious repeated subsection numbering": not re.search(r"\\b(\\d+\\.\\d+)\\s+\\1\\b", plain),
    "Word fields update on open": "updateFields" in settings,
    "at least three section properties": document.count("<w:sectPr") >= 3,
    "Heading styles do not add their own numbering": heading_has_no_numpr("Heading1") and heading_has_no_numpr("Heading2") and heading_has_no_numpr("Heading3"),
    "header font size is 10 pt": visible_text_runs_have_size(header_root, "20"),
    "footer font size is 8 pt": visible_text_runs_have_size(footer_root, "16"),
    "Chapter 1 uses normal problem/objective numbering": "P1." not in plain and "P2." not in plain and "P3." not in plain and "O1." not in plain and "O2." not in plain and "O3." not in plain,
    "no problem-objective alignment table remains": "Problem-objective alignment" not in plain,
    "Appendix A matrix table exists": matrix_tbl is not None,
    "Appendix A matrix section is landscape only": orientations.count("landscape") == 1,
    "Appendix A matrix font size is 8 pt": matrix_run_sizes_ok,
    "Appendix A matrix header repeats": matrix_header_repeats,
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
