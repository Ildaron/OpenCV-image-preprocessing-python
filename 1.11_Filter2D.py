import cv2 
import numpy as np
src = cv2.imread('path.jpg')

ddepth = -1
change_resolution = 0
while True:
 kernel_size = 3 + 2 * (change_resolution % 5)
 kernel = np.ones((kernel_size, kernel_size), dtype=np.float32)
 kernel /= (kernel_size * kernel_size)
 dst = cv2.filter2D(src, ddepth, kernel) 
 cv2.imshow("ildar", dst)
 c = cv2.waitKey(500)
 if c == 27:
  break
 change_resolution += 1


