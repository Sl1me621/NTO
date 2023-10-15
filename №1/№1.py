import cv2 
import numpy as np
import math

def distances(contour1, contour2):
    x1, y1, w1, h1 = cv2.boundingRect(contour1)
    x2, y2, w2, h2 = cv2.boundingRect(contour2)
    center1 = (x1 + w1 // 2, y1 + h1 // 2)
    center2 = (x2 + w2 // 2, y2 + h2 // 2)
    #cv2.line(my_photo, center1,center2,(255,255,255),3)
    distance = np.sqrt((center2[0] - center1[0])**2 + (center2[1] - center1[1])**2)
    return distance


my_photo = cv2.imread("№ss1/images/e63f4c78-0756-48b2-91a1-dd249ec57684.png")
img_grey = cv2.cvtColor(my_photo,cv2.COLOR_BGR2GRAY)
img_grey = cv2.Canny(my_photo,100,200)

thresh = 100

#get threshold image
ret,thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)

#find contours
contours = []
cnt, hierarchy = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for c in cnt:
    print(len(c))
    if len(c) > 200:
        contours.append(c)

contours = sorted(contours, key= cv2.contourArea,reverse=True)
print(len(contours))

# approx = cv2.approxPolyDP(contours[1], 0.01*cv2.arcLength(contours[1], True), True)
# print('app=',approx)
shapes = []
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

print("Количество фигур: ", num_shapes)
print("Типы фигур: ", shapes)

#  Проход по контурам
# for contour in contours:
#      Проверка размера контура
#     if cv2.contourArea(contour) < 100:
#         ind = contours.index(contour)
#         contours = np.delete(contours,[contour]) 
#         a= contours[~np.isin(np.arange(contours.size), contour)]

max_dist = 0
print(len(contours))

for i in range(len(contours)):
    for j in range(i+1, len(contours)):
        distance = distances(contours[i],contours[j])
        #print(distance)

        if distance> max_dist:
            max_dist = distance

            n = i
           
            m = j
            print(n,m)

min_dist = 1000
# x2, y2, w2, h2 = cv2.boundingRect(contours[n])
# center1 = (x2 + w2 // 2, y2 + h2 // 2)



for cnt_1 in contours[m]:
    x1, y1 = cnt_1[0]
    for cnt_2 in contours[n]:
        x2,y2 = cnt_2[0]
        dist = np.sqrt((x1-x2)**2+(y1-y2)**2)
        if dist < min_dist:
            min_dist = dist
print(min_dist)            

        


# cv2.drawContours(my_photo, contours[m], -1, (0,255,0), 3)
# cv2.drawContours(my_photo, contours[n], -1, (0,255,0), 3)
#cv2.drawContours(my_photo, contours, 6, (0,255,0), 3)
# for c in contours:
#     p= cv2.arcLength(c,True)
#     approx = cv2.approxpolyDP(c,0.02 * p, True)
#     if len(approx) > 3:
#         cv2.drawContours(my_photo, contours, -1, (0,255,0), 3)
cv2.imshow('gray', img_grey)
cv2.imshow('thresh', thresh_img)
cv2.imshow('my_photo', my_photo) # выводим итоговое изображение в окно
# cv2.setMouseCallback('my_photo',clik)    
cv2.waitKey()
# cv2.destroyAllWindows()