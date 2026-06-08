# Jessica Amgad Anis ID:231001218

# Alzheimer's Disease Prediction Using RNA-Seq Gene Expression Data

This project uses machine learning techniques to predict Alzheimer's disease using RNA-Seq gene expression data. The workflow includes data preprocessing, exploratory data analysis (EDA), feature engineering, feature selection, model training, hyperparameter tuning, evaluation, and deployment using Streamlit.

---

# Project Objective

The main objective of this project is to develop a machine learning model capable of distinguishing Alzheimer's disease samples from control samples using RNA-seq gene expression data.

---

# Dataset Description

The dataset contains RNA-seq gene expression counts collected from multiple biological samples.

Classes:
- Alzheimer's Disease (AD)
- Old Controls
- Young Controls

The classification problem was converted into a binary classification task:
- AD = 1
- Control = 0

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib

---

# Machine Learning Workflow

## 1. Data Preprocessing
- Data loading
- Dataset transposition
- Target variable creation
- Removing constant genes
- Feature scaling

## 2. Exploratory Data Analysis (EDA)
- Distribution analysis
- Boxplots
- Heatmaps
- Scatterplots
- Violin plots

## 3. Feature Engineering
- Created Neuro Activity Index feature

## 4. Feature Selection
- SelectKBest with ANOVA F-test
- Top informative genes selected

## 5. Machine Learning Models
The following models were trained and evaluated:
- Logistic Regression
- Decision Tree
- Random Forest

## 6. Hyperparameter Tuning
- GridSearchCV used for Random Forest optimization

## 7. Model Evaluation
Evaluation metrics:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

---

# Final Model Performance

| Model | Accuracy | Precision | Recall | F1-Score |
|------|------|------|------|------|
| Logistic Regression | 1.00 | 1.00 | 1.00 | 1.00 |
| Decision Tree | 0.83 | 0.67 | 1.00 | 0.80 |
| Random Forest | 1.00 | 1.00 | 1.00 | 1.00 |

The Random Forest model was selected as the final deployment model.

---

# Deployment

The application was deployed using Streamlit Community Cloud.

Features:
- Interactive web interface
- Real-time prediction
- Public cloud deployment
- GitHub integration
# link for web app 
https://alzheimer-disease-prediction-dymtmrk4lczrtixxfdgprg.streamlit.app/
--
# link for video presentation
https://drive.google.com/file/d/1V65g4cyMpBDgctcJFHddJ7i6kovDqoZj/view?usp=sharing


# Repository Structure

```text
Alzheimer_Project/
│
├── app.py
├── requirements.txt
├── model.pkl
├── notebook.ipynb
├── dataset.csv
└── README.md

# Installation

Clone the repository:

git clone https://github.com/Jessicaron/Alzheimer-Disease-Prediction.git

Move into the project folder:

cd Alzheimer-Disease-Prediction

Install dependencies:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run app.py
Streamlit Deployment

# The application can be deployed directly using:

GitHub repository
Streamlit Community Cloud
Challenges Encountered

During deployment and development:

Dependency compatibility issues
GitHub authentication problems
Incorrect package names
Python version conflicts
Streamlit deployment path configuration

These issues were resolved successfully.

# Conclusion

This project demonstrates a complete machine learning pipeline for Alzheimer's disease prediction using RNA-seq gene expression data. The project highlights the importance of preprocessing, feature selection, model evaluation, and deployment in bioinformatics and healthcare applications.

# Author

Jessica Ron

