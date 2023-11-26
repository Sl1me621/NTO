import cv2
import numpy
ans = numpy.array([[[0, 0, 0],
        [0, 0, 0], 
        [0, 0, 0]],
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]])
graymin =0,0,20
graymax =179,26,71
greenmin =50,83,26
greenmax =95,255,110
orangemin =2,120,150
orangemax =164,230,255
redmin =156,203,113
redmax =255,255,255
# col_pix_sloy_1_gray = 7124911
# col_pix_sloy_1_orange = 9999218
# col_pix_sloy_1_green = 5670068
# col_pix_sloy_1_red = 8390306

# col_pix_sloy_2_1_1_gray = 
# col_pix_sloy_2_1_1_green = 204231
# col_pix_sloy_2_1_1_red = 283688
# col_pix_sloy_2_1_1_orange = 

# col_pix_sloy_2_1_2_gray = 221684
# col_pix_sloy_2_1_2_green = 
# col_pix_sloy_2_1_2_red = 
# col_pix_sloy_2_1_2_orange = 279328

# col_pix_sloy_2_1_3_gray = 3838269
# col_pix_sloy_2_1_3_green = 3043529
# col_pix_sloy_2_1_3_red = 4353057
# col_pix_sloy_2_1_3_orange = 5112074

# col_pix_sloy_2_2_1_gray = 359410
# col_pix_sloy_2_2_1_green = 291038
# col_pix_sloy_2_2_1_red = 395524
# col_pix_sloy_2_2_1_orange = 

# col_pix_sloy_2_2_2_gray = 
# col_pix_sloy_2_2_2_green = 2826692
# col_pix_sloy_2_2_2_red = 4059576
# col_pix_sloy_2_2_2_orange = 

# col_pix_sloy_2_3_1_gray = 260052
# col_pix_sloy_2_3_1_green = 
# col_pix_sloy_2_3_1_red = 
# col_pix_sloy_2_3_1_orange = 337107

# col_pix_sloy_2_3_2_gray = 
# col_pix_sloy_2_3_2_green = 
# col_pix_sloy_2_3_2_red = 
# col_pix_sloy_2_3_2_orange =   228753

# col_pix_sloy_2_3_3_gray = 3852794
# col_pix_sloy_2_3_3_green = 
# col_pix_sloy_2_3_3_red = 4290158
# col_pix_sloy_2_3_3_orange =

# col_pix_sloy_2_4_1_gray = 
# col_pix_sloy_2_4_1_green = 290950
# col_pix_sloy_2_4_1_red = 395485
# col_pix_sloy_2_4_1_orange = 486264

# col_pix_sloy_2_4_2_gray = 
# col_pix_sloy_2_4_2_green = 3310910
# col_pix_sloy_2_4_2_red = 
# col_pix_sloy_2_4_2_orange = 5611070

# col_pix_sloy_2_5_1_gray = 4511829
# col_pix_sloy_2_5_1_green = 
# col_pix_sloy_2_5_1_red = 5304200
# col_pix_sloy_2_5_1_orange =

# col_pix_sloy_2_6_1_gray = 359332
# col_pix_sloy_2_6_1_green = 
# col_pix_sloy_2_6_1_red = 391570
# col_pix_sloy_2_6_1_orange = 483450

# col_pix_sloy_2_6_2_gray = 
# col_pix_sloy_2_6_2_green = 
# col_pix_sloy_2_6_2_red = 
# col_pix_sloy_2_6_2_orange =

# col_pix_sloy_2_7_1_gray = 221640
# col_pix_sloy_2_7_1_green = 
# col_pix_sloy_2_7_1_red = 242818
# col_pix_sloy_2_7_1_orange = 

# col_pix_sloy_2_7_2_gray = 
# col_pix_sloy_2_7_2_green = 
# col_pix_sloy_2_7_2_red = 203576
# col_pix_sloy_2_7_2_orange = 

# col_pix_sloy_2_7_3_gray = 3800733
# col_pix_sloy_2_7_3_green = 
# col_pix_sloy_2_7_3_red = 4352578
# col_pix_sloy_2_7_3_orange = 5135640

