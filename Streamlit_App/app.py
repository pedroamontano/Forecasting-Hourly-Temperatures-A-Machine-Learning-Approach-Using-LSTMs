#!/usr/bin/env python3

import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
import joblib
from PIL import Image
import base64

def image_to_base64(img_path):
    with open(img_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

img_base64 = image_to_base64('Streamlit_App/hot.png')

# Function to load saved resources
def load_resources(scaler_filepath, model_filepath):
    scaler = joblib.load(scaler_filepath)
    model = load_model(model_filepath)
    return scaler, model

# Function to make prediction on a single row of unscaled data
def make_single_prediction(unscaled_data, scaler, model):
    unscaled_data = np.array(unscaled_data).reshape(1, -1)
    scaled_data = scaler.transform(unscaled_data)
    scaled_data = scaled_data.reshape(1, 1, scaled_data.shape[1])
    prediction = model.predict(scaled_data)
    return prediction


# Load resources
scaler, lstm_model = load_resources('Streamlit_App/stdscaler.pkl', 'Streamlit_App/model_6_1_dew.h5')


# Streamlit app
st.title("LSTM Model Prediction")

if 'prediction' not in st.session_state:
    st.session_state['prediction'] = None

# Get user input
pressure_station = st.number_input("Pressure Station:", value=0.0)
wind_speed = st.number_input("Wind Speed:", value=0.0)
wind_gust = st.number_input("Wind Gust:", value=0.0)
relative_humidity = st.number_input("Relative Humidity:", value=0.0)
dew_point = st.number_input("Dew Point:", value=0.0)
windchill = st.number_input("Windchill:", value=0.0)
humidex = st.number_input("Humidex:", value=0.0)
visibility = st.number_input("Visibility:", value=0.0)
health_index = st.number_input("Health Index:", value=0.0)
cloud_okta = st.number_input("Cloud Okta:", value=0.0)

# Make prediction
if st.button("Predict"):
    features = [pressure_station, wind_speed, wind_gust, relative_humidity, dew_point, windchill, humidex, visibility, health_index, cloud_okta]
    prediction = make_single_prediction(features, scaler, lstm_model)
    st.write(f"Prediction: {prediction}")

    if prediction > 25:
    hot = image_to_base64('Streamlit_App/hot.png')
    st.markdown(
        f"<div style='text-align: right'><img src='data:image/png;base64,{hot}'></div>",
        unsafe_allow_html=True,
    )
    
    if prediction < 10:
    cold = image_to_base64('Streamlit_App/cold.png')
    st.markdown(
        f"<div style='text-align: right'><img src='data:image/png;base64,{cold}'></div>",
        unsafe_allow_html=True,
    )

    # if prediction > 25:
    #     img = Image.open('Streamlit_App/hot.png')
    #     img = img.resize((200, 200))  # Resizing to 300x200 pixels
    #     st.image(img, caption='Hot Weather')
    # elif prediction < 10:
    #     img = Image.open('Streamlit_App/cold.png')
    #     img = img.resize((200, 200))  # Resizing to 300x200 pixels
    #     st.image(img, caption='Cold Weather')


# Clear prediction
if st.button("Clear"):
    st.session_state['prediction'] = None
    st.write("Prediction cleared.")