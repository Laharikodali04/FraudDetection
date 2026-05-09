import streamlit as st
import joblib
import numpy as np

<<<<<<< HEAD
# Load trained model
model = joblib.load("models/fraud_model.pkl")

# Page settings
=======
# Load model
model = joblib.load("../models/fraud_model.pkl")

# Page config
>>>>>>> c954d8bde715767772a05ab88f7a33a23104a77a
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

<<<<<<< HEAD
# Store inputs
features = []

# Create 30 input fields
=======
features = []

# Input fields
>>>>>>> c954d8bde715767772a05ab88f7a33a23104a77a
for i in range(30):
    value = st.number_input(f"Feature V{i}", value=0.0)
    features.append(value)

<<<<<<< HEAD
# Predict button
if st.button("Predict Transaction"):

    # Convert to numpy array
    input_data = np.array(features).reshape(1, -1)

    # Prediction
    prediction = model.predict(input_data)
=======
# Prediction button
if st.button("Predict Transaction"):

    prediction = model.predict([features])
>>>>>>> c954d8bde715767772a05ab88f7a33a23104a77a

    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.error("⚠ Fraudulent Transaction Detected")
    else:
        st.success("✅ Normal Transaction")

<<<<<<< HEAD
# Footer
=======
>>>>>>> c954d8bde715767772a05ab88f7a33a23104a77a
st.markdown("---")
st.caption("Built using Machine Learning and Streamlit")