# col_pix_sloy_2_8_1_gray = 359338
# col_pix_sloy_2_8_1_green = 289152
# col_pix_sloy_2_8_1_red = 391855
# col_pix_sloy_2_8_1_orange = 483412

# col_pix_sloy_2_8_2_gray = 
# col_pix_sloy_2_8_2_green = 2851122
# col_pix_sloy_2_8_2_red = 
# col_pix_sloy_2_8_2_orange = 4629938

# col_pix_sloy_2_9_1_gray = 
# col_pix_sloy_2_9_1_green = 
# col_pix_sloy_2_9_1_red = 
# col_pix_sloy_2_9_1_orange = 211618

# col_pix_sloy_2_9_2_gray = 
# col_pix_sloy_2_9_2_green =
# col_pix_sloy_2_9_2_red = 
# col_pix_sloy_2_9_2_orange = 

# col_pix_sloy_2_9_3_gray = 3844737
# col_pix_sloy_2_9_3_green = 
# col_pix_sloy_2_9_3_red = 4377893
# col_pix_sloy_2_9_3_orange = 5154203
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
frame = cv2.imread('NTO/stage2/task 4/images/be974195-8189-4f0c-946f-25247883e9d2.jpg')
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

# cv2.line(frame_line,(120,120),(480,120),(0,255,0),1)
# cv2.line(frame_line,(120,120),(120,480),(0,255,0),1)
# cv2.line(frame_line,(120,480),(480,480),(0,255,0),1)
# cv2.line(frame_line,(480,480),(480,120),(0,255,0),1)
# cv2.line(frame_line,(120,240),(480,240),(0,255,0),1)
# cv2.line(frame_line,(120,360),(480,360),(0,255,0),1)
# cv2.line(frame_line,(240,120),(240,480),(0,255,0),1)
# cv2.line(frame_line,(360,120),(360,480),(0,255,0),1)

# cv2.line(frame_line,(435,255),(165,255),(0,255,0),1)
# cv2.line(frame_line,(435,345),(165,345),(0,255,0),1)

# cv2.line(frame_line,(240,240),(255,255),(0,255,0),1)
# cv2.line(frame_line,(360,240),(345,255),(0,255,0),1)

# cv2.line(frame_line,(240,360),(255,345),(0,255,0),1)
# cv2.line(frame_line,(360,360),(345,345),(0,255,0),1)

# cv2.line(frame_line,(480,240),(435,255),(0,255,0),1)
# cv2.line(frame_line,(375,240),(375,255),(0,255,0),1)

# cv2.line(frame_line,(345,165),(345,435),(0,255,0),1)
# cv2.line(frame_line,(255,165),(255,435),(0,255,0),1)

# cv2.line(frame_line,(345,165),(360,120),(0,255,0),1)
# cv2.line(frame_line,(240,225),(255,225),(0,255,0),1)

# cv2.line(frame_line,(360,225),(245,225),(0,255,0),1)
# cv2.line(frame_line,(255,165),(240,120),(0,255,0),1)

# cv2.line(frame_line,(225,240),(225,255),(0,255,0),1)
# cv2.line(frame_line,(120,240),(165,255),(0,255,0),1)

# cv2.line(frame_line,(120,360),(165,345),(0,255,0),1)
# cv2.line(frame_line,(225,360),(225,345),(0,255,0),1)

# cv2.line(frame_line,(240,480),(255,435),(0,255,0),1)
# cv2.line(frame_line,(240,375),(255,375),(0,255,0),1)

# cv2.line(frame_line,(360,480),(345,435),(0,255,0),1)
# cv2.line(frame_line,(360,375),(345,375),(0,255,0),1)

# cv2.line(frame_line,(480,360),(435,345),(0,255,0),1)
# cv2.line(frame_line,(375,360),(375,345),(0,255,0),1)

