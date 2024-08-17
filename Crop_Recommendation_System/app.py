import streamlit as st
import pickle
import numpy as np
# Page title

st.title('Crop Recommendation System') 

col1, col2 = st.columns(2)

with col1:
    Nitrogen= st.text_input('Nitrogen')
with col2:
    Phosphorus = st.text_input('Phosphorus')
with col1:
    Potassium = st.text_input('Potassium')
with col2:
    Temperature = st.text_input('Temperature')
with col1:
    Humidity = st.text_input('Humidity')
with col2:
    pH = st.text_input('pH')
with col1:
    Rainfall = st.text_input('Rainfall')

prediction = ''
model = pickle.load(open('trained_model.sav', 'rb'))
mx = pickle.load(open('minmaxscaler.sav', 'rb'))
sc = pickle.load(open('standardscaler.sav', 'rb'))
class_names = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
       'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
       'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
       'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']
if st.button('Recommend Crop'):
    input = (Nitrogen,Phosphorus,Potassium,Temperature, Humidity, pH, Rainfall)
    input = np.array(input)
    input = input.reshape(1,-1)
    input = mx.transform(input)
    input = sc.transform(input)
    res = model.predict(input)
    prediction = class_names[res[0]-1]
    st.success(f"The Recommended Crop is {prediction}")