# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:38:31 2024

@author: sahil
"""

import json
import requests

url = 'http://127.0.0.1:8000/diabetes_prediction'

input_data = {
    'Pregnancies' : 6,
    'Glucose': 148,
    'BloodPressure' : 72,
    'SkinThickness' : 35, 
    'Insulin' : 0,
    'BMI' : 33.6,
    'DiabetesPedigreeFunction' : 0.627,
    'Age' :  50
    }
    
input_data = json.dumps(input_data)

response = requests.post(url, data=input_data)

print(response.text)