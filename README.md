# HeartDiseasePrediction

# Heart Disease Prediction using Machine Learning and Streamlit

This project presents a web application designed to predict the likelihood of heart disease in individuals based on various health parameters. The application leverages a machine learning model and is implemented using Streamlit for an interactive user interface.

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Features](#features)
- [Usage](#usage)
- [Model Training](#model-training)

## Overview

Cardiovascular diseases are a leading cause of mortality globally. Early detection and intervention can significantly improve patient outcomes. This project aims to assist in the early prediction of heart disease by analyzing patient data through a machine learning model.

## Dataset

The model is trained on the [Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+disease) from the UCI Machine Learning Repository. This dataset comprises several medical attributes related to heart health.

**Attributes:**

1. **Age**: Age of the individual.
2. **Sex**: Gender (1 = male; 0 = female).
3. **Chest Pain Type (cp)**:
   - 0: Typical Angina
   - 1: Atypical Angina
   - 2: Non-anginal Pain
   - 3: Asymptomatic
4. **Resting Blood Pressure (trestbps)**: In mm Hg.
5. **Serum Cholesterol (chol)**: In mg/dl.
6. **Fasting Blood Sugar (fbs)**: > 120 mg/dl (1 = true; 0 = false).
7. **Resting Electrocardiographic Results (restecg)**:
   - 0: Normal
   - 1: ST-T wave abnormality
   - 2: Left ventricular hypertrophy
8. **Maximum Heart Rate Achieved (thalach)**.
9. **Exercise Induced Angina (exang)**: (1 = yes; 0 = no).
10. **ST Depression Induced by Exercise (oldpeak)**.
11. **Slope of the Peak Exercise ST Segment (slope)**:
    - 0: Upsloping
    - 1: Flat
    - 2: Downsloping
12. **Number of Major Vessels Colored by Fluoroscopy (ca)**: 0–3.
13. **Thalassemia (thal)**:
    - 0: Normal
    - 1: Fixed Defect
    - 2: Reversible Defect
14. **Target**: Diagnosis of heart disease (1 = presence; 0 = absence).

## Features

- **User-Friendly Interface**: Input patient data through an intuitive web interface.
- **Real-Time Prediction**: Obtain immediate predictions on heart disease likelihood.
- **Data Visualization**: Visual representations of input data distributions.
- **Model Explainability**: Insights into feature importance using SHAP values.

Model Training
The machine learning model is developed using the following steps:

Data Preprocessing: Handling missing values, encoding categorical variables, and feature scaling.

Exploratory Data Analysis (EDA): Understanding data distributions and relationships.

Model Selection: Evaluating various algorithms to identify the best performer.

Training and Evaluation: Training the selected model and assessing its performance using appropriate metrics.

Explainability: Utilizing SHAP values to interpret model predictions.


Run the Streamlit Application:
streamlit run SL_App.py

Interact with the App:

Input the required health parameters.
Visualize the contribution of each feature to the prediction.
