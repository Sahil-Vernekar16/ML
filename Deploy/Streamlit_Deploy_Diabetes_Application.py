# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('D:/ML/Models/diabetes_model.sav','rb'))

def diabetes_prediction(input):
    input_as_numpy_array = np.asarray(input)
    input_reshaped = input_as_numpy_array.reshape(1,-1)
    prediction = model.predict(input_reshaped)
    print(prediction)
    if (prediction[0] == 0):
        return ('The person is not diabetic')
    else:
        return ('The person is diabetic')

def main():
    st.title("Diabetes Prediction App")
    
    
    
    Pregnancies = st.text_input("Pregnancies")
    Glucose = st.text_input("Glucose")
    BloodPressure = st.text_input("BloodPressure")
    SkinThickness = st.text_input("SkinThickness")
    Insulin = st.text_input("Insulin")
    BMI = st.text_input("BMI")
    DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction")
    Age = st.text_input("Age")
    
    diagnosis=''
    
    if st.button('Predict Diabetes'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()