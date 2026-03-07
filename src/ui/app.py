import streamlit as st
import joblib
import re

model = joblib.load("src/models/phishing_model.joblib")
vectorizer = joblib.load("src/models/tfidf_vectorizer.joblib")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "URL", text)
    text = re.sub(r"\S+@\S+", "EMAIL", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text

st.title("AI-Powered Phishing Email Detector")

email = st.text_area("Paste email content")

if st.button("Analyze"):
    cleaned = clean_text(email)
    vec = vectorizer.transform([cleaned])
    prediction = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0][1]

    if prediction == 1:
        st.error(f"Phishing detected (risk score: {prob:.2f})")
    else:
        st.success(f"Legitimate email (risk score: {prob:.2f})")
