import cv2
import numpy as np
import math

frame = cv2.imread("images/6ac8ff37-ede0-4351-93f2-bb8f74533b84.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray,10,50)
cv2.imshow('frame', frame)
cv2.imshow('gray', gray)
cv2.imshow('canny',canny)
cv2.waitKey()