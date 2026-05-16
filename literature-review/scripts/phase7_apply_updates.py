from __future__ import annotations

import csv
import json
import re
import textwrap
import urllib.parse
import urllib.request
from collections import Counter
from copy import deepcopy
from datetime import date
from pathlib import Path


TODAY = date.today().isoformat()
YEAR_ELIGIBILITY = "Eligible: 2022-2026"


CURATED = [
    {
        "match": "10.5005/jp-journals-11002-0068",
        "decision": "Maybe",
        "relevance": 3,
        "priority": "2",
        "utility": "Background support",
        "useful_for": "background; software/prototype; research gap",
        "reason": "Recent systematic review on digital stethoscope use in neonates; useful for clinical/software context but not a separation method.",
        "method": "Systematic review of neonatal digital stethoscope use.",
        "dataset": "Neonatal digital stethoscope literature; no separation dataset identified from metadata.",
        "metrics": "Review-level outcomes; not a source-separation metric paper.",
        "contribution": "Supports background on neonatal digital stethoscope workflows and adoption constraints.",
        "limitation": "Not a cardiopulmonary source-separation study.",
        "chapter": "background; software/prototype; research gap",
    },
    {
        "match": "10.1186/s40779-023-00479-3",
        "decision": "Maybe",
        "relevance": 3,
        "priority": "2",
        "utility": "Background support",
        "useful_for": "background; preprocessing; model; research gap",
        "reason": "Relevant lung sound deep learning/intelligent stethoscope background; useful for preprocessing and model context but not heart-lung separation.",
        "method": "Deep learning-based lung sound analysis for intelligent stethoscope applications.",
        "dataset": "Lung sound data discussed in paper metadata.",
        "metrics": "Classification/analysis metrics rather than separation metrics.",
        "contribution": "Provides recent lung-sound ML context for digital stethoscope systems.",
        "limitation": "Lung-sound analysis focus; no heart/lung source separation output.",
        "chapter": "background; preprocessing; model; research gap",
    },
    {
        "match": "10.1109/icsps66615.2025.11347745",
        "decision": "Include",
        "relevance": 5,
        "priority": "1",
        "utility": "Directly useful",
        "useful_for": "related work; preprocessing; model; evaluation; research gap",
        "reason": "Direct cardiorespiratory sound separation paper using singular spectrum analysis on electronic stethoscope recordings.",
        "method": "Multi-stage Singular Spectrum Analysis framework for cardiac and respiratory sound separation.",
        "dataset": "Real-world cardiorespiratory recordings from electronic digital stethoscopes according to metadata.",
        "metrics": "Metadata indicates validation on real-world recordings; exact metrics require full-text audit.",
        "contribution": "Adds a recent non-deep-learning direct separation method for comparison against NMF/VMD/deep models.",
        "limitation": "Full text not locally audited yet; metadata-only screening.",
        "chapter": "related work; preprocessing; model; evaluation; research gap",
    },
    {
        "match": "10.3390/s23125750",
        "decision": "Maybe",
        "relevance": 3,
        "priority": "2",
        "utility": "System/prototype support",
        "useful_for": "background; software/prototype; dataset; research gap",
        "reason": "Digital auscultation platform for pediatrics; useful for software/prototype and data acquisition context.",
        "method": "Digital auscultation platform and pediatric workflow support.",
        "dataset": "Pediatric auscultation platform data; public dataset status requires full-text check.",
        "metrics": "Platform evaluation metrics; not separation metrics.",
        "contribution": "Supports FYP discussion of usable biomedical audio collection/prototype workflows.",
        "limitation": "Platform paper rather than separation algorithm.",
        "chapter": "background; dataset; software/prototype; research gap",
    },
    {
        "match": "10.36001/phmap.2023.v4i1.3604",
        "decision": "Maybe",
        "relevance": 3,
        "priority": "2",
        "utility": "Dataset support",
        "useful_for": "dataset; evaluation; background; research gap",
        "reason": "Respiratory illness sound dataset and baseline AI system; useful as dataset/evaluation background.",
        "method": "Respiratory sound dataset with baseline AI system.",
        "dataset": "Sound-Dr respiratory illness sound dataset.",
        "metrics": "Baseline AI system metrics; exact details require full-text audit.",
        "contribution": "Adds a respiratory audio dataset reference for Chapter 2 dataset limitations and evaluation context.",
        "limitation": "Respiratory illness focus; not heart-lung source separation.",
        "chapter": "dataset; evaluation; background; research gap",
        "dataset_inventory": {
            "dataset_id": "Sound-Dr",
            "dataset_name": "Sound-Dr respiratory illness sound dataset",
            "dataset_doi": "",
            "data_type": "Respiratory sound audio dataset",
            "contains_heart_sounds": "No",
            "contains_lung_sounds": "Yes",
            "contains_mixed_sounds": "No",
            "contains_source_signals": "No",
            "possible_use_in_fyp": "Background/evaluation context for respiratory sound datasets; not a primary separation training set.",
            "access_status": "Metadata recorded; access requires manual verification.",
        },
    },
    {
        "match": "10.1109/embc58623.2025.11253482",
        "decision": "Maybe",
        "relevance": 4,
        "priority": "2",
        "utility": "Preprocessing/evaluation support",
        "useful_for": "preprocessing; model; evaluation; software/prototype",
        "reason": "CNN-based reconstruction of acoustic cardiopulmonary signals is relevant to preprocessing and system implementation, although not direct separation.",
        "method": "Compressed sensing and CNN-based reconstruction for acoustic cardiopulmonary signals.",
        "dataset": "Acoustic cardiopulmonary signals; dataset availability requires full-text audit.",
        "metrics": "Reconstruction quality metrics expected; exact metrics require full-text audit.",
        "contribution": "Useful for signal acquisition/reconstruction issues in a software prototype.",
        "limitation": "Reconstruction paper, not heart/lung source separation.",
        "chapter": "preprocessing; model; evaluation; software/prototype",
    },
    {
        "match": "10.1109/access.2022.3144355",
        "decision": "Maybe",
        "relevance": 4,
        "priority": "2",
        "utility": "Evaluation support",
        "useful_for": "evaluation; preprocessing; dataset; software/prototype",
        "reason": "Neonatal heart/lung sound quality assessment is useful for quality control and evaluation before/after separation.",
        "method": "Real-time multi-level neonatal heart and lung sound quality assessment.",
        "dataset": "Neonatal heart and lung sound recordings; public status requires manual verification.",
        "metrics": "Sound quality assessment metrics and telehealth validation.",
        "contribution": "Supports Chapter 2 discussion on input quality and quality-aware evaluation.",
        "limitation": "Quality assessment rather than separation.",
        "chapter": "evaluation; preprocessing; dataset; software/prototype",
    },
    {
        "match": "10.18280/ts.410521",
        "decision": "Maybe",
        "relevance": 3,
        "priority": "2",
        "utility": "System/prototype support",
        "useful_for": "software/prototype; model; background",
        "reason": "Digital stethoscope plus TinyML/CNN system paper; useful for embedded/prototype discussion.",
        "method": "CNN-based organ sound analysis on embedded/TinyML digital stethoscope hardware.",
        "dataset": "Organ sound data; details require full-text audit.",
        "metrics": "Embedded classification/system metrics; not separation metrics.",
        "contribution": "Useful for explaining feasible biomedical audio software/system design constraints.",
        "limitation": "Organ sound analysis/classification rather than separation.",
        "chapter": "software/prototype; model; background",
    },
    {
        "match": "10.1063/5.0071316",
        "decision": "Maybe",
        "relevance": 3,
        "priority": "2",
        "utility": "Preprocessing support",
        "useful_for": "preprocessing; feature extraction; evaluation",
        "reason": "VMD and multi-wavelet anti-noise segmentation for wearable heart sound acquisition is useful preprocessing background.",
        "method": "Variational mode decomposition and multi-wavelet anti-noise segmentation.",
        "dataset": "Wearable heart sound acquisition data.",
        "metrics": "Segmentation/noise robustness metrics; exact metrics require full-text audit.",
        "contribution": "Adds VMD/wavelet preprocessing evidence relevant to noisy auscultation signals.",
        "limitation": "Heart sound acquisition/segmentation only; no lung source output.",
        "chapter": "preprocessing; feature extraction; evaluation",
    },
    {
        "match": "10.1371/journal.pdig.0000324",
        "decision": "Maybe",
        "relevance": 4,
        "priority": "2",
        "utility": "Dataset/evaluation support",
        "useful_for": "dataset; evaluation; background; research gap",
        "reason": "PhysioNet Challenge 2022 paper documents a large pediatric PCG dataset and challenge scoring, useful for dataset/evaluation context.",
        "method": "Open challenge and benchmark for heart murmur detection from PCG recordings.",
        "dataset": "George B. Moody PhysioNet Challenge 2022 / CirCor DigiScope pediatric PCG data.",
        "metrics": "Challenge scoring function; murmur/outcome metrics.",
        "contribution": "Useful open dataset/evaluation benchmark for heart sound analysis, even though not separation.",
        "limitation": "Heart murmur detection focus rather than heart-lung separation.",
        "chapter": "dataset; evaluation; background; research gap",
        "dataset_inventory": {
            "dataset_id": "PhysioNet-Challenge-2022",
            "dataset_name": "Heart Murmur Detection from Phonocardiogram Recordings: The George B. Moody PhysioNet Challenge 2022",
            "dataset_doi": "10.13026/t49p-5v35",
            "data_type": "Pediatric phonocardiogram WAV recordings with demographic and murmur/outcome labels",
            "contains_heart_sounds": "Yes",
            "contains_lung_sounds": "No",
            "contains_mixed_sounds": "No",
            "contains_source_signals": "No",
            "possible_use_in_fyp": "Evaluation/background dataset for PCG preprocessing and benchmarking; not suitable as a direct heart-lung separation paired-source dataset.",
            "access_status": "Open PhysioNet dataset; manual dataset download only if later needed.",
        },
    },
    {
        "match": "10.1016/j.engappai.2025.112286",
        "decision": "Maybe",
        "relevance": 4,
        "priority": "2",
        "utility": "Preprocessing support",
        "useful_for": "preprocessing; model; evaluation",
        "reason": "Recent robust PCG denoising model explicitly treats lung sounds and clinical noise as contaminants; useful preprocessing evidence.",
        "method": "Transformer-BiLSTM/deep denoising model for PCG signals in clinical noise.",
        "dataset": "Multiple PCG datasets according to metadata.",
        "metrics": "Denoising performance metrics; exact values require full-text audit.",
        "contribution": "Supports denoising/preprocessing choices before cardiopulmonary separation.",
        "limitation": "Heart sound denoising, not dual-source heart/lung separation.",
        "chapter": "preprocessing; model; evaluation",
    },
    {
        "match": "10.1016/j.bspc.2025.108818",
        "decision": "Maybe",
        "relevance": 4,
        "priority": "2",
        "utility": "Preprocessing support",
        "useful_for": "preprocessing; model; evaluation",
        "reason": "Self-attention lung sound denoising model is useful for noisy respiratory audio preprocessing.",
        "method": "Uformer-style CNN/Transformer encoder-decoder lung sound denoiser.",
        "dataset": "Noisy lung sound data; details require full-text audit.",
        "metrics": "Denoising and real-time performance metrics expected.",
        "contribution": "Adds recent transformer-based lung sound denoising evidence.",
        "limitation": "Lung denoising only; no cardiac source output.",
        "chapter": "preprocessing; model; evaluation",
    },
    {
        "match": "10.1016/j.bspc.2025.108232",
        "decision": "Maybe",
        "relevance": 4,
        "priority": "2",
        "utility": "Preprocessing support",
        "useful_for": "preprocessing; feature extraction; model; evaluation",
        "reason": "UNet-based adaptive DWT thresholding for respiratory sound denoising supports wavelet/UNet preprocessing discussion.",
        "method": "Adaptive DWT coefficient thresholding using UNet.",
        "dataset": "Real-life respiratory sounds with noisy normal/abnormal cases according to metadata.",
        "metrics": "SNR and downstream classification impact according to metadata.",
        "contribution": "Useful for multiscale denoising and representation choices.",
        "limitation": "Respiratory denoising rather than heart-lung separation.",
        "chapter": "preprocessing; feature extraction; model; evaluation",
    },
    {
        "match": "10.1016/j.bspc.2021.103329",
        "decision": "Maybe",
        "relevance": 3,
        "priority": "2",
        "utility": "Preprocessing support",
        "useful_for": "preprocessing; feature extraction; evaluation",
        "reason": "DWT-ANN lung sound denoising is useful as classical/ML preprocessing background and is published in 2022.",
        "method": "Discrete wavelet transform and artificial neural network lung sound denoising.",
        "dataset": "Lung sound signals; exact dataset requires full-text audit.",
        "metrics": "Signal quality criteria for denoising.",
        "contribution": "Supports wavelet and neural denoising discussion for lung sounds.",
        "limitation": "Not a heart-lung separation paper.",
        "chapter": "preprocessing; feature extraction; evaluation",
    },
    {
        "match": "10.1109/healthcom60970.2024.10880716",
        "decision": "Maybe",
        "relevance": 3,
        "priority": "2",
        "utility": "Preprocessing support",
        "useful_for": "preprocessing; model; evaluation",
        "reason": "Transfer-learning heart sound denoising paper; useful as preprocessing background.",
        "method": "Transfer learning approach for heart sound denoising.",
        "dataset": "Heart sound data; dataset details require full-text audit.",
        "metrics": "Denoising quality metrics require full-text audit.",
        "contribution": "Adds transfer-learning denoising evidence for noisy PCG signals.",
        "limitation": "Heart sound denoising/classification support rather than heart-lung separation.",
        "chapter": "preprocessing; model; evaluation",
    },
    {
        "match": "10.1016/j.bspc.2024.106315",
        "decision": "Maybe",
        "relevance": 3,
        "priority": "2",
        "utility": "Preprocessing/evaluation support",
        "useful_for": "preprocessing; evaluation; dataset",
        "reason": "Breathing phase identification on lung sound recordings is useful for segmentation and evaluation context.",
        "method": "Second-derivative based breathing phase identification from lung sounds.",
        "dataset": "Large heterogeneous real lung sound dataset according to metadata.",
        "metrics": "Sensitivity, positive predictive value, and F1-score according to metadata.",
        "contribution": "Supports segmentation/preprocessing issues in respiratory audio.",
        "limitation": "Respiratory phase segmentation, not source separation.",
        "chapter": "preprocessing; evaluation; dataset",
    },
    {
        "match": "10.3233/ica-220686",
        "decision": "Exclude",
        "relevance": 1,
        "priority": "3",
        "utility": "Not used",
        "useful_for": "not used",
        "reason": "Metadata appears too broad/general biomedical audio-HPC; weak connection to heart-lung sound separation.",
        "exclusion": "E14",
        "method": "High-performance computing system for biomedical audio signal processing.",
        "dataset": "Unclear from metadata.",
        "metrics": "Unclear from metadata.",
        "contribution": "Potential software background only.",
        "limitation": "Too broad for Chapter 2 priority set.",
        "chapter": "not used",
    },
    {
        "match": "10.3390/diagnostics13172772",
        "decision": "Exclude",
        "relevance": 1,
        "priority": "3",
        "utility": "Not used",
        "useful_for": "not used",
        "reason": "Deep learning chest disease classification using X-rays/CT/cough images; not cardiopulmonary sound separation.",
        "exclusion": "E08",
        "method": "Disease classification using images/cough sound images.",
        "dataset": "X-ray, CT, and cough image datasets.",
        "metrics": "Classification metrics.",
        "contribution": "Not used.",
        "limitation": "Non-target modalities and diagnosis focus.",
        "chapter": "not used",
    },
    {
        "match": "10.3390/diagnostics13101748",
        "decision": "Exclude",
        "relevance": 1,
        "priority": "3",
        "utility": "Not used",
        "useful_for": "not used",
        "reason": "Lung disease diagnosis overview; useful generally but not needed because stronger respiratory audio background papers are already selected.",
        "exclusion": "E03",
        "method": "Review of acoustic lung disease diagnosis architectures.",
        "dataset": "Respiratory disease datasets.",
        "metrics": "Classification metrics.",
        "contribution": "Not prioritized.",
        "limitation": "Diagnosis-only review; no separation method.",
        "chapter": "not used",
    },
    {
        "match": "10.3390/bioengineering11060586",
        "decision": "Exclude",
        "relevance": 1,
        "priority": "3",
        "utility": "Not used",
        "useful_for": "not used",
        "reason": "Pulmonary disease detection paper; classification focus without clear separation/dataset gap contribution.",
        "exclusion": "E03",
        "method": "Parallel transformation and deep learning for pulmonary disease detection.",
        "dataset": "Pulmonary disease auscultation data.",
        "metrics": "Classification metrics.",
        "contribution": "Not prioritized.",
        "limitation": "Diagnosis-only, no source separation.",
        "chapter": "not used",
    },
    {
        "match": "10.1109/jtehm.2024.3433448",
        "decision": "Exclude",
        "relevance": 1,
        "priority": "3",
        "utility": "Not used",
        "useful_for": "not used",
        "reason": "Cardiopulmonary resuscitation training system; sound recognition context is not relevant to heart/lung auscultation separation.",
        "exclusion": "E10",
        "method": "Sound recognition-based CPR training system.",
        "dataset": "CPR training sounds.",
        "metrics": "Training system recognition metrics.",
        "contribution": "Not used.",
        "limitation": "Outside FYP scope.",
        "chapter": "not used",
    },
    {
        "match": "10.11591/ijai.v15.i2.pp1746-1761",
        "decision": "Exclude",
        "relevance": 1,
        "priority": "3",
        "utility": "Not used",
        "useful_for": "not used",
        "reason": "Cardiovascular disease classification from auscultation sounds; diagnosis-only and not separation-focused.",
        "exclusion": "E03",
        "method": "Deep learning classification of cardiovascular disease via auscultation sounds.",
        "dataset": "Heart auscultation sounds.",
        "metrics": "Classification metrics.",
        "contribution": "Not used.",
        "limitation": "Disease classification only.",
        "chapter": "not used",
    },
    {
        "match": "10.1109/aicas57966.2023.10168624",
        "decision": "Exclude",
        "relevance": 1,
        "priority": "3",
        "utility": "Not used",
        "useful_for": "not used",
        "reason": "Adventitious cardiopulmonary sound classification; not a source separation or preprocessing method needed for the FYP.",
        "exclusion": "E12",
        "method": "MMoE with STFT/MFCC spectrograms for classification.",
        "dataset": "Cardiopulmonary classification dataset.",
        "metrics": "Classification metrics.",
        "contribution": "Not prioritized.",
        "limitation": "Classification-only.",
        "chapter": "not used",
    },
    {
        "match": "10.1109/access.2023.3344813",
        "decision": "Exclude",
        "relevance": 1,
        "priority": "3",
        "utility": "Not used",
        "useful_for": "not used",
        "reason": "General audio enhancement survey; broad scope and not specific enough to biomedical heart/lung separation.",
        "exclusion": "E13",
        "method": "Survey of audio enhancement by image U-Net.",
        "dataset": "General audio domains.",
        "metrics": "General enhancement metrics.",
        "contribution": "Not used.",
        "limitation": "General audio only.",
        "chapter": "not used",
    },
    {
        "match": "10.1007/s11227-024-06411-3",
        "decision": "Exclude",
        "relevance": 1,
        "priority": "3",
        "utility": "Not used",
        "useful_for": "not used",
        "reason": "Respiratory-rate estimation with NMF is adjacent but not useful enough for heart/lung separation Chapter 2.",
        "exclusion": "E14",
        "method": "Noise-tolerant NMF for respiratory rate estimation.",
        "dataset": "Respiratory signal data.",
        "metrics": "Respiratory rate estimation metrics.",
        "contribution": "Not prioritized.",
        "limitation": "Estimation task rather than separation.",
        "chapter": "not used",
    },
    {
        "match": "10.1038/s44325-024-00027-5",
        "decision": "Exclude",
        "relevance": 1,
        "priority": "3",
        "utility": "Not used",
        "useful_for": "not used",
        "reason": "Foundation model paper for cardiovascular disease detection via digital stethoscope biosignals; diagnosis focus and includes ECG/PCG rather than separation.",
        "exclusion": "E03",
        "method": "Foundation models for digital stethoscope biosignals.",
        "dataset": "Digital stethoscope PCG/ECG clinical data.",
        "metrics": "Disease detection metrics.",
        "contribution": "Not used.",
        "limitation": "Diagnosis-only and multimodal ECG/PCG scope.",
        "chapter": "not used",
    },
]


