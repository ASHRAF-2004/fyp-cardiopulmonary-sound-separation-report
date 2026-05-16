# Chapter 3 Notes

Draft date: 2026-05-16

## Assumptions Made

1. The corrected report title is `Machine Learning-Based System for Cardiopulmonary Sound Separation`.
2. The project remains an application-based Software Engineering FYP with a prototype/proof-of-concept contribution.
3. Python is the main implementation language, consistent with the proposal.
4. The prototype will process mixed cardiopulmonary audio and produce separated heart and lung sound outputs.
5. The project does not include medical diagnosis, disease detection, clinical decision-making, or hardware development.
6. Public or accessible datasets will be used for training, testing, or evaluation.
7. HLS-CMDS is treated as the strongest current dataset candidate because `dataset_inventory.csv` records heart sounds, lung sounds, mixed sounds, and source signals.
8. The final machine learning model has not yet been selected, so the methodology describes feasible model families rather than one fixed architecture.
9. Evaluation metrics are described as planned categories because the final metrics depend on the chosen dataset and model.

## Missing Technical Details Requiring Supervisor Confirmation

1. Whether Chapter 3 should be titled "Methodology" as requested here or "Requirements Analysis" to match the application-based FYP1 handbook structure.
2. Which dataset will be used first for implementation and whether HLS-CMDS should be downloaded and used as the primary experiment dataset.
3. Whether the project should train a model from scratch, adapt an existing model, or implement a simpler baseline plus a lightweight ML model.
4. Whether the system should be a command-line prototype, notebook-based prototype, desktop/web interface, or backend/API plus frontend.
5. Which exact evaluation metrics should be reported in FYP1 and which should be reserved for FYP2.
6. Whether a baseline method such as NMF should be implemented for comparison.
7. Whether the final report should include requirements analysis content in Chapter 3 or move it to Chapter 4.

## Parts That Depend on Final Prototype Implementation

| Draft section | Depends on implementation detail |
|---|---|
| Dataset Selection and Preparation | Final dataset availability, folder structure, file format, train/validation/test split, and license/access handling. |
| Audio Preprocessing | Final sample rate, segment duration, silence trimming, normalization, filtering, and padding strategy. |
| Feature Extraction / Input Representation | Whether the model uses raw waveform, STFT, mel spectrogram, magnitude/phase representation, or learned features. |
| Machine Learning Model Approach | Final model architecture, training strategy, loss functions, baselines, and model complexity. |
| System Architecture Overview | Whether the prototype is script-based, notebook-based, web-based, or API-based. |
| System Modules | Actual module names, file paths, storage design, and user interaction flow. |
| Evaluation Methodology | Final metrics, reference source availability, qualitative review process, and testing sample size. |
| Tools and Technologies | Final audio libraries, ML framework, plotting tools, and interface framework. |

## Diagrams to Create Later

The following diagrams should be created after the implementation direction is confirmed:

1. Methodology workflow diagram showing dataset selection, preprocessing, model separation, reconstruction, and evaluation.
2. System architecture diagram showing input, preprocessing, model, output storage, evaluation, and interface layers.
3. Data flow diagram for mixed audio input to separated heart/lung outputs.
4. Module interaction diagram showing how the main software modules communicate.
5. Dataset preparation flowchart showing raw dataset, metadata extraction, preprocessing, splitting, and evaluation inputs.
6. Evaluation workflow diagram showing reference signals, separated outputs, metrics, and result reporting.

## Citation and Scope Notes

The draft uses existing citation keys from `literature-review/references/references.bib` only. Citations are used for method families, dataset rationale, preprocessing context, and evaluation rationale. No new references were added and `references.bib` was not edited.

The methodology intentionally avoids medical diagnosis claims. Papers related to disease classification or clinical use should remain background evidence only unless the project scope changes with supervisor approval.
