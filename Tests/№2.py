import cv2
import numpy as np
import math

frame = cv2.imread("NTO/Tests/images/7158497f-3f55-4c52-be25-97e58d63c0ac.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray,10,50)
thresh = 100
ret,thresh_img = cv2.threshold(canny, thresh, 255, cv2.THRESH_BINARY)

contours =[]
cnt, hierarchy = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for c in cnt:
        #     if len(c) > 200 :
         contours.append(c)
contours = sorted(contours, key= cv2.contourArea,reverse=True)
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
    #  else:
    #       shapes.append("circle")
num_shapes = len(shapes)

print("Количество фигур: ", num_shapes)
print("Типы фигур: ", shapes) 
# min_dist =1000
# k=0
# for cnt_1 in contours[6]:
#         x1, y1 = cnt_1[0]
#         for cnt_2 in contours[3]:
#             x2,y2 = cnt_2[0]
#             dist = np.sqrt((x1-x2)**2+(y1-y2)**2)
#             if dist < min_dist:
#                 min_dist = dist
#                 min_dist = float(min_dist) 
# if min_dist < 10:
#     	k+=1
# print('kol',k)
# print(min_dist)                               
cv2.drawContours(frame, contours, -1, (0,255,0), 1)
cv2.imshow('frame', frame)
cv2.imshow('canny',canny)
cv2.waitKey()