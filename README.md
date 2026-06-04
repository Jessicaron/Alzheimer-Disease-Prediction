# 🧠 Alzheimer's Disease Prediction Using RNA-Seq Gene Expression Data
## 👩‍💻 Team Members

- **Jessica Amgad Anis** — ID: 231001218

---

## 🏫 Course

CBIO313: Data Mining and Machine Learning — Final Project
---

## 📋 Project Description

This project applies machine learning techniques to predict Alzheimer's disease
using RNA-Seq gene expression data. The complete data science pipeline is followed,
including data preprocessing, exploratory data analysis (EDA), feature engineering,
feature selection, model training, hyperparameter tuning, evaluation, and deployment
via a Flask web application.

The dataset contains gene expression counts from 30 biological samples classified
into Alzheimer's Disease (AD) and Control groups (Old and Young Controls).
The problem is framed as a binary classification task where AD samples are labeled
as 1 and control samples as 0.

---

## 📂 Dataset

- **Source:** NCBI GEO Database
- **Accession:** GSE153873
- **Download Link:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE153873
- **File used:** `GSE153873_summary_count.star.txt`
- **Size:** 30 samples × 27,000+ gene expression features
- **Note:** The raw dataset is not pre-cleaned. Preprocessing steps including
  constant gene removal and feature selection were applied as part of this project.



## 🚀 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Install Required Libraries
```bash
pip install -r requirements.txt
```
pandas
numpy
matplotlib
seaborn
scikit-learn
flask
joblib

### 3. Run the Notebook
Open `Machine_learning_project.ipynb` in Jupyter Notebook or JupyterLab and run
all cells from top to bottom.

### 4. Run the Flask Web App
```bash
python app.py
```
Then open your browser and go to: https://alzheimer-disease-prediction-dymtmrk4lczrtixxfdgprg.streamlit.app/


Install all at once:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn flask joblib
```

---

## 📊 Results

### Model Comparison

| Model                | Accuracy | Precision | Recall | F1-Score |
|----------------------|----------|-----------|--------|----------|
| Logistic Regression  | 1.00     | 1.00      | 1.00   | 1.00     |
| Decision Tree        | 0.83     | 0.67      | 1.00   | 0.80     |
| Random Forest ✅     | 1.00     | 1.00      | 1.00   | 1.00     |

**Best Model:** Random Forest (after GridSearchCV hyperparameter tuning)

### Top 3 Most Important Genes
- ERI3-IT1
- DPH2
- LHX4-AS1

---

## 📁 Project Structure
├── Machine_learning_project.ipynb   # Main notebook
├── app.py                           # Flask deployment app
├── alzheimers_model.pkl             # Saved trained model
├── feature_selector.pkl             # Saved feature selector
├── requirements.txt                 # Required libraries
├── screenshots/                     # Output plots and screenshots
└── README.md                        # This file

---

