import cv2 
import numpy as np

img = cv2.imread("path.jpg")
img = cv2.GaussianBlur(img, (51, 51), 2)
cv2.imshow('ImageWindow', img)

