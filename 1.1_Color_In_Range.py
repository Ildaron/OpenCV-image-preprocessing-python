import cv2 
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("path.jpg")
cv2.imshow('ImageWindow', img)

hsv_min = np.array((30, 0, 0), np.uint8)
hsv_max = np.array((83, 255, 255), np.uint8)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
thresh = cv2.inRange(hsv, hsv_min, hsv_max)
cv2.imshow('result', thresh)

cap.release()
cv2.destroyAllWindows()
