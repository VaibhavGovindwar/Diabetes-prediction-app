# 🩺 Diabetes Prediction using Binary Classification

The Pima Indians Diabetes Dataset is a well-known benchmark dataset from the UCI Machine Learning Repository used for binary classification tasks. The dataset originates from a study by the National Institute of Diabetes and Digestive and Kidney Diseases, aiming to predict whether a patient is likely to develop diabetes based on specific diagnostic measurements.  
This is a web application built with **Streamlit** that predicts whether a person is likely to be diabetic based on input health parameters. It uses a pre-trained deep learning model (.keras) and a `StandardScaler` object (.save) hosted on Google Drive for download during runtime.

## 📁 Dataset Information:
Total Samples: 768.  

Features: 8 numerical features.  

Target: Binary (0 = No Diabetes, 1 = Diabetes).  

## 🧪 Features Used:

1. Pregnancies – Number of times pregnant.
2. Glucose – Plasma glucose concentration.
3. BloodPressure – Diastolic blood pressure (mm Hg).
4. SkinThickness – Triceps skin fold thickness (mm).
5. Insulin – 2-Hour serum insulin (mu U/ml)
6. BMI – Body mass index (weight in kg/(height in m)^2)
7. DiabetesPedigreeFunction – A function that scores likelihood of diabetes based on family history
8. Age – Age in years
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

## ⚙️ Tools & Techniques:  

TensorFlow / Keras for model building.  

StandardScaler for data normalization.  

Train-test split for model validation.  

Binary Crossentropy Loss and Adam Optimizer.  

Accuracy as performance metric.  

## ✅ Outcomes:  
Achieved consistent accuracy on unseen test data.  

Demonstrated how deep learning can be applied to structured medical data.  

Built a clean and modular pipeline for binary classification problems.  