def clean_text(value) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return " ".join(clean_text(v) for v in value if v)
    text = re.sub(r"<[^>]+>", " ", str(value))
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize_doi(doi: str) -> str:
    doi = clean_text(doi)
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi, flags=re.I)
    return doi.strip().strip(".").lower()


def normalize_title(title: str) -> str:
    title = clean_text(title).lower()
    title = re.sub(r"[^a-z0-9]+", " ", title)
    return re.sub(r"\s+", " ", title).strip()


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def request_crossref(doi: str) -> dict:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    req = urllib.request.Request(url, headers={"User-Agent": "FYP Phase 7 metadata updater"})
    with urllib.request.urlopen(req, timeout=15) as response:
        return json.loads(response.read().decode("utf-8", errors="replace")).get("message", {})


def crossref_to_record(message: dict) -> dict:
    title = clean_text((message.get("title") or [""])[0])
    authors = []
    for author in message.get("author", []) or []:
        name = " ".join(part for part in [author.get("given", ""), author.get("family", "")] if part).strip()
        if name:
            authors.append(name)
    issued = message.get("published-print") or message.get("published-online") or message.get("issued") or {}
    parts = issued.get("date-parts") or []
    year = str(parts[0][0]) if parts and parts[0] else ""
    venue = clean_text((message.get("container-title") or [""])[0])
    publisher = clean_text(message.get("publisher", ""))
    return {
        "title": title,
        "authors": "; ".join(authors),
        "year": year,
        "doi": message.get("DOI", ""),
        "official_url": message.get("URL", ""),
        "venue": venue or publisher,
        "publisher": publisher,
        "publication_type": message.get("type", ""),
        "abstract": clean_text(message.get("abstract", "")),
        "source_database": "Crossref",
        "source_record_id": message.get("DOI", ""),
    }


