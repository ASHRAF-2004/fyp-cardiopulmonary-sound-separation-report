# Chapter 2 Citation Plan

Draft status: planning companion for `chapter_2_draft.md`. All citation keys below are present in `literature-review/references/references.bib` and come from the 35 recommended Chapter 2 writing papers.

## 2.1 Introduction

| Paper | Citation key | Why it is used |
|---|---|---|
| P005 | `grooby2023noisyneonatal` | Introduces early neonatal chest sound separation and NMF/NMCF baseline context. |
| P009 | `poh2024neossnet` | Establishes real-time deep learning chest sound separation as a core related-work anchor. |
| P011 | `roy2024pcgreview` | Provides PCG preprocessing and feature-extraction background. |
| P019 | `zhao2024heartanalysis` | Provides recent deep learning heart sound analysis background and dataset context. |
| P021 | `poh2026reprogramming2` | Shows emerging foundation-model/ASR reprogramming direction. |
| P022 | `wang2025phase2` | Introduces phase-aware transformer-based chest sound separation as recent state of the art. |
| P040 | `fattahi2022blind2` | Provides traditional blind filtering background for noisy neonatal chest sounds. |
| P073 | `han2025cardiorespiratory` | Adds a recent direct cardiorespiratory separation candidate using singular spectrum analysis. |

## 2.2 Cardiopulmonary Sound Characteristics

| Paper | Citation key | Why it is used |
|---|---|---|
| P002 | `ali2023lunet` | Supports the claim that lung/breathing and environmental noise affect heart sound processing. |
| P011 | `roy2024pcgreview` | Supports definitions of PCG preprocessing, segmentation, and feature extraction. |
| P019 | `zhao2024heartanalysis` | Supports the broader heart sound AI background. |
| P077 | `grooby2022real` | Supports discussion of neonatal heart/lung sound quality assessment. |
| P081 | `jakubec2025robust` | Supports robust PCG denoising in noisy clinical environments. |
| P082 | `shuvo2026self` | Supports lung sound denoising and noisy respiratory recording discussion. |
| P083 | `behera2026adaptive` | Supports DWT/UNet respiratory sound denoising context. |
| P084 | `pouyani2022signal` | Supports DWT-ANN lung sound denoising context. |
| P086 | `pal2024automatic` | Supports respiratory phase and segmentation discussion. |

## 2.3 Heart and Lung Sound Separation Problem

| Paper | Citation key | Why it is used |
|---|---|---|
| P005 | `grooby2023noisyneonatal` | Demonstrates neonatal heart/lung sound separation with NMF/NMCF. |
| P009 | `poh2024neossnet` | Core deep learning real-time neonatal chest sound separation evidence. |
| P020 | `zheng2024cardiopulmonary` | Shows cardiopulmonary separation used before downstream respiratory analysis. |
| P021 | `poh2026reprogramming2` | Shows model reprogramming for neonatal chest sound separation. |
| P022 | `wang2025phase2` | Supports the importance of phase-aware single-channel separation. |
| P037 | `zheng2025identifying2` | Shows single-channel separation used before respiratory sound identification. |
| P040 | `fattahi2022blind2` | Provides blind filtering comparison for noisy neonatal chest sounds. |
| P073 | `han2025cardiorespiratory` | Adds direct cardiorespiratory separation evidence. |

## 2.4 Traditional Signal Processing Methods

| Paper | Citation key | Why it is used |
|---|---|---|
| P005 | `grooby2023noisyneonatal` | Baseline NMF/NMCF separation evidence. |
| P013 | `sun2024daenmfvmd` | Hybrid DAE-NMF-VMD method combining decomposition and neural components. |
| P015 | `ullah2024unsupervised` | Data-constrained unsupervised single-channel separation method. |
| P017 | `wang2023nmfdl` | NMF plus deep learning separation evidence. |
| P023 | `torabi2025large2` | LLM-assisted NMF parameter tuning extension. |
| P025 | `torabi2023negative2` | Periodicity-guided NMF baseline for cardiovascular/respiratory separation. |
| P035 | `zhang2026efficient2` | GIHO-VMD optimized decomposition method. |
| P039 | `rocha2023automatic2` | Respiratory HPSS/EMD preprocessing and segmentation support. |
| P040 | `fattahi2022blind2` | Blind filtering framework for neonatal chest sound preprocessing/separation. |
| P073 | `han2025cardiorespiratory` | Singular spectrum analysis cardiorespiratory separation candidate. |

