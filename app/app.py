import streamlit as st
import joblib
import numpy as np

# Load model


import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "notebooks", "models", "fraud_model.pkl")
model = joblib.load(model_path)
# Page config
st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="💳",
    layout="centered"
)

# Title
st.title("💳 Credit Card Fraud Detection System")

st.markdown("""
This application predicts whether a credit card transaction is:

- ✅ Normal Transaction
- ⚠ Fraudulent Transaction

Enter transaction feature values below.
""")

features = []

# Input fields
for i in range(30):
    value = st.number_input(f"Feature V{i}", value=0.0)
    features.append(value)

# Prediction button
if st.button("Predict Transaction"):

    prediction = model.predict([features])

    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.error("⚠ Fraudulent Transaction Detected")
    else:
        st.success("✅ Normal Transaction")

st.markdown("---")
st.caption("Built using Machine Learning and Streamlit")
