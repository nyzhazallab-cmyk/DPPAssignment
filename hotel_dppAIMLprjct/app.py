import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Hotel Cancellation Predictor", layout="wide")

# Load model (pipeline)
model = pickle.load(open("model.pkl", "rb"))

st.title("🏨 Hotel Booking Cancellation Predictor")

st.markdown("Predict whether a booking will be canceled.")

# -------- SIDEBAR INPUT --------
st.sidebar.header("Enter Booking Details")

lead_time = st.sidebar.slider("Lead Time", 0, 500, 50)
adr = st.sidebar.slider("ADR", 0, 500, 100)
adults = st.sidebar.slider("Adults", 1, 5, 2)
children = st.sidebar.slider("Children", 0, 5, 0)
babies = st.sidebar.slider("Babies", 0, 2, 0)

week_nights = st.sidebar.slider("Week Nights", 0, 10, 2)
weekend_nights = st.sidebar.slider("Weekend Nights", 0, 5, 1)

deposit_type = st.sidebar.selectbox(
    "Deposit Type", ["No Deposit", "Non Refund", "Refundable"]
)

customer_type = st.sidebar.selectbox(
    "Customer Type", ["Transient", "Contract", "Group"]
)

# -------- CREATE INPUT --------
input_data = pd.DataFrame({
    'lead_time':[lead_time],
    'adr':[adr],
    'adults':[adults],
    'children':[children],
    'babies':[babies],
    'stays_in_week_nights':[week_nights],
    'stays_in_weekend_nights':[weekend_nights],
    'deposit_type':[deposit_type],
    'customer_type':[customer_type]
})

# -------- FEATURE ENGINEERING --------
input_data['total_nights'] = (
    input_data['stays_in_week_nights'] + input_data['stays_in_weekend_nights']
)

input_data['total_people'] = (
    input_data['adults'] + input_data['children'] + input_data['babies']
)

# -------- PREDICTION --------
if st.button("Predict"):

    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    col1, col2 = st.columns(2)

    with col1:
        if prediction == 1:
            st.error("⚠️ High Risk of Cancellation")
        else:
            st.success("✅ Booking Likely to be Honored")

    with col2:
        st.metric("Cancellation Probability", f"{prob:.2f}")

    # -------- INSIGHTS --------
    st.subheader("📊 Insights")

    if lead_time > 100:
        st.write("🔹 Long lead time increases cancellation risk.")

    if deposit_type == "No Deposit":
        st.write("🔹 No deposit bookings are riskier.")

    if adr > 150:
        st.write("🔹 Higher ADR may increase uncertainty.")