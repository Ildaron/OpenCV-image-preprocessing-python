import cv2
import numpy as np
import imutils
from itertools import product
import math

image = cv2.imread("data_6.jpg")
scale_percent = 40
x = int(image.shape[1] * scale_percent / 100)
y = int(image.shape[0] * scale_percent / 100)
images=image=cv2.resize(image,(x,y))

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret,image = cv2.threshold(image,195,255,cv2.THRESH_BINARY) #cv2.THRESH_BINARY_INV,cv2.THRESH_TRUNC,cv2.THRESH_TOZERO,cv2.THRESH_TOZERO_INV

kernel = np.ones((6,6),np.uint8)
image = cv2.erode(image,kernel,iterations = 1)
kernel_3 = np.ones((8,8),np.uint8)
image = cv2.dilate(image,kernel_3,iterations = 1)

colorLower = (250, 250, 250)
colorUpper = (255, 255, 255)
cnts = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
lengh_cnts=len(cnts)
amount_figure= [1.0] *lengh_cnts 
amount_axeX= [1.0] *lengh_cnts
amount_axeY= [1.0] *lengh_cnts

count=0
radius_max=[]
x_max=[]
y_max=[]
if cnts is ():
 print ("none")   
 cv2.imshow('Vertical', image)
 key = cv2.waitKey(1) & 0xFF
else:
 for c in cnts:    
  ((x, y), radius) = cv2.minEnclosingCircle(c)
  radius_max.append(radius)
  x_max.append(x)
  y_max.append(y)
 index = radius_max.index(max(radius_max))

 print ("image.shape", image.shape)
 print ("image.shape", image.shape[0])
 print ("image.shape", image.shape[1])
      
 if radius > 0:  
  cv2.circle(images, (int(x_max[index]), int(y_max[index])), int(radius_max[index]),(100, 0, 255), 2)
  cv2.circle(image, (int(x_max[index]), int(y_max[index])), int(radius_max[index]),(100, 0, 255), 2)
  b=((amount_figure.index(max(amount_figure))))

  white_color=0
  black_color=0
  for a_x in range(0,image.shape[0]+1,1):
   for a_y in range(0,image.shape[1]+1,1):   
    distance = math.sqrt((a_x - x_max[index])**2 + (a_y - y_max[index])**2)    
    if radius_max[index]>=distance:
     #cv2.imshow("Frame", images)
     #key = cv2.waitKey(1) & 0xFF 
     if image[a_y,a_x]>200:
      white_color=white_color+1
     else:
      black_color=black_color+1
  circle=white_color+black_color
  percentage=100*white_color/circle
  print("percentage",percentage)
  
 #cv2.putText(image, 'object was found', (int (amount_axeX[b]) , int (amount_axeY[b])), cv2.FONT_ITALIC, 0.4, 255) # # cv2.putText(frame,text,location,font,font size,font color, font weight, line)
  cv2.imshow("Frame", images)
  cv2.imshow('Vertical', image)
  key = cv2.waitKey(1) & 0xFF
