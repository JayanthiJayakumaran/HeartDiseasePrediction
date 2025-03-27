#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load(r"C:\Users\jayan\Downloads\Heart disease predictor\Models\xgb_heart_model.pkl")

# Title of the app
st.title('Heart Disease Risk Prediction')

# Sidebar for user input parameters
st.sidebar.header('User Input Parameters')

def user_input_features():
    age = st.sidebar.slider('Age', 29, 77, 54)
    sex = st.sidebar.selectbox('Sex', ('Male', 'Female'))
    cp = st.sidebar.selectbox('Chest Pain Type', ('Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'))
    trestbps = st.sidebar.slider('Resting Blood Pressure (mm Hg)', 94, 200, 130)
    chol = st.sidebar.slider('Serum Cholesterol (mg/dl)', 126, 564, 246)
    fbs = st.sidebar.selectbox('Fasting Blood Sugar > 120 mg/dl', ('Yes', 'No'))
    restecg = st.sidebar.selectbox('Resting Electrocardiographic Results', ('Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'))
    thalach = st.sidebar.slider('Maximum Heart Rate Achieved', 71, 202, 150)
    exang = st.sidebar.selectbox('Exercise Induced Angina', ('Yes', 'No'))
    oldpeak = st.sidebar.slider('ST Depression Induced by Exercise', 0.0, 6.2, 1.0)
    slope = st.sidebar.selectbox('Slope of the Peak Exercise ST Segment', ('Upsloping', 'Flat', 'Downsloping'))
    ca = st.sidebar.slider('Number of Major Vessels Colored by Fluoroscopy', 0, 3, 1)
    thal = st.sidebar.selectbox('Thalassemia', ('Normal', 'Fixed Defect', 'Reversible Defect'))
    
    data = {
        'age': age,
        'sex': 1 if sex == 'Male' else 0,
        'cp': ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'].index(cp),
        'trestbps': trestbps,
        'chol': chol,
        'fbs': 1 if fbs == 'Yes' else 0,
        'restecg': ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'].index(restecg),
        'thalach': thalach,
        'exang': 1 if exang == 'Yes' else 0,
        'oldpeak': oldpeak,
        'slope': ['Upsloping', 'Flat', 'Downsloping'].index(slope),
        'ca': ca,
        'thal': ['Normal', 'Fixed Defect', 'Reversible Defect'].index(thal)
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Display user input
st.subheader('User Input Parameters')
st.write(input_df)

# Prediction
prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

st.subheader('Prediction')
st.write('Heart Disease' if prediction[0] == 1 else 'No Heart Disease')

st.subheader('Prediction Probability')
st.write(f'Probability of Heart Disease: {prediction_proba[0][1]:.2f}')
st.write(f'Probability of No Heart Disease: {prediction_proba[0][0]:.2f}')

