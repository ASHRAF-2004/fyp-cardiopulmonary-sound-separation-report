from __future__ import annotations

import argparse
import csv
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path


YEAR_START = 2022
YEAR_END = 2026

QUERIES = [
    "cardiopulmonary sound separation",
    "heart lung sound separation",
    "heart and lung sound separation",
    '"chest sound separation" "deep learning"',
    "single-channel chest sound separation",
    "neonatal chest sound separation",
    "cardiorespiratory sound separation",
    "respiratory cardiac sound separation",
    '"stethoscope sound separation" "machine learning"',
    '"auscultation sound separation" "deep learning"',
    '"biomedical audio source separation" "deep learning"',
    '"U-Net" "heart sound" "lung sound" separation',
    '"transformer" "chest sound separation"',
    '"nonnegative matrix factorization" "heart lung sound separation"',
    '"variational mode decomposition" "heart lung sound separation"',
    "heart lung sound dataset",
    "cardiopulmonary sound dataset",
    '"digital stethoscope dataset" "heart lung"',
    '"source separation metrics" "biomedical audio"',
    '"respiratory sound separation" "cardiac sound"',
]


def request_json(url: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "FYP literature review metadata collector (mailto:student@example.com)",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=12) as response:
        data = response.read()
    return json.loads(data.decode("utf-8", errors="replace"))


def clean_text(value) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return " ".join(clean_text(v) for v in value if v)
    text = re.sub(r"<[^>]+>", " ", str(value))
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize_doi(doi: str) -> str:
    doi = clean_text(doi).strip()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi, flags=re.I)
    doi = doi.strip().strip(".")
    return doi.lower()


def normalize_title(title: str) -> str:
    title = clean_text(title).lower()
    title = re.sub(r"[^a-z0-9]+", " ", title)
    return re.sub(r"\s+", " ", title).strip()


def inverted_index_to_text(index: dict | None) -> str:
    if not index:
        return ""
    words = []
    for word, positions in index.items():
        for pos in positions:
            words.append((pos, word))
    return " ".join(word for _, word in sorted(words))


def year_from(value) -> int | None:
    if value is None:
        return None
    match = re.search(r"(20\d{2})", str(value))
    if match:
        return int(match.group(1))
    return None


def author_names(items, style: str) -> str:
    names: list[str] = []
    if style == "openalex":
        for item in items or []:
            name = item.get("author", {}).get("display_name")
            if name:
                names.append(name)
    elif style == "semantic":
        for item in items or []:
            name = item.get("name")
            if name:
                names.append(name)
    elif style == "crossref":
        for item in items or []:
            parts = [item.get("given", ""), item.get("family", "")]
            name = " ".join(p for p in parts if p).strip()
            if name:
                names.append(name)
    elif style == "pubmed":
        for item in items or []:
            if item:
                names.append(str(item))
    return "; ".join(names)


def add_candidate(candidates: dict, item: dict) -> None:
    title = clean_text(item.get("title"))
    if not title:
        return
    doi = normalize_doi(item.get("doi", ""))
    title_key = normalize_title(title)
    key = f"doi:{doi}" if doi else f"title:{title_key}"
    existing = candidates.get(key)
    if existing:
        sources = set(existing.get("sources", []))
        sources.update(item.get("sources", []))
        existing["sources"] = sorted(sources)
        if not existing.get("abstract") and item.get("abstract"):
            existing["abstract"] = item["abstract"]
        for field in ("pmid", "arxiv_id", "official_url", "venue", "authors"):
            if not existing.get(field) and item.get(field):
                existing[field] = item[field]
        existing["queries"] = sorted(set(existing.get("queries", [])) | set(item.get("queries", [])))
        return
    item["doi"] = doi
    item["title_key"] = title_key
    candidates[key] = item


def search_openalex(query: str, limit: int) -> list[dict]:
    params = {
        "search": query,
        "filter": f"from_publication_date:{YEAR_START}-01-01,to_publication_date:{YEAR_END}-12-31",
        "per-page": str(limit),
        "select": "id,doi,display_name,publication_year,authorships,primary_location,locations,abstract_inverted_index,type,cited_by_count,open_access",
    }
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    data = request_json(url)
    records = []
    for result in data.get("results", []):
        loc = result.get("primary_location") or {}
        source = loc.get("source") or {}
        doi = normalize_doi(result.get("doi", ""))
        records.append(
            {
                "title": result.get("display_name"),
                "authors": author_names(result.get("authorships"), "openalex"),
                "year": result.get("publication_year"),
                "doi": doi,
                "official_url": result.get("doi") or result.get("id"),
                "venue": source.get("display_name", ""),
                "publication_type": result.get("type", ""),
                "abstract": inverted_index_to_text(result.get("abstract_inverted_index")),
                "source_database": "OpenAlex",
                "source_record_id": result.get("id", ""),
                "is_oa": bool((result.get("open_access") or {}).get("is_oa")),
                "cited_by_count": result.get("cited_by_count", 0),
                "queries": [query],
                "sources": ["OpenAlex"],
            }
        )
    return records


