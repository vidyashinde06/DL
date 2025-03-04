# -*- coding: utf-8 -*-
"""cheat1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cLN7ydRTEscbD01rGtvlDB6lhEwvWIdm
"""

# 1.import library
import tensorflow as tf

from tensorflow import keras
import matplotlib.pyplot as plt
import random

# 2. load training and testing data
 mnist=tf.keras.datasets.mnist #mnist is a module in tensoorlow
(x_train,y_train),(x_test,y_test)=mnist.load_data() #download and load dataset into memory

x_train = x_train/255
x_test = x_test/255
# performs normalization
# In the MNIST dataset, each image is 28x28 pixels, and each pixel is represented by a grayscale value between 0 and 255.
# 0 represents black, and 255 represents white, with values in between representing various shades of gray.
# Dividing by 255 scales all pixel values to a range between 0 and 1.
# After this operation, each pixel’s intensity is represented as a float between 0.0 (black) and 1.0 (white).

#3.define network architecture
model=keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)), #Input Shape: 28x28 pixels (MNIST images). convert 2d into 1d as neural network works with 1d
    keras.layers.Dense(128,activation="relu"), #Hidden Layer: A dense layer with 128 neurons and ReLU activation.
    keras.layers.Dense(10,activation="softmax") # A dense layer with 10 neurons and softmax activation, producing a probability distribution over 10 classes (digits 0 to 9).
])
model.summary()

#4. train model using SGD
#compiles and train the model
model.compile(optimizer="sgd", #deine optimization algorithm used to update the weights of the model during training.
              loss="sparse_categorical_crossentropy", #loss function
              metrics=['accuracy'])

history=model.fit(x_train,y_train, #training feature
                 validation_data=(x_test,y_test),#testing feature
                 epochs=3) #specify no.of time the dataset pass through model

#evaluate model
test_loss,test_acc=model.evaluate(x_test,y_test)
print("Loss=%.3f" %test_loss)
print("Accuracy=%.3f" %test_acc)

#plot
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train','validation'], loc='upper right')
plt.show()

#plotting train loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['Train','Validation'], loc='upper right')
plt.show()