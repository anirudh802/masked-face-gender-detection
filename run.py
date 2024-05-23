import os
import cv2  
import numpy as np
import random
from tensorflow.keras.layers import Input, Lambda, Dense, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import tensorflow as tf
import keras

import numpy as np
from glob import glob
import matplotlib.pyplot as plt


modell=tf.keras.models.load_model('final_face.keras')

while True:
    path=input('enter path to image: ')
    l=[]
    img=cv2.imread(path)
    img=cv2.resize(img,(224,224))
    l.append(img)
    pred=modell.predict(np.array(l))
    hola=[]
    for i in pred:
        if i >0.02:
            hola.append("female")
        else:
            hola.append("male")
    plt.imshow(cv2.cvtColor(l[0],cv2.COLOR_BGR2RGB))
    plt.title(hola[0])  
    plt.axis('off')
    plt.show()
