$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptDir "..\..\..")
$paper = Join-Path $repoRoot "report\quarto\paper.qmd"
$bib = Join-Path $repoRoot "literature-review\references\references.bib"
$docx = Join-Path $repoRoot "report\generated\paper.docx"
$chapter1 = Join-Path $repoRoot "report\quarto\chapters\chapter-1.qmd"
$chapter2 = Join-Path $repoRoot "report\quarto\chapters\chapter-2.qmd"
$chapter3 = Join-Path $repoRoot "report\quarto\chapters\chapter-3.qmd"
$chapter4 = Join-Path $repoRoot "report\quarto\chapters\chapter-4.qmd"
$chapter5 = Join-Path $repoRoot "report\quarto\chapters\chapter-5.qmd"
$chapter6 = Join-Path $repoRoot "report\quarto\chapters\chapter-6.qmd"
$postProcess = Join-Path $repoRoot "report\quarto\scripts\fix-docx-format.py"
$prismaDocx = Join-Path $repoRoot "literature-review\prisma\prisma_flow_diagram_filled.docx"
$prismaPdf = Join-Path $repoRoot "literature-review\prisma\prisma_flow_diagram_filled.pdf"
$prismaPng = Join-Path $repoRoot "literature-review\prisma\prisma_flow_diagram_filled.png"
$reportPrismaPng = Join-Path $repoRoot "report\quarto\figures\prisma\prisma_flow_diagram.png"
$quartoCmd = Get-Command quarto -ErrorAction SilentlyContinue
if (-not $quartoCmd) {
  $fallbackQuarto = "C:\Program Files\Quarto\bin\quarto.exe"
  if (Test-Path $fallbackQuarto) {
    $quartoCmd = $fallbackQuarto
  }
}

$plantumlSources = @(
  "diagrams\plantuml\context_diagram.puml",
  "diagrams\plantuml\use_case_diagram.puml",
  "diagrams\plantuml\activity_diagram.puml",
  "diagrams\plantuml\class_diagram.puml",
  "diagrams\plantuml\sequence_diagram.puml"
)

$plantumlImages = @(
  "report\quarto\figures\plantuml\context_diagram.png",
  "report\quarto\figures\plantuml\use_case_diagram.png",
  "report\quarto\figures\plantuml\activity_diagram.png",
  "report\quarto\figures\plantuml\class_diagram.png",
  "report\quarto\figures\plantuml\sequence_diagram.png"
)

foreach ($check in @(
  @{ Name = "paper.qmd exists"; Pass = Test-Path $paper },
  @{ Name = "chapter-1.qmd exists"; Pass = Test-Path $chapter1 },
  @{ Name = "chapter-2.qmd exists"; Pass = Test-Path $chapter2 },
  @{ Name = "chapter-3.qmd exists"; Pass = Test-Path $chapter3 },
  @{ Name = "chapter-4.qmd exists"; Pass = Test-Path $chapter4 },
  @{ Name = "chapter-5.qmd exists"; Pass = Test-Path $chapter5 },
  @{ Name = "chapter-6.qmd exists"; Pass = Test-Path $chapter6 },
  @{ Name = "references.bib exists"; Pass = Test-Path $bib },
  @{ Name = "DOCX post-processing script exists"; Pass = Test-Path $postProcess },
  @{ Name = "Quarto executable available"; Pass = [bool]$quartoCmd },
  @{ Name = "Python available on PATH"; Pass = [bool](Get-Command python -ErrorAction SilentlyContinue) },
  @{ Name = "PlantUML wrapper exists"; Pass = Test-Path (Join-Path $repoRoot "tools\plantuml.cmd") },
  @{ Name = "PRISMA source DOCX exists"; Pass = Test-Path $prismaDocx },
  @{ Name = "PRISMA converted PDF exists"; Pass = Test-Path $prismaPdf },
  @{ Name = "PRISMA converted PNG exists"; Pass = Test-Path $prismaPng },
  @{ Name = "Report PRISMA PNG exists"; Pass = Test-Path $reportPrismaPng },
  @{ Name = "DOCX output exists"; Pass = Test-Path $docx }
)) {
  if ($check.Pass) {
    Write-Host "PASS: $($check.Name)"
  } else {
    Write-Host "FAIL: $($check.Name)"
  }
}

foreach ($relative in $plantumlSources) {
  if (Test-Path (Join-Path $repoRoot $relative)) {
    Write-Host "PASS: PlantUML source exists - $relative"
  } else {
    Write-Host "FAIL: PlantUML source exists - $relative"
  }
}

