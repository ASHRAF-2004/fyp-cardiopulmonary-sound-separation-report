from __future__ import annotations

import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

from lxml import etree


W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS = {"w": W, "r": R}

PROJECT_ID = "985"
STUDENT_NAME = "AL-SALOUL, ASHRAF ALI HUSSEIN"
COURSE_CODE = "CPT6314"
TERM = "2610 Term"
HEADER_FONT_SIZE = "20"  # OpenXML uses half-points: 20 = 10 pt.
FOOTER_FONT_SIZE = "16"  # OpenXML uses half-points: 16 = 8 pt.


def qn(namespace: str, tag: str) -> str:
    return f"{{{namespace}}}{tag}"


def w(tag: str) -> str:
    return qn(W, tag)


def r(tag: str) -> str:
    return qn(R, tag)


def parse_xml(data: bytes) -> etree._Element:
    return etree.fromstring(data)


def xml_bytes(root: etree._Element) -> bytes:
    return etree.tostring(
        root,
        xml_declaration=True,
        encoding="UTF-8",
        standalone="yes",
    )


def paragraph_text(p: etree._Element) -> str:
    return "".join(p.xpath(".//w:t/text()", namespaces=NS)).strip()


def remove_heading_style_numbering(styles_root: etree._Element) -> None:
    for style_id in ("Heading1", "Heading2", "Heading3"):
        styles = styles_root.xpath(f".//w:style[@w:styleId='{style_id}']", namespaces=NS)
        for style in styles:
            for num_pr in style.xpath("./w:pPr/w:numPr", namespaces=NS):
                parent = num_pr.getparent()
                parent.remove(num_pr)


def ensure_update_fields(settings_root: etree._Element) -> None:
    existing = settings_root.find("w:updateFields", namespaces=NS)
    if existing is None:
        existing = etree.Element(w("updateFields"))
        settings_root.insert(0, existing)
    existing.set(w("val"), "true")


def clone_or_default_pg_sz(template_sect_pr: etree._Element | None) -> etree._Element:
    if template_sect_pr is not None:
        pg_sz = template_sect_pr.find("w:pgSz", namespaces=NS)
        if pg_sz is not None:
            return etree.fromstring(etree.tostring(pg_sz))
    pg_sz = etree.Element(w("pgSz"))
    pg_sz.set(w("w"), "11906")
    pg_sz.set(w("h"), "16838")
    return pg_sz


def pg_mar(left: str, right: str, top: str, bottom: str) -> etree._Element:
    elem = etree.Element(w("pgMar"))
    elem.set(w("top"), top)
    elem.set(w("right"), right)
    elem.set(w("bottom"), bottom)
    elem.set(w("left"), left)
    elem.set(w("header"), "720")
    elem.set(w("footer"), "720")
    elem.set(w("gutter"), "0")
    return elem


def header_footer_ref(kind: str, rel_id: str) -> etree._Element:
    elem = etree.Element(w(f"{kind}Reference"))
    elem.set(w("type"), "default")
    elem.set(r("id"), rel_id)
    return elem


def section_properties(
    template_sect_pr: etree._Element | None,
    *,
    page_fmt: str | None,
    start: str | None,
    include_header_footer: bool,
    header_rel: str | None,
    footer_rel: str | None,
    cover_margins: bool,
    continuous: bool,
) -> etree._Element:
    sect_pr = etree.Element(w("sectPr"))
    if include_header_footer and header_rel:
        sect_pr.append(header_footer_ref("header", header_rel))
    if include_header_footer and footer_rel:
        sect_pr.append(header_footer_ref("footer", footer_rel))

    if continuous:
        type_elem = etree.Element(w("type"))
        type_elem.set(w("val"), "continuous")
        sect_pr.append(type_elem)

    if page_fmt or start:
        pg_num_type = etree.Element(w("pgNumType"))
        if page_fmt:
            pg_num_type.set(w("fmt"), page_fmt)
        if start:
            pg_num_type.set(w("start"), start)
        sect_pr.append(pg_num_type)

    sect_pr.append(clone_or_default_pg_sz(template_sect_pr))
    if cover_margins:
        # 25.4 mm = 1 inch = 1440 twips on all sides.
        sect_pr.append(pg_mar("1440", "1440", "1440", "1440"))
    else:
        # Main report margins from the handbook: left 38 mm, right/top/bottom 28 mm.
        # Approximate twips: 38 mm ~= 2154; 28 mm ~= 1587.
        sect_pr.append(pg_mar("2154", "1587", "1587", "1587"))
    return sect_pr