def search_semantic_scholar(query: str, limit: int) -> list[dict]:
    fields = ",".join(
        [
            "paperId",
            "title",
            "year",
            "authors",
            "abstract",
            "venue",
            "publicationVenue",
            "publicationTypes",
            "externalIds",
            "url",
            "isOpenAccess",
            "citationCount",
        ]
    )
    params = {
        "query": query,
        "year": f"{YEAR_START}-{YEAR_END}",
        "limit": str(limit),
        "fields": fields,
    }
    url = "https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode(params)
    data = request_json(url)
    records = []
    for result in data.get("data", []):
        external = result.get("externalIds") or {}
        venue = result.get("venue") or ((result.get("publicationVenue") or {}).get("name", ""))
        records.append(
            {
                "title": result.get("title"),
                "authors": author_names(result.get("authors"), "semantic"),
                "year": result.get("year"),
                "doi": external.get("DOI", ""),
                "pmid": external.get("PubMed", ""),
                "arxiv_id": external.get("ArXiv", ""),
                "official_url": result.get("url", ""),
                "venue": venue,
                "publication_type": "; ".join(result.get("publicationTypes") or []),
                "abstract": result.get("abstract", ""),
                "source_database": "Semantic Scholar",
                "source_record_id": result.get("paperId", ""),
                "is_oa": bool(result.get("isOpenAccess")),
                "cited_by_count": result.get("citationCount", 0),
                "queries": [query],
                "sources": ["Semantic Scholar"],
            }
        )
    return records


def search_crossref(query: str, limit: int) -> list[dict]:
    params = {
        "query.bibliographic": query,
        "filter": f"from-pub-date:{YEAR_START}-01-01,until-pub-date:{YEAR_END}-12-31,type:journal-article",
        "rows": str(limit),
        "select": "DOI,title,author,published-print,published-online,issued,container-title,publisher,abstract,URL,type,is-referenced-by-count",
    }
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
    data = request_json(url)
    records = []
    for result in data.get("message", {}).get("items", []):
        issued = (
            result.get("published-print")
            or result.get("published-online")
            or result.get("issued")
            or {}
        )
        parts = issued.get("date-parts") or []
        year = parts[0][0] if parts and parts[0] else None
        records.append(
            {
                "title": clean_text((result.get("title") or [""])[0]),
                "authors": author_names(result.get("author"), "crossref"),
                "year": year,
                "doi": result.get("DOI", ""),
                "official_url": result.get("URL", ""),
                "venue": clean_text((result.get("container-title") or [""])[0]),
                "publisher": result.get("publisher", ""),
                "publication_type": result.get("type", ""),
                "abstract": result.get("abstract", ""),
                "source_database": "Crossref",
                "source_record_id": result.get("DOI", ""),
                "is_oa": False,
                "cited_by_count": result.get("is-referenced-by-count", 0),
                "queries": [query],
                "sources": ["Crossref"],
            }
        )
    return records


def search_arxiv(query: str, limit: int) -> list[dict]:
    search_query = f'all:"{query}" AND submittedDate:[{YEAR_START}01010000 TO {YEAR_END}12312359]'
    params = {
        "search_query": search_query,
        "start": "0",
        "max_results": str(limit),
        "sortBy": "relevance",
        "sortOrder": "descending",
    }
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "FYP literature review metadata collector"})
    with urllib.request.urlopen(req, timeout=12) as response:
        xml = response.read().decode("utf-8", errors="replace")
    entries = re.findall(r"<entry>(.*?)</entry>", xml, flags=re.S)
    records = []
    for entry in entries:
        title = clean_text(re.search(r"<title>(.*?)</title>", entry, flags=re.S).group(1)) if re.search(r"<title>(.*?)</title>", entry, flags=re.S) else ""
        summary = clean_text(re.search(r"<summary>(.*?)</summary>", entry, flags=re.S).group(1)) if re.search(r"<summary>(.*?)</summary>", entry, flags=re.S) else ""
        published = clean_text(re.search(r"<published>(.*?)</published>", entry, flags=re.S).group(1)) if re.search(r"<published>(.*?)</published>", entry, flags=re.S) else ""
        authors = "; ".join(clean_text(a) for a in re.findall(r"<author>\s*<name>(.*?)</name>\s*</author>", entry, flags=re.S))
        arxiv_url = clean_text(re.search(r"<id>(.*?)</id>", entry, flags=re.S).group(1)) if re.search(r"<id>(.*?)</id>", entry, flags=re.S) else ""
        arxiv_id = arxiv_url.rsplit("/", 1)[-1] if arxiv_url else ""
        doi_match = re.search(r"<arxiv:doi[^>]*>(.*?)</arxiv:doi>", entry, flags=re.S)
        records.append(
            {
                "title": title,
                "authors": authors,
                "year": year_from(published),
                "doi": clean_text(doi_match.group(1)) if doi_match else "",
                "arxiv_id": arxiv_id,
                "official_url": arxiv_url,
                "venue": "arXiv",
                "publication_type": "Preprint",
                "abstract": summary,
                "source_database": "arXiv",
                "source_record_id": arxiv_id,
                "is_oa": True,
                "cited_by_count": 0,
                "queries": [query],
                "sources": ["arXiv"],
            }
        )
    return records