foreach ($relative in $plantumlImages) {
  if (Test-Path (Join-Path $repoRoot $relative)) {
    Write-Host "PASS: Rendered PlantUML image exists - $relative"
  } else {
    Write-Host "FAIL: Rendered PlantUML image exists - $relative"
  }
}

if (Get-Command python -ErrorAction SilentlyContinue) {
  $pythonCheck = @"
import re
import sys
import zipfile
from pathlib import Path
from lxml import etree

repo = Path(r"$repoRoot")
paper = repo / "report/quarto/paper.qmd"
bib = repo / "literature-review/references/references.bib"
docx = repo / "report/generated/paper.docx"
source_paths = [
    paper,
    repo / "report/quarto/chapters/chapter-1.qmd",
    repo / "report/quarto/chapters/chapter-2.qmd",
    repo / "report/quarto/chapters/chapter-3.qmd",
    repo / "report/quarto/chapters/chapter-4.qmd",
    repo / "report/quarto/chapters/chapter-5.qmd",
    repo / "report/quarto/chapters/chapter-6.qmd",
]

failures = []

def check(name, ok):
    print(("PASS" if ok else "FAIL") + ": " + name)
    if not ok:
        failures.append(name)

def read(path):
    return path.read_text(encoding="utf-8") if path.exists() else ""

paper_text = read(paper)
chapter_texts = {path.name: read(path) for path in source_paths[1:]}
source_text = "\n".join(read(path) for path in source_paths if path.exists())

def section(text, heading):
    pattern = rf"^##\s+{re.escape(heading)}\s*$"
    match = re.search(pattern, text, flags=re.M)
    if not match:
        return ""
    next_match = re.search(r"^##\s+", text[match.end():], flags=re.M)
    end = match.end() + next_match.start() if next_match else len(text)
    return text[match.end():end]

def heading_order(text, headings):
    positions = []
    for heading in headings:
        idx = text.find(heading)
        if idx < 0:
            return False
        positions.append(idx)
    return positions == sorted(positions)

ch1 = chapter_texts.get("chapter-1.qmd", "")
ch2 = chapter_texts.get("chapter-2.qmd", "")
ch3 = chapter_texts.get("chapter-3.qmd", "")
ch4 = chapter_texts.get("chapter-4.qmd", "")
ch5 = chapter_texts.get("chapter-5.qmd", "")
ch6 = chapter_texts.get("chapter-6.qmd", "")

problem_items = re.findall(r"(?ms)^\d+\.\s+(.*?)(?=^\d+\.\s+|^##\s+Project Objectives|\Z)", section(ch1, "Problem Statement"))
objective_items = re.findall(r"(?m)^\d+\.\s+", section(ch1, "Project Objectives"))
objective_sentences = [
    "To study and apply suitable preprocessing techniques to reduce noise and improve the quality of cardiopulmonary sound recordings.",
    "To design and implement a machine learning-based approach for separating mixed cardiopulmonary recordings into heart and lung sound outputs.",
    "To develop a reusable software prototype and evaluate its separation performance using public datasets and suitable performance metrics.",
]

check("Chapter order includes Introduction, Literature Review, Requirements Analysis, System Design, Implementation Plan, Conclusion", heading_order(paper_text, [
    "{{< include chapters/chapter-1.qmd >}}",
    "{{< include chapters/chapter-2.qmd >}}",
    "{{< include chapters/chapter-3.qmd >}}",
    "{{< include chapters/chapter-4.qmd >}}",
    "{{< include chapters/chapter-5.qmd >}}",
    "{{< include chapters/chapter-6.qmd >}}",
]))
check("Chapter 1 has exactly 3 problem statements", len(problem_items) == 3)
check("Chapter 1 problem statements are cited", len(problem_items) == 3 and all("@" in item for item in problem_items))
check("Chapter 1 has exactly 3 objectives", len(objective_items) == 3)
check("Chapter 1 objectives match required wording", all(sentence in ch1 for sentence in objective_sentences))
check("No P1/O1 labels exist", not re.search(r"\b[PO]\d+\b", source_text))
check("No problem-objective alignment table exists", "problem-objective alignment" not in source_text.lower())

check("Chapter 2 uses required literature review headings", heading_order(ch2, [
    "## Overview",
    "## Literature Search and Screening Process",
    "## Cardiopulmonary Sound Characteristics",
    "## Heart and Lung Sound Separation Techniques",
    "### Traditional Signal Processing Methods",
    "### Machine Learning and Deep Learning Methods",
    "## Datasets for Cardiopulmonary Sound Separation",
    "## Evaluation Metrics",
    "## Existing Systems and Prototype Relevance",
    "## Literature Review Matrix",
    "## Research Gaps",
    "## Summary",
]))
check("Chapter 2 points to professional PRISMA PNG", "figures/prisma/prisma_flow_diagram.png" in ch2)
check("Mermaid is not used for PRISMA in report sources", "mermaid" not in ch2.lower())
check("PRISMA counts are preserved", all(token in ch2 or token in paper_text for token in ["96", "47", "49", "35", "18", "17", "14"]))
check("Chapter 2 matrix refers to Appendix D", "Appendix D" in ch2)

check("Chapter 3 is Requirements Analysis", "# Chapter 3: Requirements Analysis" in ch3)
check("Chapter 3 is not Methodology", "# Chapter 3: Methodology" not in ch3)
check("Chapter 3 includes required fact-finding headings", heading_order(ch3, [
    "## Fact-Finding Techniques",
    "### Justification",
    "### Literature and Document Review",
    "### Existing System Observation / Benchmarking",
    "### Supervisor Consultation",
    "### Questionnaire Design",
    "## Requirement Analysis",
    "### Functional Requirements",
    "### Non-Functional Requirements",
    "### User Requirements",
    "## Summary",
]))
check("Chapter 3 states survey response analysis is pending", "pending" in ch3.lower() and "responses have not yet been collected" in ch3.lower())
check("Chapter 3 does not claim completed survey results", not re.search(r"(survey responses were collected|questionnaire results show|respondents participated|google form results)", ch3, flags=re.I))

check("Chapter 4 is System Design", "# Chapter 4: System Design" in ch4)
check("Chapter 4 includes required design headings", heading_order(ch4, [
    "## Context Diagram",
    "## Use Case Diagram",
    "### Use Case Description",
    "#### Actors",
    "#### Preconditions",
    "#### Normal Flow",
    "#### Postconditions",
    "#### Alternative Flows and Exceptions",
    "#### Non-Functional Requirements",
    "## Activity Diagram",
    "## Class Diagram",
    "## Sequence Diagram",
    "## Interface Design",
    "## Summary",
]))
check("PlantUML diagrams are referenced in Chapter 4", all(name in ch4 for name in [
    "context_diagram.png",
    "use_case_diagram.png",
    "activity_diagram.png",
    "class_diagram.png",
    "sequence_diagram.png",
]))
check("Chapter 5 is Implementation Plan", "# Chapter 5: Implementation Plan" in ch5)
check("Chapter 5 is not Testing and Evaluation", "# Chapter 5: Testing and Evaluation" not in ch5)
check("Chapter 5 uses planned testing language", "testing is presented as planned work" in ch5.lower() and "no user acceptance results are included" in ch5.lower())
check("Chapter 6 Conclusion exists", "# Chapter 6: Conclusion" in ch6)

appendix_order = [
    "# Appendix A: Gantt Chart",
    "# Appendix B: FYP1 Meeting Logs",
    "# Appendix C: Turnitin Similarity Index Page",
    "# Appendix D: Full Literature Review Matrix",
    "# Appendix E: PRISMA Screening Summary",
    "# Appendix F: System Design Diagrams",
    "# Appendix G: Planned Test Cases and Evaluation Metrics",
]
check("Appendices follow required order", heading_order(paper_text, appendix_order))
appendix_d = re.search(r"(?ms)# Appendix D: Full Literature Review Matrix.*?(?=# Appendix E: PRISMA Screening Summary)", paper_text)
matrix_rows = re.findall(r"(?m)^\|\s*\d+\s*\|", appendix_d.group(0) if appendix_d else "")
check("Appendix D full matrix has 35 selected studies", len(matrix_rows) == 35)
check("Appendix G includes planned test cases and evaluation metrics", "# Appendix G: Planned Test Cases and Evaluation Metrics" in paper_text and "Planned evaluation metrics" in paper_text)

bib_text = read(bib)
bib_keys = set(re.findall(r"^@\w+\{([^,]+),", bib_text, flags=re.M))
source_at_keys = set(re.findall(r"(?<![\w-])@([A-Za-z0-9_:-]+)", source_text))
missing_citation_keys = sorted(
    key for key in source_at_keys
    if key not in bib_keys and not key.startswith(("fig-", "tbl-", "sec-", "eq-"))
)
selected_keys = set(re.findall(r"\[@([A-Za-z0-9_:-]+)\]", appendix_d.group(0) if appendix_d else ""))
used_citation_keys = {key for key in source_at_keys if key in bib_keys}
check("No missing citation keys", len(missing_citation_keys) == 0)
check("Cited selected studies remain within Appendix D matrix", used_citation_keys.issubset(selected_keys))

forbidden_terms = [
    "Codex",
    "GitHub",
    "Quarto workflow",
    "papers_master.csv",
    "download_queue.csv",
    "extraction_matrix.csv",
    "evidence map",
    "validation script",
    "internal file",
]
check("Report body avoids internal workflow names", not any(term.lower() in source_text.lower() for term in forbidden_terms))

if docx.exists():
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    W = ns["w"]
    def w(tag):
        return f"{{{W}}}{tag}"
    with zipfile.ZipFile(docx) as zf:
        document = zf.read("word/document.xml")
        settings = zf.read("word/settings.xml").decode("utf-8", errors="ignore")
        styles = zf.read("word/styles.xml")
        header = zf.read("word/header1.xml") if "word/header1.xml" in zf.namelist() else b""
        footer = zf.read("word/footer1.xml") if "word/footer1.xml" in zf.namelist() else b""
    root = etree.fromstring(document)
    body = root.find("w:body", namespaces=ns)
    paragraphs = body.findall("w:p", namespaces=ns)
    all_paragraphs = root.xpath(".//w:p", namespaces=ns)
    plain = " ".join(root.xpath(".//w:t/text()", namespaces=ns))

    def para_text(p):
        return "".join(p.xpath(".//w:t/text()", namespaces=ns)).strip().replace("\u00a0", " ")

    def para_style(p):
        style = p.find("w:pPr/w:pStyle", namespaces=ns)
        return style.get(w("val")) if style is not None else ""

    def body_child_index(target):
        for i, child in enumerate(list(body)):
            if child is target:
                return i
        return -1

    def find_para(needle):
        for p in paragraphs:
            if needle in para_text(p):
                return p
        return None

    def section_children_between(start_needle, end_needle):
        start_para = find_para(start_needle)
        end_para = find_para(end_needle)
        if start_para is None or end_para is None:
            return []
        start = body_child_index(start_para) + 1
        end = body_child_index(end_para)
        return list(body)[start:end] if end > start else []

    def section_instrs(start_needle, end_needle):
        instrs = []
        for child in section_children_between(start_needle, end_needle):
            instrs.extend(child.xpath(".//w:instrText/text()", namespaces=ns))
        return instrs

    def section_anchors(start_needle, end_needle):
        anchors = []
        for child in section_children_between(start_needle, end_needle):
            anchors.extend(child.xpath(".//w:hyperlink/@w:anchor", namespaces=ns))
        return anchors

    def caption_texts(prefix):
        return [
            para_text(p)
            for p in all_paragraphs
            if para_style(p) == "ImageCaption" and para_text(p).startswith(prefix + " ")
        ]

    def caption_bookmarks(prefix):
        count = 0
        for p in all_paragraphs:
            text = para_text(p)
            if para_style(p) == "ImageCaption" and text.startswith(prefix + " "):
                names = [b.get(w("name")) for b in p.xpath("./w:bookmarkStart", namespaces=ns)]
                if any(name and name.startswith("_FYP" + prefix) for name in names):
                    count += 1
        return count

    def heading_bookmarks():
        count = 0
        for p in paragraphs:
            text = para_text(p)
            if para_style(p) == "Heading1" and text.startswith("Appendix "):
                names = [b.get(w("name")) for b in p.xpath("./w:bookmarkStart", namespaces=ns)]
                if any(name and name.startswith("_FYPAppendix") for name in names):
                    count += 1
        return count

    def visible_runs_have_size(xml_bytes, expected):
        if not xml_bytes:
            return False
        root_xml = etree.fromstring(xml_bytes)
        runs = root_xml.xpath(".//w:r[w:t]", namespaces=ns)
        if not runs:
            return False
        for run in runs:
            size = run.find("w:rPr/w:sz", namespaces=ns)
            size_cs = run.find("w:rPr/w:szCs", namespaces=ns)
            if size is None or size.get(w("val")) != expected:
                return False
            if size_cs is None or size_cs.get(w("val")) != expected:
                return False
        return True

    table_captions = caption_texts("Table")
    figure_captions = caption_texts("Figure")
    table_anchors = section_anchors("List of Tables", "List of Figures")
    figure_anchors = section_anchors("List of Figures", "List of Abbreviations/Symbols")
    appendix_anchors = section_anchors("List of Appendices", "Chapter 1: Introduction")
    sects = root.xpath(".//w:sectPr", namespaces=ns)
    orientations = []
    section_numbers = []
    for sect in sects:
        pg = sect.find("w:pgSz", namespaces=ns)
        pg_num = sect.find("w:pgNumType", namespaces=ns)
        orientations.append(pg.get(w("orient"), "portrait") if pg is not None else "portrait")
        section_numbers.append({
            "fmt": pg_num.get(w("fmt"), "") if pg_num is not None else "",
            "start": pg_num.get(w("start"), "") if pg_num is not None else "",
        })

    check("DOCX contains application-based chapter headings", heading_order(plain, [
        "Chapter 1: Introduction",
        "Chapter 2: Literature Review",
        "Chapter 3: Requirements Analysis",
        "Chapter 4: System Design",
        "Chapter 5: Implementation Plan",
        "Chapter 6: Conclusion",
    ]))
    check("DOCX has no obsolete chapter headings", "Chapter 3: Methodology" not in plain and "Chapter 5: Testing and Evaluation" not in plain)
    check("DOCX table captions use continuous numbering", bool(table_captions) and all(text.startswith(f"Table {i}:") for i, text in enumerate(table_captions, start=1)))
    check("DOCX figure captions use continuous numbering", bool(figure_captions) and all(text.startswith(f"Figure {i}:") for i, text in enumerate(figure_captions, start=1)))
    check("DOCX has no chapter-based table or figure numbering", not re.search(r"\b(Table|Figure)\s+\d+\.\d+", plain))
    check("List of Tables uses internal hyperlinks", len(table_anchors) == caption_bookmarks("Table") and len(table_anchors) > 0 and all(anchor.startswith("_FYPTable") for anchor in table_anchors))
    check("List of Tables has PAGEREF fields", sum(1 for instr in section_instrs("List of Tables", "List of Figures") if "PAGEREF _FYPTable" in instr and "\\h" in instr) == caption_bookmarks("Table"))
    check("List of Figures uses internal hyperlinks", len(figure_anchors) == caption_bookmarks("Figure") and len(figure_anchors) > 0 and all(anchor.startswith("_FYPFigure") for anchor in figure_anchors))
    check("List of Figures has PAGEREF fields", sum(1 for instr in section_instrs("List of Figures", "List of Abbreviations/Symbols") if "PAGEREF _FYPFigure" in instr and "\\h" in instr) == caption_bookmarks("Figure"))
    check("List of Appendices uses internal hyperlinks", len(appendix_anchors) == heading_bookmarks() and len(appendix_anchors) == 7 and all(anchor.startswith("_FYPAppendix") for anchor in appendix_anchors))
    check("List of Appendices has PAGEREF fields", sum(1 for instr in section_instrs("List of Appendices", "Chapter 1: Introduction") if "PAGEREF _FYPAppendix" in instr and "\\h" in instr) == heading_bookmarks())
    check("Word fields update on open", "updateFields" in settings)
    check("Header remains 10 pt", visible_runs_have_size(header, "20"))
    check("Footer remains 8 pt", visible_runs_have_size(footer, "16"))
    check("Front matter Roman numbering starts at iii", any(item["fmt"] == "lowerRoman" and item["start"] == "3" for item in section_numbers))
    check("Main chapters use Arabic numbering from 1", any(item["fmt"] == "decimal" and item["start"] == "1" for item in section_numbers))
    check("Appendix D landscape formatting exists", orientations.count("landscape") == 1)
    check("Report text avoids internal workflow names in DOCX", not any(term.lower() in plain.lower() for term in forbidden_terms))
else:
    check("DOCX checks skipped because output does not exist", False)

print("")
if failures:
    print(f"SUMMARY: {len(failures)} validation check(s) failed.")
else:
    print("SUMMARY: all validation checks passed.")
"@
  $pythonCheck | python -
}

Write-Host ""
Write-Host "Manual DOCX checks still required: refresh Word fields, confirm final displayed page numbers, cover page spacing, meeting log insertion, Gantt chart insertion, Turnitin page insertion, and supervisor confirmation."
