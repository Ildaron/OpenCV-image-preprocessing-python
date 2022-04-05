import cv2  
import numpy as np   
def CannyThreshold(lowThreshold):    
 detected_edges = cv2.GaussianBlur(gray,(3,3),0)  
 detected_edges = cv2.Canny(detected_edges,lowThreshold, lowThreshold*ratio, apertureSize = kernel_size)  #Обнаружение края  

 #dst = cv2.bitwise_and(img,img,mask = detected_edges) # just add some colours to edges from original image.  
 #kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
 #closed = cv2.morphologyEx(detected_edges, cv2.MORPH_CLOSE, kernel)
 
 contours = cv2.findContours(detected_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
 #print (contours)
 for cont in contours:
  sm = cv2.arcLength(cont, True)
  apd = cv2.approxPolyDP(cont, 0.02*sm, True)
  if len(apd) == 6:
   cv2.drawContours(detected_edges, [apd], -1, (120,55,70), 4)
   
 cv2.imshow('image',detected_edges)
 cv2.moveWindow('image',200,200) 
       
lowThreshold = 0    
max_lowThreshold = 100    
ratio = 3    
kernel_size = 3    
    
img = cv2.imread('img1.jpg')
img=cv2.resize(img,(360,460))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
    
cv2.namedWindow('canny demo')    
cv2.moveWindow('canny demo',600,200)     

cv2.createTrackbar('Min threshold','canny demo',lowThreshold, max_lowThreshold, CannyThreshold)    
CannyThreshold(0)  
if cv2.waitKey(0) == 27:  
    cv2.destroyAllWindows()
