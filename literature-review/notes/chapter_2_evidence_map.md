# Chapter 2 Evidence Map

FYP title: Machine Learning-Based System for Cardiopulmonary Sound Separation

Updated: 2026-05-16

Scope: final Chapter 2 selection from existing Include/Maybe records only. No new searches, downloads, logins, record deletion, or PDF deletion were performed.

## Selection Summary

| Metric | Count |
|---|---:|
| Include records reviewed | 18 |
| Maybe records reviewed | 31 |
| Total useful pool reviewed | 49 |
| Recommended for actual Chapter 2 writing | 35 |
| Backup / not needed unless space allows | 14 |

| Chapter 2 role | Count |
|---|---:|
| Core Chapter 2 paper | 16 |
| Dataset/evaluation paper | 5 |
| Supporting paper | 18 |
| Background-only paper | 6 |
| Not needed unless space allows | 4 |

| Priority | Count |
|---|---:|
| High | 17 |
| Medium | 19 |
| Low | 13 |

## Best Papers for Chapter 2 Writing

Use these 35 papers first. They cover direct separation methods, datasets, preprocessing, evaluation, and prototype relevance without relying on excluded or inaccessible papers.

| Paper | Priority | Section | Why use it |
|---|---|---|---|
| P002: An End-to-End Deep Learning Framework for Real-Time Denoising of Heart Sounds for Cardiac Di... | Medium | signal processing / preprocessing | Heart-sound denoising overlaps with P081/P085; keep as audited LU-Net denoising support. |
| P005: Noisy Neonatal Chest Sound Separation for High-Quality Heart and Lung Sounds | High | cardiopulmonary sound separation | Neonatal NMF/NMCF baseline; overlaps with P009/P021/P022/P040 but provides earlier traditional baseline. |
| P009: NeoSSNet: Real-Time Neonatal Chest Sound Separation Using Deep Learning | High | cardiopulmonary sound separation | Core NeoSSNet paper; overlaps with P021 as same neonatal research line but distinct method. |
| P011: Recent Advances in PCG Signal Analysis using AI: A Review | Medium | deep learning / ML methods | PCG AI review; overlaps with P019 but useful for preprocessing/feature background. |
| P013: Research on Heart and Lung Sound Separation Method Based on DAE-NMF-VMD | High | heart-lung sound separation methods | Core hybrid DAE-NMF-VMD method; overlaps with P016/P017/P035/P027 decomposition family. |
| P015: Unsupervised Framework for Single Channel Heart and Lung Sounds Separation in Data Constrain... | High | heart-lung sound separation methods | Core unsupervised/data-constrained single-channel separation method. |
| P016: A Multi-Channel UNet Framework Based on SNMF-DCNN for Robust Heart-Lung-Sound Separation | High | heart-lung sound separation methods | Core SNMF-DCNN-MCUNet paper; use for hybrid NMF plus U-Net comparison. |
| P017: Heart-Lung Sound Separation by Nonnegative Matrix Factorization and Deep Learning | High | heart-lung sound separation methods | Core NMF plus deep learning method; overlaps with P023/P025 but remains key baseline. |
| P018: JASSNet: Heart and Lung Sound Separation Network Based on Joint Attention Mechanism and Semi... | High | deep learning / ML methods | Core attention/semi-supervised separation model; use as recent deep-learning evidence. |
| P019: Deep Learning in Heart Sound Analysis: From Techniques to Clinical Applications | Medium | deep learning / ML methods | Heart-sound DL review; overlaps with P011 but stronger for datasets and DL landscape. |
| P020: Separation of Cardiopulmonary Sound Signals for Classification of Respiratory Diseases | High | cardiopulmonary sound separation | Direct cardiopulmonary sound separation paper, though downstream objective is disease classification. |
| P021: Reprogramming Automatic Speech Recognition Models for Neonatal Chest Sound Separation | High | deep learning / ML methods | Foundation/ASR reprogramming neonatal separation; overlaps with P009 but newer and distinct. |
| P022: A Phase-Enhanced Neural Network With Dual-Path Transformer for Single-Channel Chest Sound Se... | High | deep learning / ML methods | Phase-aware transformer separation; central for evaluation and research gap. |
| P023: Large Language Model-based Nonnegative Matrix Factorization For Cardiorespiratory Sound Sepa... | High | heart-lung sound separation methods | LingoNMF/LLM-assisted NMF; overlaps with P025 but is a distinct extension. |
| P025: A New Non-Negative Matrix Factorization Approach for Blind Source Separation of Cardiovascul... | High | heart-lung sound separation methods | Periodicity-guided NMF baseline; overlaps with P023 but should be cited before LingoNMF. |
| P029: Separation of Heart and Lung Sounds by A Deep Network-Based Model | High | deep learning / ML methods | Simple deep network heart/lung separation; useful for FYP feasibility despite synthetic-mixture limits. |
| P035: An efficient lung sound separation algorithm base on GIHO-VMD | High | heart-lung sound separation methods | GIHO-VMD optimized decomposition method; strong recent signal-processing comparator. |
| P037: Identifying the Respiratory Sound Based on Single-Channel Separation and Hyperdimensional Co... | Medium | deep learning / ML methods | Single-channel separation used for respiratory sound identification; useful but classification objective dominates. |
| P038: Descriptor: Heart and Lung Sounds Dataset Recorded from a Clinical Manikin using Digital Ste... | High | datasets | Primary HLS-CMDS dataset descriptor with mixed and source heart/lung signals. |
| P039: Automatic Wheeze Segmentation Using Harmonic-Percussive Source Separation and Empirical Mode... | Medium | signal processing / preprocessing | Respiratory HPSS/EMD preprocessing support; not heart-lung separation. |
| P040: A Blind Filtering Framework for Noisy Neonatal Chest Sounds | High | signal processing / preprocessing | Blind filtering framework for noisy neonatal chest sounds; strong traditional comparator. |
| P065: A Dual Classifier-Regressor Architecture for Heart Sound Onset/Offset Detection | Medium | signal processing / preprocessing | Heart sound onset/offset segmentation support for preprocessing/evaluation. |
| P066: BUET multi-disease heart sound dataset: A comprehensive auscultation dataset for developing ... | Medium | datasets | Public heart-sound dataset support; not a separation dataset. |
| P073: Cardiorespiratory Sound Separation Using Singular Spectrum Analysis | High | cardiopulmonary sound separation | Newest direct cardiorespiratory separation candidate; metadata-only, so cite after manual access if possible. |
| P074: StethAid: A Digital Auscultation Platform for Pediatrics | Medium | software/prototype relevance | Digital auscultation platform context for pediatric workflow and application design. |
| P075: Sound-Dr: Reliable Sound Dataset and Baseline Artificial Intelligence System for Respiratory... | Medium | datasets | Respiratory dataset/background evidence; not paired heart-lung separation. |
| P076: Compressed Sensing of Acoustic Cardiopulmonary Signals Using a CNN-based Reconstruction Method | Medium | software/prototype relevance | CNN reconstruction/acquisition support for cardiopulmonary signal software pipeline. |
| P077: Real-Time Multi-Level Neonatal Heart and Lung Sound Quality Assessment for Telehealth Applic... | Medium | evaluation metrics | Quality assessment for neonatal heart/lung sounds; useful for evaluation and input quality. |
| P078: Bridging Auscultation and Tiny Machine Learning: A Digital Stethoscope Leveraging Convolutio... | Medium | software/prototype relevance | TinyML/digital stethoscope implementation context; not source separation. |
| P080: Heart murmur detection from phonocardiogram recordings: The George B. Moody PhysioNet Challe... | Medium | datasets | PhysioNet/CirCor benchmark support for heart-sound dataset/evaluation context. |
| P081: A robust deep learning based model for denoising phonocardiogram signals in clinical environ... | Medium | signal processing / preprocessing | Recent PCG denoising; overlaps with P002/P085 but stronger current denoising support. |
| P082: A self-attention-driven deep denoiser model for real time lung sound denoising in noisy envi... | Medium | signal processing / preprocessing | Recent self-attention lung sound denoising; supports preprocessing section. |
| P083: Adaptive thresholding of DWT coefficients using UNet for denoising real-life respiratory sounds | Medium | signal processing / preprocessing | UNet/DWT respiratory denoising; good multiscale preprocessing support. |
| P084: Lung sound signal denoising using discrete wavelet transform and artificial neural network | Medium | signal processing / preprocessing | DWT-ANN lung denoising; useful classical+ML denoising support. |
| P086: Automatic breathing phase identification based on the second derivative of the recorded lung... | Medium | signal processing / preprocessing | Breathing phase segmentation support for lung-sound preprocessing/evaluation. |

