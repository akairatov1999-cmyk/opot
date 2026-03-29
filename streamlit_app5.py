import streamlit as st
import numpy as np
import joblib

st.title("BMW Revenue Prediction")

model = joblib.load("model.joblib")

st.write("Enter BMW sales indicators")

units = st.number_input("Units Sold")
price = st.number_input("Average Price EUR")
bev = st.number_input("BEV Share")
premium = st.number_input("Premium Share")
gdp = st.number_input("GDP Growth")
fuel = st.number_input("Fuel Price Index")

if st.button("Predict Revenue Class"):

    X = np.array([[units, price, bev, premium, gdp, fuel]])
    X = scaler.transform(X)

    prediction = model.predict(X)

    if prediction[0] == 1:
        st.success("High Revenue")
    else:
        st.warning("Low Revenue")
