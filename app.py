
import streamlit as st
import numpy as np
import joblib
from tensorflow.keras.models import load_model
from PIL import Image
import base64
import os
import gdown

# ---- CONFIG ----
MODEL_DRIVE_ID = "1cRgj5rD8AxNxNhgfHTarJOMSn7zmZ3cR"        # Replace with your .keras file ID
SCALER_DRIVE_ID = "116xY6ceBm7VwgZa5RcBPSJcaolyhroUd"       # Replace with your scaler.save file ID

# ---- DOWNLOAD FILES IF NOT EXISTS ----
def download_from_drive(file_id, filename):
    if not os.path.exists(filename):
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, filename, quiet=False)

download_from_drive(MODEL_DRIVE_ID, "diabetes_model.keras")
download_from_drive(SCALER_DRIVE_ID, "scaler.save")

# ---- LOAD FILES ----
model = load_model("diabetes_model.keras")
scaler = joblib.load("scaler.save")

# Set background image using base64
def add_bg(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            font-family: 'sans-serif';
            overflow: hidden;
        }}

        h1{{
            position: fixed;
            top: 45px;
            left: 0;
            width: 100%;
            padding: 1rem;
            text-align: center;
            z-index: 100;
            font-size: 28px;
            font-weight: bold;

        }}
        .block-container {{
            padding-top: 80px;
            position: fixed;
            margin-left: -650px
        }}
        .left-form {{
            margin-left: -100px;
            padding: 20px;
            border-radius: 12px;
            max-width: 100px;
        }}

        label, .stNumberInput > label {{
            color: white !important;
        }}
        .css-1cpxqw2 {{
            color: white !important;
        }}
        input{{
            max-width: 100px !important;
            overflow: hidden;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg("diabetes-prediction.jpg")  # Your uploaded image path

# Page layout settings
st.markdown("<h1 style='color: white;'>DIABETES PREDICTION APP</h1>", unsafe_allow_html=True)

# Left-aligned form box in 2x4 grid
with st.container():
    st.markdown("<div class='left-form'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
        blood_pressure = st.number_input("Blood Pressure", min_value=0)
        insulin = st.number_input("Insulin", min_value=0.0)
        dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)

    with col2:
        glucose = st.number_input("Glucose", min_value=0)
        skin_thickness = st.number_input("Skin Thickness", min_value=0)
        bmi = st.number_input("BMI", min_value=0.0)
        age = st.number_input("Age", min_value=0)

# Prediction button and result
if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                            insulin, bmi, dpf, age]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0][0]
    result = "Diabetic" if prediction >= 0.5 else "Not Diabetic"
    st.markdown(f"<h3 style='color:white;'>Prediction: {result}</h3>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='color:white;'>Probability: {prediction:.2f}</h4>", unsafe_allow_html=True)
