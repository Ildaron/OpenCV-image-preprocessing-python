import cv2
import numpy as np
import imutils

image = cv2.imread("data_44.jpg")
images=image=cv2.resize(image,(256,256))
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret,image = cv2.threshold(image,195,255,cv2.THRESH_BINARY) #cv2.THRESH_BINARY_INV,cv2.THRESH_TRUNC,cv2.THRESH_TOZERO,cv2.THRESH_TOZERO_INV

kernel = np.ones((6,6),np.uint8)
image = cv2.erode(image,kernel,iterations = 1)
kernel_3 = np.ones((8,8),np.uint8)
image = cv2.dilate(image,kernel_3,iterations = 1)
contours, hierarchy = cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#max_contours = max(contours, key = cv2.contourArea)
#contours=contours[0]

M = cv2.moments(contours[0])
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])
cv2.circle(image, (cX, cY), 4, (105, 55, 55), -1)

image=cv2.drawContours(image,contours,-1,(190,50,155),3)
cv2.imshow('None_approximation', image)
cv2.waitKey(0)

#M = cv2.moments(c)
