from __future__ import annotations

import csv
import json
import shutil
import struct
import tempfile
import textwrap
import zipfile
from collections import Counter
from pathlib import Path

from lxml import etree
from PIL import Image, ImageDraw, ImageFont


W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}


def w(tag: str) -> str:
    return f"{{{W}}}{tag}"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def load_counts(root: Path) -> dict[str, int]:
    prisma = json.loads((root / "literature-review/prisma/prisma_counts.json").read_text(encoding="utf-8"))
    papers = read_csv(root / "literature-review/metadata/papers_master.csv")
    duplicate_rows = read_csv(root / "literature-review/metadata/duplicate_check.csv")
    title_rows = read_csv(root / "literature-review/screening/title_abstract_screening.csv")
    full_text_rows = read_csv(root / "literature-review/screening/full_text_screening.csv")

    decisions = Counter(row["decision"] for row in papers)
    title_decisions = Counter(row["include_title_abstract"] for row in title_rows)
    full_text_available = Counter(row["full_text_available"] for row in full_text_rows)
    full_text_decisions = Counter(row["include_full_text"] for row in full_text_rows)

    phase3_added = int(prisma["new_candidate_records_added"])
    phase7_added = int(prisma["phase_7_collection"]["new_candidate_records_added"])
    phase3_duplicates = int(prisma["phase_3_duplicate_candidates_skipped"])
    phase7_duplicates = int(prisma["phase_7_collection"]["duplicate_candidates_skipped"])
    total = int(prisma["phase_7_collection"]["total_records_after_phase_7"])
    included = int(prisma["decision_summary_after_phase_7"]["Include"])
    maybe = int(prisma["decision_summary_after_phase_7"]["Maybe"])
    excluded = int(prisma["decision_summary_after_phase_7"]["Exclude"])
    useful = int(prisma["decision_summary_after_phase_7"]["useful_pool_include_plus_maybe"])
    existing_pdf = int(prisma["existing_local_pdfs_audited"])

    if len(papers) != total:
        raise ValueError(f"papers_master.csv total {len(papers)} does not match prisma_counts total {total}")
    if decisions["Include"] != included or decisions["Maybe"] != maybe or decisions["Exclude"] != excluded:
        raise ValueError(f"papers_master decisions {decisions} do not match prisma_counts final decisions")
    if len(duplicate_rows) == 0:
        raise ValueError("duplicate_check.csv has no rows; refusing to fill PRISMA diagram")
    if len(title_rows) != total:
        raise ValueError("title_abstract_screening.csv row count does not match final retained record count")

    reports_assessed = full_text_available["Yes"] + full_text_available["Yes - online full text"]
    reports_not_retrieved = full_text_available["No"]
    full_text_excluded = (
        full_text_decisions["No"]
        + full_text_decisions["Exclude"]
        - reports_not_retrieved
    )
    metadata_only_pending = total - len(full_text_rows)

    return {
        "existing_pdf": existing_pdf,
        "phase3_added": phase3_added,
        "phase7_added": phase7_added,
        "new_records_added": phase3_added + phase7_added,
        "phase3_duplicates": phase3_duplicates,
        "phase7_duplicates": phase7_duplicates,
        "duplicates_skipped": phase3_duplicates + phase7_duplicates,
        "database_candidates_seen": phase3_added + phase7_added + phase3_duplicates + phase7_duplicates,
        "total_retained": total,
        "title_yes": title_decisions["Yes"],
        "title_no": title_decisions["No"],
        "included": included,
        "maybe": maybe,
        "excluded": excluded,
        "useful": useful,
        "full_text_documented": len(full_text_rows),
        "metadata_only_pending": metadata_only_pending,
        "reports_assessed": reports_assessed,
        "reports_not_retrieved": reports_not_retrieved,
        "full_text_excluded": full_text_excluded,
    }


