import cv2 
import numpy as np

img = cv2.imread('path.jpg')
img = cv2.erode(img, None, iterations=2)
img = cv2.dilate(img, None, iterations=2)
cv2.imshow('ImageWindow', img ) 

