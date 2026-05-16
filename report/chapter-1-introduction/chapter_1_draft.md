# Chapter 1: Introduction

Draft status: first academic FYP1 draft. This chapter is aligned with the approved proposal for `Machine Learning-Based System for Cardiopulmonary Sound Separation` and should be reviewed by the supervisor before final report formatting.

## 1.1 Introduction / Background

Cardiopulmonary sounds are acoustic signals produced by heart activity and respiratory airflow. In practical auscultation, these sounds are commonly recorded from the chest using a stethoscope or digital stethoscope. Because the heart and lungs are close to each other anatomically and their acoustic components can overlap in a recording, a single chest sound signal may contain both heart sounds and lung sounds at the same time. This creates a signal separation problem: the system must estimate useful heart-related and lung-related components from a mixed cardiopulmonary recording.

Recent literature shows that cardiopulmonary sound processing is moving from purely traditional signal processing toward machine learning and deep learning approaches. Classical methods such as non-negative matrix factorization, blind filtering, and decomposition-based techniques remain useful because they are explainable and can work under limited-data conditions [@grooby2023noisyneonatal; @fattahi2022blind2]. More recent methods use deep learning architectures, phase-aware modeling, and hybrid approaches to improve single-channel chest sound separation [@poh2024neossnet; @wang2025phase2]. These studies show that machine learning-based sound separation is a relevant research and software development direction.

This project is proposed as an application-based Software Engineering FYP. The focus is not to diagnose heart or lung disease. Instead, the focus is to design and develop a structured software prototype that can accept mixed cardiopulmonary audio, perform preprocessing, apply a machine learning-based separation method, and produce separated heart sound and lung sound outputs. Publicly available or accessible datasets are important for this project because they allow the system to be tested and explained without relying on restricted clinical data. The HLS-CMDS dataset is especially relevant because it provides heart sounds, lung sounds, mixed recordings, and corresponding source signals recorded using a digital stethoscope and clinical manikin [@torabi2025hlscmds].

## 1.2 Problem Statement

Heart and lung sounds can overlap in both time and frequency when recorded together from the chest. This overlap can make it difficult to separate the two sound sources using simple filtering or manual inspection. Noise from recording conditions, stethoscope placement, breathing variation, and environmental interference can further reduce the quality of the recorded signal.

Existing research provides several methods for cardiopulmonary sound separation, including traditional signal processing, hybrid methods, and deep learning models [@grooby2023noisyneonatal; @poh2024neossnet; @sun2024daenmfvmd]. However, many works focus mainly on algorithms, classification tasks, or medical analysis outcomes rather than on a complete, reusable software prototype for sound separation. Some datasets are also designed for diagnosis or classification rather than paired source separation, which creates a practical challenge when building and evaluating a student-level system.

Therefore, the problem addressed in this project is the need for a structured machine learning-based software system that can separate mixed cardiopulmonary audio into heart and lung sound outputs, while remaining feasible for an FYP prototype. The system should support audio preprocessing, model-based separation, output generation, and evaluation using suitable signal-level metrics, without making unsupported clinical or diagnostic claims.

## 1.3 Project Aim

The aim of this project is to design and develop a machine learning-based software prototype for cardiopulmonary sound separation that can process mixed chest sound recordings and produce separated heart sound and lung sound outputs.

## 1.4 Project Objectives

The objectives of this project are:

1. To study existing techniques and datasets related to cardiopulmonary, heart-lung, and chest sound separation.
2. To design a software system architecture for processing mixed cardiopulmonary audio signals.
3. To implement audio preprocessing and machine learning-based separation modules for separating heart and lung sounds.
4. To test the system using suitable public or accessible audio datasets.
5. To evaluate the separated outputs using appropriate signal-level or separation-related metrics.

## 1.5 Project Scope

This project is limited to the development of a software prototype for cardiopulmonary sound separation. The system will focus on mixed audio recordings that contain heart and lung sound components and will produce two separated audio outputs: one representing the heart sound component and one representing the lung sound component.

