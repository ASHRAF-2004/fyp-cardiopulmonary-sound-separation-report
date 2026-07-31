# Google Form Creation Guide: User Requirements Questionnaire for Machine Learning-Based Cardiopulmonary Sound Separation System

## Document Purpose

This guide explains how to manually create the Google Form for the user requirements questionnaire of the Final Year Project titled **Machine Learning-Based System for Cardiopulmonary Sound Separation**.

The questionnaire is required for Chapter 3 Requirements Analysis. It will be used to collect practical user requirements for the proposed prototype, including current challenges, preferred system features, interface expectations, result presentation preferences, and evaluation needs.

This guide does not create or distribute the Google Form automatically. It is intended to be followed manually in Google Forms.

## Target Respondents

The questionnaire is intended for respondents who can provide useful feedback about a software prototype for cardiopulmonary sound separation. Suitable respondent groups include:

- Software Engineering / Computer Science students
- AI / Machine Learning students
- Biomedical Engineering / health-related students
- Researchers or students interested in biomedical audio or signal processing
- Supervisors or evaluators where appropriate

## Google Form Title

Use this title exactly:

**User Requirements Questionnaire for Machine Learning-Based Cardiopulmonary Sound Separation System**

## Google Form Description / Introduction

Paste the following text into the Google Form description:

> Welcome and thank you for participating in this questionnaire.
>
> This questionnaire is conducted as part of a Final Year Project at Multimedia University (MMU) involving the development of a machine learning-based system for cardiopulmonary sound separation. The proposed system aims to allow users to upload a mixed cardiopulmonary audio recording and obtain separated heart and lung sound outputs.
>
> The purpose of this questionnaire is to understand user background, current challenges in working with biomedical or audio-processing tasks, and user preferences regarding system features, interface design, output presentation, and evaluation needs.
>
> Your responses will help identify user requirements and support the design of the proposed prototype. There are no right or wrong answers. All responses will be used for academic purposes only and will remain confidential.
>
> Estimated completion time: 3-5 minutes.

## Manual Google Forms Setup Steps

1. Go to `https://forms.google.com` and click **Blank Form**.
2. Set the form title to **User Requirements Questionnaire for Machine Learning-Based Cardiopulmonary Sound Separation System**.
3. Paste the introduction text from this guide into the form description.
4. Create these sections:
   - Section A - Respondent Background
   - Section B - Current Challenges in Cardiopulmonary Audio Processing
   - Section C - System Feature Preferences
   - Section D - Interface and Output Preferences
   - Section E - Evaluation and Improvement
5. Add all questions exactly as listed in this guide.
6. Set all objective questions as **Required**. Set the final open-ended paragraph question as **Required** only when the supervisor wants complete written feedback; otherwise it may be left not required. The questionnaire itself is still required for the project.
7. Open **Settings** and configure:
   - Collect email addresses: Off unless supervisor requires it
   - Limit to 1 response: Off unless using MMU accounts only
   - Allow response editing: Off
   - Show progress bar: On
   - Shuffle question order: Off
   - Make this a quiz: Off
8. Click **Preview** and test the form.
9. Send the form link to target respondents.
10. After collecting responses, export responses to Google Sheets or CSV for Chapter 3 analysis.

## Section A - Respondent Background

### Q1. What is your age group?

| Field | Value |
|---|---|
| Type | Multiple choice |
| Required | Yes |
| Options | Under 18; 18-25; 26-35; 36 and above |

### Q2. What best describes you?

| Field | Value |
|---|---|
| Type | Multiple choice |
| Required | Yes |
| Options | Software Engineering / Computer Science student; AI / Machine Learning student; Biomedical Engineering / Health-related student; Researcher; Lecturer / Supervisor; Other |

### Q3. How familiar are you with audio processing or signal processing?

| Field | Value |
|---|---|
| Type | Multiple choice |
| Required | Yes |
| Options | Not familiar; Basic; Intermediate; Advanced |

### Q4. Have you worked with biomedical audio before?

| Field | Value |
|---|---|
| Type | Multiple choice |
| Required | Yes |
| Options | Yes; No; Not sure |

### Q5. Which type of audio-related task are you most familiar with?

| Field | Value |
|---|---|
| Type | Multiple choice |
| Required | Yes |
| Options | Audio recording; Audio editing; Audio classification; Audio separation; Machine learning model testing; I have not worked with audio tasks before |

## Section B - Current Challenges in Cardiopulmonary Audio Processing

### Q6. How difficult do you think it is to separate heart and lung sounds from a mixed cardiopulmonary recording?

| Field | Value |
|---|---|
| Type | Multiple choice |
| Required | Yes |
| Options | Very easy; Easy; Neutral; Difficult; Very difficult |

### Q7. What problems do you think affect cardiopulmonary sound processing the most?