## 2.5 Machine Learning and Deep Learning Methods

| Paper | Citation key | Why it is used |
|---|---|---|
| P002 | `ali2023lunet` | Heart sound denoising with encoder-decoder deep learning. |
| P009 | `poh2024neossnet` | Core deep learning model for real-time chest sound separation. |
| P013 | `sun2024daenmfvmd` | Hybrid deep autoencoder and decomposition method. |
| P016 | `wang2023mcunet` | SNMF-DCNN-MCUNet hybrid deep separation method. |
| P018 | `zhang2025jassnet` | Joint attention and semi-supervised heart/lung separation model. |
| P021 | `poh2026reprogramming2` | ASR model reprogramming for neonatal chest sound separation. |
| P022 | `wang2025phase2` | Phase-enhanced dual-path transformer separation model. |
| P029 | `tsai2023separation2` | Simpler deep network-based heart/lung separation example. |
| P037 | `zheng2025identifying2` | Separation plus hyperdimensional computing workflow. |
| P081 | `jakubec2025robust` | Recent PCG denoising model for preprocessing support. |
| P082 | `shuvo2026self` | Self-attention lung sound denoising model. |
| P083 | `behera2026adaptive` | UNet-based respiratory denoising method. |
| P084 | `pouyani2022signal` | DWT-ANN denoising support for lung sounds. |

## 2.6 Datasets for Cardiopulmonary Sound Separation

| Paper | Citation key | Why it is used |
|---|---|---|
| P011 | `roy2024pcgreview` | Background on PCG datasets and preprocessing pipelines. |
| P019 | `zhao2024heartanalysis` | Background on heart sound datasets and deep learning applications. |
| P038 | `torabi2025hlscmds` | Primary HLS-CMDS dataset descriptor; contains mixed and source heart/lung recordings. |
| P066 | `ali2026buet2` | Public heart sound dataset support, clearly not a separation dataset. |
| P075 | `hoang2023reliable` | Respiratory sound dataset and baseline AI context. |
| P080 | `reyna2023murmur` | PhysioNet/CirCor benchmark context for PCG evaluation and datasets. |

## 2.7 Evaluation Metrics

| Paper | Citation key | Why it is used |
|---|---|---|
| P005 | `grooby2023noisyneonatal` | Separation baseline metrics and neonatal chest sound evaluation context. |
| P013 | `sun2024daenmfvmd` | Hybrid separation metrics and method comparison context. |
| P016 | `wang2023mcunet` | Standard metric comparison for robust heart-lung separation. |
| P017 | `wang2023nmfdl` | NMF/deep learning evaluation context. |
| P022 | `wang2025phase2` | Phase-aware and single-channel separation evaluation emphasis. |
| P035 | `zhang2026efficient2` | Objective metrics for optimized VMD lung separation. |
| P037 | `zheng2025identifying2` | Distinguishes separation support from downstream classification metrics. |
| P065 | `somarathne2026dual2` | Heart sound onset/offset segmentation support. |
| P077 | `grooby2022real` | Input quality assessment for neonatal heart/lung sounds. |
| P080 | `reyna2023murmur` | Benchmark scoring context, used carefully as dataset/evaluation background. |
| P086 | `pal2024automatic` | Respiratory phase identification and segmentation evaluation support. |

## 2.8 Existing Systems and Prototype Relevance

