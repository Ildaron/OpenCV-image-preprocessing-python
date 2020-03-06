import cv2
import numpy as np
img1 = cv2.imread('path.jpg')
cv2.imshow('ImageWindow', img1)
img1 = cv2.resize(img1, (64, 64))
cv2.imshow('ImageWindow1', img1) 
print(img1.shape) 
