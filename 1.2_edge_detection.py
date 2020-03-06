import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('path')
edges = cv2.Canny(img,10,50)
cv2.imshow('ImageWindow2', edges) 
plt.show()