def make_summary(text: str, fallback: str) -> str:
    text = clean_text(text) or fallback
    if len(text) <= 420:
        return text
    return textwrap.shorten(text, width=420, placeholder="...")


def citation_key(authors: str, year: str, title: str, used: set[str]) -> str:
    first = "paper"
    if authors:
        first_author = authors.split(";")[0].strip()
        first = re.sub(r"[^A-Za-z]", "", first_author.split()[-1]).lower() or "paper"
    word = "phase7"
    stop = {"the", "and", "for", "with", "using", "based", "from", "sound", "sounds", "heart", "lung"}
    for candidate in re.findall(r"[A-Za-z0-9]+", title):
        if candidate.lower() not in stop and len(candidate) > 3:
            word = candidate.lower()
            break
    base = f"{first}{year}{word}"
    key = base
    suffix = 2
    while key in used:
        key = f"{base}{suffix}"
        suffix += 1
    used.add(key)
    return key


def bibtex_authors(authors: str) -> str:
    return " and ".join(a.strip() for a in authors.split(";") if a.strip())


def apa_authors(authors: str) -> str:
    return ", ".join(a.strip() for a in authors.split(";") if a.strip())


def escape_bib(value: str) -> str:
    return clean_text(value).replace("{", "").replace("}", "")