## Backup Papers

Keep these records. They are useful only if Chapter 2 needs extra background or if a recommended paper becomes unusable.

| Paper | Priority | Section | Reason kept as backup |
|---|---|---|---|
| P001: Unsupervised Deep Learning of Sparse Signals against Low-Rank Backgrounds with Application t... | Low | signal processing / preprocessing | Unsupervised lung sparse/low-rank separation; useful only if discussing RPCA-like background. |
| P003: A Robust Hybrid Neural Network Architecture for Blind Source Separation of Speech Signals Ex... | Low | deep learning / ML methods | General speech separation only; use only for generic BSS architecture context. |
| P004: Multi-resolution Analysis Based Time-Domain Audio Source Separation with Optimized U-NET Model | Low | deep learning / ML methods | General audio U-Net/source separation; no biomedical dataset. |
| P006: Generative AI Respiratory and Cardiac Sound Separation Using Variational Autoencoders (VAEs) | Low | deep learning / ML methods | Title suggests separation but audited evidence is classification/feature-extraction oriented; use cautiously. |
| P007: Non-Contact Heart Sound Measurement Using Independent Component Analysis | Low | signal processing / preprocessing | ICA/non-contact heart extraction only; not heart-lung separation. |
| P010: Separation of the Aortic and Pulmonary Components of the Second Heart Sound via Alternating ... | Low | signal processing / preprocessing | Separates heart-sound subcomponents, not heart/lung sources. |
| P014: Feature-Based Fusion Using CNN for Lung and Heart Sound Classification | Medium | datasets | Classification-only but useful for ICBHI/heart-sound dataset and feature-fusion context. |
| P027: HEART SOUND NOISE SEPARATION FROM LUNG SOUND BASED ON ENHANCED VARIATIONAL MODE DECOMPOSITIO... | Low | signal processing / preprocessing | Online-only enhanced VMD paper; diagnosis focus and no PDF, so keep as backup. |
| P030: Real Time Lung Sound Separation from Cardiac Sounds by Adaptive Algorithm Technique | Low | signal processing / preprocessing | Weak adaptive filtering evidence with limited dataset detail. |
| P036: ASIC-Based Lung Sound Separation: Performance Analysis of Adaptive Line Enhancer with Least ... | Low | software/prototype relevance | ASIC/hardware-heavy ALE paper; peripheral to Python software prototype. |
| P070: Phonocardiogram Signal Processing with Heart Sound Classification Using Transfer Learning | Low | deep learning / ML methods | Transfer-learning PCG classification only; use only if extra feature-extraction background is needed. |
| P071: Digital Stethoscope Use in Neonates: A Systematic Review | Low | software/prototype relevance | Neonatal digital stethoscope systematic review; useful only for short context. |
| P072: Deep learning-based lung sound analysis for intelligent stethoscope | Low | deep learning / ML methods | Intelligent stethoscope lung analysis; no separation output. |
| P085: Clearer Lub-Dub: A Novel Approach in Heart Sound Denoising Based on Transfer Learning | Low | signal processing / preprocessing | Heart-sound transfer-learning denoising; backup because P002/P081 cover stronger PCG denoising evidence. |