def set_paragraph_section(p: etree._Element, sect_pr: etree._Element) -> None:
    p_pr = p.find("w:pPr", namespaces=NS)
    if p_pr is None:
        p_pr = etree.Element(w("pPr"))
        p.insert(0, p_pr)
    for existing in p_pr.xpath("./w:sectPr", namespaces=NS):
        p_pr.remove(existing)
    p_pr.append(sect_pr)


def find_paragraph_index(paragraphs: list[etree._Element], needle: str) -> int:
    for idx, p in enumerate(paragraphs):
        if needle in paragraph_text(p):
            return idx
    raise ValueError(f"Could not find paragraph containing: {needle}")


def first_rel_ids(final_sect_pr: etree._Element | None) -> tuple[str | None, str | None]:
    if final_sect_pr is None:
        return None, None
    header = final_sect_pr.find("w:headerReference", namespaces=NS)
    footer = final_sect_pr.find("w:footerReference", namespaces=NS)
    return (
        header.get(r("id")) if header is not None else None,
        footer.get(r("id")) if footer is not None else None,
    )


def apply_section_numbering(document_root: etree._Element) -> None:
    body = document_root.find("w:body", namespaces=NS)
    if body is None:
        raise ValueError("DOCX document body not found")

    final_sect_pr = body.find("w:sectPr", namespaces=NS)
    header_rel, footer_rel = first_rel_ids(final_sect_pr)
    paragraphs = body.findall("w:p", namespaces=NS)

    copyright_idx = find_paragraph_index(paragraphs, "Copyright")
    chapter1_idx = find_paragraph_index(paragraphs, "Chapter 1: Introduction")
    if copyright_idx == 0 or chapter1_idx == 0:
        raise ValueError("Unable to insert section breaks at required positions")

    template_sect_pr = final_sect_pr
    cover_sect = section_properties(
        template_sect_pr,
        page_fmt=None,
        start=None,
        include_header_footer=False,
        header_rel=None,
        footer_rel=None,
        cover_margins=True,
        continuous=True,
    )
    front_sect = section_properties(
        template_sect_pr,
        page_fmt="lowerRoman",
        start="3",
        include_header_footer=True,
        header_rel=header_rel,
        footer_rel=footer_rel,
        cover_margins=False,
        continuous=True,
    )
    body_sect = section_properties(
        template_sect_pr,
        page_fmt="decimal",
        start="1",
        include_header_footer=True,
        header_rel=header_rel,
        footer_rel=footer_rel,
        cover_margins=False,
        continuous=False,
    )

    set_paragraph_section(paragraphs[copyright_idx - 1], cover_sect)
    set_paragraph_section(paragraphs[chapter1_idx - 1], front_sect)

    if final_sect_pr is not None:
        body.remove(final_sect_pr)
    body.append(body_sect)


def apply_run_size(run: etree._Element, size: str | None) -> etree._Element:
    if not size:
        return run
    r_pr = run.find("w:rPr", namespaces=NS)
    if r_pr is None:
        r_pr = etree.Element(w("rPr"))
        run.insert(0, r_pr)
    for tag in ("sz", "szCs"):
        elem = r_pr.find(f"w:{tag}", namespaces=NS)
        if elem is None:
            elem = etree.SubElement(r_pr, w(tag))
        elem.set(w("val"), size)
    return run


def field_run(instr: str, fallback: str = "", size: str | None = None) -> list[etree._Element]:
    runs: list[etree._Element] = []
    begin = etree.Element(w("r"))
    apply_run_size(begin, size)
    begin_char = etree.SubElement(begin, w("fldChar"))
    begin_char.set(w("fldCharType"), "begin")
    runs.append(begin)

    instr_run = etree.Element(w("r"))
    apply_run_size(instr_run, size)
    instr_text = etree.SubElement(instr_run, w("instrText"))
    instr_text.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    instr_text.text = f" {instr} "
    runs.append(instr_run)

    separate = etree.Element(w("r"))
    apply_run_size(separate, size)
    separate_char = etree.SubElement(separate, w("fldChar"))
    separate_char.set(w("fldCharType"), "separate")
    runs.append(separate)

    if fallback:
        fallback_run = etree.Element(w("r"))
        apply_run_size(fallback_run, size)
        text = etree.SubElement(fallback_run, w("t"))
        text.text = fallback
        runs.append(fallback_run)

    end = etree.Element(w("r"))
    apply_run_size(end, size)
    end_char = etree.SubElement(end, w("fldChar"))
    end_char.set(w("fldCharType"), "end")
    runs.append(end)
    return runs


def text_run(text: str, size: str | None = None) -> etree._Element:
    run = etree.Element(w("r"))
    apply_run_size(run, size)
    t = etree.SubElement(run, w("t"))
    t.text = text
    return run