| Field | Value |
|---|---|
| Type | Checkboxes |
| Required | Yes |
| Options | Background noise; Overlap between heart and lung sounds; Low recording quality; Difficulty identifying useful sound components; Lack of simple software tools; Lack of clear output visualization; Other |

### Q8. Do you think noisy audio recordings can reduce the quality of machine learning-based sound processing?

| Field | Value |
|---|---|
| Type | Linear scale or Likert multiple choice |
| Required | Yes |
| Options | Strongly disagree; Disagree; Neutral; Agree; Strongly agree |

### Q9. Do you think a simple software prototype for heart-lung sound separation would be useful for students or researchers?

| Field | Value |
|---|---|
| Type | Linear scale or Likert multiple choice |
| Required | Yes |
| Options | Strongly disagree; Disagree; Neutral; Agree; Strongly agree |

## Section C - System Feature Preferences

### Q10. Which feature would be most important in the proposed system?

| Field | Value |
|---|---|
| Type | Multiple choice |
| Required | Yes |
| Options | Upload mixed cardiopulmonary audio; Preprocess noisy audio; Separate heart and lung sounds; Preview separated audio; Download separated outputs; View processing history; View evaluation results |

### Q11. Which output would you prefer after sound separation?

| Field | Value |
|---|---|
| Type | Multiple choice |
| Required | Yes |
| Options | Heart and lung audio files only; Audio files with waveform visualization; Audio files with spectrogram visualization; Audio files with evaluation metrics; All of the above |

### Q12. How important is it for the system to provide a preview of the separated heart and lung sounds?

| Field | Value |
|---|---|
| Type | Linear scale or Likert multiple choice |
| Required | Yes |
| Options | Not important; Slightly important; Moderately important; Important; Very important |

### Q13. How important is it for the system to allow users to download separated audio outputs?

| Field | Value |
|---|---|
| Type | Linear scale or Likert multiple choice |
| Required | Yes |
| Options | Not important; Slightly important; Moderately important; Important; Very important |

### Q14. How important is it for the system to show basic processing information, such as file name, processing status, and completion time?

| Field | Value |
|---|---|
| Type | Linear scale or Likert multiple choice |
| Required | Yes |
| Options | Not important; Slightly important; Moderately important; Important; Very important |

### Q15. Should the system include a history page showing previously uploaded files and separation results?

| Field | Value |
|---|---|
| Type | Multiple choice |
| Required | Yes |
| Options | Yes; No; Not sure |

## Section D - Interface and Output Preferences

### Q16. How would you prefer the separated results to be displayed?

| Field | Value |
|---|---|
| Type | Multiple choice |
| Required | Yes |
| Options | Simple audio player only; Audio player with waveform; Audio player with spectrogram; Audio player with waveform, spectrogram, and metrics; Not sure |

### Q17. Which interface style would you prefer?

| Field | Value |
|---|---|
| Type | Multiple choice |
| Required | Yes |
| Options | Simple interface with only main features; Detailed interface with many technical options; Balanced interface with simple view and optional advanced details |

### Q18. How important is it for the system interface to be easy for non-expert users?

| Field | Value |
|---|---|
| Type | Linear scale or Likert multiple choice |
| Required | Yes |
| Options | Not important; Slightly important; Moderately important; Important; Very important |

### Q19. What information should appear first after separation is completed?

| Field | Value |
|---|---|
| Type | Multiple choice |
| Required | Yes |
| Options | Download buttons for heart and lung sounds; Audio preview players; Waveform or spectrogram visualization; Evaluation metrics; Processing status summary |

### Q20. What type of error message would be most helpful if the uploaded file is invalid?

| Field | Value |
|---|---|
| Type | Multiple choice |
| Required | Yes |
| Options | Short message only; Message explaining the problem; Message explaining the problem and suggested fix; Not sure |

## Section E - Evaluation and Improvement

### Q21. How important is it for the system to show evaluation metrics for the separated output?

| Field | Value |
|---|---|
| Type | Linear scale or Likert multiple choice |
| Required | Yes |
| Options | Not important; Slightly important; Moderately important; Important; Very important |

### Q22. Which evaluation information would be most useful?

| Field | Value |
|---|---|
| Type | Multiple choice |
| Required | Yes |
| Options | Signal quality score; Separation accuracy score; Noise reduction information; Processing time; All of the above |

### Q23. Would you use a prototype that separates mixed cardiopulmonary audio into heart and lung sound outputs?

| Field | Value |
|---|---|
| Type | Multiple choice |
| Required | Yes |
| Options | Yes; No; Maybe |

### Q24. What improvement or feature would you like to see in a cardiopulmonary sound separation system?

| Field | Value |
|---|---|
| Type | Paragraph answer |
| Required | No unless supervisor requires complete written feedback |

## After Response Collection

After real responses are collected, export the Google Form responses to Google Sheets or CSV. Use the real response data to replace the Chapter 3 placeholder figures, summarize findings, and refine the functional, non-functional, and user requirements. Do not insert percentages, charts, or findings until real response data exists.
