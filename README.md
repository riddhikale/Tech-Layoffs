# LayoffWatch — Tech Layoff Risk Predictor 📉

## Overview

LayoffWatch is an end-to-end data science project that analyzes global tech layoffs and predicts the risk of large layoffs using machine learning. The project includes data cleaning, exploratory data analysis (EDA), feature engineering, model building, and deployment using Streamlit.

The goal of the project is to understand layoff trends across industries, countries, company stages, and funding patterns while building an interactive app for layoff risk prediction.

---

## Features

- 📊 Exploratory Data Analysis (EDA)
- 🌍 Country-wise and industry-wise layoff analysis
- 🚀 Funding stage and layoff wave analysis
- 🤖 Machine Learning prediction model
- 📈 Random Forest classification model
- 🌐 Interactive Streamlit web application
- 📉 Layoff risk score prediction

---

## Tech Stack

### Languages & Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit

---

## Dataset

Dataset used: Tech Layoffs Dataset (Layoffs.fyi)

The dataset contains information such as:

- Company
- Industry
- Country
- Funding raised
- Layoff count
- Funding stage
- Date of layoffs
- Percentage of workforce affected

---

## Machine Learning Workflow

### Data Preprocessing

- Handled missing values
- Converted date columns
- Created time-based features
- Engineered layoff wave feature

### Models Used

- Logistic Regression
- Random Forest Classifier

### Evaluation Metrics

- ROC-AUC Score
- Classification Report
- Confusion Matrix

---

## Key Insights

- Layoffs peaked during early 2023
- Funding does not always prevent layoffs
- Large companies had high layoff counts, while startups showed higher layoff percentages
- Layoffs occurred in waves rather than steadily
- Mid-stage startups were highly affected

---

## Streamlit App

The app allows users to:

- Enter company-related details
- Predict layoff risk
- View layoff risk category:
  - 🟢 Low Risk
  - 🟡 Medium Risk
  - 🔴 High Risk

---

## Project Structure

```bash id="o6yjlwm"
tech-layoffs-analysis/
│
├── data/
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_ml_model.ipynb
│
├── models/
│   └── layoff_model.pkl
│
├── images/
│   └── app.png
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Run Locally

### Clone Repository

```bash id="4jlwmj"
git clone https://github.com/your-username/layoffwatch.git
```

### Install Dependencies

```bash id="5jlwmk"
pip install -r requirements.txt
```

### Run Streamlit App

```bash id="vjlwmx"
streamlit run app.py
```

---

## Future Improvements

- Add more advanced ML models
- Use real-time layoff news APIs
- Add interactive dashboards and charts
- Deploy using Docker or cloud platforms

---

## Author

Riddhi Kale

---

## License

This project is for educational and portfolio purposes.
