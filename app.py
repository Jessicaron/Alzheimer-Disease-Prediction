import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("alzheimers_model.pkl")

st.title("🧠 Alzheimer's Disease Prediction System")

st.write("Enter gene expression values:")

# Inputs (same 3 genes you used)
dph2 = st.number_input("DPH2")
znf449 = st.number_input("ZNF449")
rabgef1 = st.number_input("RABGEF1")

if st.button("Predict"):
    features = np.array([[dph2, znf449, rabgef1]])
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.error("🧠 Alzheimer's Detected")
    else:
        st.success("✅ Healthy")