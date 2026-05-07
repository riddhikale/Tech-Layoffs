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