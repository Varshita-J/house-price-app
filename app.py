import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)
st.title("🏠 House Price Prediction App")

# ----------- Model Loading -----------
model_path = "rf_pipeline_model.pkl"

if not os.path.exists(model_path):
    st.error("Model file not found. Please check path.")
    st.stop()

try:
    model = joblib.load(model_path)
    st.success("Model loaded successfully")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()


# ----------- User Inputs -----------
st.sidebar.header("Enter House Features")

MedInc = st.sidebar.number_input("Median Income", 0.0)
HouseAge = st.sidebar.number_input("House Age", 0.0)
AveRooms = st.sidebar.number_input("Average Rooms", 0.0)
AveBedrms = st.sidebar.number_input("Average Bedrooms", 0.0)
Population = st.sidebar.number_input("Population", 0.0)
AveOccup = st.sidebar.number_input("Average Occupancy", 0.0)
Latitude = st.sidebar.number_input("Latitude", -90.0, 90.0)
Longitude = st.sidebar.number_input("Longitude", -180.0, 180.0)


# ----------- Prediction -----------
if st.button("🔮 Predict", type="primary"):
    input_df = pd.DataFrame(
        [[
            MedInc,
            HouseAge,
            AveRooms,
            AveBedrms,
            Population,
            AveOccup,
            Latitude,
            Longitude
        ]],
        columns=[
            "MedInc",
            "HouseAge",
            "AveRooms",
            "AveBedrms",
            "Population",
            "AveOccup",
            "Latitude",
            "Longitude"
        ]
    )

    st.subheader("Entered Values")

    st.write({
    "Median Income": MedInc,
    "House Age": HouseAge,
    "Average Rooms": AveRooms,
    "Average Bedrooms": AveBedrms,
    "Population": Population,
    "Average Occupancy": AveOccup,
    "Latitude": Latitude,
    "Longitude": Longitude
    })

    prediction = model.predict(input_df)

    PRICE_SCALE = 100000
    st.success(f"🏡 Predicted House Price: ${prediction[0] * PRICE_SCALE:,.2f}")