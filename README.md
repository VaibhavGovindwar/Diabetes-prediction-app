# 🩺 Diabetes Prediction App using Streamlit

This is a web application built with **Streamlit** that predicts whether a person is likely to be diabetic based on input health parameters. It uses a pre-trained deep learning model (.keras) and a `StandardScaler` object (.save) hosted on Google Drive for download during runtime.

## 🚀 Features

- 📦 Pre-trained model for diabetes prediction
- 📊 Takes 8 standard medical inputs:
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age
- 🎨 Beautiful custom background and styling
- ☁️ Model and scaler are downloaded automatically from Google Drive

---

## 📁 Folder Structure
├── app.py # Main Streamlit app  
├── Pima Indian Diabetes (Binary Classification) # Python code  
├── dataset.csv # dataset  
├── requirements.txt # Python dependencies  
├── diabetes-prediction.jpg # Background image  
└── README.md # This file  



---

## 🧠 Model Details

- Model Format: `.keras`  
- Scaler Format: `.save` (joblib)
- Auto-downloaded via `gdown` from Google Drive

---

## 🔧 Installation & Running Locally

1. **Clone the Repository**

```bash
git clone https://github.com/VaibhavGovindwar/Diabetes-prediction-app.git
cd Diabetes-prediction-app
```

2. Install Dependencies

```bash
pip install -r requirements.txt
```
3. Run the App

```bash
streamlit run app.py
```
The app will open in your default browser.
