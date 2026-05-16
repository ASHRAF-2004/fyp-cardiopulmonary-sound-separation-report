# Chapter 2 Literature Review Outline

## 2.1 Introduction

- Introduce the purpose of the literature review.
- Link the review to the FYP title: Machine Learning-Based System for Cardiopulmonary Sound Separation.
- Clarify that the project is a software engineering proof of concept, not a clinical disease detection system.
- Summarize the review scope: datasets, preprocessing, feature extraction, model implementation, and evaluation.

## 2.2 Cardiopulmonary Sound Background

- Explain heart sounds, lung sounds, respiratory sounds, and chest auscultation signals.
- Discuss why heart and lung sounds overlap in real recordings.
- Explain the challenge of single-channel or mixed cardiopulmonary recordings.
- Define key terms: PCG, respiratory sounds, source separation, denoising, signal decomposition.

## 2.3 Public Datasets for Heart and Lung Sound Research

- Review public heart sound datasets such as PhysioNet/CinC heart sound resources.
- Review public respiratory or lung sound datasets such as ICBHI resources.
- Compare dataset properties: signal type, sampling rate, labels, noise, recording device, availability, and licensing.
- Identify dataset limitations for supervised separation, such as lack of clean ground-truth isolated sources.
- Include HLS-CMDS (P038) as a priority dataset because it provides heart-only, lung-only, mixed heart-lung, and corresponding source recordings; cite the descriptor paper DOI 10.1109/IEEEDATA.2025.3566012 and record dataset access through DOI/PID 10.17632/8972jxbpmp.
- Add Phase 7 dataset/evaluation candidates: PhysioNet Challenge 2022/CirCor pediatric PCG data (P080) for heart-sound benchmarking context and Sound-Dr (P075) for respiratory dataset context; treat both as background/evaluation resources rather than paired heart-lung separation datasets.

## 2.4 Preprocessing and Signal Representation

- Discuss resampling, normalization, filtering, segmentation, denoising, and artifact handling.
- Review time-domain, frequency-domain, and time-frequency representations.
- Cover spectrograms, STFT, Mel spectrograms, wavelets, envelope features, and other relevant features.
- Explain how preprocessing choices affect model training and separation quality.
- Use Phase 7 denoising/preprocessing candidates (P081-P086) to discuss PCG/lung sound denoising, wavelet/UNet methods, transformer denoisers, and segmentation as supporting methods before separation.

## 2.5 Traditional Signal Processing Approaches

- Review blind source separation methods, including ICA where relevant.
- Review NMF, SNMF, VMD, DAE-NMF-VMD, filtering, and decomposition methods.
- Compare strengths and weaknesses of traditional methods for cardiopulmonary sounds.
- Identify which ideas are useful as baselines for a Python prototype.

## 2.6 Machine Learning and Deep Learning Approaches

- Review supervised, unsupervised, and semi-supervised approaches.
- Cover neural architectures used for audio separation, such as CNN, U-Net, autoencoders, VAEs, attention models, and NeoSSNet-like models.
- Discuss input-output design: waveform-to-waveform, spectrogram mask prediction, reconstruction, or hybrid pipelines.
- Compare model complexity against FYP feasibility.

## 2.7 Cardiopulmonary Sound Separation Studies

- Organize related work thematically rather than paper by paper.
- Suggested themes:
  - Heart and lung sound separation with deep learning.
  - Hybrid decomposition and neural methods.
  - Real-time or low-latency separation.
  - Unsupervised or data-constrained separation.
  - Neonatal or chest sound separation studies.
- Summarize each theme using evidence from the extraction matrix.

## 2.8 Evaluation Metrics

- Review separation and audio quality metrics such as SDR, SIR, SAR, SNR improvement, RMSE, MAE, correlation, and reconstruction loss.
- Include perceptual or intelligibility metrics only if relevant to the reviewed papers.
- Distinguish separation metrics from disease classification metrics.
- Explain which metrics are suitable for the FYP prototype and why.

## 2.9 Software Engineering and Prototype Considerations

- Discuss how reviewed methods can be converted into a Python implementation.
- Link literature evidence to application requirements: upload audio, preprocess, separate heart/lung components, save outputs, and display results.
- Consider model runtime, reproducibility, local storage, and explainability for viva presentation.
- Keep this section focused on an application-based proof of concept.

## 2.10 Comparative Summary of Reviewed Studies

- Present a comparison table using fields from `screening/extraction_matrix.csv`.
- Suggested columns: paper, dataset, signal type, method, preprocessing, metrics, key result, limitation, relevance to FYP.
- Compare studies across methods, datasets, and evaluation choices.

## 2.11 Research Gap

