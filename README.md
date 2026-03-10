# AI-Powered Phishing Email Detector

An end-to-end machine learning system that detects phishing emails using real-world datasets.  
The project includes a complete pipeline: **data ingestion, preprocessing, feature engineering, model training, evaluation, and a simple web interface for prediction.**

This repository is structured like a **production ML project** so contributors can easily extend or improve the system.

---

# Project Objective

Phishing emails remain one of the most common initial attack vectors in cyber attacks. Traditional rule-based spam filters often fail against **modern, adaptive phishing techniques**.

This project aims to build a **machine learning model that classifies emails as:**

- **Phishing**
- **Legitimate**

The final result is a reproducible ML pipeline with a working prediction interface.

---

# Project Scope

### Problem
Email phishing continues to bypass traditional rule-based filtering systems.

### Goal
Train and deploy a machine learning model that detects phishing emails based on email text content.

### Constraints

- No real private emails
- Public datasets only
- Fully reproducible training
- Transparent and explainable results

---

# Repository Structure

```
ai-phishing-email-detector
│
├── data
│   ├── raw
│   └── processed
│
├── notebooks
│
├── src
│   ├── data
│   │   └── make_dataset.py
│   │
│   ├── features
│   │   └── build_features.py
│   │
│   ├── models
│   │   ├── train.py
│   │   ├── evaluate.py
│   │   └── phishing_model.joblib
│   │
│   ├── api
│   │
│   ├── ui
│   │   └── app.py
│   │
│   └── utils
│
├── tests
├── docs
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Environment Setup

### 1. Clone the repository

```
git clone https://github.com/yourusername/ai-phishing-email-detector.git
cd ai-phishing-email-detector
```

---

### 2. Create a virtual environment

```
python -m venv .venv
source .venv/bin/activate
```

Windows:

```
.venv\Scripts\activate
```

---

### 3. Install dependencies

```
pip install -U pip
pip install -r requirements.txt
```

Main dependencies include:

- pandas
- numpy
- scikit-learn
- nltk
- matplotlib
- seaborn
- jupyter
- streamlit
- joblib

---

# Dataset

This project uses **public phishing email datasets**.

Recommended sources:

- Enron Spam Dataset
- Kaggle phishing email datasets

Dataset format:

```
email_text,label
```

Where:

- `label = 1` → phishing  
- `label = 0` → legitimate

Place the dataset in:

```
data/raw/emails.csv
```

⚠️ Do **not commit raw datasets** if licensing restricts redistribution.

---

# Data Pipeline

The project follows a simple ML pipeline:

```
Raw Data
   ↓
Data Cleaning
   ↓
Text Preprocessing
   ↓
TF-IDF Feature Extraction
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Prediction Interface
```

---

# Data Ingestion

File:

```
src/data/make_dataset.py
```

Purpose:

- Load raw dataset
- Remove missing values
- Save cleaned dataset

Run:

```
python src/data/make_dataset.py
```

Output:

```
data/processed/emails_clean.csv
```

---

# Feature Engineering

File:

```
src/features/build_features.py
```

Steps:

- Lowercase text
- Replace URLs with placeholder
- Replace email addresses
- Remove non-alphabetic characters
- Convert text to TF-IDF features

Run:

```
python src/features/build_features.py
```

Outputs:

```
src/models/tfidf_vectorizer.joblib
data/processed/features.joblib
```

---

# Model Training

File:

```
src/models/train.py
```

Model used:

**Logistic Regression**

Steps:

1. Load feature matrix
2. Split dataset into train/test sets
3. Train classifier
4. Save trained model

Run:

```
python src/models/train.py
```

Outputs:

```
src/models/phishing_model.joblib
data/processed/test_data.joblib
```

---

# Model Evaluation

File:

```
src/models/evaluate.py
```

Metrics used:

- Precision
- Recall
- F1-score
- Confusion Matrix

Run:

```
python src/models/evaluate.py
```

Example output:

```
              precision    recall  f1-score   support

legitimate       0.96      0.95      0.95
phishing         0.94      0.95      0.94

accuracy                             0.95
```

---

# Prediction Interface

A simple **Streamlit web app** allows users to paste an email and check if it is phishing.

File:

```
src/ui/app.py
```

Run the app:

```
streamlit run src/ui/app.py
```

Then open:

```
http://localhost:8501
```

Users can paste email content and receive:

- Prediction result
- Risk score

---

# Example Usage

Input:

```
Dear user,

Your bank account has been suspended.
Click the link below to verify immediately.

http://secure-login-update.com
```

Output:

```
Phishing detected
Risk score: 0.92
```

---

# Ethical Considerations

This project is for **educational and defensive cybersecurity purposes only**.

Important considerations:

- No real personal emails are used
- Public datasets only
- Model predictions should assist humans, not replace them
- False positives and false negatives are possible

---

# Future Improvements

Potential improvements include:

- Deep learning models (LSTM / Transformers)
- Email header analysis
- URL feature extraction
- Domain reputation scoring
- API deployment with FastAPI
- Docker containerization
- Continuous model retraining

---

# Contributing

Contributions are welcome.

You can contribute by:

- Improving preprocessing
- Testing new ML models
- Adding datasets
- Improving the UI
- Adding API endpoints

Typical workflow:

```
fork repo
create branch
commit changes
open pull request
```

---

# License

MIT License
