import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
 
 
img1 = cv.imread('img.jpg', 0)
img2 = cv.imread('marks.jpg', 0)
 
def sift_flann_demo():
    sift = cv.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
     
    # Укажите алгоритм
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict (check = 50) # Указываем количество рекурсий
 
    flann = cv.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)
    # Need to draw only good matches, so create a mask
    matchesMask = [[0, 0] for i in range(len(matches))]
    # ratio test as per Lowe's paper
    for i,(m, n) in enumerate(matches):
        if m.distance < 0.7 * n.distance:
            matchesMask[i] = [1, 0]
 
    draw_params = dict(matchColor = (0, 255, 0),
                       singlePointColor = (255, 0, 0),
                       matchesMask = matchesMask,
                       flags = 0)
    img3 = cv.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **draw_params)
 
    cv.namedWindow('img',cv.WINDOW_AUTOSIZE)
    cv.imshow('img',img3)
 
sift_flann_demo()
cv.waitKey(0)
cv.destroyAllWindows()
