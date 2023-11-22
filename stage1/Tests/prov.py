
import cv2
import numpy as np
import math
import os
import pandas as pd
contours =[]
frame = cv2.imread('C:/Users/Sl1m/kvantorium/NTO/Tests/images/6ac8ff37-ede0-4351-93f2-bb8f74533b84.png')
canny = cv2.Canny(frame,100,100)
cv2.imshow('canny',canny)
cv2.imshow('frame',frame)
cv2.waitKey()