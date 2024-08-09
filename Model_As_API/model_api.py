from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int
    
    
model = pickle.load(open('diabetes_model.sav','rb'))

@app.post('/diabetes_prediction')



def diabetes_pred(input_parameters : model_input):
    input = input_parameters.json()
    input = json.loads(input)
    
    pre = input['Pregnancies']
    glu = input['Glucose']
    bp = input['BloodPressure']
    st = input['SkinThickness']
    ins = input['Insulin']
    bmi = input['BMI']
    dpf = input['DiabetesPedigreeFunction']
    age = input['Age']
    
    input_list = [pre,glu,bp,st,ins,bmi,dpf,age]
    
    prediction = model.predict([input_list])
    
    if(prediction[0] == 0):
        return "Person is Not Diabetic"
    else :
        return "Person is Diabetic"
        