import streamlit as st
import pandas as pd
import joblib

st.title("Internet Usage Prediction")

# Loading the dataset
wb = pd.read_csv("data/world-bank.csv")

# Loading model
model = joblib.load("models/random_forest_model.joblib")

st.subheader("World Bank Dataset")
st.dataframe(wb.head())

st.subheader("Internet Usage Prediction")

# Inputs
st.text("Keep in mind when entering values that as the higher the political stability is both negative and positive.")
gdp = st.number_input("GDP", value=50000000.0)
political = st.number_input("Political Stability", value=0.0)

income = st.selectbox(
    "Income Group",
    ["Low", "Lower Middle", "Upper Middle", "High"]
)

# Map income groups to numeric values if needed
income_map = {
    "Low":0,
    "Lower Middle":1,
    "Upper Middle":2,
    "High":3
}

income_value = income_map[income]

if st.button("Predict"):

    input_df = pd.DataFrame({
        "GDP":[gdp],
        "PoliticalStability":[political],
        "Income":[income_value]
    })

    pred = model.predict(input_df)[0]

    st.success(f"Predicted Internet Usage: {pred:.2f}%")