kub_1_1 = frame[75:225, 75:225]
kub_1_2 = frame[75:225, 225:375]
kub_1_3 = frame[75:225, 375:525]
kub_1_4 = frame[225:375, 75:225]
kub_1_5 = frame[225:375, 225:375]
kub_1_6 = frame[225:375, 375:525]
kub_1_7 = frame[375:525, 75:225]
kub_1_8 = frame[375:525, 225:375]
kub_1_9 = frame[375:525, 375:525]

kub_2_1 = frame[120:240, 120:240]

kub_2_1_1 = frame[165:225, 240:255]
kub_2_1_2 = frame[240:255, 175:225]
kub_2_1_3 = frame[120:225, 120:225]

kub_2_2 = frame[120:240, 240:360]

kub_2_2_1 = frame[240:255, 255:345]
kub_2_2_2 = frame[120:225, 255:345]

kub_2_3 = frame[120:240, 360:480]

kub_2_3_1 = frame[165:225, 345:360]
kub_2_3_2 = frame[240:255, 375:415]
kub_2_3_3 = frame[120:225, 375:480]

kub_2_4 = frame[240:360, 120:240]

kub_2_4_1 = frame[255:345, 240:255]
kub_2_4_2 = frame[240:360, 120:225]

kub_2_5 = frame[240:360, 240:360]

kub_2_6 = frame[240:360,360:480]

kub_2_6_1 = frame[255:345, 345:360]
kub_2_6_2 = frame[120:225, 375:480]

kub_2_7 = frame[360:480,120:240]

kub_2_7_1 = frame[345:360, 175:225]
kub_2_7_2 = frame[375:415, 240:255]
kub_2_7_3 = frame[375:480, 120:225]

kub_2_8 = frame[360:480,240:360]

kub_2_8_1 = frame[345:360, 255:345]
kub_2_8_2 = frame[375:480, 255:345]

kub_2_9 = frame[360:480,360:480]

kub_2_9_1 = frame[375:415, 345:360]
kub_2_9_2 = frame[345:360, 375:415]
kub_2_9_3 = frame[375:480, 375:480]

kubs_1 = [kub_1_1,kub_1_2,kub_1_3]
kubs_2 = [kub_1_4,kub_1_5,kub_1_6]
kubs_3 = [kub_1_7,kub_1_8,kub_1_9]

# h = numpy.sum(kub_2_9_1)
# print(h)
# cv2.imshow('213',kub_2_9_3)
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


# kub_2_1_1 = cv2.bitwise_and(kub_2_1_1,kub_2_1_1,mask=mask_green)
# cv2.imshow("kub1_9", kub_2_1_1)

if numpy.sum(kub_1_1)< 7130000 and numpy.sum(kub_1_1)> 7120000:
    ans[0,0,0] = 4
if numpy.sum(kub_1_1)< 10010000 and numpy.sum(kub_1_1)> 9990000:
    ans[0,0,0] = 5  
if numpy.sum(kub_1_1)< 8400000 and numpy.sum(kub_1_1)> 8380000:
    ans[0,0,0] = 2 
if numpy.sum(kub_1_1)< 5680000 and numpy.sum(kub_1_1)> 5660000:
    ans[0,0,0] = 3 

if numpy.sum(kub_1_2)< 7130000 and numpy.sum(kub_1_2)> 7120000:
    ans[0,0,1] = 4
if numpy.sum(kub_1_2)< 10010000 and numpy.sum(kub_1_2)> 9990000:
    ans[0,0,1] = 5  
if numpy.sum(kub_1_2)< 8400000 and numpy.sum(kub_1_2)> 8380000:
    ans[0,0,1] = 2 
if numpy.sum(kub_1_2)< 5680000 and numpy.sum(kub_1_2)> 5660000:
    ans[0,0,1] = 3     

if numpy.sum(kub_1_3)< 7130000 and numpy.sum(kub_1_3)> 7120000:
    ans[0,0,2] = 4
if numpy.sum(kub_1_3)< 10010000 and numpy.sum(kub_1_3)> 9990000:
    ans[0,0,2] = 5  
