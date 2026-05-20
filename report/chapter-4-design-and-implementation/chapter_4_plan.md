# Chapter 4 Design and Implementation Plan

FYP title: Machine Learning-Based System for Cardiopulmonary Sound Separation

Purpose: This file prepares the direction for Chapter 4 only. It is not a full Chapter 4 draft.

## 1. Introduction

- Briefly explain that Chapter 4 will describe how the proposed software prototype is designed and implemented.
- Link the chapter to Chapter 3 methodology and keep the focus on cardiopulmonary sound separation rather than disease diagnosis.

## 2. System Overview

- Describe the prototype as a software system that accepts mixed cardiopulmonary audio and produces separated heart and lung sound outputs.
- Explain the main user flow: upload/select audio, preprocess audio, run separation model, save outputs, and view or download results.

## 3. System Architecture

- Present the high-level architecture of the prototype.
- Show the interaction between user interface, backend/application logic, preprocessing service, separation model, storage, and evaluation module.

## 4. Main Modules

- Audio input module.
- Preprocessing module.
- Feature/input representation module.
- Machine learning separation module.
- Output management module.
- Evaluation module.
- User interface module.

## 5. Database / Storage Design

- Define what metadata should be stored for each processing job.
- Store file paths and processing metadata rather than large audio content inside the database unless a strong reason is confirmed.
- Include upload path, separated heart sound output path, separated lung sound output path, processing status, parameters, timestamps, and metric results.

## 6. Audio Upload and Preprocessing Flow

- Explain how input audio is accepted and validated.
- Include likely preprocessing steps such as loading, resampling, mono conversion if needed, normalization, segmentation/windowing, and time-frequency representation.
- Clarify which preprocessing steps depend on the final model choice.

## 7. Separation Model Integration

- Describe how the selected machine learning or model-assisted separation approach will be integrated into the prototype.
- Include input format, model inference flow, output reconstruction, and error handling.
- Keep the implementation feasible for an FYP prototype.

## 8. Output and Result Management

- Explain how separated heart and lung sound outputs are stored and presented.
- Include output file naming, result metadata, metric display, and basic user review.

## 9. User Interface Design

- Plan the main screens or interface sections: upload area, processing status, separated output review, metric summary, and history/results section.
- Keep the interface simple and suitable for demonstrating the prototype during viva or supervisor review.

## 10. Chapter Summary

- Summarize how the design supports the project objectives.
- Transition to the later implementation, testing, and evaluation chapters.

## 11. Required Diagrams

- System architecture diagram.
- Data flow diagram for audio upload, preprocessing, separation, and output generation.
- Use case diagram.
- Activity diagram for the separation workflow.
- Sequence diagram for upload-to-result processing.
- Database/storage schema diagram.
- User interface wireframe or screen flow diagram.
