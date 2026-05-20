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
$chapter4 = Join-Path $repoRoot "report\quarto\chapters\chapter-4.qmd"
$chapter5 = Join-Path $repoRoot "report\quarto\chapters\chapter-5.qmd"
$postProcess = Join-Path $repoRoot "report\quarto\scripts\fix-docx-format.py"
$plantumlUseCase = Join-Path $repoRoot "diagrams\plantuml\use_case_diagram.puml"
$plantumlComponent = Join-Path $repoRoot "diagrams\plantuml\component_diagram.puml"
$plantumlSequence = Join-Path $repoRoot "diagrams\plantuml\sequence_diagram.puml"
$plantumlUseCasePng = Join-Path $repoRoot "report\quarto\figures\plantuml\use_case_diagram.png"
$plantumlComponentPng = Join-Path $repoRoot "report\quarto\figures\plantuml\component_diagram.png"
$plantumlSequencePng = Join-Path $repoRoot "report\quarto\figures\plantuml\sequence_diagram.png"
$mermaidWorkflow = Join-Path $repoRoot "diagrams\mermaid\audio_processing_workflow.mmd"
$mermaidWorkflowPng = Join-Path $repoRoot "report\quarto\figures\mermaid\audio_processing_workflow.png"

$checks = @(
  @{ Name = "paper.qmd exists"; Pass = Test-Path $paper },
  @{ Name = "chapter-1.qmd exists"; Pass = Test-Path $chapter1 },
  @{ Name = "chapter-2.qmd exists"; Pass = Test-Path $chapter2 },
  @{ Name = "chapter-3.qmd exists"; Pass = Test-Path $chapter3 },
  @{ Name = "chapter-4.qmd exists"; Pass = Test-Path $chapter4 },
  @{ Name = "chapter-5.qmd exists"; Pass = Test-Path $chapter5 },
  @{ Name = "literature-review references.bib exists"; Pass = Test-Path $bib },
  @{ Name = "DOCX post-processing script exists"; Pass = Test-Path $postProcess },
  @{ Name = "Quarto available on PATH"; Pass = [bool](Get-Command quarto -ErrorAction SilentlyContinue) },
  @{ Name = "PlantUML use case source exists"; Pass = Test-Path $plantumlUseCase },
  @{ Name = "PlantUML component source exists"; Pass = Test-Path $plantumlComponent },
  @{ Name = "PlantUML sequence source exists"; Pass = Test-Path $plantumlSequence },
  @{ Name = "Rendered PlantUML use case image exists"; Pass = Test-Path $plantumlUseCasePng },
  @{ Name = "Rendered PlantUML component image exists"; Pass = Test-Path $plantumlComponentPng },
  @{ Name = "Rendered PlantUML sequence image exists"; Pass = Test-Path $plantumlSequencePng },
  @{ Name = "Mermaid workflow source exists"; Pass = Test-Path $mermaidWorkflow },
  @{ Name = "Rendered Mermaid workflow image exists"; Pass = Test-Path $mermaidWorkflowPng },
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
all_paragraphs = body_root.xpath(".//w:p", namespaces=ns)

def para_text(p):
    return "".join(p.xpath(".//w:t/text()", namespaces=ns)).strip()

def find_para(needle):
    for i, p in enumerate(paragraphs):
        if needle in para_text(p):
            return i, p
    return -1, None

def find_para_with_style(needle, style_id):
    for i, p in enumerate(paragraphs):
        style = p.find("w:pPr/w:pStyle", namespaces=ns)
        current_style = style.get(f"{{{ns['w']}}}val") if style is not None else ""
        if current_style == style_id and needle in para_text(p):
            return i, p
    return -1, None

def section_children_between(start_needle, end_needle):
    _, start_para = find_para(start_needle)
    _, end_para = find_para(end_needle)
    if start_para is None or end_para is None:
        return []
    start = body_child_index(start_para) + 1
    end = body_child_index(end_para)
    if start < 0 or end <= start:
        return []
    return list(body)[start:end]

def section_instrs(start_needle, end_needle):
    instrs = []
    for child in section_children_between(start_needle, end_needle):
        instrs.extend(child.xpath(".//w:instrText/text()", namespaces=ns))
    return instrs

def section_hyperlink_anchors(start_needle, end_needle):
    anchors = []
    for child in section_children_between(start_needle, end_needle):
        anchors.extend(child.xpath(".//w:hyperlink/@w:anchor", namespaces=ns))
    return anchors

def section_has_table(start_needle, end_needle):
    return any(child.tag == f"{{{ns['w']}}}tbl" for child in section_children_between(start_needle, end_needle))

def caption_bookmark_count(prefix):
    count = 0
    for p in all_paragraphs:
        style = p.find("w:pPr/w:pStyle", namespaces=ns)
        style_id = style.get(f"{{{ns['w']}}}val") if style is not None else ""
        text = para_text(p).replace("\u00a0", " ")
        if style_id == "ImageCaption" and text.startswith(prefix + " "):
            names = [
                b.get(f"{{{ns['w']}}}name")
                for b in p.xpath("./w:bookmarkStart", namespaces=ns)
            ]
            if any(name.startswith("_FYP" + prefix) for name in names):
                count += 1
    return count

def heading_bookmark_count(prefix):
    count = 0
    for p in paragraphs:
        style = p.find("w:pPr/w:pStyle", namespaces=ns)
        style_id = style.get(f"{{{ns['w']}}}val") if style is not None else ""
        text = para_text(p).replace("\u00a0", " ")
        if style_id == "Heading1" and text.startswith(prefix):
            names = [
                b.get(f"{{{ns['w']}}}name")
                for b in p.xpath("./w:bookmarkStart", namespaces=ns)
            ]
            if any(name.startswith("_FYPAppendix") for name in names):
                count += 1
    return count

def section_orientations():
    result = []
    for sect in body_root.xpath(".//w:sectPr", namespaces=ns):
        pg = sect.find("w:pgSz", namespaces=ns)
        if pg is not None:
            result.append(pg.get(f"{{{ns['w']}}}orient", "portrait"))
    return result

def section_page_numbering():
    result = []
    for sect in body_root.xpath(".//w:sectPr", namespaces=ns):
        pg = sect.find("w:pgSz", namespaces=ns)
        pg_num = sect.find("w:pgNumType", namespaces=ns)
        result.append({
            "orient": pg.get(f"{{{ns['w']}}}orient", "portrait") if pg is not None else "portrait",
            "fmt": (pg_num.get(f"{{{ns['w']}}}fmt") or "") if pg_num is not None else "",
            "start": (pg_num.get(f"{{{ns['w']}}}start") or "") if pg_num is not None else "",
        })
    return result

def body_child_index(target):
    for i, child in enumerate(list(body)):
        if child is target:
            return i
    return -1

def appendix_matrix_table():
    a_idx, a_para = find_para_with_style("Appendix A: Full Literature Review Matrix", "Heading1")
    b_idx, b_para = find_para_with_style("Appendix B: PRISMA Screening Summary", "Heading1")
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
section_numbers = section_page_numbering()
toc_instrs = section_instrs("Table of Contents", "List of Tables")
table_anchors = section_hyperlink_anchors("List of Tables", "List of Figures")
figure_anchors = section_hyperlink_anchors("List of Figures", "List of Abbreviations/Symbols")
appendix_anchors = section_hyperlink_anchors("List of Appendices", "Chapter 1: Introduction")
table_caption_bookmarks = caption_bookmark_count("Table")
figure_caption_bookmarks = caption_bookmark_count("Figure")
appendix_heading_bookmarks = heading_bookmark_count("Appendix ")

repo = Path(r"$repoRoot")
bib_text = Path(r"$bib").read_text(encoding="utf-8")
bib_keys = set(re.findall(r"^@\w+\{([^,]+),", bib_text, flags=re.M))
source_paths = [
    repo / "report/quarto/paper.qmd",
    repo / "report/quarto/chapters/chapter-1.qmd",
    repo / "report/quarto/chapters/chapter-2.qmd",
    repo / "report/quarto/chapters/chapter-3.qmd",
    repo / "report/quarto/chapters/chapter-4.qmd",
    repo / "report/quarto/chapters/chapter-5.qmd",
]
source_text = "\n".join(path.read_text(encoding="utf-8") for path in source_paths if path.exists())
source_at_keys = set(re.findall(r"(?<![\w-])@([A-Za-z0-9_:-]+)", source_text))
missing_citation_keys = sorted(
    key for key in source_at_keys
    if key not in bib_keys and not key.startswith(("fig-", "tbl-", "sec-", "eq-"))
)
forbidden_terms = [
    "papers_master.csv",
    "extraction_matrix.csv",
    "download_queue.csv",
    "chapter_2_evidence_map.md",
    "evidence map",
    "Codex",
    "GitHub",
    "Quarto scripts",
    "validation scripts",
]

checks = {
    "cover appears before table of contents": plain.find("FINAL YEAR PROJECT INTERIM REPORT") != -1 and plain.find("Table of Contents") != -1 and plain.find("FINAL YEAR PROJECT INTERIM REPORT") < plain.find("Table of Contents"),
    "chapter 1 appears after front matter": plain.find("Chapter 1: Introduction") > plain.find("List of Appendices"),
    "no obvious repeated subsection numbering": not re.search(r"\\b(\\d+\\.\\d+)\\s+\\1\\b", plain),
    "Word fields update on open": "updateFields" in settings,
    "front matter Roman numbering starts at iii": any(section["fmt"] == "lowerRoman" and section["start"] == "3" for section in section_numbers),
    "main chapters use Arabic numbering from 1": any(section["fmt"] == "decimal" and section["start"] == "1" for section in section_numbers),
    "References Roman numbering starts at xiv": any(section["fmt"] == "lowerRoman" and section["start"] == "14" for section in section_numbers),
    "Appendix A landscape section continues Roman numbering": any(section["orient"] == "landscape" and section["fmt"] == "lowerRoman" and section["start"] == "" for section in section_numbers),
    "post-Appendix A sections continue Roman numbering": section_numbers[-1]["fmt"] == "lowerRoman" and section_numbers[-1]["start"] == "" and section_numbers[-1]["orient"] == "portrait",
    "Table of Contents is a navigatable Word TOC field": any("TOC" in instr and "\\h" in instr and '"1-3"' in instr for instr in toc_instrs),
    "List of Tables uses generated internal hyperlinks": len(table_anchors) == table_caption_bookmarks and table_caption_bookmarks > 0 and all(anchor.startswith("_FYPTable") for anchor in table_anchors),
    "List of Tables has PAGEREF fields": sum(1 for instr in section_instrs("List of Tables", "List of Figures") if "PAGEREF _FYPTable" in instr and "\\h" in instr) == table_caption_bookmarks,
    "List of Tables is not a static table": not section_has_table("List of Tables", "List of Figures"),
    "List of Figures uses generated internal hyperlinks": len(figure_anchors) == figure_caption_bookmarks and figure_caption_bookmarks > 0 and all(anchor.startswith("_FYPFigure") for anchor in figure_anchors),
    "List of Figures has PAGEREF fields": sum(1 for instr in section_instrs("List of Figures", "List of Abbreviations/Symbols") if "PAGEREF _FYPFigure" in instr and "\\h" in instr) == figure_caption_bookmarks,
    "List of Figures is not a static table": not section_has_table("List of Figures", "List of Abbreviations/Symbols"),
    "List of Appendices uses internal hyperlinks": len(appendix_anchors) == appendix_heading_bookmarks and appendix_heading_bookmarks > 0 and all(anchor.startswith("_FYPAppendix") for anchor in appendix_anchors),
    "List of Appendices has PAGEREF fields": sum(1 for instr in section_instrs("List of Appendices", "Chapter 1: Introduction") if "PAGEREF _FYPAppendix" in instr and "\\h" in instr) == appendix_heading_bookmarks,
    "List of Appendices is not a static table": not section_has_table("List of Appendices", "Chapter 1: Introduction"),
    "no missing citation keys": len(missing_citation_keys) == 0,
    "at least three section properties": document.count("<w:sectPr") >= 3,
    "Heading styles do not add their own numbering": heading_has_no_numpr("Heading1") and heading_has_no_numpr("Heading2") and heading_has_no_numpr("Heading3"),
    "header font size is 10 pt": visible_text_runs_have_size(header_root, "20"),
    "footer font size is 8 pt": visible_text_runs_have_size(footer_root, "16"),
    "Chapter 1 uses normal problem/objective numbering": "P1." not in plain and "P2." not in plain and "P3." not in plain and "O1." not in plain and "O2." not in plain and "O3." not in plain,
    "no problem-objective alignment table remains": "Problem-objective alignment" not in plain,
    "Chapter 4 is included": "Chapter 4: Design and Implementation" in plain,
    "Chapter 5 is included": "Chapter 5: Testing and Evaluation" in plain,
    "no placeholder report text remains": "Placeholder" not in plain,
    "no draft wording remains in report text": "draft" not in plain.lower(),
    "no obsolete Chapter 6 remains": "Chapter 6:" not in plain,
    "report text avoids internal workflow names": not any(term in plain for term in forbidden_terms),
    "references section appears": "References" in plain,
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
