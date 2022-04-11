import cv2

import os

import numpy as np

from tensorflow.keras.models import load_model

from tensorflow.keras.preprocessing.image import load_img,img_to_array
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.python.keras import utils 


from PIL import Image
import PIL
import numpy as np
def load_image(image_path):
    img = Image.open( image_path )
    newImg = img.resize((299,299), PIL.Image.BILINEAR).convert("RGB")
    data = np.array( newImg.getdata() )
    return 2*( data.reshape( (newImg.size[0], newImg.size[1], 3) ).astype( np.float32 )/255 ) - 1


current_path = os.getcwd()

model = load_model(r'static/inception.h5')

def predictor(img_path): # here image is file name 

    image = load_image(img_path)
    image = np.expand_dims(image, axis=0)
    preds = model.predict(image)
    print('Predicted:', decode_predictions(preds))
    return(preds)