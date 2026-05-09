import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("models/fraud_model.pkl")

# Page settings
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

# Store inputs
features = []

# Create 30 input fields
for i in range(30):
    value = st.number_input(f"Feature V{i}", value=0.0)
    features.append(value)

# Predict button
if st.button("Predict Transaction"):

    # Convert to numpy array
    input_data = np.array(features).reshape(1, -1)

    # Prediction
    prediction = model.predict(input_data)

    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.error("⚠ Fraudulent Transaction Detected")
    else:
        st.success("✅ Normal Transaction")

# Footer
st.markdown("---")
st.caption("Built using Machine Learning and Streamlit")