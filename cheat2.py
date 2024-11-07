# -*- coding: utf-8 -*-
"""cheat2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bgkEGjCNgFHihN4r8lTkszL1OlGP9OON
"""

import tensorflow as tf
from tensorflow import keras
from keras import models,layers
import matplotlib.pyplot as plt

cifar10=tf.keras.datasets.cifar10
(x_train,y_train),(x_test,y_test)=cifar10.load_data()

x_train=x_train/255
x_test=x_test/255

model=models.Sequential([
    layers.Conv2D(32,(3,3),input_shape=(32,32,3),activation='relu'),# 32 filter of 3*3 size to image
    layers.MaxPooling2D(2,2),#2*2 window
    layers.Conv2D(64,(3,3),activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64,(3,3),activation='relu'),
    layers.Flatten(),#This layer flattens the 3D output from the last convolutional layer (height, width, and depth) into a 1D array.
    layers.Dense(64,activation='relu'),#fully connected layer
    layers.Dense(10)


])
model.summary()

#train model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

his=model.fit(x_train,y_train,validation_data=(x_test,y_test),epochs=3)

train_loss,train_acc=model.evaluate(x_test,y_test)
print("loss%.3f" %train_loss)
print("accuracy%.3f"%train_acc)

