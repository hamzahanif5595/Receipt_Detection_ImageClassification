
import matplotlib.pyplot as plt
import seaborn as sns

import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D , MaxPool2D , Flatten , Dropout 
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam

from sklearn.metrics import classification_report,confusion_matrix

import tensorflow as tf

import cv2
import os
import json

import numpy as np

from tensorflow import keras

import traceback
import numpy as np
from PIL import Image

img_size = 224

def classify(file_path, model):
    try:
        img_arr = cv2.imread(file_path)[...,::-1]
        resized_arr = cv2.resize(img_arr, (img_size, img_size))
        resized_np_arr = np.array(resized_arr)
        img_np_arr = [resized_np_arr]
        images = np.array(img_np_arr) / 244
        images.reshape(-1, img_size, img_size, 1)
        pred = model.predict_classes(images, batch_size = 1)
        result = pred[0][0]

        if result == 0:
            response = {"Result" : "Correct"} 
            return response
        else:
            response = {"Result" : "Incorrect"} 
            return response
    except Exception as e:
        response = {"Result" : e} 
        return response