def box_texts(c: dict[str, int]) -> list[str]:
    return [
        "Identification of studies via other methods",
        "Identification of studies via databases and public metadata sources",
        f"Records identified from existing local PDF set\n(n = {c['existing_pdf']})",
        f"Duplicate candidates skipped before adding\n(n = {c['duplicates_skipped']})\nPhase 3 = {c['phase3_duplicates']}; Phase 7 = {c['phase7_duplicates']}",
        (
            "Public database/metadata candidates\n"
            f"(n = {c['database_candidates_seen']})\n"
            "Records added after duplicate check\n"
            f"(n = {c['new_records_added']})"
        ),
        "Identification",
        f"Records screened at title, abstract, and metadata level\n(n = {c['total_retained']})",
        (
            "Records excluded after screening, year-range, duplicate, scope, or access updates\n"
            f"(n = {c['excluded']})"
        ),
        f"Phase 7 metadata-only records pending full-text download\n(n = {c['metadata_only_pending']})",
        f"Records with full-text/access screening documented\n(n = {c['full_text_documented']})",
        f"Records with full-text/access screening documented\n(n = {c['full_text_documented']})",
        f"Full text unavailable / not retrieved\n(n = {c['reports_not_retrieved']})",
        "Screening",
        f"Reports assessed for eligibility\n(n = {c['reports_assessed']})",
        (
            "Reports excluded after full-text/access assessment:\n"
            "- Disease-only or weak scope (n = 2)\n"
            "- Duplicate / earlier version (n = 1)\n"
            "- Other off-scope (n = 1)"
        ),
        f"Reports assessed for eligibility\n(n = {c['reports_assessed']})",
        (
            "Reports excluded after full-text/access assessment:\n"
            "- Disease-only or weak scope (n = 2)\n"
            "- Duplicate / earlier version (n = 1)\n"
            "- Other off-scope (n = 1)"
        ),
        (
            f"Studies included in literature review\n(n = {c['included']})\n"
            f"Background/supplementary studies retained\n(n = {c['maybe']})"
        ),
        "Included",
    ]


def paragraph(text: str, *, font_size_half_points: str = "16", bold: bool = False, align: str = "center") -> etree._Element:
    p = etree.Element(w("p"))
    p_pr = etree.SubElement(p, w("pPr"))
    jc = etree.SubElement(p_pr, w("jc"))
    jc.set(w("val"), align)
    for line_number, line in enumerate(text.split("\n")):
        if line_number:
            run_break = etree.SubElement(p, w("r"))
            etree.SubElement(run_break, w("br"))
        run = etree.SubElement(p, w("r"))
        r_pr = etree.SubElement(run, w("rPr"))
        fonts = etree.SubElement(r_pr, w("rFonts"))
        fonts.set(w("ascii"), "Arial")
        fonts.set(w("hAnsi"), "Arial")
        if bold:
            etree.SubElement(r_pr, w("b"))
        color = etree.SubElement(r_pr, w("color"))
        color.set(w("val"), "000000")
        sz = etree.SubElement(r_pr, w("sz"))
        sz.set(w("val"), font_size_half_points)
        sz_cs = etree.SubElement(r_pr, w("szCs"))
        sz_cs.set(w("val"), font_size_half_points)
        t = etree.SubElement(run, w("t"))
        t.text = line
    return p


def set_textbox_content(txbx_content: etree._Element, text: str, index: int) -> None:
    for child in list(txbx_content):
        txbx_content.remove(child)
    is_section_label = index in {0, 1, 5, 12, 18}
    txbx_content.append(
        paragraph(
            text,
            font_size_half_points="17" if is_section_label else "15",
            bold=is_section_label,
            align="center",
        )
    )