if numpy.sum(kub_1_3)< 8400000 and numpy.sum(kub_1_3)> 8380000:
    ans[0,0,2] = 2 
if numpy.sum(kub_1_3)< 5680000 and numpy.sum(kub_1_3)> 5660000:
    ans[0,0,2] = 3     

if numpy.sum(kub_1_4)< 7130000 and numpy.sum(kub_1_4)> 7120000:
    ans[0,1,0] = 4
if numpy.sum(kub_1_4)< 10005000 and numpy.sum(kub_1_4)> 9990000:
    ans[0,1,0] = 5  
if numpy.sum(kub_1_4)< 8400000 and numpy.sum(kub_1_4)> 8380000:
    ans[0,1,0] = 2 
if numpy.sum(kub_1_4)< 5680000 and numpy.sum(kub_1_4)> 5660000:
    ans[0,1,0] = 3    

if numpy.sum(kub_1_5)< 7130000 and numpy.sum(kub_1_5)> 7120000:
    ans[0,1,1] = 4
if numpy.sum(kub_1_5)< 10010000 and numpy.sum(kub_1_5)> 9990000:
    ans[0,1,1] = 5  
if numpy.sum(kub_1_5)< 8400000 and numpy.sum(kub_1_5)> 8380000:
    ans[0,1,1] = 2 
if numpy.sum(kub_1_5)< 5680000 and numpy.sum(kub_1_5)> 5660000:
    ans[0,1,1] = 3 

if numpy.sum(kub_1_6)< 7130000 and numpy.sum(kub_1_6)> 7120000:
    ans[0,1,2] = 4
if numpy.sum(kub_1_6)< 10010000 and numpy.sum(kub_1_6)> 9990000:
    ans[0,1,2] = 5  
if numpy.sum(kub_1_6)< 8400000 and numpy.sum(kub_1_6)> 8380000:
    ans[0,1,2] = 2 
if numpy.sum(kub_1_6)< 5680000 and numpy.sum(kub_1_6)> 5660000:
    ans[0,1,2] = 3  
    
if numpy.sum(kub_1_7)< 7130000 and numpy.sum(kub_1_7)> 7120000:
    ans[0,2,0] = 4
if numpy.sum(kub_1_7)< 10010000 and numpy.sum(kub_1_7)> 9990000:
    ans[0,2,0] = 5  
if numpy.sum(kub_1_7)< 8400000 and numpy.sum(kub_1_7)> 8380000:
    ans[0,2,0] = 2 
if numpy.sum(kub_1_7)< 5680000 and numpy.sum(kub_1_7)> 5660000:
    ans[0,2,0] = 3 
    
if numpy.sum(kub_1_8)< 7130000 and numpy.sum(kub_1_8)> 7120000:
    ans[0,2,1] = 4
if numpy.sum(kub_1_8)< 10010000 and numpy.sum(kub_1_8)> 9990000:
    ans[0,2,1] = 5  
if numpy.sum(kub_1_8)< 8400000 and numpy.sum(kub_1_8)> 8380000:
    ans[0,2,1] = 2 
if numpy.sum(kub_1_8)< 5680000 and numpy.sum(kub_1_8)> 5660000:
    ans[0,2,1] = 3 
    
if numpy.sum(kub_1_9)< 7130000 and numpy.sum(kub_1_9)> 7120000:
    ans[0,2,2] = 4
if numpy.sum(kub_1_9)< 10010000 and numpy.sum(kub_1_9)> 9990000:
    ans[0,2,2] = 5  
if numpy.sum(kub_1_9)< 8400000 and numpy.sum(kub_1_9)> 8380000:
    ans[0,2,2] = 2 
if numpy.sum(kub_1_9)< 5680000 and numpy.sum(kub_1_9)> 5660000:
    ans[0,2,2] = 3    
    
    
