import cv2
cap = cv2.VideoCapture(0)
while True:
    cv2.imshow('fdf',cap)
cv2.waitKey()