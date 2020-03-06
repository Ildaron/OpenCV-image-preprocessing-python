import cv2
import numpy as np

#predict_datagen = ImageDataGenerator(rescale=1./255)

img1 = cv2.imread('path')
cv2.imshow('ImageWindow', img1)
img1 = cv2.resize(img1, (64, 64))
cv2.imshow('ImageWindow1', img1) 
print(img1.shape) 