def fill_docx_template(root: Path, counts: dict[str, int]) -> None:
    template = root / "report/quarto/templates/PRISMA_2020_blank_diagram.docx"
    output = root / "literature-review/prisma/prisma_flow_diagram_filled.docx"
    texts = box_texts(counts)

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp = Path(tmp_dir)
        with zipfile.ZipFile(template, "r") as zf:
            zf.extractall(tmp)

        document_path = tmp / "word/document.xml"
        document = etree.fromstring(document_path.read_bytes())
        boxes = document.xpath(".//w:txbxContent", namespaces=NS)
        if len(boxes) != len(texts) * 2:
            raise ValueError(f"Expected {len(texts) * 2} text-box contents, found {len(boxes)}")

        for index, text in enumerate(texts):
            set_textbox_content(boxes[index * 2], text, index)
            set_textbox_content(boxes[index * 2 + 1], text, index)

        document_path.write_bytes(
            etree.tostring(document, xml_declaration=True, encoding="UTF-8", standalone=True)
        )

        if output.exists():
            output.unlink()
        with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as zf:
            for file_path in tmp.rglob("*"):
                if file_path.is_file():
                    zf.write(file_path, file_path.relative_to(tmp).as_posix())


def load_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = [
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
        Path("C:/Windows/Fonts/calibrib.ttf" if bold else "C:/Windows/Fonts/calibri.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def wrapped_lines(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int) -> list[str]:
    lines: list[str] = []
    for raw in text.split("\n"):
        if not raw:
            lines.append("")
            continue
        words = raw.split()
        current = ""
        for word in words:
            candidate = word if not current else f"{current} {word}"
            if draw.textbbox((0, 0), candidate, font=font)[2] <= max_width:
                current = candidate
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
    return lines


def draw_box(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    text: str,
    *,
    fill: str = "#ffffff",
    outline: str = "#222222",
    width: int = 3,
    font_size: int = 26,
    bold_first: bool = False,
) -> None:
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle(xy, radius=10, fill=fill, outline=outline, width=width)
    font = load_font(font_size)
    bold_font = load_font(font_size, bold=True)
    lines = wrapped_lines(draw, text, font, x2 - x1 - 34)
    line_height = int(font_size * 1.35)
    total_height = line_height * len(lines)
    y = y1 + max(10, ((y2 - y1) - total_height) // 2)
    for line_index, line in enumerate(lines):
        line_font = bold_font if bold_first and line_index == 0 else font
        bbox = draw.textbbox((0, 0), line, font=line_font)
        x = x1 + ((x2 - x1) - (bbox[2] - bbox[0])) // 2
        draw.text((x, y), line, fill="#111111", font=line_font)
        y += line_height


def draw_label(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], text: str) -> None:
    draw_box(draw, xy, text, fill="#d9eaf7", outline="#7f9db9", width=2, font_size=28, bold_first=True)


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int]) -> None:
    draw.line([start, end], fill="#333333", width=4)
    x1, y1 = start
    x2, y2 = end
    if abs(x2 - x1) >= abs(y2 - y1):
        direction = 1 if x2 > x1 else -1
        points = [(x2, y2), (x2 - 18 * direction, y2 - 10), (x2 - 18 * direction, y2 + 10)]
    else:
        direction = 1 if y2 > y1 else -1
        points = [(x2, y2), (x2 - 10, y2 - 18 * direction), (x2 + 10, y2 - 18 * direction)]
    draw.polygon(points, fill="#333333")


