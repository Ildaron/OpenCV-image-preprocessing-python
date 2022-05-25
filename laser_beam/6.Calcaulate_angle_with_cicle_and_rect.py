import time
start_time = time.time()
import cv2 
import numpy as np
from matplotlib import pyplot as plt
import math

img = cv2.imread("img1.jpg")
resize=100 #%
x = int(img.shape[1] * resize / 100)
y = int(img.shape[0] * resize / 100)
source=img=cv2.resize(img,(x,y))

img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
h_min = np.array((64, 42, 52), np.uint8)    # h_min = np.array((42, 28, 64), np.uint8)
h_max = np.array((255, 255, 255), np.uint8) # h_max = np.array((151, 255, 237), np.uint8)
in_range=img = cv2.inRange(img, h_min, h_max)
#img = cv2.erode(img, None, iterations=5)
#img = cv2.dilate(img, None, iterations=5)
kernel2 = np.ones((2, 2), np.float32)/25
img = cv2.filter2D(src=img, ddepth=-1, kernel=kernel2)

edges=img
edges = cv2.Canny(img,1,2, L2gradient = True)
#ret,edges = cv2.threshold(edges,200,250,cv2.THRESH_BINARY) #cv2.THRESH_BINARY_INV,cv2.THRESH_TRUNC,cv2.THRESH_TOZERO,cv2.THRESH_TOZERO_INV
#cv2.imshow("Frame", edges)
plt.imshow(edges)
plt.show()

contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
for i, c in enumerate(contours):
  area = cv2.contourArea(c)
  img=cv2.drawContours(source, contours, i, (78, 0, 55), 2)

cnts = cv2.findContours(in_range, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
color_blue = (255,0,0)
color_yellow = (0,255,255)

for c in cnts:  
 ((x, y), radius) = cv2.minEnclosingCircle(c)
 if radius > 10:
  source=cv2.circle(source, (int(x), int(y)), int(radius),(0, 255, 255), 2)
  source=cv2.circle(source, (int(x), int(y)), 2,(0, 255, 255), 2)

  rect = cv2.minAreaRect(c) # пытаемся вписать прямоугольник
  box = cv2.boxPoints(rect) # поиск четырех вершин прямоугольника
  box = np.int0(box) # округление координат
  center = (int(rect[0][0]),int(rect[0][1]))
  area = int(rect[1][0]*rect[1][1]) # вычисление площади

  #вычисление координат двух векторов, являющихся сторонам прямоугольника
  edge1 = np.int0((box[1][0] - box[0][0],box[1][1] - box[0][1]))
  edge2 = np.int0((box[2][0] - box[1][0], box[2][1] - box[1][1]))

    # выясняем какой вектор больше
  usedEdge = edge1
  if cv2.norm(edge2) > cv2.norm(edge1):
   usedEdge = edge2
  reference = (1,0) # горизонтальный вектор, задающий горизонт

    # вычисляем угол между самой длинной стороной прямоугольника и горизонтом
  angle = 180.0/math.pi * math.acos((reference[0]*usedEdge[0] + reference[1]*usedEdge[1]) / (cv2.norm(reference) *cv2.norm(usedEdge)))
  if area > 500:
   cv2.drawContours(img,[box],0,(255,0,0),2) # рисуем прямоугольник
   cv2.circle(img, center, 5, (255,0,0), 2)  # рисуем маленький кружок в центре прямоугольника
        # выводим в кадр величину угла наклона
   if(center[0]-x>0.1 and center[1]-y>0.1):     #if (center[0]-x>20 and center[1]-y>20):
    cv2.putText(img, str(-(round (180-angle,1))), (center[0]+20, center[1]-20), cv2.FONT_HERSHEY_SIMPLEX, 1, color_yellow, 2)
   elif (center[0]-x>0.1 and center[1]-y<0.1):
    cv2.putText(img, str(-(round (angle,1))), (center[0]+20, center[1]-20), cv2.FONT_HERSHEY_SIMPLEX, 1, color_yellow, 2)
   elif (center[0]-x<0.1 and center[1]-y>0.1):
    cv2.putText(img, str(90+(round (angle,1))), (center[0]+20, center[1]-20), cv2.FONT_HERSHEY_SIMPLEX, 1, color_yellow, 2)
   else:
    cv2.putText(img, str((round (angle,1))), (center[0]+20, center[1]-20), cv2.FONT_HERSHEY_SIMPLEX, 1, color_yellow, 2)

plt.imshow(img)
plt.show()
print("--- %s seconds ---" % (time.time() - start_time))
#https://robotclass.ru/tutorials/opencv-detect-rectangle-angle/