The project scope includes:

1. Reviewing recent literature on cardiopulmonary sound separation, heart-lung sound separation, preprocessing, datasets, and evaluation metrics.
2. Using Python-based audio processing and machine learning tools to build the prototype.
3. Implementing preprocessing steps such as audio loading, normalization, segmentation or windowing where needed, and time-frequency representation where appropriate.
4. Implementing or adapting a machine learning-based separation approach suitable for the available dataset and project timeframe.
5. Using public or accessible datasets for training, testing, or evaluation, with attention to whether the dataset provides mixed and source audio signals.
6. Producing separated heart and lung sound files as the main system output.
7. Evaluating system performance using suitable metrics such as reconstruction quality, signal error, or source separation measures where reference signals are available.

The project scope excludes:

1. Medical diagnosis, disease detection, or clinical decision-making.
2. Hardware design or development of a physical digital stethoscope.
3. Claims that the system is clinically validated for patient use.
4. Use of private clinical datasets that cannot be accessed or cited appropriately.
5. Deployment as a production medical device.

The main constraints are the two-trimester FYP timeframe, dependence on publicly available or accessible datasets, and the performance limitations of the selected machine learning method. Since dataset availability strongly affects evaluation, the project will avoid overclaiming generalizability beyond the data used for testing.

## 1.6 Project Significance

The significance of this project is mainly in software prototyping and biomedical audio processing. A working cardiopulmonary sound separation system can demonstrate how mixed chest sound recordings may be processed into separate heart and lung audio outputs. This can support future research workflows where separated audio is useful for listening, visualization, preprocessing experiments, or later model development.

From a Software Engineering perspective, the project is significant because it converts the separation problem into a structured application workflow. Instead of producing only an isolated algorithm script, the project aims to develop a reusable prototype with clear input handling, preprocessing, model inference, output storage, and evaluation. This is aligned with the proposal's focus on an application-based prototype/proof of concept.

From a research perspective, the project is significant because recent literature identifies challenges in dataset availability, method selection, evaluation, and system integration for cardiopulmonary sound separation [@poh2024neossnet; @wang2025phase2; @torabi2025hlscmds]. The project does not claim to solve these challenges completely. Its contribution is to build a feasible student-level system that demonstrates a complete separation workflow and provides a foundation for future improvement.

## 1.7 Expected Output

The expected output of this project is a functional software prototype for cardiopulmonary sound separation. The prototype is expected to:

1. Accept a mixed cardiopulmonary audio input.
2. Apply preprocessing steps required for the selected separation method.
3. Use a machine learning-based model or model-assisted pipeline to separate the input signal.
4. Produce two separated audio outputs: a heart sound output and a lung sound output.
5. Store or present the separated outputs so they can be reviewed by the user.
6. Report suitable evaluation results where reference signals or comparison data are available.

The final output is intended to be a proof of concept. It should demonstrate the feasibility of the proposed software workflow, but it should not be presented as a clinically approved diagnostic system.

## 1.8 Report Organization

This report is organized into six chapters.

Chapter 1 introduces the project background, problem statement, aim, objectives, scope, significance, expected output, and report organization.

Chapter 2 reviews recent literature related to cardiopulmonary sound characteristics, heart-lung sound separation, traditional signal processing methods, machine learning and deep learning methods, datasets, evaluation metrics, existing systems, and research gaps.

Chapter 3 will present the project methodology or requirements analysis, including the proposed development approach, data sources, preprocessing workflow, model selection, and evaluation plan.

Chapter 4 will describe the system design and implementation plan, including the software architecture, major modules, data flow, and user interaction design for the prototype.

Chapter 5 will present the testing and evaluation plan or implementation progress, depending on the final FYP1 reporting structure. This chapter will describe how the prototype will be tested and how separation results will be assessed.

Chapter 6 will summarize the work completed during FYP1, discuss limitations and issues encountered, and outline the remaining work for the next phase of the project.