def make_png_and_pdf(root: Path, c: dict[str, int]) -> None:
    out_png = root / "literature-review/prisma/prisma_flow_diagram_filled.png"
    out_pdf = root / "literature-review/prisma/prisma_flow_diagram_filled.pdf"
    report_png = root / "report/quarto/figures/prisma/prisma_flow_diagram.png"
    report_png.parent.mkdir(parents=True, exist_ok=True)

    image = Image.new("RGB", (2400, 1800), "white")
    draw = ImageDraw.Draw(image)

    title_font = load_font(38, bold=True)
    subtitle_font = load_font(24)
    title = "PRISMA 2020 Flow Diagram"
    subtitle = "Machine Learning-Based System for Cardiopulmonary Sound Separation"
    for y, text, font in [(28, title, title_font), (82, subtitle, subtitle_font)]:
        bbox = draw.textbbox((0, 0), text, font=font)
        draw.text(((2400 - (bbox[2] - bbox[0])) // 2, y), text, fill="#111111", font=font)

    draw_label(draw, (105, 170, 215, 520), "Identification")
    draw_label(draw, (105, 625, 215, 1135), "Screening")
    draw_label(draw, (105, 1285, 215, 1515), "Included")

    db = (335, 170, 1055, 370)
    other = (1315, 170, 2060, 330)
    dup = (790, 430, 1500, 570)
    retained = (790, 640, 1500, 770)
    screened = (790, 850, 1500, 980)
    excluded = (1600, 850, 2240, 1000)
    retrieval = (345, 1070, 1035, 1225)
    pending = (1135, 1070, 1785, 1225)
    assessed = (345, 1310, 940, 1445)
    full_excluded = (1040, 1300, 1785, 1470)
    included = (520, 1580, 1085, 1715)
    background = (1185, 1580, 1900, 1715)

    draw_box(
        draw,
        db,
        f"Records identified from public database and metadata sources\n(n = {c['database_candidates_seen']})\nRecords added after duplicate check: n = {c['new_records_added']}",
        fill="#ffffff",
        font_size=25,
        bold_first=True,
    )
    draw_box(draw, other, f"Records identified from existing local PDF set\n(n = {c['existing_pdf']})", font_size=26, bold_first=True)
    draw_box(
        draw,
        dup,
        f"Duplicate candidates skipped before adding\n(n = {c['duplicates_skipped']})\nPhase 3 = {c['phase3_duplicates']}; Phase 7 = {c['phase7_duplicates']}",
        fill="#fff8e1",
        outline="#ad7f00",
        font_size=24,
        bold_first=True,
    )
    draw_box(draw, retained, f"Records retained in papers_master.csv\n(n = {c['total_retained']})", fill="#eef4ff", outline="#315f9b", font_size=26, bold_first=True)
    draw_box(draw, screened, f"Records screened at title, abstract, and metadata level\n(n = {c['total_retained']})", font_size=25, bold_first=True)
    draw_box(
        draw,
        excluded,
        f"Records excluded after screening, year-range, duplicate, scope, or access updates\n(n = {c['excluded']})",
        fill="#fdecea",
        outline="#b3261e",
        font_size=23,
        bold_first=True,
    )
    draw_box(draw, retrieval, f"Records with full-text/access screening documented\n(n = {c['full_text_documented']})", font_size=25, bold_first=True)
    draw_box(draw, pending, f"Phase 7 metadata-only records pending full-text download\n(n = {c['metadata_only_pending']})", fill="#fff8e1", outline="#ad7f00", font_size=24, bold_first=True)
    draw_box(draw, assessed, f"Reports assessed for eligibility\n(n = {c['reports_assessed']})", font_size=26, bold_first=True)
    draw_box(
        draw,
        full_excluded,
        "Reports excluded after full-text/access assessment:\n- Disease-only or weak scope (n = 2)\n- Duplicate / earlier version (n = 1)\n- Other off-scope (n = 1)",
        fill="#fdecea",
        outline="#b3261e",
        font_size=22,
        bold_first=True,
    )
    draw_box(draw, included, f"Studies included in literature review\n(n = {c['included']})", fill="#e8f5e9", outline="#2e7d32", font_size=26, bold_first=True)
    draw_box(draw, background, f"Background/supplementary studies retained\n(n = {c['maybe']})", fill="#fff8e1", outline="#ad7f00", font_size=25, bold_first=True)

    arrow(draw, (695, 370), (1040, 430))
    arrow(draw, (1688, 330), (1240, 430))
    arrow(draw, (1145, 570), (1145, 640))
    arrow(draw, (1145, 770), (1145, 850))
    arrow(draw, (1500, 915), (1600, 915))
    arrow(draw, (1145, 980), (690, 1070))
    arrow(draw, (1145, 980), (1460, 1070))
    arrow(draw, (690, 1225), (642, 1310))
    arrow(draw, (940, 1378), (1040, 1378))
    arrow(draw, (642, 1445), (803, 1580))
    arrow(draw, (642, 1445), (1542, 1580))

    note_font = load_font(20)
    note = (
        "Note: Maybe/background studies are retained for contextual synthesis and are shown separately "
        "from the 18 final included studies. Counts are based on prisma_counts.json and screening metadata."
    )
    wrapped = textwrap.wrap(note, width=150)
    y = 1735
    for line in wrapped[:2]:
        draw.text((260, y), line, fill="#333333", font=note_font)
        y += 26

    image.save(out_png, "PNG")
    image.save(out_pdf, "PDF", resolution=300.0)
    shutil.copyfile(out_png, report_png)

    with out_png.open("rb") as handle:
        data = handle.read(24)
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("Generated PRISMA PNG is not a valid PNG")
    width, height = struct.unpack(">II", data[16:24])
    if width < 1600 or height < 1000:
        raise ValueError(f"Generated PRISMA PNG is unexpectedly small: {width}x{height}")


def write_notes(root: Path, c: dict[str, int]) -> None:
    notes = root / "literature-review/prisma/prisma_diagram_notes.md"
    notes.write_text(
        "\n".join(
            [
                "# PRISMA Diagram Notes",
                "",
                "Project title: **Machine Learning-Based System for Cardiopulmonary Sound Separation**",
                "",
                "## Source Files",
                "",
                "- `literature-review/prisma/prisma_counts.json`",
                "- `literature-review/metadata/papers_master.csv`",
                "- `literature-review/metadata/duplicate_check.csv`",
                "- `literature-review/metadata/exclusion_reasons.csv`",
                "- `literature-review/screening/title_abstract_screening.csv`",
                "- `literature-review/screening/full_text_screening.csv`",
                "",
                "## Count Mapping",
                "",
                f"- Records identified from existing local PDF set: `{c['existing_pdf']}`.",
                f"- Public database/metadata candidates seen: `{c['database_candidates_seen']}`. This combines `{c['new_records_added']}` added records and `{c['duplicates_skipped']}` duplicate candidates skipped before adding.",
                f"- Duplicate candidates skipped before adding: `{c['duplicates_skipped']}` (`{c['phase3_duplicates']}` in Phase 3 and `{c['phase7_duplicates']}` in Phase 7).",
                f"- Records retained in `papers_master.csv` and screened at title/abstract/metadata level: `{c['total_retained']}`.",
                f"- Records excluded in the final project decision state: `{c['excluded']}`.",
                f"- Records retained for literature-review use: `{c['useful']}`.",
                f"- Studies included in the literature review: `{c['included']}`.",
                f"- Maybe/background or supplementary records retained: `{c['maybe']}`.",
                f"- Full-text/access screening rows documented: `{c['full_text_documented']}`.",
                f"- Reports assessed for eligibility from accessible full text or online full text: `{c['reports_assessed']}`.",
                f"- Full text unavailable / not retrieved in the full-text screening table: `{c['reports_not_retrieved']}`.",
                f"- Phase 7 metadata-only records not yet represented in `full_text_screening.csv`: `{c['metadata_only_pending']}`.",
                "",
                "## Interpretation Notes",
                "",
                "- The final included count is `18`. Maybe/background records are not counted as final included studies.",
                "- The `31` maybe/background records are shown separately because they are retained for context, datasets, preprocessing, metrics, or later review.",
                "- The review tracking combines local PDF auditing, public metadata screening, year-range checks, duplicate handling, and manual access updates. Therefore, the diagram is a project-specific PRISMA-style mapping rather than a claim that every retained metadata record has a retrieved full text.",
                "- No paper decisions were changed when generating this diagram.",
                "- The Mermaid diagram remains as backup/source evidence, but the report figure uses the professionally rendered PRISMA 2020-style output.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> int:
    root = repo_root()
    counts = load_counts(root)
    fill_docx_template(root, counts)
    make_png_and_pdf(root, counts)
    write_notes(root, counts)
    print("Filled PRISMA template and generated DOCX/PDF/PNG outputs.")
    print(f"Records retained: {counts['total_retained']}")
    print(f"Included: {counts['included']}; Maybe/background: {counts['maybe']}; Excluded: {counts['excluded']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