def search_pubmed(query: str, limit: int) -> list[dict]:
    term = f'({query}) AND ("{YEAR_START}"[Date - Publication] : "{YEAR_END}"[Date - Publication])'
    params = {
        "db": "pubmed",
        "term": term,
        "retmode": "json",
        "retmax": str(limit),
        "sort": "relevance",
    }
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(params)
    data = request_json(url)
    ids = data.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    sum_params = {"db": "pubmed", "id": ",".join(ids), "retmode": "json"}
    sum_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + urllib.parse.urlencode(sum_params)
    summary = request_json(sum_url)
    records = []
    for pmid in ids:
        result = summary.get("result", {}).get(pmid, {})
        article_ids = {item.get("idtype"): item.get("value") for item in result.get("articleids", [])}
        records.append(
            {
                "title": result.get("title", ""),
                "authors": author_names([a.get("name", "") for a in result.get("authors", [])], "pubmed"),
                "year": year_from(result.get("pubdate", "")),
                "doi": article_ids.get("doi", ""),
                "pmid": pmid,
                "official_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                "venue": result.get("fulljournalname", result.get("source", "")),
                "publication_type": "; ".join(result.get("pubtype", [])),
                "abstract": "",
                "source_database": "PubMed",
                "source_record_id": pmid,
                "is_oa": "pmc" in article_ids,
                "cited_by_count": 0,
                "queries": [query],
                "sources": ["PubMed"],
            }
        )
    return records


def load_existing(root: Path) -> tuple[set[str], set[str], int]:
    path = root / "literature-review" / "metadata" / "papers_master.csv"
    dois: set[str] = set()
    titles: set[str] = set()
    max_id = 0
    with path.open(newline="", encoding="utf-8-sig") as handle:
        for row in csv.DictReader(handle):
            if row.get("doi"):
                dois.add(normalize_doi(row["doi"]))
            if row.get("title"):
                titles.add(normalize_title(row["title"]))
            match = re.match(r"P(\d+)", row.get("paper_id", ""))
            if match:
                max_id = max(max_id, int(match.group(1)))
    return dois, titles, max_id


