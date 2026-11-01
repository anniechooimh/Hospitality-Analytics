import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the saved sales regression model
@st.cache_resource
def load_model():
    return joblib.load('salesregression.pkl')

model = load_model()

st.title("🤖 Booking Cancellation ML Predictor")

# Input fields
val1 = st.number_input("Lead_time", value=90)
val2 = st.number_input("Total_nights", value=3)
val3 = st.text_input("Customer_type", value='Group')
val4 = st.text_input("Market_segment", value='Online TA')
val5 = st.number_input("ADR", value=100)
val6 = st.text_input("Deposit_type", value='Non Refund')

if st.button("Predict"):
    # 1. Arrange inputs into a dictionary mapping to your exact original dataset column names
    input_dict = {
        "Lead_time": [val1],
        "Total_nights": [val2],
        "Customer_type": [val3],
        "Market_segment": [val4],
        "ADR": [val5],
        "Deposit_type": [val6]
    }

    # 2. Convert the dictionary into a pandas DataFrame
    input_df = pd.DataFrame(input_dict)

    # 3. Pass the DataFrame to the model instead of the numpy array
    prediction = model.predict(input_df)

    st.success(f"Prediction: {prediction[0]}")
