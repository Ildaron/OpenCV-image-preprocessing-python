import cv2
import numpy as np
import imutils

image = cv2.imread("data_1.jpg")
image=cv2.resize(image,(256,256))
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret,image = cv2.threshold(image,195,255,cv2.THRESH_BINARY) #cv2.THRESH_BINARY_INV,cv2.THRESH_TRUNC,cv2.THRESH_TOZERO,cv2.THRESH_TOZERO_INV

kernel = np.ones((6,6),np.uint8)
image = cv2.erode(image,kernel,iterations = 1)
kernel_3 = np.ones((9,9),np.uint8)
image = cv2.dilate(image,kernel_3,iterations = 1)
contours, hierarchy = cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#max_contours = max(contours, key = cv2.contourArea)
#contours=contours[0]
output = image.copy()
M = cv2.moments(contours[0])
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])
cv2.circle(image, (cX, cY), 4, (105, 55, 55), -1)


circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT,1,20, param1=5,param2=3,minRadius=0,maxRadius=30)
print ("circles", circles)
if circles is not None:
 circles = np.round(circles[0, :]).astype('int')
 for (x, y, r) in ((circles)):
  print(x,y,r)   
  cv2.circle(image, (x, y), r, (150, 150, 70), 4)
  cv2.imshow('output',image)
  cv2.waitKey(0)
  #cv2.destroyAllWindows()

cv2.imshow('None_approximation', image)
cv2.waitKey(0)

#M = cv2.moments(c)

