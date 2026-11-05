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

# --------------------------------------------------
# TABS
# --------------------------------------------------
tab1, tab2 = st.tabs(
    ["🔮 Prediction", "📊 Model Performance"]
)

# ==================================================
# TAB 1 : PREDICTION
# ==================================================
with tab1:
    
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

    adr = st.number_input(
        "ADR",
        min_value=0.0,
        value=100.0
    )
    
    total_nights = st.number_input(
        "Total Nights",
        min_value=1,
        max_value=30,
        value=3
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
    "lead_time": [lead_time],
    "adr": [adr],
    "total_nights": [total_nights],
    "customer_type": [customer_type],
    "market_segment": [market_segment],
    "deposit_type": [deposit_type]
    }

# 2. Convert the dictionary into a pandas DataFrame
    input_df = pd.DataFrame(input_dict)

# 3. Pass the DataFrame to the model instead of the numpy array

    # Convert categorical values to dummy variables
    input_df = pd.get_dummies(
        input_df,
        columns=[
            'customer_type',
            'market_segment',
            'deposit_type'
        ]
    )

# Align with model training columns
    input_df = input_df.reindex(
        columns=model.feature_names_in_,
        fill_value=0
    )

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


# ==================================================
# TAB 2 : MODEL PERFORMANCE
# ==================================================
with tab2:

    st.subheader("Model Evaluation Metrics")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Accuracy", "78.44%")
    col2.metric("Precision", "88.11%")
    col3.metric("Recall", "48.33%")
    col4.metric("F1 Score", "62.42%")
    col5.metric("AUC-ROC", "86.30%")

    st.markdown("---")

    st.subheader("Performance Interpretation")

    st.write("""
    **Accuracy (78.44%)**
    - 78.44% of all predictions are correct.

    **Precision (88.11%)**
    - When the model predicts a cancellation, it is correct 88.11% of the time.

    **Recall (48.33%)**
    - The model identifies 48.33% of actual cancellations.

    **F1-Score (62.42%)**
    - Indicates the balance between Precision and Recall.

    **AUC-ROC (86.30%)**
    - Demonstrates strong ability to distinguish cancelled and non-cancelled bookings.
    """)