def build_bib_entry(row: dict[str, str]) -> str:
    entry_type = "inproceedings" if "conference" in row["publication_type"].lower() or "proceeding" in row["publication_type"].lower() else "article"
    fields = {
        "author": bibtex_authors(row["authors"]),
        "title": row["title"],
        "journal": row["venue_source"],
        "year": row["year"],
        "doi": row["doi"],
        "url": row["official_url"] or row["url"],
        "note": f"Phase 7 metadata-only candidate. Decision: {row['decision']}. Relevance score: {row['relevance_score']}/5. Chapter 2 use: {row['chapter_2_use']}.",
    }
    lines = [f"@{entry_type}{{{row['bibtex_key']},"]
    for key, value in fields.items():
        if value:
            lines.append(f"  {key} = {{{escape_bib(value)}}},")
    lines[-1] = lines[-1].rstrip(",")
    lines.append("}")
    return "\n".join(lines)


def main() -> None:
    root = Path(".").resolve()
    meta = root / "literature-review" / "metadata"
    screening = root / "literature-review" / "screening"
    refs = root / "literature-review" / "references"
    prisma = root / "literature-review" / "prisma" / "prisma_counts.json"
    outline_path = root / "literature-review" / "notes" / "chapter_2_outline.md"

    raw_path = meta / "phase7_candidate_search_raw.json"
    raw_data = json.loads(raw_path.read_text(encoding="utf-8"))
    raw_by_doi = {normalize_doi(item.get("doi", "")): item for item in raw_data.get("selected", []) if item.get("doi")}

    papers_fields, papers_rows = read_csv(meta / "papers_master.csv")
    queue_fields, queue_rows = read_csv(meta / "download_queue.csv")
    title_fields, title_rows = read_csv(screening / "title_abstract_screening.csv")
    extraction_fields, extraction_rows = read_csv(screening / "extraction_matrix.csv")
    dataset_fields, dataset_rows = read_csv(meta / "dataset_inventory.csv")
    duplicate_fields, duplicate_rows = read_csv(meta / "duplicate_check.csv")
    search_fields, search_rows = read_csv(meta / "search_log.csv")

    existing_dois = {normalize_doi(r.get("doi", "")): r for r in papers_rows if r.get("doi")}
    existing_titles = {normalize_title(r.get("title", "")): r for r in papers_rows if r.get("title")}
    max_pid = max(int(r["paper_id"][1:]) for r in papers_rows if re.match(r"P\d+", r.get("paper_id", "")))
    max_dup = max(int(r["duplicate_group_id"][1:]) for r in duplicate_rows if re.match(r"D\d+", r.get("duplicate_group_id", "")))
    used_keys = set()
    for match in re.finditer(r"@\w+\{([^,]+),", (refs / "references.bib").read_text(encoding="utf-8")):
        used_keys.add(match.group(1))

    additions: list[dict[str, str]] = []
    skipped: list[tuple[dict, str, str]] = []
    for item in CURATED:
        doi_norm = normalize_doi(item["match"])
        raw = deepcopy(raw_by_doi.get(doi_norm, {}))
        enriched = {}
        try:
            enriched = crossref_to_record(request_crossref(item["match"]))
        except Exception:
            enriched = {}
        record = {**raw, **{k: v for k, v in enriched.items() if v}}
        record["doi"] = item["match"]
        title = clean_text(record.get("title", ""))
        if doi_norm in existing_dois:
            skipped.append((item, "doi", existing_dois[doi_norm]["paper_id"]))
            continue
        if normalize_title(title) in existing_titles:
            skipped.append((item, "title", existing_titles[normalize_title(title)]["paper_id"]))
            continue
        max_pid += 1
        paper_id = f"P{max_pid:03d}"
        year = str(record.get("year") or "")
        authors = clean_text(record.get("authors", ""))
        venue = clean_text(record.get("venue", ""))
        doi = item["match"]
        url = f"https://doi.org/{doi}" if doi else clean_text(record.get("official_url", ""))
        official_url = clean_text(record.get("official_url", "")) or url
        source_database = clean_text(record.get("source_database", "")) or "Crossref"
        raw_sources = record.get("sources") or []
        if raw_sources:
            source_database = "; ".join(sorted(set(raw_sources + ["Crossref"])))
        abstract = clean_text(record.get("abstract", ""))
        summary = make_summary(abstract, item["contribution"])
        bib_key = citation_key(authors, year, title, used_keys)
        decision = item["decision"]
        exclusion = item.get("exclusion", "") if decision == "Exclude" else ""
        access_type = "Open Access" if any(s in official_url.lower() for s in ["plos", "mdpi", "frontiers", "nature.com/articles", "physionet"]) else "Metadata Only"
        if decision == "Exclude":
            download_status = "Not downloaded"
            zotero_status = "Do not download - excluded"
        else:
            download_status = "Not downloaded"
            zotero_status = "Pending"
        note = (
            f"Phase 7 metadata-only candidate added {TODAY}. No PDF downloaded, no login attempted. "
            f"Search sources: {source_database}. Decision based on title/abstract metadata only."
        )
        paper_row = {
            "paper_id": paper_id,
            "record_source": "phase7_metadata_search",
            "source_database": source_database,
            "source_record_id": clean_text(record.get("source_record_id", "")) or doi,
            "file_name": "",
            "title": title,
            "authors": authors,
            "year": year,
            "publication_type": clean_text(record.get("publication_type", "")) or "Journal/conference metadata record",
            "venue_source": venue,
            "doi": doi,
            "url": url,
            "official_url": official_url,
            "abstract_summary": summary,
            "abstract": abstract or summary,
            "keywords": "",
            "keywords_used": "; ".join(record.get("queries", [])) if isinstance(record.get("queries"), list) else "",
            "method_model": item["method"],
            "dataset_used": item["dataset"],
            "evaluation_metrics": item["metrics"],
            "key_contribution": item["contribution"],
            "limitation": item["limitation"],
            "relevance_score": str(item["relevance"]),
            "decision": decision,
            "reason_for_decision": item["reason"],
            "exclusion_reason_id": exclusion,
            "access_type": access_type,
            "download_status": download_status,
            "zotero_status": zotero_status,
            "local_pdf_path": "",
            "zotero_key": "",
            "bibtex_key": bib_key,
            "duplicate_group_id": "",
            "screening_status": "metadata_screened",
            "notes": note,
            "last_updated": TODAY,
            "utility_level": item["utility"],
            "download_priority": item["priority"],
            "useful_for": item["useful_for"],
            "phase4_verification_reason": "",
            "year_eligibility": YEAR_ELIGIBILITY,
            "previous_decision_before_year_rule": "",
            "manual_access_status": "",
            "preprocessing_method": item["method"] if "preprocessing" in item["chapter"] else "",
            "feature_extraction_method": item["method"] if "feature" in item["chapter"] else "",
            "chapter_2_use": item["chapter"],
            "phase6_pdf_audit_status": "",
        }
        additions.append(paper_row)

        queue_rows.append(
            {
                "paper_id": paper_id,
                "title": title,
                "authors": authors,
                "year": year,
                "doi": doi,
                "official_url": official_url,
                "source_database": source_database,
                "access_type": access_type,
                "download_status": download_status,
                "zotero_status": zotero_status,
                "priority": item["priority"],
                "reason": item["reason"],
                "notes": note,
                "date_added": TODAY,
                "utility_level": item["utility"],
                "useful_for": item["useful_for"],
                "phase4_decision": decision,
                "year_eligibility": YEAR_ELIGIBILITY,
                "previous_priority_before_year_rule": "",
                "manual_access_status": "",
                "pdf_filename": "",
                "phase6_decision": "",
                "phase6_relevance_score": "",
                "phase6_chapter_2_use": "",
            }
        )
        title_rows.append(
            {
                "paper_id": paper_id,
                "title": title,
                "publication_year": year,
                "abstract_available": "Yes" if abstract or summary else "No",
                "scope_ml_sound_separation": "Yes" if decision != "Exclude" and ("model" in item["chapter"] or "separation" in item["reason"].lower()) else "No",
                "heart_lung_or_cardiopulmonary_focus": "Yes" if any(t in (title + item["reason"]).lower() for t in ["heart", "lung", "cardio", "respiratory", "auscultation", "stethoscope"]) else "No",
                "public_dataset_mentioned": "Yes" if "dataset" in item["chapter"] or item.get("dataset_inventory") else "No",
                "python_or_reproducible_method_mentioned": "Unclear",
                "disease_detection_only": "Yes" if exclusion in {"E03", "E12"} else "No",
                "include_title_abstract": "Yes" if decision != "Exclude" else "No",
                "exclusion_reason_id": exclusion,
                "screened_by": "Codex Phase 7 metadata collection",
                "screened_date": TODAY,
                "notes": note,
                "utility_level": item["utility"],
                "download_priority": item["priority"],
                "useful_for": item["useful_for"],
                "reason_for_decision": item["reason"],
                "year_eligibility": YEAR_ELIGIBILITY,
                "previous_title_abstract_decision_before_year_rule": "",
            }
        )
        apa = (
            f"{apa_authors(authors)}. ({year}). {title}. "
            f"{('*' + venue + '*') if venue else ''}. https://doi.org/{doi} "
            f"Decision: {decision}; relevance {item['relevance']}/5."
        )
        extraction_rows.append(
            {
                "paper_id": paper_id,
                "bibtex_key": bib_key,
                "apa_reference": apa,
                "study_type": paper_row["publication_type"],
                "research_objective": item["reason"],
                "signal_type": "heart/lung/cardiopulmonary/auscultation audio" if decision != "Exclude" else "not used",
                "dataset_names": item["dataset"],
                "dataset_public": "Yes" if item.get("dataset_inventory") else "Unclear",
                "preprocessing_steps": item["method"] if "preprocessing" in item["chapter"] else "",
                "feature_extraction": item["method"] if "feature" in item["chapter"] else "",
                "model_or_algorithm": item["method"],
                "implementation_language": "",
                "baseline_methods": "",
                "evaluation_metrics": item["metrics"],
                "main_results": "Metadata-only candidate; full text not audited.",
                "key_findings": item["contribution"],
                "limitations": item["limitation"],
                "relevance_to_fyp": f"{item['relevance']}/5 - {decision}; {item['reason']}",
                "chapter_2_theme": item["chapter"],
                "notes": note,
                "year_eligibility": YEAR_ELIGIBILITY,
                "previous_relevance_before_year_rule": "",
                "manual_access_status": "Metadata only; not downloaded",
            }
        )
        if item.get("dataset_inventory"):
            inv = item["dataset_inventory"]
            if not any(r.get("dataset_id") == inv["dataset_id"] for r in dataset_rows):
                dataset_rows.append(
                    {
                        "dataset_id": inv["dataset_id"],
                        "dataset_name": inv["dataset_name"],
                        "related_paper_id": paper_id,
                        "paper_title": title,
                        "paper_doi": doi,
                        "dataset_doi": inv["dataset_doi"],
                        "dataset_source": official_url,
                        "year": year,
                        "data_type": inv["data_type"],
                        "contains_heart_sounds": inv["contains_heart_sounds"],
                        "contains_lung_sounds": inv["contains_lung_sounds"],
                        "contains_mixed_sounds": inv["contains_mixed_sounds"],
                        "contains_source_signals": inv["contains_source_signals"],
                        "possible_use_in_fyp": inv["possible_use_in_fyp"],
                        "access_status": inv["access_status"],
                        "notes": f"Phase 7 metadata-only dataset record. Related paper decision: {decision}.",
                    }
                )

    papers_rows.extend(additions)

    # Add one duplicate note for the HLS-CMDS arXiv preprint variants encountered in Phase 7.
    max_dup += 1
    duplicate_rows.append(
        {
            "duplicate_group_id": f"D{max_dup:03d}",
            "primary_paper_id": "P038",
            "possible_duplicate_paper_id": "Phase7:10.48550/arXiv.2410.03280; Phase7:arXiv:2410.03280v1",
            "match_type": "published data descriptor supersedes arXiv preprint metadata",
            "matched_title": "Manikin-Recorded Cardiopulmonary Sounds Dataset Using Digital Stethoscope",
            "matched_doi": "10.48550/arXiv.2410.03280",
            "similarity_notes": "Phase 7 search rediscovered the older HLS-CMDS arXiv preprint after P038 had been updated to the IEEE Data Descriptions paper DOI.",
            "decision": "Do not add duplicate candidate; retain P038 with paper DOI 10.1109/IEEEDATA.2025.3566012 and dataset DOI/PID 10.17632/8972jxbpmp.",
            "decision_date": TODAY,
            "reviewer": "Codex Phase 7 metadata collection",
            "notes": "No record or PDF deleted.",
        }
    )

    # Search log: aggregate one row per metadata source.
    source_logs = {}
    for log in raw_data.get("logs", []):
        source = log["source"]
        source_logs.setdefault(source, {"returned": 0, "exported": 0, "errors": []})
        source_logs[source]["returned"] += int(log.get("results_returned") or 0)
        source_logs[source]["exported"] += int(log.get("records_exported") or 0)
        if log.get("status") != "ok":
            source_logs[source]["errors"].append(f"{log['query']}: {log['status']}")
    selected_source_counts = Counter()
    for row in additions:
        for source in row["source_database"].split("; "):
            if source:
                selected_source_counts[source] += 1
    next_search_num = len(search_rows) + 1
    all_queries = " | ".join(raw_data.get("queries", []))
    for source, values in source_logs.items():
        search_rows.append(
            {
                "search_id": f"S07-{next_search_num:03d}-{source.upper().replace(' ', '')}",
                "date_searched": TODAY,
                "source": source,
                "search_string": all_queries,
                "search_concepts": "Phase 7 gap-filling search: heart/lung/cardiopulmonary/chest sound separation; biomedical audio source separation; datasets; denoising; evaluation metrics; software prototypes",
                "filters": "metadata only; no PDFs; no login; publication years 2022-2026; avoid IOP Science and ASTM Digital Library priority downloads",
                "date_range": "2022-2026",
                "language": "English where available",
                "access_method": "Public metadata API / public web metadata",
                "results_returned": str(values["returned"]),
                "records_exported": str(values["exported"]),
                "records_added_to_master": str(selected_source_counts.get(source, 0)),
                "export_file": "literature-review/metadata/phase7_candidate_search_raw.json",
                "performed_by": "Codex Phase 7 metadata collection",
                "notes": "No PDFs downloaded; no restricted portals or logins used. " + ("API limits/errors: " + " || ".join(values["errors"][:6]) if values["errors"] else "API queries completed."),
            }
        )
        next_search_num += 1

    # References.
    bib_path = refs / "references.bib"
    bib_text = bib_path.read_text(encoding="utf-8").rstrip() + "\n\n"
    bib_text += "\n\n".join(build_bib_entry(row) for row in additions) + "\n"
    bib_path.write_text(bib_text, encoding="utf-8")

    apa_path = refs / "references_apa.md"
    apa_text = apa_path.read_text(encoding="utf-8").rstrip() + "\n\n## Phase 7 Additional Metadata Candidates\n\n"
    for row in additions:
        apa_text += (
            f"- [{row['paper_id']}] {apa_authors(row['authors'])}. ({row['year']}). {row['title']}. "
            f"{('*' + row['venue_source'] + '*') if row['venue_source'] else ''}. "
            f"https://doi.org/{row['doi']} Decision: {row['decision']}; relevance {row['relevance_score']}/5; "
            f"priority {row['download_priority']}.\n"
        )
    apa_path.write_text(apa_text, encoding="utf-8")

    write_csv(meta / "papers_master.csv", papers_fields, papers_rows)
    write_csv(meta / "download_queue.csv", queue_fields, queue_rows)
    write_csv(screening / "title_abstract_screening.csv", title_fields, title_rows)
    write_csv(screening / "extraction_matrix.csv", extraction_fields, extraction_rows)
    write_csv(meta / "dataset_inventory.csv", dataset_fields, dataset_rows)
    write_csv(meta / "duplicate_check.csv", duplicate_fields, duplicate_rows)
    write_csv(meta / "search_log.csv", search_fields, search_rows)

    counts = Counter(row["decision"] for row in papers_rows)
    priority_counts = Counter(row.get("priority", "") for row in queue_rows)
    prisma_data = json.loads(prisma.read_text(encoding="utf-8"))
    prisma_data["phase"] = "Phase 7 additional metadata candidate collection completed"
    prisma_data["last_updated"] = TODAY
    prisma_data["phase_7_collection"] = {
        "previous_total_records": 70,
        "new_candidate_records_added": len(additions),
        "total_records_after_phase_7": len(papers_rows),
        "useful_new_records_added": sum(1 for row in additions if row["decision"] in {"Include", "Maybe"}),
        "new_records_marked_exclude": sum(1 for row in additions if row["decision"] == "Exclude"),
        "duplicate_candidates_skipped": len(raw_data.get("duplicates_skipped", [])) + len(skipped),
        "sources_used": ["OpenAlex", "Semantic Scholar", "Crossref", "PubMed", "arXiv", "public web metadata"],
        "pdf_downloads_performed": False,
        "restricted_logins_performed": False,
        "publication_year_range": "2022-2026",
    }
    prisma_data["decision_summary_after_phase_7"] = {
        "Include": counts.get("Include", 0),
        "Maybe": counts.get("Maybe", 0),
        "Exclude": counts.get("Exclude", 0),
        "useful_pool_include_plus_maybe": counts.get("Include", 0) + counts.get("Maybe", 0),
    }
    prisma_data["download_priority_summary_after_phase_7"] = {
        "Priority 1": priority_counts.get("1", 0),
        "Priority 2": priority_counts.get("2", 0),
        "Priority 3": priority_counts.get("3", 0),
    }
    prisma_data.setdefault("notes_after_phase_7", [])
    prisma_data["notes_after_phase_7"] = [
        "Phase 7 used public metadata APIs and public metadata pages only.",
        "No PDFs were downloaded and no publisher, university, IEEE, ScienceDirect, Springer, ResearchGate, IOP Science, or ASTM login was attempted.",
        "Weak diagnosis-only or general-audio records were retained as Exclude for PRISMA traceability and are not recommended for Zotero download.",
        "The older HLS-CMDS arXiv preprint was detected as a duplicate and not added; P038 remains the published IEEE Data Descriptions paper.",
    ]
    prisma.write_text(json.dumps(prisma_data, indent=2), encoding="utf-8")

    outline = outline_path.read_text(encoding="utf-8")
    dataset_bullet = (
        "- Add Phase 7 dataset/evaluation candidates: PhysioNet Challenge 2022/CirCor pediatric PCG data "
        "(P080) for heart-sound benchmarking context and Sound-Dr (P075) for respiratory dataset context; "
        "treat both as background/evaluation resources rather than paired heart-lung separation datasets."
    )
    preprocessing_bullet = (
        "- Use Phase 7 denoising/preprocessing candidates (P081-P086) to discuss PCG/lung sound denoising, "
        "wavelet/UNet methods, transformer denoisers, and segmentation as supporting methods before separation."
    )
    if dataset_bullet not in outline:
        outline = outline.replace(
            "- Include HLS-CMDS (P038) as a priority dataset because it provides heart-only, lung-only, mixed heart-lung, and corresponding source recordings; cite the descriptor paper DOI 10.1109/IEEEDATA.2025.3566012 and record dataset access through DOI/PID 10.17632/8972jxbpmp.",
            "- Include HLS-CMDS (P038) as a priority dataset because it provides heart-only, lung-only, mixed heart-lung, and corresponding source recordings; cite the descriptor paper DOI 10.1109/IEEEDATA.2025.3566012 and record dataset access through DOI/PID 10.17632/8972jxbpmp.\n" + dataset_bullet,
        )
    if preprocessing_bullet not in outline:
        outline = outline.replace(
            "- Explain how preprocessing choices affect model training and separation quality.",
            "- Explain how preprocessing choices affect model training and separation quality.\n" + preprocessing_bullet,
        )
    phase7_section = "\n## Phase 7 Gap-Filling Notes\n\n"
    phase7_section += "- Added 25 metadata-only records from 2022-2026 public metadata searches.\n"
    phase7_section += "- Prioritize P073 first for Zotero because it is the strongest new direct cardiorespiratory sound separation paper.\n"
    phase7_section += "- Use Phase 7 Maybe records mainly for dataset, preprocessing, evaluation, and prototype context; do not use Exclude records in Chapter 2 unless explaining search boundaries.\n"
    if "## Phase 7 Gap-Filling Notes" not in outline:
        outline = outline.rstrip() + phase7_section
    outline_path.write_text(outline, encoding="utf-8")

    print(
        json.dumps(
            {
                "added": len(additions),
                "skipped_existing": skipped,
                "decision_counts": dict(counts),
                "useful_pool": counts.get("Include", 0) + counts.get("Maybe", 0),
                "priority_counts": dict(priority_counts),
                "new_ids": [row["paper_id"] for row in additions],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
