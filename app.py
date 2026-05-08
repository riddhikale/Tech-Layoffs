import streamlit as st
import pandas as pd
import pickle

# Load model
with open('models/layoff_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("📉 LayoffWatch — Tech Layoff Risk Predictor")

st.write("Predict the risk of large layoffs based on company details.")

# Inputs
industry = st.selectbox(
    "Industry",
    ['Consumer', 'Retail', 'Finance', 'Healthcare', 'Crypto', 'Transportation']
)

country = st.selectbox(
    "Country",
    ['United States', 'India', 'United Kingdom', 'Canada', 'Germany']
)

stage = st.selectbox(
    "Funding Stage",
    ['Seed', 'Series A', 'Series B', 'Series C', 'Post-IPO']
)

funds = st.slider(
    "Funds Raised (Millions)",
    0,
    5000,
    100
)

percentage = st.slider(
    "Percentage of Workforce Affected",
    0.0,
    1.0,
    0.2
)

month = st.slider(
    "Month",
    1,
    12,
    1
)


#create input df
input_data = pd.DataFrame({
    'Funds_Raised': [funds],
    'year': [2024],
    'month': [month],
    'Percentage': [percentage],
    'wave_month': [0]
})

# Prediction button
if st.button("Predict Layoff Risk"):
    
    prediction = model.predict_proba(input_data)[0][1]
    
    st.subheader(f"Layoff Risk Score: {prediction:.2f}")

    if prediction > 0.7:
        st.error("🔴 High Risk of Large Layoff")
    
    elif prediction > 0.4:
        st.warning("🟡 Medium Risk")
    
    else:
        st.success("🟢 Low Risk")