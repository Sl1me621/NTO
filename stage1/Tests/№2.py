import cv2
import numpy as np
import math
import os
import requests
num_shapes= 0
frame = cv2.imread("Tests/images/6ac8ff37-ede0-4351-93f2-bb8f74533b84.png")
hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv,(0,0,0),(255,255,250))
gray= cv2.bitwise_and(frame,frame,mask=mask)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#canny = cv2.Canny(gray,100,100)
thresh = 150
ret,thresh_img = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY_INV)

contours =[]
cnt, hierarchy = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for c in cnt:
    if len(c) > 100 :
        contours.append(c)
contours = sorted(contours, key= cv2.contourArea,reverse=True)
length = len(contours)
# min_dist = 1000
# for i in range(len(contours)):
#     for cnt_1 in contours[i-1]:
#         x1, y1 = cnt_1[0]
#         for cnt_2 in contours[i]:
#             x2,y2 = cnt_2[0]
#             dist = np.sqrt((x1-x2)**2+(y1-y2)**2)
#             if dist < min_dist:
#                 min_dist = dist
#     print(min_dist)            
shapes=[]
for cnt in contours:
     approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
     if len(approx) == 3:
         shapes.append("triangle")
     elif len(approx) == 4:
         x,y,w,h = cv2.boundingRect(cnt)
         if abs(w-h) <= 10:
             shapes.append("square")
         else:
             shapes.append("rectangle")
     elif len(approx) > 4 and len(approx) <= 6:
         shapes.append("polygon")
     else:
          shapes.append("circle")   
num_shapes = len(shapes)
print('cnt=',length)
print("Количество фигур: ", num_shapes)
print("Типы фигур: ", shapes)                               
cv2.drawContours(frame, contours, -1, (0,255,0), 3)
cv2.imshow('frame', frame)
cv2.imshow('gray', gray)
cv2.imshow('thresh', thresh_img)
#cv2.imshow('canny',canny)
cv2.waitKey()