def score_candidate(item: dict) -> dict:
    title = clean_text(item.get("title"))
    abstract = clean_text(item.get("abstract"))
    haystack = f"{title} {abstract} {item.get('venue', '')}".lower()
    score = 0
    reasons = []
    direct_terms = [
        "cardiopulmonary sound separation",
        "heart-lung sound separation",
        "heart lung sound separation",
        "heart and lung sound separation",
        "cardiorespiratory sound separation",
        "chest sound separation",
        "neonatal chest sound separation",
        "respiratory and cardiac sound separation",
        "respiratory cardiac sound separation",
    ]
    if any(term in haystack for term in direct_terms):
        score += 4
        reasons.append("direct heart/lung or chest sound separation")
    if "source separation" in haystack and any(t in haystack for t in ["heart", "lung", "respiratory", "cardiac", "auscultation", "stethoscope"]):
        score += 3
        reasons.append("biomedical source separation relevance")
    if any(t in haystack for t in ["dataset", "database", "corpus"]) and any(t in haystack for t in ["heart", "lung", "respiratory", "cardiopulmonary", "auscultation", "stethoscope"]):
        score += 2
        reasons.append("dataset relevance")
    if any(t in haystack for t in ["deep learning", "machine learning", "transformer", "u-net", "unet", "autoencoder", "vae", "neural", "nmf", "vmd", "singular spectrum"]):
        score += 1
        reasons.append("method/model relevance")
    if any(t in haystack for t in ["evaluation metric", "si-sdr", "sdr", "stoi", "pesq", "source-to-distortion"]):
        score += 1
        reasons.append("evaluation metric relevance")
    diagnosis_only = (
        any(t in haystack for t in ["classification", "diagnosis", "detection", "recognition"])
        and not any(t in haystack for t in ["separation", "separate", "source signal", "denoising", "enhancement", "dataset"])
    )
    if diagnosis_only:
        score -= 2
        reasons.append("appears diagnosis/classification focused")
    unrelated_audio = any(t in haystack for t in ["speech separation", "music source separation", "anechoic speech"]) and not any(
        t in haystack for t in ["biomedical", "heart", "lung", "respiratory", "cardiac", "auscultation", "stethoscope"]
    )
    if unrelated_audio:
        score -= 3
        reasons.append("general audio rather than biomedical")

    year = int(item.get("year") or 0)
    if year < YEAR_START or year > YEAR_END:
        decision = "Exclude"
        relevance = 1
        priority = "Priority 3"
        reason = "Outside publication year range or invalid year for Phase 7."
        useful_for = "not used"
    elif score >= 5:
        decision = "Include"
        relevance = 5
        priority = "Priority 1"
        reason = "Highly relevant metadata candidate: " + "; ".join(reasons[:3])
        useful_for = "related work; model; evaluation; research gap"
    elif score >= 3:
        decision = "Maybe"
        relevance = 4 if "separation" in haystack else 3
        priority = "Priority 2"
        reason = "Potentially useful Chapter 2 support: " + "; ".join(reasons[:3])
        useful_for = "background; preprocessing; model; evaluation; research gap"
    elif score >= 1:
        decision = "Maybe"
        relevance = 2
        priority = "Priority 3"
        reason = "Weak but possibly useful metadata-only background candidate: " + "; ".join(reasons[:3])
        useful_for = "background"
    else:
        decision = "Exclude"
        relevance = 1
        priority = "Priority 3"
        reason = "Weak relevance to cardiopulmonary sound separation."
        useful_for = "not used"

    if "dataset" in " ".join(reasons):
        useful_for = "dataset; methodology; evaluation dataset; research gap" if decision != "Exclude" else useful_for
    item.update(
        {
            "screen_score": score,
            "relevance_score": relevance,
            "initial_decision": decision,
            "download_priority": priority,
            "reason_for_decision": reason,
            "chapter_2_use": useful_for,
            "screening_reasons": reasons,
        }
    )
    return item


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--limit-per-source", type=int, default=12)
    parser.add_argument("--output", default="literature-review/metadata/phase7_candidate_search_raw.json")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    existing_dois, existing_titles, max_id = load_existing(root)
    candidates: dict[str, dict] = {}
    logs: list[dict] = []
    source_functions = [
        ("OpenAlex", search_openalex),
        ("Semantic Scholar", search_semantic_scholar),
        ("Crossref", search_crossref),
        ("PubMed", search_pubmed),
        ("arXiv", search_arxiv),
    ]

    for query in QUERIES:
        for source_name, function in source_functions:
            try:
                records = function(query, args.limit_per_source)
                status = "ok"
            except Exception as exc:  # noqa: BLE001
                records = []
                status = f"error: {type(exc).__name__}: {exc}"
            exported = 0
            for record in records:
                record["queries"] = sorted(set(record.get("queries", []) + [query]))
                add_candidate(candidates, record)
                exported += 1
            logs.append(
                {
                    "query": query,
                    "source": source_name,
                    "results_returned": len(records),
                    "records_exported": exported,
                    "status": status,
                }
            )
            time.sleep(0.25)

    screened: list[dict] = []
    duplicate_logs: list[dict] = []
    for item in candidates.values():
        doi = normalize_doi(item.get("doi", ""))
        title_key = normalize_title(item.get("title", ""))
        if doi and doi in existing_dois:
            duplicate_logs.append({"match_type": "doi", "title": item.get("title"), "doi": doi, "sources": item.get("sources")})
            continue
        if title_key and title_key in existing_titles:
            duplicate_logs.append({"match_type": "title", "title": item.get("title"), "doi": doi, "sources": item.get("sources")})
            continue
        year = int(item.get("year") or 0)
        if year < YEAR_START or year > YEAR_END:
            continue
        item = score_candidate(item)
        if item["initial_decision"] == "Exclude":
            continue
        if item["relevance_score"] < 2:
            continue
        screened.append(item)

    screened.sort(
        key=lambda r: (
            r["initial_decision"] == "Include",
            r["relevance_score"],
            r.get("screen_score", 0),
            r.get("cited_by_count", 0),
            bool(r.get("doi")),
        ),
        reverse=True,
    )
    selected = screened[:35]
    for index, item in enumerate(selected, start=max_id + 1):
        item["paper_id"] = f"P{index:03d}"

    output = {
        "year_start": YEAR_START,
        "year_end": YEAR_END,
        "queries": QUERIES,
        "logs": logs,
        "duplicates_skipped": duplicate_logs,
        "candidate_count_after_dedup": len(candidates),
        "screened_useful_count": len(screened),
        "selected_count": len(selected),
        "selected": selected,
    }
    out_path = root / args.output
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"selected_count": len(selected), "screened_useful_count": len(screened), "output": str(out_path)}, indent=2))


if __name__ == "__main__":
    main()
