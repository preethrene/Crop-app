# Step 1: Saving Streamlit App code to a Python file with UTF-8 encoding

code = """
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import requests

def load_data():
    data = pd.DataFrame({
        'Temperature': np.random.uniform(20, 35, 100),
        'Humidity': np.random.uniform(30, 90, 100),
        'Rainfall': np.random.uniform(50, 200, 100),
        'Soil_pH': np.random.uniform(5.5, 7.5, 100),
        'Organic_Fertilizer': np.random.uniform(0, 100, 100),
        'Yield': np.random.uniform(2000, 5000, 100)
    })
    return data

def preprocess_data(data):
    X = data.drop('Yield', axis=1)
    y = data['Yield']
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2

def predict_yield(model, input_data):
    prediction = model.predict([input_data])
    return prediction[0]

def main():
    st.title("🌾 AI-Powered Crop Yield Prediction")
    st.write("Predict crop yield based on soil conditions, weather, and fertilizer usage.")

    st.sidebar.header("Enter Input Parameters")
    temperature = st.sidebar.slider("Temperature (°C)", 10, 50, 25)
    humidity = st.sidebar.slider("Humidity (%)", 10, 100, 50)
    rainfall = st.sidebar.slider("Rainfall (mm)", 0, 300, 100)
    soil_ph = st.sidebar.slider("Soil pH", 4.0, 9.0, 6.5)
    fertilizer = st.sidebar.slider("Organic Fertilizer Usage (kg/ha)", 0, 200, 50)

    data = load_data()
    X_train, X_test, y_train, y_test = preprocess_data(data)

    model = train_model(X_train, y_train)
    mse, r2 = evaluate_model(model, X_test, y_test)

    st.write(f"### Model Performance:")
    st.write(f"- Mean Squared Error: {mse:.2f}")
    st.write(f"- R² Score: {r2:.2f}")

    if st.button("Predict Crop Yield"):
        input_data = [temperature, humidity, rainfall, soil_ph, fertilizer]
        prediction = predict_yield(model, input_data)
        st.success(f"🌿 **Predicted Crop Yield:** {prediction:.2f} kg/ha")

    if st.button("Save Model"):
        joblib.dump(model, "crop_yield_model.pkl")
        st.success("✅ Model saved successfully!")

    if st.button("Load Model"):
        loaded_model = joblib.load("crop_yield_model.pkl")
        st.info("📂 Model loaded successfully!")
        loaded_prediction = predict_yield(loaded_model, [temperature, humidity, rainfall, soil_ph, fertilizer])
        st.success(f"🌿 **Predicted Yield (Loaded Model):** {loaded_prediction:.2f} kg/ha")

if __name__ == "__main__":
    main()
"""

# ✅ Save the code with UTF-8 encoding to avoid UnicodeEncodeError
with open("crop_yield_app.py", "w", encoding="utf-8") as file:
    file.write(code)

print("✅ crop_yield_app.py file saved successfully with UTF-8 encoding.")
import subprocess

# Run the Streamlit app with subprocess
subprocess.run(["streamlit", "run", "crop_yield_app.py"])
