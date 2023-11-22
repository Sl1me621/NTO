import cv2
import numpy
graymin =0,0,20
graymax =179,26,71
greenmin =50,83,26
greenmax =95,255,110
orangemin =2,120,150
orangemax =164,230,255
redmin =156,203,113
redmax =255,255,255
def findcolors_(img,colmin,colmax):
    cv2.imshow('frame',img)
    hsv_ = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_,(colmin),(colmax))    
    mask = cv2.erode(mask,None,iterations=2)
    mask = cv2.dilate(mask,None,iterations=4)
    cv2.imshow('mask',mask)

    contours = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    contours =contours[0]

    if contours:
        sorted(contours, key=cv2.contourArea,reverse=True)
        cv2.drawContours(img, contours,-1,(255,0,0),3)
        k= 1
        return k
        time.sleep(1)    
frame = cv2.imread('stage2/task 4/images/bac84567-18a3-42bf-9299-caa192417aa5.jpg')
# canny = cv2.Canny(frame,100,100)
# gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
frame_line = frame
# cv2.line(frame_line, (75,75),(525,75),(0,255,0),3)
# cv2.line(frame_line, (75,75),(75,525),(0,255,0),3)
# cv2.line(frame_line, (525,525),(525,75),(0,255,0),3)
# cv2.line(frame_line, (75,525),(525,525),(0,255,0),3)
# cv2.line(frame_line, (75,225),(525,225),(0,255,0),3)
# cv2.line(frame_line, (75,375),(525,375),(0,255,0),3)
# cv2.line(frame_line, (225,75),(225,525),(0,255,0),3)
# cv2.line(frame_line, (375,75),(375,525),(0,255,0),3)

cv2.line(frame_line,(120,120),(480,120),(0,255,0),1)
cv2.line(frame_line,(120,120),(120,480),(0,255,0),1)
cv2.line(frame_line,(120,480),(480,480),(0,255,0),1)
cv2.line(frame_line,(480,480),(480,120),(0,255,0),1)
cv2.line(frame_line,(120,240),(480,240),(0,255,0),1)
cv2.line(frame_line,(120,360),(480,360),(0,255,0),1)
cv2.line(frame_line,(240,120),(240,480),(0,255,0),1)
cv2.line(frame_line,(360,120),(360,480),(0,255,0),1)

cv2.line(frame_line,(435,255),(165,255),(0,255,0),1)
cv2.line(frame_line,(435,345),(165,345),(0,255,0),1)

cv2.line(frame_line,(240,240),(255,255),(0,255,0),1)
cv2.line(frame_line,(360,240),(345,255),(0,255,0),1)

cv2.line(frame_line,(240,360),(255,345),(0,255,0),1)
cv2.line(frame_line,(360,360),(345,345),(0,255,0),1)

cv2.line(frame_line,(480,240),(435,255),(0,255,0),1)
cv2.line(frame_line,(375,240),(375,255),(0,255,0),1)

cv2.line(frame_line,(345,165),(345,435),(0,255,0),1)
cv2.line(frame_line,(255,165),(255,435),(0,255,0),1)

cv2.line(frame_line,(345,165),(360,120),(0,255,0),1)
cv2.line(frame_line,(240,225),(255,225),(0,255,0),1)

cv2.line(frame_line,(360,225),(245,225),(0,255,0),1)
cv2.line(frame_line,(255,165),(240,120),(0,255,0),1)

cv2.line(frame_line,(225,240),(225,255),(0,255,0),1)
cv2.line(frame_line,(120,240),(165,255),(0,255,0),1)

cv2.line(frame_line,(120,360),(165,345),(0,255,0),1)
cv2.line(frame_line,(225,360),(225,345),(0,255,0),1)

cv2.line(frame_line,(240,480),(255,435),(0,255,0),1)
cv2.line(frame_line,(240,375),(255,375),(0,255,0),1)

cv2.line(frame_line,(360,480),(345,435),(0,255,0),1)
cv2.line(frame_line,(360,375),(345,375),(0,255,0),1)

cv2.line(frame_line,(480,360),(435,345),(0,255,0),1)
cv2.line(frame_line,(375,360),(375,345),(0,255,0),1)

kub_1_1 = frame[75:225, 75:225]
kub_1_2 = frame[75:225, 225:375]
kub_1_3 = frame[75:225, 375:525]
kub_1_4 = frame[225:375, 75:225]
kub_1_5 = frame[225:375, 225:375]
kub_1_6 = frame[225:375, 375:525]
kub_1_7 = frame[375:525, 75:225]
kub_1_8 = frame[375:525, 225:375]
kub_1_9 = frame[375:525, 375:525]

kub_2_1 = frame[75:225, 75:225]

hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
mask_green = cv2.inRange(hsv,(greenmin),(greenmax))
mask_gray = cv2.inRange(hsv,(graymin),(graymax))
mask_orange = cv2.inRange(hsv,(orangemin),(orangemax))
mask_red = cv2.inRange(hsv,(redmin),(redmax))
mask_green = cv2.erode(mask_green,None,iterations=2)
mask_green = cv2.dilate(mask_green,None,iterations=4)
mask_gray = cv2.erode(mask_gray,None,iterations=2)
mask_gray = cv2.dilate(mask_gray,None,iterations=4)
mask_red = cv2.erode(mask_red,None,iterations=2)
mask_red = cv2.dilate(mask_red,None,iterations=4)
mask_orange = cv2.erode(mask_orange,None,iterations=2)
mask_orange = cv2.dilate(mask_orange,None,iterations=4)
green = cv2.bitwise_and(frame,frame,mask=mask_green)
gray = cv2.bitwise_and(frame,frame,mask=mask_gray)
orange = cv2.bitwise_and(frame,frame,mask=mask_orange)
red = cv2.bitwise_and(frame,frame,mask=mask_red)
# cv2.imshow("kub1", kub_1_1)
# cv2.imshow("kub2", kub_1_2)
# cv2.imshow("kub3", kub_1_3)
# cv2.imshow("kub4", kub_1_4)
# cv2.imshow("kub5", kub_1_5)
# cv2.imshow("kub6", kub_1_6)
# cv2.imshow("kub7", kub_1_7)
# cv2.imshow("kub8", kub_1_8)
# cv2.imshow("kub9", kub_1_9)
# cv2.imshow('gray',gray)
# cv2.imshow('green',green)
# cv2.imshow('red',red)
# cv2.imshow('orange',orange)
# cv2.imshow('mask_gray',mask_gray)
# cv2.imshow('mask_green',mask_green)
# cv2.imshow('mask_red',mask_red)
# cv2.imshow('mask_orange',mask_orange)
cv2.imshow('frame',frame)
# k =findcolors_(kub_1_1,orangemin,orangemax)
# print(k)
cv2.waitKey()
cv2.destroyAllWindows()