## Evidence by Theme

### Cardiopulmonary Sound Separation

- P005 (High, recommended): Noisy Neonatal Chest Sound Separation for High-Quality Heart and Lung Sounds
- P009 (High, recommended): NeoSSNet: Real-Time Neonatal Chest Sound Separation Using Deep Learning
- P020 (High, recommended): Separation of Cardiopulmonary Sound Signals for Classification of Respiratory Diseases
- P073 (High, recommended): Cardiorespiratory Sound Separation Using Singular Spectrum Analysis

### Heart-Lung Sound Separation Methods

- P013 (High, recommended): Research on Heart and Lung Sound Separation Method Based on DAE-NMF-VMD
- P015 (High, recommended): Unsupervised Framework for Single Channel Heart and Lung Sounds Separation in Data Constrained Environments
- P016 (High, recommended): A Multi-Channel UNet Framework Based on SNMF-DCNN for Robust Heart-Lung-Sound Separation
- P017 (High, recommended): Heart-Lung Sound Separation by Nonnegative Matrix Factorization and Deep Learning
- P023 (High, recommended): Large Language Model-based Nonnegative Matrix Factorization For Cardiorespiratory Sound Separation
- P025 (High, recommended): A New Non-Negative Matrix Factorization Approach for Blind Source Separation of Cardiovascular and Respiratory Sound Based on the Periodicity of Heart and Lung Function
- P035 (High, recommended): An efficient lung sound separation algorithm base on GIHO-VMD

