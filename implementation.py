# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 18:46:16 2024

@author: roopa
"""

import pickle
import streamlit as st
import numpy as np
import time

# Load model and scaler
loaded_model = pickle.load(open("pcod_model (1).sav", "rb"))
scaler = pickle.load(open("scaler.sav", "rb"))

def pcosprediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)
    std_data = scaler.transform(input_data_as_numpy_array)
    prediction = loaded_model.predict(std_data)
    return 'The woman is having PCOD.' if prediction[0] == 1 else 'The woman is not having PCOD.'

def main():
    # Inject custom CSS for styling the fields
    st.markdown(
        """
        <style>
        div[data-baseweb="input"] > div {
            background-color: #ffe4e1; /* Light pink */
            border: 2px solid #ffb6c1; /* Soft pink border */
            border-radius: 8px;
        }
        div[data-baseweb="select"] > div {
            background-color: #ffe4e1; /* Light pink */
            border: 2px solid #ffb6c1; /* Soft pink border */
            border-radius: 8px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Introduction
    st.title("PCOS Prediction Web App")
    st.markdown(
        """
        ### Welcome to the PCOS Prediction Web App!
        This web app helps predict the likelihood of Polycystic Ovary Syndrome (PCOS) based on key health indicators.
        
        PCOS is a common hormonal disorder among women of reproductive age. Early detection and management can help 
        improve health outcomes significantly. Enter the required details below to get a prediction.
        
        ---
        """
    )
    
    # Create input fields
    st.markdown("### Please fill in the details below:")
    col1, col2 = st.columns(2)
    with col1:
        follicle_left = st.number_input('Number of follicles in the left ovary', min_value=0, step=1)
        weight_gain = st.selectbox('Weight gain observed?', options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        pimples = st.selectbox('Experienced acne?', options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        fast_food = st.selectbox('Frequently consumes fast food?', options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    with col2:
        follicle_right = st.number_input('Number of follicles in the right ovary', min_value=0, step=1)
        hair_growth = st.selectbox('Excessive hair growth?', options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        skin_darkening = st.selectbox('Dark patches of skin observed?', options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        amh_level = st.number_input('Anti-Müllerian Hormone level (ng/mL)', min_value=0.0, format="%.2f")

    # Prediction process
    if st.button('PCOS Prediction Result'):
        if any(x is None or x == "" for x in [follicle_left, follicle_right, weight_gain, hair_growth, pimples, skin_darkening, fast_food, amh_level]):
            st.warning("Please fill in all the fields.")
        else:
            status_placeholder = st.empty()  # Placeholder for dynamic text
            status_placeholder.info("Analyzing your data...")
            progress = st.progress(0)  # Initialize the progress bar
            
            # Simulate a loading process
            for i in range(100):
                time.sleep(0.02)  # Add delay to simulate processing
                progress.progress(i + 1)
            
            # Update the status message
            status_placeholder.success("Prediction completed successfully!")
            
            # Display the prediction result
            diagnosis = pcosprediction([follicle_left, follicle_right, weight_gain, hair_growth, pimples, skin_darkening, fast_food, amh_level])
            st.success(diagnosis)

if __name__ == '__main__':
    main()