| Paper | Citation key | Why it is used |
|---|---|---|
| P002 | `ali2023lunet` | Real-time denoising support and noisy-input handling for a software pipeline. |
| P009 | `poh2024neossnet` | Real-time separation relevance for a prototype system. |
| P074 | `arjoune2023stethaid` | Digital auscultation platform context. |
| P076 | `baeyens2025compressed` | Acquisition/reconstruction support for cardiopulmonary signal workflows. |
| P078 | `mutlu2024bridging` | TinyML/digital stethoscope implementation context, used as software-system background. |
| P082 | `shuvo2026self` | Real-time lung sound denoising support. |

## 2.9 Research Gaps

| Paper | Citation key | Why it is used |
|---|---|---|
| P005 | `grooby2023noisyneonatal` | Shows traditional baseline limits and neonatal data constraints. |
| P009 | `poh2024neossnet` | Shows real-time deep model strengths and private/clinical data limitations. |
| P013 | `sun2024daenmfvmd` | Shows hybrid method usefulness and reproducibility/data access limitations. |
| P016 | `wang2023mcunet` | Shows strong hybrid deep method but dataset/public access limitations. |
| P018 | `zhang2025jassnet` | Shows recent attention/semi-supervised method complexity. |
| P020 | `zheng2024cardiopulmonary` | Shows separation sometimes remains tied to classification objectives. |
| P021 | `poh2026reprogramming2` | Shows promise and complexity of model reprogramming. |
| P022 | `wang2025phase2` | Shows need for broader real-world validation and phase-aware evaluation. |
| P023 | `torabi2025large2` | Shows AI-assisted parameter tuning but also added system complexity. |
| P025 | `torabi2023negative2` | Shows synthetic/manikin evaluation limits in NMF baselines. |
| P035 | `zhang2026efficient2` | Shows simulated-mixture limitation in optimized decomposition work. |
| P038 | `torabi2025hlscmds` | Shows HLS-CMDS dataset value and manikin-data limitation. |
| P065 | `somarathne2026dual2` | Shows preprocessing/segmentation remains a separate unresolved support task. |
| P066 | `ali2026buet2` | Shows many useful datasets remain classification-oriented, not separation-ready. |
| P077 | `grooby2022real` | Shows need for quality assessment before/around separation. |
| P080 | `reyna2023murmur` | Shows benchmark value but classification-task mismatch. |
| P081 | `jakubec2025robust` | Shows denoising remains important before separation. |
| P086 | `pal2024automatic` | Shows segmentation/phase processing remains relevant to respiratory audio. |

## 2.10 Summary

| Paper | Citation key | Why it is used |
|---|---|---|
| P005 | `grooby2023noisyneonatal` | Summarizes traditional baseline evidence. |
| P009 | `poh2024neossnet` | Summarizes real-time deep learning separation evidence. |
| P015 | `ullah2024unsupervised` | Summarizes data-constrained unsupervised separation evidence. |
| P022 | `wang2025phase2` | Summarizes phase-aware modern deep separation evidence. |
| P038 | `torabi2025hlscmds` | Summarizes the primary dataset direction for the FYP. |
| P073 | `han2025cardiorespiratory` | Summarizes recent direct cardiorespiratory separation evidence. |

## Coverage Check

The draft uses all 35 recommended papers at least once:

`ali2023lunet`, `grooby2023noisyneonatal`, `poh2024neossnet`, `roy2024pcgreview`, `sun2024daenmfvmd`, `ullah2024unsupervised`, `wang2023mcunet`, `wang2023nmfdl`, `zhang2025jassnet`, `zhao2024heartanalysis`, `zheng2024cardiopulmonary`, `poh2026reprogramming2`, `wang2025phase2`, `torabi2025large2`, `torabi2023negative2`, `tsai2023separation2`, `zhang2026efficient2`, `zheng2025identifying2`, `torabi2025hlscmds`, `rocha2023automatic2`, `fattahi2022blind2`, `somarathne2026dual2`, `ali2026buet2`, `han2025cardiorespiratory`, `arjoune2023stethaid`, `hoang2023reliable`, `baeyens2025compressed`, `grooby2022real`, `mutlu2024bridging`, `reyna2023murmur`, `jakubec2025robust`, `shuvo2026self`, `behera2026adaptive`, `pouyani2022signal`, `pal2024automatic`.
