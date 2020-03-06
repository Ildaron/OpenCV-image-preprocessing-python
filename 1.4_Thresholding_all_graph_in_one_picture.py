import cv2 
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('path.jpg')

ret,thresh1 = cv2.threshold(img,127,155,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,155,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,155,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,155,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,155,cv2.THRESH_TOZERO_INV)
thresh1 = cv2.erode(thresh1, None, iterations=2)
thresh1 = cv2.dilate(thresh1, None, iterations=3)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
