from helper import *

import streamlit as st

import os

import matplotlib.pyplot as plt

import seaborn as sns

sns.set_theme(style="darkgrid")

sns.set()

from PIL import Image

st.title('Object Detection ')

def save_uploaded_file(uploaded_file):

    try:

        with open(os.path.join('static/videos',uploaded_file.name),'wb') as f:

            f.write(uploaded_file.getbuffer())

        return 1    

    except:

        return 0
search = st.text_input("Search for an Object here....",)
uploaded_file = st.file_uploader("Upload Video")
if uploaded_file is not None:

    if save_uploaded_file(uploaded_file): 
        	
        capture = cv2.VideoCapture(os.path.join('static/videos',uploaded_file.name))
        frameNr = 0
        
        while (True):
        
            success, frame = capture.read()
        
            if success:
                cv2.imwrite(f'static/images/{frameNr}.jpg', frame)
                prediction = predictor(os.path.join(f'static/images/{frameNr}.jpg'))
                prediction = decode_predictions(prediction)
                predition_names = []
                for each in prediction[0]:
                    predition_names.append(each[1])
                if search in predition_names : 
                    st.image(frame)
                    st.text('Predictions :-')
                    st.text(prediction)
                    os.remove(os.path.join(f'static/images/{frameNr}.jpg'))
            else:
                break
        
            frameNr = frameNr+1
        
        capture.release()
        os.remove('static/videos/'+uploaded_file.name)

        # display the image


        