### Deep Learning / Ml Methods

- P003 (Low, backup): A Robust Hybrid Neural Network Architecture for Blind Source Separation of Speech Signals Exploiting Deep Learning
- P004 (Low, backup): Multi-resolution Analysis Based Time-Domain Audio Source Separation with Optimized U-NET Model
- P006 (Low, backup): Generative AI Respiratory and Cardiac Sound Separation Using Variational Autoencoders (VAEs)
- P011 (Medium, recommended): Recent Advances in PCG Signal Analysis using AI: A Review
- P018 (High, recommended): JASSNet: Heart and Lung Sound Separation Network Based on Joint Attention Mechanism and Semi-Supervised Learning
- P019 (Medium, recommended): Deep Learning in Heart Sound Analysis: From Techniques to Clinical Applications
- P021 (High, recommended): Reprogramming Automatic Speech Recognition Models for Neonatal Chest Sound Separation
- P022 (High, recommended): A Phase-Enhanced Neural Network With Dual-Path Transformer for Single-Channel Chest Sound Separation
- P029 (High, recommended): Separation of Heart and Lung Sounds by A Deep Network-Based Model
- P037 (Medium, recommended): Identifying the Respiratory Sound Based on Single-Channel Separation and Hyperdimensional Computing
- P070 (Low, backup): Phonocardiogram Signal Processing with Heart Sound Classification Using Transfer Learning
- P072 (Low, backup): Deep learning-based lung sound analysis for intelligent stethoscope

### Signal Processing / Preprocessing

- P001 (Low, backup): Unsupervised Deep Learning of Sparse Signals against Low-Rank Backgrounds with Application to Online Lung Sound Separation
- P002 (Medium, recommended): An End-to-End Deep Learning Framework for Real-Time Denoising of Heart Sounds for Cardiac Disease Detection in Unseen Noise
- P007 (Low, backup): Non-Contact Heart Sound Measurement Using Independent Component Analysis
- P010 (Low, backup): Separation of the Aortic and Pulmonary Components of the Second Heart Sound via Alternating Optimization
- P027 (Low, backup): HEART SOUND NOISE SEPARATION FROM LUNG SOUND BASED ON ENHANCED VARIATIONAL MODE DECOMPOSITION FOR DIAGNOSING PULMONARY DISEASES
- P030 (Low, backup): Real Time Lung Sound Separation from Cardiac Sounds by Adaptive Algorithm Technique
- P039 (Medium, recommended): Automatic Wheeze Segmentation Using Harmonic-Percussive Source Separation and Empirical Mode Decomposition
- P040 (High, recommended): A Blind Filtering Framework for Noisy Neonatal Chest Sounds
- P065 (Medium, recommended): A Dual Classifier-Regressor Architecture for Heart Sound Onset/Offset Detection
- P081 (Medium, recommended): A robust deep learning based model for denoising phonocardiogram signals in clinical environments
- P082 (Medium, recommended): A self-attention-driven deep denoiser model for real time lung sound denoising in noisy environments
- P083 (Medium, recommended): Adaptive thresholding of DWT coefficients using UNet for denoising real-life respiratory sounds
- P084 (Medium, recommended): Lung sound signal denoising using discrete wavelet transform and artificial neural network
- P085 (Low, backup): Clearer Lub-Dub: A Novel Approach in Heart Sound Denoising Based on Transfer Learning
- P086 (Medium, recommended): Automatic breathing phase identification based on the second derivative of the recorded lung sounds