- Identify gaps in existing work that justify the FYP.
- Possible gaps:
  - Limited use of public datasets for heart-lung separation with clear reproducible pipelines.
  - Limited practical student-level implementations that connect ML separation to a usable application prototype.
  - Many disease-focused works do not address clean separation as the main objective.
  - Some high-performing models may be too complex or insufficiently documented for direct reproduction.
- State the specific gap this FYP addresses.

## 2.12 Chapter Summary

- Summarize the main findings from the literature.
- State which methods, datasets, and metrics will inform Chapter 3 methodology.
- Transition to the proposed system design and implementation approach.

<!-- Phase 6 PDF audit guidance starts -->

## Phase 6 Chapter 2 Use Guidance

- Prioritize full-text-audited separation papers over metadata-only candidates.
- Use the 2026 Whisper reprogramming paper, 2025 phase-enhanced PENN paper, 2022 blind filtering paper, GIHO-VMD, LingoNMF, periodicity-NMF, and the HLS-CMDS dataset descriptor as the strongest newly audited evidence.
- Treat ALE/FxLMS hardware papers, PCG-only segmentation/classification papers, and diagnosis-only datasets as background or Maybe evidence only.
- Keep P027 online-only for possible later manual evaluation; do not exclude it only because the PDF is unavailable.

Recommended first papers for Chapter 2 after Phase 6:

- P021: Reprogramming Automatic Speech Recognition Models for Neonatal Chest Sound Separation
- P022: A Phase-Enhanced Neural Network With Dual-Path Transformer for Single-Channel Chest Sound Separation
- P040: A Blind Filtering Framework for Noisy Neonatal Chest Sounds
- P035: An efficient lung sound separation algorithm base on GIHO-VMD
- P023: Large Language Model-based Nonnegative Matrix Factorization For Cardiorespiratory Sound Separation
- P025: A New Non-Negative Matrix Factorization Approach for Blind Source Separation of Cardiovascular and Respiratory Sound Based on the Periodicity of Heart and Lung Function
- P038: Descriptor: Heart and Lung Sounds Dataset Recorded from a Clinical Manikin using Digital Stethoscope (HLS-CMDS)
- P009: retain from Phase 2 audited shortlist
- P013: retain from Phase 2 audited shortlist
- P015: retain from Phase 2 audited shortlist
- P016: retain from Phase 2 audited shortlist
- P017: retain from Phase 2 audited shortlist
- P018: retain from Phase 2 audited shortlist
- P020: retain from Phase 2 audited shortlist
- P029: Separation of Heart and Lung Sounds by A Deep Network-Based Model

<!-- Phase 6 PDF audit guidance ends -->

<!-- Phase 4 category adjustment starts -->

## Phase 4 Screening Categories for Candidate Papers

Use the Phase 4 fields in `metadata/papers_master.csv`, `metadata/download_queue.csv`, and `screening/title_abstract_screening.csv` when selecting papers for Chapter 2:

- Priority 1: direct heart-lung, cardiopulmonary, chest sound, or cardiac-respiratory source separation papers to download and screen first.
- Priority 2: useful backup papers for traditional methods, preprocessing, denoising, datasets, evaluation metrics, or implementation context.
- Priority 3: weak, older, hardware-heavy, classification-only, or peripheral papers; do not download unless Chapter 2 needs extra support.
- Use `useful_for` to group papers by background, related work, dataset, preprocessing, feature extraction, model/method, evaluation metrics, research gap, and software/prototype relevance.
- Do not cite metadata-only candidates as final evidence until the PDF has been manually downloaded and screened.

<!-- Phase 4 category adjustment ends -->
## Phase 7 Gap-Filling Notes

- Added 25 metadata-only records from 2022-2026 public metadata searches.
- Prioritize P073 first for Zotero because it is the strongest new direct cardiorespiratory sound separation paper.
- Use Phase 7 Maybe records mainly for dataset, preprocessing, evaluation, and prototype context; do not use Exclude records in Chapter 2 unless explaining search boundaries.
## Final Chapter 2 Evidence Plan

- Use `notes/chapter_2_evidence_map.md` as the source map for Chapter 2 writing.
- Recommended writing set: 35 papers (P002, P005, P009, P011, P013, P015, P016, P017, P018, P019, P020, P021, P022, P023, P025, P029, P035, P037, P038, P039, P040, P065, P066, P073, P074, P075, P076, P077, P078, P080, P081, P082, P083, P084, P086).
- High-priority core papers should lead the related-work synthesis; Medium papers should support datasets, preprocessing, evaluation, and software/prototype context.
- Keep Low-priority Maybe records as backup only. Do not delete them; they remain useful for PRISMA traceability and optional background.
- Do not use Exclude records as evidence except when explaining screening/access limitations.
- Write Chapter 2 thematically, not as one paragraph per paper.