# if numpy.sum(kub_2_1_3)< 3900000 and numpy.sum(kub_2_1_3)> 3800000:
#     ans[1,0,0] = 4
# if numpy.sum(kub_2_1_3)< 5200000 and numpy.sum(kub_2_1_3)> 5100000:
#     ans[1,0,0] = 5  
# if numpy.sum(kub_2_1_3)< 4400000 and numpy.sum(kub_2_1_3)> 4300000:
#     ans[1,0,0] = 2 
# if numpy.sum(kub_2_1_3)< 3100000 and numpy.sum(kub_2_1_3)> 3000000:
#     ans[1,0,0] = 3
    
# if numpy.sum(kub_2_1_1)< 3900000 and numpy.sum(kub_2_1_1)> 3800000:
#     ans[1,0,0] = 4
# if numpy.sum(kub_2_1_1)< 5200000 and numpy.sum(kub_2_1_1)> 5100000:
#     ans[1,0,0] = 5  
# if numpy.sum(kub_2_1_1)< 4400000 and numpy.sum(kub_2_1_1)> 4300000:
#     ans[1,0,0] = 2 
# if numpy.sum(kub_2_1_1)< 3100000 and numpy.sum(kub_2_1_1)> 3000000:
#     ans[1,0,0] = 3        
                                                                                                      
# h = numpy.sum(kub_1_1)
# print(h)
print(ans)
# cv2.imshow("kub1_1", kub_1_1)
# cv2.imshow("kub1_2", kub_1_2)
# cv2.imshow("kub1_3", kub_1_3)
# cv2.imshow("kub1_4", kub_1_4)
# cv2.imshow("kub1_5", kub_1_5)
# cv2.imshow("kub1_6", kub_1_6)
# cv2.imshow("kub1_7", kub_1_7)
# cv2.imshow("kub1_8", kub_1_8)
# cv2.imshow("kub1_9", kub_1_9)
# cv2.imshow("kub2_1", kub_2_1)
# cv2.imshow("kub2_1_1", kub_2_1_1)
# cv2.imshow("kub2_1_2", kub_2_1_2)
# cv2.imshow("kub2_1_3", kub_2_1_3)
# cv2.imshow("kub2_2", kub_2_2)
# cv2.imshow("kub2_2_1", kub_2_2_1)
# cv2.imshow("kub2_2_2", kub_2_2_2)
# cv2.imshow("kub2_3", kub_2_3)
# cv2.imshow("kub2_3_1", kub_2_3_1)
# cv2.imshow("kub2_3_2", kub_2_3_2)
# cv2.imshow("kub2_3_3", kub_2_3_3)
# cv2.imshow("kub2_4", kub_2_4)
# cv2.imshow("kub2_4_1", kub_2_4_1)
# cv2.imshow("kub2_4_2", kub_2_4_2)
# cv2.imshow("kub2_5", kub_2_5)
# cv2.imshow("kub2_6", kub_2_6)
# cv2.imshow("kub2_6_1", kub_2_6_1)
# cv2.imshow("kub2_6_2", kub_2_6_2)
# cv2.imshow("kub2_7", kub_2_7)
# cv2.imshow("kub2_7_1", kub_2_7_1)
# cv2.imshow("kub2_7_2", kub_2_7_2)
# cv2.imshow("kub2_7_3", kub_2_7_3)
# cv2.imshow("kub2_8", kub_2_8)
# cv2.imshow("kub2_8_1", kub_2_8_1)
# cv2.imshow("kub2_8_2", kub_2_8_2)
# cv2.imshow("kub2_9", kub_2_9)
# cv2.imshow("kub2_9_1", kub_2_9_1)
# cv2.imshow("kub2_9_2", kub_2_9_2)
# cv2.imshow("kub2_9_3", kub_2_9_3)
# cv2.imshow('gray',gray)
# cv2.imshow('green',green)
# cv2.imshow('red',red)
# cv2.imshow('orange',orange)
# cv2.imshow('mask_gray',mask_gray)
# cv2.imshow('mask_green',mask_green)
# cv2.imshow('mask_red',mask_red)
#cv2.imshow('mask_orange',mask_orange)
cv2.imshow('frame',frame)
# k =findcolors_(kub_1_1,orangemin,orangemax)
# print(k)
cv2.waitKey()
cv2.destroyAllWindows()