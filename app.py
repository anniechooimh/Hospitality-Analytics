import streamlit as st
import joblib
import numpy as np
import pandas as pd

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Hotel Booking Cancellation Predictor",
    page_icon="🏨",
    layout="wide"
)

# -------------------------------------------------
# Load the saved sales regression model
# -------------------------------------------------
@st.cache_resource
def load_model():
    return joblib.load('salesregression.pkl')

model = load_model()


# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title("🏨 Hotel Booking Cancellation Predictor")
st.markdown("Predict whether an upcoming booking is likely to be cancelled.")

# Input fields
st.subheader("Booking Details")

col1, col2 = st.columns(2)

with col1:
    
    lead_time = st.number_input(
        "Lead Time",
        min_value=0,
        max_value=800,
        value=90
    )

    total_nights = st.number_input(
        "Total Nights",
        min_value=1,
        max_value=30,
        value=3
    )

    adr = st.number_input(
        "ADR",
        min_value=0.0,
        value=100.0
    )

with col2:
    
    customer_type = st.selectbox(
        "Customer Type",
        [
            "Transient",
            "Transient-Party",
            "Contract",
            "Group"
        ]
    )

    market_segment = st.selectbox(
        "Market Segment",
        [
            "Online TA",
            "Offline TA/TO",
            "Direct",
            "Corporate",
            "Groups"
        ]
    )

    deposit_type = st.selectbox(
        "Deposit Type",
        [
            "No Deposit",
            "Non Refund",
            "Refundable"
        ]
    )

if st.button("Predict Cancellation Risk"):

# Build DataFrame using the same column names used during model training

    input_dict = {
        "Lead_time": [lead_time],
        "Total_nights": [total_nights],
        "Customer_type": [customer_type],
        "Market_segment": [market_segment],
        "ADR": [adr],
        "Deposit_type": [deposit_type]
        }

# 2. Convert the dictionary into a pandas DataFrame
    input_df = pd.DataFrame(input_dict)

# 3. Pass the DataFrame to the model instead of the numpy array
    prediction = model.predict(input_df)

st.markdown("---")

if prediction[0] == 1:
    st.error("⚠️ High Risk: This booking is likely to be cancelled.")
else:
    st.success("✅ Low Risk: This booking is likely to be honoured.")

    # Probability (if available)
    try:
        probability = model.predict_proba(input_df)[0][1]

        st.metric(
            "Cancellation Probability",
            f"{probability:.2%}"
            )
    except:
        st.info("Prediction probability is not available for this model.")
