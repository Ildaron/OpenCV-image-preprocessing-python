import cv2 
import numpy as np
img = cv2.imread("path.jpg")
blurred = cv2.blur(img, (9, 9))
cv2.imshow('ImageWindow', img)