def table_borders_none(tbl_pr: etree._Element) -> None:
    borders = etree.SubElement(tbl_pr, w("tblBorders"))
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        edge = etree.SubElement(borders, w(side))
        edge.set(w("val"), "nil")


def cell(
    text_or_runs: str | list[etree._Element],
    width: str,
    align: str | None = None,
    size: str | None = None,
) -> etree._Element:
    tc = etree.Element(w("tc"))
    tc_pr = etree.SubElement(tc, w("tcPr"))
    tc_w = etree.SubElement(tc_pr, w("tcW"))
    tc_w.set(w("w"), width)
    tc_w.set(w("type"), "dxa")
    p = etree.SubElement(tc, w("p"))
    if align:
        p_pr = etree.SubElement(p, w("pPr"))
        jc = etree.SubElement(p_pr, w("jc"))
        jc.set(w("val"), align)
    if isinstance(text_or_runs, str):
        p.append(text_run(text_or_runs, size))
    else:
        for run in text_or_runs:
            p.append(run)
    return tc


def table_row(cells: list[etree._Element]) -> etree._Element:
    tr = etree.Element(w("tr"))
    for tc in cells:
        tr.append(tc)
    return tr


def simple_table(rows: list[list[etree._Element]], widths: list[str]) -> etree._Element:
    tbl = etree.Element(w("tbl"))
    tbl_pr = etree.SubElement(tbl, w("tblPr"))
    tbl_w = etree.SubElement(tbl_pr, w("tblW"))
    tbl_w.set(w("w"), "0")
    tbl_w.set(w("type"), "auto")
    table_borders_none(tbl_pr)
    grid = etree.SubElement(tbl, w("tblGrid"))
    for width in widths:
        col = etree.SubElement(grid, w("gridCol"))
        col.set(w("w"), width)
    for row in rows:
        tbl.append(table_row(row))
    return tbl


def make_header_xml() -> bytes:
    hdr = etree.Element(w("hdr"), nsmap={"w": W, "r": R})
    hdr.append(
        simple_table(
            [[
                cell(f"Project ID: {PROJECT_ID}", "5000", size=HEADER_FONT_SIZE),
                cell(field_run("PAGE", "i", HEADER_FONT_SIZE), "3000", "right"),
            ]],
            ["5000", "3000"],
        )
    )
    return xml_bytes(hdr)


def make_footer_xml() -> bytes:
    ftr = etree.Element(w("ftr"), nsmap={"w": W, "r": R})
    ftr.append(
        simple_table(
            [[
                cell(f"Prepared by: {STUDENT_NAME}", "4300", size=FOOTER_FONT_SIZE),
                cell(COURSE_CODE, "1700", "center", FOOTER_FONT_SIZE),
                cell(TERM, "2000", "right", FOOTER_FONT_SIZE),
            ]],
            ["4300", "1700", "2000"],
        )
    )
    return xml_bytes(ftr)


def patch_docx(input_path: Path, output_path: Path) -> None:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        with zipfile.ZipFile(input_path, "r") as zf:
            zf.extractall(tmp)

        document_path = tmp / "word" / "document.xml"
        styles_path = tmp / "word" / "styles.xml"
        settings_path = tmp / "word" / "settings.xml"
        header_path = tmp / "word" / "header1.xml"
        footer_path = tmp / "word" / "footer1.xml"

        document_root = parse_xml(document_path.read_bytes())
        apply_section_numbering(document_root)
        document_path.write_bytes(xml_bytes(document_root))

        styles_root = parse_xml(styles_path.read_bytes())
        remove_heading_style_numbering(styles_root)
        styles_path.write_bytes(xml_bytes(styles_root))

        settings_root = parse_xml(settings_path.read_bytes())
        ensure_update_fields(settings_root)
        settings_path.write_bytes(xml_bytes(settings_root))

        header_path.write_bytes(make_header_xml())
        footer_path.write_bytes(make_footer_xml())

        if output_path.exists():
            output_path.unlink()
        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
            for file_path in tmp.rglob("*"):
                if file_path.is_file():
                    zf.write(file_path, file_path.relative_to(tmp).as_posix())


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python fix-docx-format.py <input.docx> <output.docx>", file=sys.stderr)
        return 2
    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    if not input_path.exists():
        print(f"Input DOCX not found: {input_path}", file=sys.stderr)
        return 1
    tmp_output = output_path.with_suffix(".tmp.docx")
    patch_docx(input_path, tmp_output)
    shutil.move(str(tmp_output), str(output_path))
    print(f"Post-processed DOCX formatting: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
