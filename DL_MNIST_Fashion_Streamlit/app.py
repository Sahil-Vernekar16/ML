import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import os

working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = f'{working_dir}/fashion_mnist_model.h5'
model = tf.keras.models.load_model(model_path)

classes = ['T-shirt/top', 'Trouser', 'Pullover' , 'Dress' , 'Coat' , 'Sandal' , 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

def process_image(image):
    img = Image.open(image)
    img = img.resize((28,28))
    img = img.convert('L')
    img_array = np.array(img)
    img_array = img_array/255.0
    img_reshaped = img_array.reshape((1,28,28,1))
    return img_reshaped

uploaded_image = st.file_uploader('Upload an Image',  type=['png','jpg'])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    col1,col2 = st.columns(2)
    with col1:
        image = image.resize((128,128))
        st.image(image)
        
    with col2:
        if st.button('Classify'):
            processed_image = process_image(image)
            prediction = model.predict(processed_image)
            prediction_result = np.argmax(prediction)
            predicted_label = classes[prediction_result]
            st.success(predicted_label)
        