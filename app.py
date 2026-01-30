import streamlit as st
import numpy as np
import joblib
import os

MODEL_PATH = "best_fire_detection_model.pkl"
SCALER_PATH = "scaler.pkl"

model = None
scaler = None

if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    st.success("Model and scaler loaded")
else:
    st.warning("Model/Scaler not found. Running in CI mode (mock).")

st.set_page_config(page_title="Fire Type Classifier", layout="centered")
st.title("Fire Type Classification")
st.markdown("Predict fire type based on MODIS satellite readings.")

brightness = st.number_input("Brightness", value=300.0)
bright_t31 = st.number_input("Brightness T31", value=290.0)
frp = st.number_input("Fire Radiative Power (FRP)", value=15.0)
scan = st.number_input("Scan", value=1.0)
track = st.number_input("Track", value=1.0)
confidence = st.selectbox("Confidence Level", ["low", "nominal", "high"])

confidence_map = {"low": 0, "nominal": 1, "high": 2}
confidence_val = confidence_map[confidence]

input_data = np.array([[brightness, bright_t31, frp, scan, track, confidence_val]])

if st.button("Predict Fire Type"):
    if model is None or scaler is None:
        st.info("CI mode: returning dummy prediction")
        st.success("**Predicted Fire Type:** Vegetation Fire (Mock)")
    else:
        scaled_input = scaler.transform(input_data)
        prediction = model.predict(scaled_input)[0]

        fire_types = {
            0: "Vegetation Fire",
            2: "Other Static Land Source",
            3: "Offshore Fire"
        }

        result = fire_types.get(prediction, "Unknown")
        st.success(f"**Predicted Fire Type:** {result}")
