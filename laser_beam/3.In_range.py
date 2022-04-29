import cv2
import numpy as np
import imutils
from itertools import product

image = cv2.imread("data_44.jpg")
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


 def points_in_circle(radius):
   
  for x, y in product(range(int(radius) + 1), repeat=2):
   if x**2 + y**2 <= radius**2:
    yield from set(((x, y), (x, -y), (-x, y), (-x, -y),))
 print (list(points_in_circle(radius_max[1])))
 #points_in_circle(radius_max[1])
 
 if radius > 0:  
  cv2.circle(images, (int(x_max[index]), int(y_max[index])), int(radius_max[index]),(100, 0, 255), 2)
  cv2.circle(image, (int(x_max[index]), int(y_max[index])), int(radius_max[index]),(100, 0, 255), 2)
  for a in list(points_in_circle(radius_max[1])):
   #count = cv2.countNonZero

   a_x=a[0]+x_max[1]
   a_y = a[1]+y_max[1] 
   print ("ok",image[int(a_x),int(a_y)])
  
  
  b=((amount_figure.index(max(amount_figure))))
   #cv2.putText(image, 'object was found', (int (amount_axeX[b]) , int (amount_axeY[b])), cv2.FONT_ITALIC, 0.4, 255) # # cv2.putText(frame,text,location,font,font size,font color, font weight, line)
  cv2.imshow("Frame", images)
  cv2.imshow('Vertical', image)
  key = cv2.waitKey(1) & 0xFF


   
