import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")

st.title("Credit Card Fraud Detection")

uploaded_file = st.file_uploader("Upload a CSV file of transactions to check for fraud", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    if 'Class' in df.columns:
        X = df.drop('Class', axis=1)
    else:
        X = df.copy()
    
    X_scaled = scaler.transform(X)
    
    predictions = model.predict(X_scaled)
    
    df['Prediction'] = predictions
    
    st.write(df)