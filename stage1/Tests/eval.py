# -*- coding: utf-8 -*-
import cv2
import numpy as np


def count_contours(image) -> int:
    frame = cv2.imread(image)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray,100,200)
    thresh = 100
    ret,thresh_img = cv2.threshold(canny, thresh, 255, cv2.THRESH_BINARY)

    contours =[]
    cnt, hierarchy = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    for c in cnt:
            #     if len(c) > 200 :
            contours.append(c)
    contours = sorted(contours, key= cv2.contourArea,reverse=True)
    
    shapes=[]
    for cnt in contours:
        print(cnt)
        approx = cv2.approxPolyDP(cnt, 0.1*cv2.arcLength(cnt, False), True)
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
        # else:
        #     shapes.append("circle")
    num_shapes = len(shapes)
    return num_shapes