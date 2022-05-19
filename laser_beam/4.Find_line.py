import cv2 
import numpy as np
from matplotlib import pyplot as plt
import math

img = cv2.imread("img.jpg")
resize=100 #%
x = int(img.shape[1] * resize / 100)
y = int(img.shape[0] * resize / 100)
source=img=cv2.resize(img,(x,y))

img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
h_min = np.array((42, 28, 64), np.uint8)
h_max = np.array((151, 255, 237), np.uint8)
in_range=img = cv2.inRange(img, h_min, h_max)
#img = cv2.erode(img, None, iterations=5)
#img = cv2.dilate(img, None, iterations=5)
#kernel2 = np.ones((2, 2), np.float32)/25
#img = cv2.filter2D(src=img, ddepth=-1, kernel=kernel2)

edges=img
edges = cv2.Canny(img,1,2, L2gradient = True)
#ret,edges = cv2.threshold(edges,200,250,cv2.THRESH_BINARY) #cv2.THRESH_BINARY_INV,cv2.THRESH_TRUNC,cv2.THRESH_TOZERO,cv2.THRESH_TOZERO_INV
#cv2.imshow("Frame", edges)
plt.imshow(edges)
plt.show()

contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
for i, c in enumerate(contours):
  area = cv2.contourArea(c)
  img=cv2.drawContours(source, contours, i, (78, 90, 55), 1)

rho = 1 # distance resolution in pixels of the Hough grid
theta = np.pi / 250  # angular resolution in radians of the Hough grid
threshold = 50 # 15 minimum number of votes (intersections in Hough grid cell)
min_line_length = 60  # 150 minimum number of pixels making up a line
max_line_gap = 10  # maximum gap in pixels between connectable line segments
lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),min_line_length, max_line_gap)

number =0
cnts = cv2.findContours(in_range, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
for c in cnts:  
 ((x, y), radius) = cv2.minEnclosingCircle(c)
 if radius > 10:
  source=cv2.circle(source, (int(x), int(y)), int(radius),(255, 255, 255), 1)
  source=cv2.circle(source, (int(x), int(y)), 1,(0, 255, 255), 1)
  
for line in lines:
    #print (line)  
    for x1,y1,x2,y2 in line:
     if math.hypot(x2-x1, y2-y1)>10:
      cv2.line(source,(x1,y1),(x2,y2),(255,0,0),1)
      cv2.line(source,(x2,y2-100),(x2,y2),(15,10,0),1)      
      ba=np.array([x1,y1])-np.array([x2,y2])
      bc =np.array([x2,y2+100]) - np.array([x2,y2])
      cosine_angle = np.dot(ba,bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
      angle = np.arccos(cosine_angle) 
      pAngle = np.degrees(angle)
      print ("number"," ", number,"anble", "", pAngle)
      cv2.putText(source, str(round(pAngle,1)), (int (x1) , int (y1)-65), cv2.FONT_ITALIC, 4, 255, thickness = 20)
      cv2.putText(source, str(number), (int (x1)+45, int (y1)+45), cv2.FONT_ITALIC, 4, 255, thickness = 20)
      number +=1
plt.imshow(source)
plt.show()