### Datasets

- P014 (Medium, backup): Feature-Based Fusion Using CNN for Lung and Heart Sound Classification
- P038 (High, recommended): Descriptor: Heart and Lung Sounds Dataset Recorded from a Clinical Manikin using Digital Stethoscope (HLS-CMDS)
- P066 (Medium, recommended): BUET multi-disease heart sound dataset: A comprehensive auscultation dataset for developing computer-aided diagnostic systems
- P075 (Medium, recommended): Sound-Dr: Reliable Sound Dataset and Baseline Artificial Intelligence System for Respiratory Illnesses
- P080 (Medium, recommended): Heart murmur detection from phonocardiogram recordings: The George B. Moody PhysioNet Challenge 2022

### Evaluation Metrics

- P077 (Medium, recommended): Real-Time Multi-Level Neonatal Heart and Lung Sound Quality Assessment for Telehealth Applications

### Software/Prototype Relevance

- P036 (Low, backup): ASIC-Based Lung Sound Separation: Performance Analysis of Adaptive Line Enhancer with Least Mean Square Algorithm Across Scaled CMOS Technologies
- P071 (Low, backup): Digital Stethoscope Use in Neonates: A Systematic Review
- P074 (Medium, recommended): StethAid: A Digital Auscultation Platform for Pediatrics
- P076 (Medium, recommended): Compressed Sensing of Acoustic Cardiopulmonary Signals Using a CNN-based Reconstruction Method
- P078 (Medium, recommended): Bridging Auscultation and Tiny Machine Learning: A Digital Stethoscope Leveraging Convolutional Neural Networks on an Embedded Device for Organ Sound Analysis

## Overlap and Deduplication Notes

- P009 and P021 are related neonatal chest sound separation papers from the same research line, but they use different methods; retain both and explain the progression from NeoSSNet to ASR model reprogramming.
- P023 and P025 overlap in the NMF/cardiorespiratory separation line; use P025 as the periodicity-guided NMF baseline and P023 as the later LLM-assisted extension.
- P005, P009, P021, P022, and P040 all support neonatal or chest sound separation; organize them chronologically and by method family instead of repeating similar background.
- P013, P016, P017, P023, P025, P027, and P035 overlap in decomposition/NMF/VMD-style methods; prioritize P013, P016, P017, P023, P025, and P035, while keeping P027 as online-only backup.
- P011 and P019 are review/background papers; use them sparingly for PCG and heart-sound AI context, not as direct separation evidence.
- P002, P081, and P085 overlap in heart-sound denoising; use P002 and P081 first, keep P085 as backup.
- P082, P083, P084, and P086 overlap in lung/respiratory preprocessing; cite only the most relevant examples needed for denoising and segmentation.
- P038 is the primary dataset/evaluation record for this FYP because HLS-CMDS includes mixed and source signals. P066, P075, and P080 are supporting dataset/background records, not direct paired separation datasets.

## Suggested Chapter 2 Writing Flow

1. Start with cardiopulmonary sound overlap and source-separation motivation using P005, P009, P040, P021, and P022.
2. Compare method families: classical blind filtering and NMF/VMD methods, hybrid decomposition-neural methods, and modern deep/foundation models.
3. Introduce datasets after methods, emphasizing that HLS-CMDS (P038) is unusually useful because it contains mixed and corresponding source heart/lung recordings.
4. Use denoising and segmentation papers as support for preprocessing choices, not as the main related-work story.
5. End with the research gap: recent methods are promising, but many rely on private/synthetic data, inaccessible full texts, complex architectures, or limited software-prototype integration.
