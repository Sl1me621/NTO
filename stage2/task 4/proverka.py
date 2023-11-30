import cv2
import numpy 
graymin =0,0,20
graymax =185,37,77
greenmin =50,83,26
greenmax =95,255,110
orangemin =2,120,150
orangemax =164,230,255
redmin =156,203,113
redmax =255,255,255
  
def load_tools() -> list:
    tools = []
    return tools


def count_the_types_of_cubes(image) -> numpy.array:
    frame = image
    frame = cv2.imread(frame)
    result = numpy.array([[[0, 0, 0],[0, 0, 0],[0, 0, 0]],[[0, 0, 0],[0, 0, 0],[0, 0, 0]]])
    ans = numpy.array([[[0, 0, 0],[0, 0, 0],[0, 0, 0]],[[0, 0, 0],[0, 0, 0],[0, 0, 0]]])
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
    kub_2_6_2 = frame[240:360, 375:480]

    kub_2_7 = frame[360:480,120:240]

    kub_2_7_1 = frame[345:360, 175:225]
    kub_2_7_2 = frame[375:415, 240:255]
    kub_2_7_3 = frame[375:480, 120:225]

    kub_2_8 = frame[360:480,240:360]

    kub_2_8_1 = frame[345:360, 255:345]
    kub_2_8_2 = frame[375:480, 255:345]

    kub_2_9 = frame[360:480,360:480]

    kub_2_9_1 = frame[345:360, 375:415]
    kub_2_9_2 = frame[375:415, 345:360]
    kub_2_9_3 = frame[375:480, 375:480]

    kubs_1 = [kub_1_1,kub_1_2,kub_1_3]
    kubs_2 = [kub_1_4,kub_1_5,kub_1_6]
    kubs_3 = [kub_1_7,kub_1_8,kub_1_9]
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

    # cv2.imshow('fdf', mask_gray)


    hsv_2_1_1 = cv2.cvtColor(kub_2_1_1 ,cv2.COLOR_BGR2HSV)
    mask_green_2_1_1  = cv2.inRange(hsv_2_1_1 ,(greenmin),(greenmax))
    mask_gray_2_1_1  = cv2.inRange(hsv_2_1_1 ,(graymin),(graymax))
    mask_orange_2_1_1  = cv2.inRange(hsv_2_1_1 ,(orangemin),(orangemax))
    mask_red_2_1_1  = cv2.inRange(hsv_2_1_1 ,(redmin),(redmax))
    # mask_green_2_1_1  = cv2.erode(mask_green_2_1_1 ,None,iterations=2)
    # mask_green_2_1_1  = cv2.dilate(mask_green_2_1_1 ,None,iterations=4)
    # mask_gray_2_1_1 = cv2.erode(mask_gray_2_1_1 ,None,iterations=2)
    # mask_gray_2_1_1  = cv2.dilate(mask_gray_2_1_1 ,None,iterations=4)
    # mask_red_2_1_1  = cv2.erode(mask_red_2_1_1 ,None,iterations=2)
    # mask_red_2_1_1 = cv2.dilate(mask_red_2_1_1 ,None,iterations=4)
    # mask_orange_2_1_1  = cv2.erode(mask_orange_2_1_1 ,None,iterations=2)
    # mask_orange_2_1_1  = cv2.dilate(mask_orange_2_1_1 ,None,iterations=4)
    green_2_1_1  = cv2.bitwise_and(kub_2_1_1 ,kub_2_1_1 ,mask=mask_green_2_1_1 )
    gray_2_1_1  = cv2.bitwise_and(kub_2_1_1 ,kub_2_1_1 ,mask=mask_gray_2_1_1 )
    orange_2_1_1 = cv2.bitwise_and(kub_2_1_1 ,kub_2_1_1 ,mask=mask_orange_2_1_1 )
    red_2_1_1  = cv2.bitwise_and(kub_2_1_1 ,kub_2_1_1  ,mask=mask_red_2_1_1 )

    hsv_2_1_2 = cv2.cvtColor(kub_2_1_2  ,cv2.COLOR_BGR2HSV)
    mask_green_2_1_2   = cv2.inRange(hsv_2_1_2  ,(greenmin),(greenmax))
    mask_gray_2_1_2   = cv2.inRange(hsv_2_1_2  ,(graymin),(graymax))
    mask_orange_2_1_2   = cv2.inRange(hsv_2_1_2  ,(orangemin),(orangemax))
    mask_red_2_1_2   = cv2.inRange(hsv_2_1_2  ,(redmin),(redmax))
    # mask_green_2_1_2   = cv2.erode(mask_green_2_1_2  ,None,iterations=2)
    # mask_green_2_1_2   = cv2.dilate(mask_green_2_1_2  ,None,iterations=4)
    # mask_gray_2_1_2  = cv2.erode(mask_gray_2_1_2  ,None,iterations=2)
    # mask_gray_2_1_2  = cv2.dilate(mask_gray_2_1_2  ,None,iterations=4)
    # mask_red_2_1_2   = cv2.erode(mask_red_2_1_2   ,None,iterations=2)
    # mask_red_2_1_2  = cv2.dilate(mask_red_2_1_2 ,None,iterations=4)
    # mask_orange_2_1_2   = cv2.erode(mask_orange_2_1_2  ,None,iterations=2)
    # mask_orange_2_1_2   = cv2.dilate(mask_orange_2_1_2  ,None,iterations=4)
    green_2_1_2   = cv2.bitwise_and(kub_2_1_2  ,kub_2_1_2  ,mask=mask_green_2_1_2 )
    gray_2_1_2  = cv2.bitwise_and(kub_2_1_2  ,kub_2_1_2  ,mask=mask_gray_2_1_2  )
    orange_2_1_2  = cv2.bitwise_and(kub_2_1_2  ,kub_2_1_2  ,mask=mask_orange_2_1_2  )
    red_2_1_2  = cv2.bitwise_and(kub_2_1_2  ,kub_2_1_2   ,mask=mask_red_2_1_2  )



    hsv_2_1_3 = cv2.cvtColor(kub_2_1_3 ,cv2.COLOR_BGR2HSV)
    mask_green_2_1_3  = cv2.inRange(hsv_2_1_3 ,(greenmin),(greenmax))
    mask_gray_2_1_3  = cv2.inRange(hsv_2_1_3 ,(graymin),(graymax))
    mask_orange_2_1_3  = cv2.inRange(hsv_2_1_3 ,(orangemin),(orangemax))
    mask_red_2_1_3  = cv2.inRange(hsv_2_1_3 ,(redmin),(redmax))
    mask_green_2_1_3  = cv2.erode(mask_green_2_1_3 ,None,iterations=2)
    mask_green_2_1_3  = cv2.dilate(mask_green_2_1_3 ,None,iterations=4)
    mask_gray_2_1_3 = cv2.erode(mask_gray_2_1_3 ,None,iterations=2)
    mask_gray_2_1_3  = cv2.dilate(mask_gray_2_1_3 ,None,iterations=4)
    mask_red_2_1_3  = cv2.erode(mask_red_2_1_3 ,None,iterations=2)
    mask_red_2_1_3  = cv2.dilate(mask_red_2_1_3 ,None,iterations=4)
    mask_orange_2_1_3  = cv2.erode(mask_orange_2_1_3 ,None,iterations=2)
    mask_orange_2_1_3  = cv2.dilate(mask_orange_2_1_3 ,None,iterations=4)
    green_2_1_3  = cv2.bitwise_and(kub_2_1_3 ,kub_2_1_3 ,mask=mask_green_2_1_3 )
    gray_2_1_3  = cv2.bitwise_and(kub_2_1_3 ,kub_2_1_3 ,mask=mask_gray_2_1_3 )
    orange_2_1_3 = cv2.bitwise_and(kub_2_1_3 ,kub_2_1_3 ,mask=mask_orange_2_1_3 )
    red_2_1_3  = cv2.bitwise_and(kub_2_1_3 ,kub_2_1_3  ,mask=mask_red_2_1_3 )

    hsv_2_2_1 = cv2.cvtColor(kub_2_2_1,cv2.COLOR_BGR2HSV)
    mask_green_2_2_1 = cv2.inRange(hsv_2_2_1,(greenmin),(greenmax))
    mask_gray_2_2_1= cv2.inRange(hsv_2_2_1,(graymin),(graymax))
    mask_orange_2_2_1 = cv2.inRange(hsv_2_2_1,(orangemin),(orangemax))
    mask_red_2_2_1 = cv2.inRange(hsv_2_2_1,(redmin),(redmax))
    # mask_green_2_2_1 = cv2.erode(mask_green_2_2_1,None,iterations=2)
    # mask_green_2_2_1 = cv2.dilate(mask_green_2_2_1,None,iterations=4)
    # mask_gray_2_2_1= cv2.erode(mask_gray_2_2_1,None,iterations=2)
    # mask_gray_2_2_1 = cv2.dilate(mask_gray_2_2_1,None,iterations=4)
    # mask_red_2_2_1 = cv2.erode(mask_red_2_2_1,None,iterations=2)
    # mask_red_2_2_1= cv2.dilate(mask_red_2_2_1,None,iterations=4)
    # mask_orange_2_2_1 = cv2.erode(mask_orange_2_2_1,None,iterations=2)
    # mask_orange_2_2_1 = cv2.dilate(mask_orange_2_2_1,None,iterations=4)
    green_2_2_1= cv2.bitwise_and(kub_2_2_1,kub_2_2_1,mask=mask_green_2_2_1)
    gray_2_2_1 = cv2.bitwise_and(kub_2_2_1,kub_2_2_1,mask=mask_gray_2_2_1)
    orange_2_2_1= cv2.bitwise_and(kub_2_2_1,kub_2_2_1,mask=mask_orange_2_2_1)
    red_2_2_1 = cv2.bitwise_and(kub_2_2_1,kub_2_2_1,mask=mask_red_2_2_1)

    hsv_2_2_2 = cv2.cvtColor(kub_2_2_2,cv2.COLOR_BGR2HSV)
    mask_green_2_2_2 = cv2.inRange(hsv_2_2_2,(greenmin),(greenmax))
    mask_gray_2_2_2 = cv2.inRange(hsv_2_2_2,(graymin),(graymax))
    mask_orange_2_2_2 = cv2.inRange(hsv_2_2_2,(orangemin),(orangemax))
    mask_red_2_2_2 = cv2.inRange(hsv_2_2_2,(redmin),(redmax))
    mask_green_2_2_2 = cv2.erode(mask_green_2_2_2,None,iterations=2)
    mask_green_2_2_2 = cv2.dilate(mask_green_2_2_2,None,iterations=4)
    mask_gray_2_2_2= cv2.erode(mask_gray_2_2_2,None,iterations=2)
    mask_gray_2_2_2 = cv2.dilate(mask_gray_2_2_2,None,iterations=4)
    mask_red_2_2_2 = cv2.erode(mask_red_2_2_2,None,iterations=2)
    mask_red_2_2_2 = cv2.dilate(mask_red_2_2_2,None,iterations=4)
    mask_orange_2_2_2 = cv2.erode(mask_orange_2_2_2,None,iterations=2)
    mask_orange_2_2_2 = cv2.dilate(mask_orange_2_2_2,None,iterations=4)
    green_2_2_2 = cv2.bitwise_and(kub_2_2_2,kub_2_2_2,mask=mask_green_2_2_2)
    gray_2_2_2 = cv2.bitwise_and(kub_2_2_2,kub_2_2_2,mask=mask_gray_2_2_2)
    orange_2_2_2= cv2.bitwise_and(kub_2_2_2,kub_2_2_2,mask=mask_orange_2_2_2)
    red_2_2_2 = cv2.bitwise_and(kub_2_2_2,kub_2_2_2,mask=mask_red_2_2_2)

    hsv_2_3_1 = cv2.cvtColor(kub_2_3_1,cv2.COLOR_BGR2HSV)
    mask_green_2_3_1 = cv2.inRange(hsv_2_3_1,(greenmin),(greenmax))
    mask_gray_2_3_1 = cv2.inRange(hsv_2_3_1,(graymin),(graymax))
    mask_orange_2_3_1 = cv2.inRange(hsv_2_3_1,(orangemin),(orangemax))
    mask_red_2_3_1 = cv2.inRange(hsv_2_3_1,(redmin),(redmax))
    # mask_green_2_3_1 = cv2.erode(mask_green_2_3_1,None,iterations=2)
    # mask_green_2_3_1 = cv2.dilate(mask_green_2_3_1,None,iterations=4)
    # mask_gray_2_3_1 = cv2.erode(mask_gray_2_3_1,None,iterations=2)
    # mask_gray_2_3_1 = cv2.dilate(mask_gray_2_3_1,None,iterations=4)
    # mask_red_2_3_1 = cv2.erode(mask_red_2_3_1,None,iterations=2)
    # mask_red_2_3_1 = cv2.dilate(mask_red_2_3_1,None,iterations=4)
    # mask_orange_2_3_1 = cv2.erode(mask_orange_2_3_1,None,iterations=2)
    # mask_orange_2_3_1 = cv2.dilate(mask_orange_2_3_1,None,iterations=4)
    green_2_3_1 = cv2.bitwise_and(kub_2_3_1,kub_2_3_1,mask=mask_green_2_3_1)
    gray_2_3_1= cv2.bitwise_and(kub_2_3_1,kub_2_3_1,mask=mask_gray_2_3_1)
    orange_2_3_1= cv2.bitwise_and(kub_2_3_1,kub_2_3_1,mask=mask_orange_2_3_1)
    red_2_3_1 = cv2.bitwise_and(kub_2_3_1,kub_2_3_1,mask=mask_red_2_3_1)


    hsv_2_3_2 = cv2.cvtColor(kub_2_3_2,cv2.COLOR_BGR2HSV)
    mask_green_2_3_2 = cv2.inRange(hsv_2_3_2,(greenmin),(greenmax))
    mask_gray_2_3_2 = cv2.inRange(hsv_2_3_2,(graymin),(graymax))
    mask_orange_2_3_2 = cv2.inRange(hsv_2_3_2,(orangemin),(orangemax))
    mask_red_2_3_2 = cv2.inRange(hsv_2_3_2,(redmin),(redmax))
    # mask_green_2_3_2 = cv2.erode(mask_green_2_3_2,None,iterations=2)
    # mask_green_2_3_2 = cv2.dilate(mask_green_2_3_2,None,iterations=4)
    # mask_gray_2_3_2 = cv2.erode(mask_gray_2_3_2,None,iterations=2)
    # mask_gray_2_3_2 = cv2.dilate(mask_gray_2_3_2,None,iterations=4)
    # mask_red_2_3_2 = cv2.erode(mask_red_2_3_2,None,iterations=2)
    # mask_red_2_3_2 = cv2.dilate(mask_red_2_3_2,None,iterations=4)
    # mask_orange_2_3_2 = cv2.erode(mask_orange_2_3_2,None,iterations=2)
    # mask_orange_2_3_2 = cv2.dilate(mask_orange_2_3_2,None,iterations=4)
    green_2_3_2 = cv2.bitwise_and(kub_2_3_2,kub_2_3_2,mask=mask_green_2_3_2)
    gray_2_3_2= cv2.bitwise_and(kub_2_3_2,kub_2_3_2,mask=mask_gray_2_3_2)
    orange_2_3_2= cv2.bitwise_and(kub_2_3_2,kub_2_3_2,mask=mask_orange_2_3_2)
    red_2_3_2 = cv2.bitwise_and(kub_2_3_2,kub_2_3_2,mask=mask_red_2_3_2)

    hsv_2_3_3 = cv2.cvtColor(kub_2_3_3,cv2.COLOR_BGR2HSV)
    mask_green_2_3_3 = cv2.inRange(hsv_2_3_3,(greenmin),(greenmax))
    mask_gray_2_3_3 = cv2.inRange(hsv_2_3_3,(graymin),(graymax))
    mask_orange_2_3_3 = cv2.inRange(hsv_2_3_3,(orangemin),(orangemax))
    mask_red_2_3_3 = cv2.inRange(hsv_2_3_3,(redmin),(redmax))
    mask_green_2_3_3 = cv2.erode(mask_green_2_3_3,None,iterations=2)
    mask_green_2_3_3 = cv2.dilate(mask_green_2_3_3,None,iterations=4)
    mask_gray_2_3_3 = cv2.erode(mask_gray_2_3_3,None,iterations=2)
    mask_gray_2_3_3 = cv2.dilate(mask_gray_2_3_3,None,iterations=4)
    mask_red_2_3_3 = cv2.erode(mask_red_2_3_3,None,iterations=2)
    mask_red_2_3_3 = cv2.dilate(mask_red_2_3_3,None,iterations=4)
    mask_orange_2_3_3 = cv2.erode(mask_orange_2_3_3,None,iterations=2)
    mask_orange_2_3_3 = cv2.dilate(mask_orange_2_3_3,None,iterations=4)
    green_2_3_3 = cv2.bitwise_and(kub_2_3_3,kub_2_3_3,mask=mask_green_2_3_3)
    gray_2_3_3 = cv2.bitwise_and(kub_2_3_3,kub_2_3_3,mask=mask_gray_2_3_3)
    orange_2_3_3= cv2.bitwise_and(kub_2_3_3,kub_2_3_3,mask=mask_orange_2_3_3)
    red_2_3_3 = cv2.bitwise_and(kub_2_3_3,kub_2_3_3,mask=mask_red_2_3_3)

    hsv_2_4_1 = cv2.cvtColor(kub_2_4_1,cv2.COLOR_BGR2HSV)
    mask_green_2_4_1= cv2.inRange(hsv_2_4_1,(greenmin),(greenmax))
    mask_gray_2_4_1= cv2.inRange(hsv_2_4_1,(graymin),(graymax))
    mask_orange_2_4_1 = cv2.inRange(hsv_2_4_1,(orangemin),(orangemax))
    mask_red_2_4_1 = cv2.inRange(hsv_2_4_1,(redmin),(redmax))
    # mask_green_2_4_1 = cv2.erode(mask_green_2_4_1,None,iterations=2)
    # mask_green_2_4_1 = cv2.dilate(mask_green_2_4_1,None,iterations=4)
    # mask_gray_2_4_1= cv2.erode(mask_gray_2_4_1,None,iterations=2)
    # mask_gray_2_4_1 = cv2.dilate(mask_gray_2_4_1,None,iterations=4)
    # mask_red_2_4_1 = cv2.erode(mask_red_2_4_1,None,iterations=2)
    # mask_red_2_4_1 = cv2.dilate(mask_red_2_4_1,None,iterations=4)
    # mask_orange_2_4_1 = cv2.erode(mask_orange_2_4_1,None,iterations=2)
    # mask_orange_2_4_1 = cv2.dilate(mask_orange_2_4_1,None,iterations=4)
    green_2_4_1 = cv2.bitwise_and(kub_2_4_1,kub_2_4_1,mask=mask_green_2_4_1)
    gray_2_4_1= cv2.bitwise_and(kub_2_4_1,kub_2_4_1,mask=mask_gray_2_4_1)
    orange_2_4_1= cv2.bitwise_and(kub_2_4_1,kub_2_4_1,mask=mask_orange_2_4_1)
    red_2_4_1= cv2.bitwise_and(kub_2_4_1,kub_2_4_1,mask=mask_red_2_4_1)

    hsv_2_4_2 = cv2.cvtColor(kub_2_4_2,cv2.COLOR_BGR2HSV)
    mask_green_2_4_2 = cv2.inRange(hsv_2_4_2,(greenmin),(greenmax))
    mask_gray_2_4_2 = cv2.inRange(hsv_2_4_2,(graymin),(graymax))
    mask_orange_2_4_2 = cv2.inRange(hsv_2_4_2,(orangemin),(orangemax))
    mask_red_2_4_2 = cv2.inRange(hsv_2_4_2,(redmin),(redmax))
    mask_green_2_4_2 = cv2.erode(mask_green_2_4_2,None,iterations=2)
    mask_green_2_4_2 = cv2.dilate(mask_green_2_4_2,None,iterations=4)
    mask_gray_2_4_2 = cv2.erode(mask_gray_2_4_2,None,iterations=2)
    mask_gray_2_4_2 = cv2.dilate(mask_gray_2_4_2,None,iterations=4)
    mask_red_2_4_2 = cv2.erode(mask_red_2_4_2,None,iterations=2)
    mask_red_2_4_2 = cv2.dilate(mask_red_2_4_2,None,iterations=4)
    mask_orange_2_4_2 = cv2.erode(mask_orange_2_4_2,None,iterations=2)
    mask_orange_2_4_2 = cv2.dilate(mask_orange_2_4_2,None,iterations=4)
    green_2_4_2 = cv2.bitwise_and(kub_2_4_2,kub_2_4_2,mask=mask_green_2_4_2)
    gray_2_4_2 = cv2.bitwise_and(kub_2_4_2,kub_2_4_2,mask=mask_gray_2_4_2)
    orange_2_4_2= cv2.bitwise_and(kub_2_4_2,kub_2_4_2,mask=mask_orange_2_4_2)
    red_2_4_2 = cv2.bitwise_and(kub_2_4_2,kub_2_4_2,mask=mask_red_2_4_2)


    hsv_2_5 = cv2.cvtColor(kub_2_5,cv2.COLOR_BGR2HSV)
    mask_green_2_5 = cv2.inRange(hsv_2_5,(greenmin),(greenmax))
    mask_gray_2_5 = cv2.inRange(hsv_2_5,(graymin),(graymax))
    mask_orange_2_5 = cv2.inRange(hsv_2_5,(orangemin),(orangemax))
    mask_red_2_5 = cv2.inRange(hsv_2_5,(redmin),(redmax))
    mask_green_2_5 = cv2.erode(mask_green_2_5,None,iterations=2)
    mask_green_2_5 = cv2.dilate(mask_green_2_5,None,iterations=4)
    mask_gray_2_5 = cv2.erode(mask_gray_2_5,None,iterations=2)
    mask_gray_2_5 = cv2.dilate(mask_gray_2_5,None,iterations=4)
    mask_red_2_5 = cv2.erode(mask_red_2_5,None,iterations=2)
    mask_red_2_5 = cv2.dilate(mask_red_2_5,None,iterations=4)
    mask_orange_2_5 = cv2.erode(mask_orange_2_5,None,iterations=2)
    mask_orange_2_5 = cv2.dilate(mask_orange_2_5,None,iterations=4)
    green_2_5 = cv2.bitwise_and(kub_2_5,kub_2_5,mask=mask_green_2_5)
    gray_2_5 = cv2.bitwise_and(kub_2_5,kub_2_5,mask=mask_gray_2_5)
    orange_2_5 = cv2.bitwise_and(kub_2_5,kub_2_5,mask=mask_orange_2_5)
    red_2_5 = cv2.bitwise_and(kub_2_5,kub_2_5,mask=mask_red_2_5)

    hsv_2_6_1 = cv2.cvtColor(kub_2_6_1 ,cv2.COLOR_BGR2HSV)
    mask_green_2_6_1  = cv2.inRange(hsv_2_6_1 ,(greenmin),(greenmax))
    mask_gray_2_6_1  = cv2.inRange(hsv_2_6_1 ,(graymin),(graymax))
    mask_orange_2_6_1  = cv2.inRange(hsv_2_6_1 ,(orangemin),(orangemax))
    mask_red_2_6_1  = cv2.inRange(hsv_2_6_1 ,(redmin),(redmax))
    # mask_green_2_6_1 = cv2.erode(mask_green_2_6_1 ,None,iterations=2)
    # mask_green_2_6_1   = cv2.dilate(mask_green_2_6_1 ,None,iterations=4)
    # mask_gray_2_6_1  = cv2.erode(mask_gray_2_6_1 ,None,iterations=2)
    # mask_gray_2_6_1 = cv2.dilate(mask_gray_2_6_1 ,None,iterations=4)
    # mask_red_2_6_1  = cv2.erode(mask_red_2_6_1  ,None,iterations=2)
    # mask_red_2_6_1  = cv2.dilate(mask_red_2_6_1  ,None,iterations=4)
    # mask_orange_2_6_1  = cv2.erode(mask_orange_2_6_1 ,None,iterations=2)
    # mask_orange_2_6_1  = cv2.dilate(mask_orange_2_6_1 ,None,iterations=4)
    green_2_6_1 = cv2.bitwise_and(kub_2_6_1 ,kub_2_6_1 ,mask=mask_green_2_6_1 )
    gray_2_6_1 = cv2.bitwise_and(kub_2_6_1 ,kub_2_6_1 ,mask=mask_gray_2_6_1 )
    orange_2_6_1  = cv2.bitwise_and(kub_2_6_1  ,kub_2_6_1 ,mask=mask_orange_2_6_1 )
    red_2_6_1  = cv2.bitwise_and(kub_2_6_1 ,kub_2_6_1 ,mask=mask_red_2_6_1 )

    hsv_2_6_2 = cv2.cvtColor(kub_2_6_2,cv2.COLOR_BGR2HSV)
    mask_green_2_6_2 = cv2.inRange(hsv_2_6_2,(greenmin),(greenmax))
    mask_gray_2_6_2 = cv2.inRange(hsv_2_6_2,(graymin),(graymax))
    mask_orange_2_6_2 = cv2.inRange(hsv_2_6_2,(orangemin),(orangemax))
    mask_red_2_6_2 = cv2.inRange(hsv_2_6_2,(redmin),(redmax))
    mask_green_2_6_2 = cv2.erode(mask_green_2_6_2,None,iterations=2)
    mask_green_2_6_2 = cv2.dilate(mask_green_2_6_2,None,iterations=4)
    mask_gray_2_6_2 = cv2.erode(mask_gray_2_6_2,None,iterations=2)
    mask_gray_2_6_2 = cv2.dilate(mask_gray_2_6_2,None,iterations=4)
    mask_red_2_6_2 = cv2.erode(mask_red_2_6_2,None,iterations=2)
    mask_red_2_6_2 = cv2.dilate(mask_red_2_6_2,None,iterations=4)
    mask_orange_2_6_2 = cv2.erode(mask_orange_2_6_2,None,iterations=2)
    mask_orange_2_6_2 = cv2.dilate(mask_orange_2_6_2,None,iterations=4)
    green_2_6_2 = cv2.bitwise_and(kub_2_6_2,kub_2_6_2,mask=mask_green_2_6_2)
    gray_2_6_2 = cv2.bitwise_and(kub_2_6_2,kub_2_6_2,mask=mask_gray_2_6_2)
    orange_2_6_2 = cv2.bitwise_and(kub_2_6_2,kub_2_6_2,mask=mask_orange_2_6_2)
    red_2_6_2 = cv2.bitwise_and(kub_2_6_2,kub_2_6_2,mask=mask_red_2_6_2)

    hsv_2_7_1 = cv2.cvtColor(kub_2_7_1,cv2.COLOR_BGR2HSV)
    mask_green_2_7_1 = cv2.inRange(hsv_2_7_1,(greenmin),(greenmax))
    mask_gray_2_7_1 = cv2.inRange(hsv_2_7_1,(graymin),(graymax))
    mask_orange_2_7_1 = cv2.inRange(hsv_2_7_1,(orangemin),(orangemax))
    mask_red_2_7_1 = cv2.inRange(hsv_2_7_1,(redmin),(redmax))
    # mask_green_2_7_1 = cv2.erode(mask_green_2_7_1,None,iterations=2)
    # mask_green_2_7_1 = cv2.dilate(mask_green_2_7_1,None,iterations=4)
    # mask_gray_2_7_1 = cv2.erode(mask_gray_2_7_1,None,iterations=2)
    # mask_gray_2_7_1 = cv2.dilate(mask_gray_2_7_1,None,iterations=4)
    # mask_red_2_7_1 = cv2.erode(mask_red_2_7_1,None,iterations=2)
    # mask_red_2_7_1 = cv2.dilate(mask_red_2_7_1,None,iterations=4)
    # mask_orange_2_7_1 = cv2.erode(mask_orange_2_7_1,None,iterations=2)
    # mask_orange_2_7_1 = cv2.dilate(mask_orange_2_7_1,None,iterations=4)
    green_2_7_1 = cv2.bitwise_and(kub_2_7_1,kub_2_7_1,mask=mask_green_2_7_1)
    gray_2_7_1 = cv2.bitwise_and(kub_2_7_1,kub_2_7_1,mask=mask_gray_2_7_1)
    orange_2_7_1 = cv2.bitwise_and(kub_2_7_1,kub_2_7_1,mask=mask_orange_2_7_1)
    red_2_7_1 = cv2.bitwise_and(kub_2_7_1,kub_2_7_1,mask=mask_red_2_7_1)

    hsv_2_7_2 = cv2.cvtColor(kub_2_7_2,cv2.COLOR_BGR2HSV)
    mask_green_2_7_2 = cv2.inRange(hsv_2_7_2,(greenmin),(greenmax))
    mask_gray_2_7_2= cv2.inRange(hsv_2_7_2,(graymin),(graymax))
    mask_orange_2_7_2 = cv2.inRange(hsv_2_7_2,(orangemin),(orangemax))
    mask_red_2_7_2 = cv2.inRange(hsv_2_7_2,(redmin),(redmax))
    # mask_green_2_7_2 = cv2.erode(mask_green_2_7_2,None,iterations=2)
    # mask_green_2_7_2= cv2.dilate(mask_green_2_7_2,None,iterations=4)
    # mask_gray_2_7_2= cv2.erode(mask_gray_2_7_2,None,iterations=2)
    # mask_gray_2_7_2 = cv2.dilate(mask_gray_2_7_2,None,iterations=4)
    # mask_red_2_7_2= cv2.erode(mask_red_2_7_2,None,iterations=2)
    # mask_red_2_7_2 = cv2.dilate(mask_red_2_7_2,None,iterations=4)
    # mask_orange_2_7_2 = cv2.erode(mask_orange_2_7_2,None,iterations=2)
    # mask_orange_2_7_2 = cv2.dilate(mask_orange_2_7_2,None,iterations=4)
    green_2_7_2 = cv2.bitwise_and(kub_2_7_2,kub_2_7_2,mask=mask_green_2_7_2)
    gray_2_7_2 = cv2.bitwise_and(kub_2_7_2,kub_2_7_2,mask=mask_gray_2_7_2)
    orange_2_7_2 = cv2.bitwise_and(kub_2_7_2,kub_2_7_2,mask=mask_orange_2_7_2)
    red_2_7_2 = cv2.bitwise_and(kub_2_7_2,kub_2_7_2,mask=mask_red_2_7_2)

    hsv_2_7_3 = cv2.cvtColor(kub_2_7_3,cv2.COLOR_BGR2HSV)
    mask_green_2_7_3 = cv2.inRange(hsv_2_7_3,(greenmin),(greenmax))
    mask_gray_2_7_3 = cv2.inRange(hsv_2_7_3,(graymin),(graymax))
    mask_orange_2_7_3 = cv2.inRange(hsv_2_7_3,(orangemin),(orangemax))
    mask_red_2_7_3 = cv2.inRange(hsv_2_7_3,(redmin),(redmax))
    mask_green_2_7_3 = cv2.erode(mask_green_2_7_3,None,iterations=2)
    mask_green_2_7_3 = cv2.dilate(mask_green_2_7_3,None,iterations=4)
    mask_gray_2_7_3 = cv2.erode(mask_gray_2_7_3,None,iterations=2)
    mask_gray_2_7_3 = cv2.dilate(mask_gray_2_7_3,None,iterations=4)
    mask_red_2_7_3 = cv2.erode(mask_red_2_7_3,None,iterations=2)
    mask_red_2_7_3 = cv2.dilate(mask_red_2_7_3,None,iterations=4)
    mask_orange_2_7_3 = cv2.erode(mask_orange_2_7_3,None,iterations=2)
    mask_orange_2_7_3 = cv2.dilate(mask_orange_2_7_3,None,iterations=4)
    green_2_7_3 = cv2.bitwise_and(kub_2_7_3,kub_2_7_3,mask=mask_green_2_7_3)
    gray_2_7_3 = cv2.bitwise_and(kub_2_7_3,kub_2_7_3,mask=mask_gray_2_7_3)
    orange_2_7_3 = cv2.bitwise_and(kub_2_7_3,kub_2_7_3,mask=mask_orange_2_7_3)
    red_2_7_3 = cv2.bitwise_and(kub_2_7_3,kub_2_7_3,mask=mask_red_2_7_3)

    hsv_2_8_1 = cv2.cvtColor(kub_2_8_1 ,cv2.COLOR_BGR2HSV)
    mask_green_2_8_1 = cv2.inRange(hsv_2_8_1 ,(greenmin),(greenmax))
    mask_gray_2_8_1  = cv2.inRange(hsv_2_8_1 ,(graymin),(graymax))
    mask_orange_2_8_1 = cv2.inRange(hsv_2_8_1 ,(orangemin),(orangemax))
    mask_red_2_8_1= cv2.inRange(hsv_2_8_1 ,(redmin),(redmax))
    # mask_green_2_8_1  = cv2.erode(mask_green_2_8_1 ,None,iterations=2)
    # mask_green_2_8_1 = cv2.dilate(mask_green_2_8_1 ,None,iterations=4)
    # mask_gray_2_8_1 = cv2.erode(mask_gray_2_8_1 ,None,iterations=2)
    # mask_gray_2_8_1  = cv2.dilate(mask_gray_2_8_1 ,None,iterations=4)
    # mask_red_2_8_1  = cv2.erode(mask_red_2_8_1 ,None,iterations=2)
    # mask_red_2_8_1  = cv2.dilate(mask_red_2_8_1 ,None,iterations=4)
    # mask_orange_2_8_1  = cv2.erode(mask_orange_2_8_1 ,None,iterations=2)
    # mask_orange_2_8_1 = cv2.dilate(mask_orange_2_8_1 ,None,iterations=4)
    green_2_8_1 = cv2.bitwise_and(kub_2_8_1,kub_2_8_1,mask=mask_green_2_8_1)
    gray_2_8_1= cv2.bitwise_and(kub_2_8_1,kub_2_8_1,mask=mask_gray_2_8_1)
    orange_2_8_1 = cv2.bitwise_and(kub_2_8_1,kub_2_8_1,mask=mask_orange_2_8_1)
    red_2_8_1 = cv2.bitwise_and(kub_2_8_1 ,kub_2_8_1 ,mask=mask_red_2_8_1)


    hsv_2_8_2 = cv2.cvtColor(kub_2_8_2 ,cv2.COLOR_BGR2HSV)
    mask_green_2_8_2  = cv2.inRange(hsv_2_8_2 ,(greenmin),(greenmax))
    mask_gray_2_8_2  = cv2.inRange(hsv_2_8_2 ,(graymin),(graymax))
    mask_orange_2_8_2  = cv2.inRange(hsv_2_8_2 ,(orangemin),(orangemax))
    mask_red_2_8_2  = cv2.inRange(hsv_2_8_2 ,(redmin),(redmax))
    mask_green_2_8_2  = cv2.erode(mask_green_2_8_2 ,None,iterations=2)
    mask_green_2_8_2  = cv2.dilate(mask_green_2_8_2 ,None,iterations=4)
    mask_gray_2_8_2  = cv2.erode(mask_gray_2_8_2 ,None,iterations=2)
    mask_gray_2_8_2  = cv2.dilate(mask_gray_2_8_2 ,None,iterations=4)
    mask_red_2_8_2  = cv2.erode(mask_red_2_8_2 ,None,iterations=2)
    mask_red_2_8_2  = cv2.dilate(mask_red_2_8_2 ,None,iterations=4)
    mask_orange_2_8_2  = cv2.erode(mask_orange_2_8_2 ,None,iterations=2)
    mask_orange_2_8_2  = cv2.dilate(mask_orange_2_8_2 ,None,iterations=4)
    green_2_8_2  = cv2.bitwise_and(kub_2_8_2,kub_2_8_2,mask=mask_green_2_8_2)
    gray_2_8_2  = cv2.bitwise_and(kub_2_8_2,kub_2_8_2,mask=mask_gray_2_8_2)
    orange_2_8_2 = cv2.bitwise_and(kub_2_8_2,kub_2_8_2,mask=mask_orange_2_8_2)
    red_2_8_2  = cv2.bitwise_and(kub_2_8_2 ,kub_2_8_2 ,mask=mask_red_2_8_2)

    hsv_2_9_1 = cv2.cvtColor(kub_2_9_1 ,cv2.COLOR_BGR2HSV)
    mask_green_2_9_1 = cv2.inRange(hsv_2_9_1 ,(greenmin),(greenmax))
    mask_gray_2_9_1= cv2.inRange(hsv_2_9_1 ,(graymin),(graymax))
    mask_orange_2_9_1 = cv2.inRange(hsv_2_9_1 ,(orangemin),(orangemax))
    mask_red_2_9_1  = cv2.inRange(hsv_2_9_1 ,(redmin),(redmax))
    # mask_green_2_9_1 = cv2.erode(mask_green_2_9_1 ,None,iterations=2)
    # mask_green_2_9_1  = cv2.dilate(mask_green_2_9_1 ,None,iterations=4)
    # mask_gray_2_9_1  = cv2.erode(mask_gray_2_9_1 ,None,iterations=2)
    # mask_gray_2_9_1 = cv2.dilate(mask_gray_2_9_1 ,None,iterations=4)
    # mask_red_2_9_1  = cv2.erode(mask_red_2_9_1,None,iterations=2)
    # mask_red_2_9_1  = cv2.dilate(mask_red_2_9_1 ,None,iterations=4)
    # mask_orange_2_9_1 = cv2.erode(mask_orange_2_9_1 ,None,iterations=2)
    # mask_orange_2_9_1  = cv2.dilate(mask_orange_2_9_1 ,None,iterations=4)
    green_2_9_1 = cv2.bitwise_and(kub_2_9_1,kub_2_9_1,mask=mask_green_2_9_1)
    gray_2_9_1  = cv2.bitwise_and(kub_2_9_1,kub_2_9_1,mask=mask_gray_2_9_1)
    orange_2_9_1 = cv2.bitwise_and(kub_2_9_1,kub_2_9_1,mask=mask_orange_2_9_1)
    red_2_9_1  = cv2.bitwise_and(kub_2_9_1 ,kub_2_9_1 ,mask=mask_red_2_9_1)

    hsv_2_9_2 = cv2.cvtColor(kub_2_9_2 ,cv2.COLOR_BGR2HSV)
    mask_green_2_9_2  = cv2.inRange(hsv_2_9_2 ,(greenmin),(greenmax))
    mask_gray_2_9_2= cv2.inRange(hsv_2_9_2 ,(graymin),(graymax))
    mask_orange_2_9_2  = cv2.inRange(hsv_2_9_2 ,(orangemin),(orangemax))
    mask_red_2_9_2= cv2.inRange(hsv_2_9_2 ,(redmin),(redmax))
    # mask_green_2_9_2 = cv2.erode(mask_green_2_9_2 ,None,iterations=2)
    # mask_green_2_9_2  = cv2.dilate(mask_green_2_9_2 ,None,iterations=4)
    # mask_gray_2_9_2  = cv2.erode(mask_gray_2_9_2 ,None,iterations=2)
    # mask_gray_2_9_2 = cv2.dilate(mask_gray_2_9_2 ,None,iterations=4)
    # mask_red_2_9_2  = cv2.erode(mask_red_2_9_2 ,None,iterations=2)
    # mask_red_2_9_2  = cv2.dilate(mask_red_2_9_2 ,None,iterations=4)
    # mask_orange_2_9_2 = cv2.erode(mask_orange_2_9_2 ,None,iterations=2)
    # mask_orange_2_9_2  = cv2.dilate(mask_orange_2_9_2 ,None,iterations=4)
    green_2_9_2 = cv2.bitwise_and(kub_2_9_2,kub_2_9_2,mask=mask_green_2_9_2)
    gray_2_9_2  = cv2.bitwise_and(kub_2_9_2,kub_2_9_2,mask=mask_gray_2_9_2)
    orange_2_9_2 = cv2.bitwise_and(kub_2_9_2,kub_2_9_2,mask=mask_orange_2_9_2 )
    red_2_9_2 = cv2.bitwise_and(kub_2_9_2 ,kub_2_9_2 ,mask=mask_red_2_9_2)


    hsv_2_9_3 = cv2.cvtColor(kub_2_9_3 ,cv2.COLOR_BGR2HSV)
    mask_green_2_9_3  = cv2.inRange(hsv_2_9_3 ,(greenmin),(greenmax))
    mask_gray_2_9_3 = cv2.inRange(hsv_2_9_3 ,(graymin),(graymax))
    mask_orange_2_9_3  = cv2.inRange(hsv_2_9_3 ,(orangemin),(orangemax))
    mask_red_2_9_3  = cv2.inRange(hsv_2_9_3 ,(redmin),(redmax))
    mask_green_2_9_3 = cv2.erode(mask_green_2_9_3 ,None,iterations=2)
    mask_green_2_9_3  = cv2.dilate(mask_green_2_9_3 ,None,iterations=4)
    mask_gray_2_9_3  = cv2.erode(mask_gray_2_9_3 ,None,iterations=2)
    mask_gray_2_9_3 = cv2.dilate(mask_gray_2_9_3 ,None,iterations=4)
    mask_red_2_9_3  = cv2.erode(mask_red_2_9_3 ,None,iterations=2)
    mask_red_2_9_3  = cv2.dilate(mask_red_2_9_3 ,None,iterations=4)
    mask_orange_2_9_3 = cv2.erode(mask_orange_2_9_3 ,None,iterations=2)
    mask_orange_2_9_3  = cv2.dilate(mask_orange_2_9_3 ,None,iterations=4)
    green_2_9_3  = cv2.bitwise_and(kub_2_9_3,kub_2_9_3,mask=mask_green_2_9_3)
    gray_2_9_3  = cv2.bitwise_and(kub_2_9_3,kub_2_9_3,mask=mask_gray_2_9_3)
    orange_2_9_3 = cv2.bitwise_and(kub_2_9_3,kub_2_9_3,mask=mask_orange_2_9_3)
    red_2_9_3  = cv2.bitwise_and(kub_2_9_3 ,kub_2_9_3 ,mask=mask_red_2_9_3)


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
        
    if ans[0,0,0] == 0:
        if numpy.sum(gray_2_1_3) > 1000000:
            ans[1,0,0] = 4
        if numpy.sum(green_2_1_3) > 1000000:
            ans[1,0,0] = 3
        if numpy.sum(red_2_1_3) > 1000000:
            ans[1,0,0] = 2
        if numpy.sum(orange_2_1_3) > 1000000:
            ans[1,0,0] = 5 

    if ans[0,0,1] == 0:
        if numpy.sum(gray_2_2_2) > 1000000:
            ans[1,0,1] = 4
        if numpy.sum(green_2_2_2) > 1000000:
            ans[1,0,1] = 3
        if numpy.sum(red_2_2_2) > 1000000:
            ans[1,0,1] = 2
        if numpy.sum(orange_2_2_2) > 1000000:
            ans[1,0,1] = 5 

    if ans[0,0,2] == 0:
        if numpy.sum(gray_2_3_3) > 1000000:
            ans[1,0,2] = 4
        if numpy.sum(green_2_3_3) > 1000000:
            ans[1,0,2] = 3
        if numpy.sum(red_2_3_3) > 1000000:
            ans[1,0,2] = 2
        if numpy.sum(orange_2_3_3) > 1000000:
            ans[1,0,2] = 5 

    if ans[0,1,0] == 0:
        if numpy.sum(gray_2_4_2) > 1000000:
            ans[1,1,0] = 4
        if numpy.sum(green_2_4_2) > 1000000:
            ans[1,1,0] = 3
        if numpy.sum(red_2_4_2) > 1000000:
            ans[1,1,0] = 2
        if numpy.sum(orange_2_4_2) > 1000000:
            ans[1,1,0] = 5 


    if ans[0,1,1] == 0:
        if numpy.sum(gray_2_5) > 1000000:
            ans[1,1,1] = 4
        if numpy.sum(green_2_5) > 1000000:
            ans[1,1,1] = 3
        if numpy.sum(red_2_5) > 1000000:
            ans[1,1,1] = 2
        if numpy.sum(orange_2_5) > 1000000:
            ans[1,1,1] = 5 

    if ans[0,1,2] == 0:
        if numpy.sum(gray_2_6_2) > 1000000:
            ans[1,1,2] = 4
        if numpy.sum(green_2_6_2) > 1000000:
            ans[1,1,2] = 3
        if numpy.sum(red_2_6_2) > 1000000:
            ans[1,1,2] = 2
        if numpy.sum(orange_2_6_2) > 1000000:
            ans[1,1,2] = 5 

    if ans[0,2,0] == 0:
        if numpy.sum(gray_2_7_3) > 1000000:
            ans[1,2,0] = 4
        if numpy.sum(green_2_7_3) > 1000000:
            ans[1,2,0] = 3
        if numpy.sum(red_2_7_3) > 1000000:
            ans[1,2,0] = 2
        if numpy.sum(orange_2_7_3) > 1000000:
            ans[1,2,0] = 5 

    if ans[0,2,1] == 0:
        if numpy.sum(gray_2_8_2) > 1000000:
            ans[1,2,1] = 4
        if numpy.sum(green_2_8_2) > 1000000:
            ans[1,2,1] = 3
        if numpy.sum(red_2_8_2) > 1000000:
            ans[1,2,1] = 2
        if numpy.sum(orange_2_8_2) > 1000000:
            ans[1,2,1] = 5   

    if ans[0,2,2] == 0:
        if numpy.sum(gray_2_9_3) > 1000000:
            ans[1,2,2] = 4
        if numpy.sum(green_2_9_3) > 1000000:
            ans[1,2,2] = 3
        if numpy.sum(red_2_9_3) > 1000000:
            ans[1,2,2] = 2
        if numpy.sum(orange_2_9_3) > 1000000:
            ans[1,2,2] = 5   

    if ans[0,0,1] == 0 and ans[1,0,1] == 0:
        if numpy.sum(gray_2_1_1) > 5000:
            ans[1,0,0] = 4
        if numpy.sum(green_2_1_1) > 5000:
            ans[1,0,0] = 3
        if numpy.sum(red_2_1_1) > 5000:
            ans[1,0,0] = 2
        if numpy.sum(orange_2_1_1) > 5000:
            ans[1,0,0] = 5

    if ans[0,1,0] == 0 and ans[1,1,0] == 0:
        if numpy.sum(gray_2_1_2) > 5000:
            ans[1,0,0] = 4
        if numpy.sum(green_2_1_2) > 5000:
            ans[1,0,0] = 3
        if numpy.sum(red_2_1_2) > 5000:
            ans[1,0,0] = 2
        if numpy.sum(orange_2_1_2) > 5000:
            ans[1,0,0] = 5

    if ans[0,1,1] == 0 and ans[1,1,1] == 0:
        if numpy.sum(gray_2_2_1) > 5000:
            ans[1,0,1] = 4
        if numpy.sum(green_2_2_1) > 5000:
            ans[1,0,1] = 3
        if numpy.sum(red_2_2_1) > 5000:
            ans[1,0,1] = 2
        if numpy.sum(orange_2_2_1) > 5000:
            ans[1,0,1] = 5

    if ans[0,0,1] == 0 and ans[1,0,1] == 0:
        if numpy.sum(gray_2_3_1) > 5000:
            ans[1,0,2] = 4
        if numpy.sum(green_2_3_1) > 5000:
            ans[1,0,2] = 3
        if numpy.sum(red_2_3_1) > 5000:
            ans[1,0,2] = 2
        if numpy.sum(orange_2_3_1) > 5000:
            ans[1,0,2] = 5

    if ans[0,1,2] == 0 and ans[1,1,2] == 0:
        if numpy.sum(gray_2_3_2) > 5000:
            ans[1,0,2] = 4
        if numpy.sum(green_2_3_2) > 5000:
            ans[1,0,2] = 3
        if numpy.sum(red_2_3_2) > 5000:
            ans[1,0,2] = 2
        if numpy.sum(orange_2_3_2) > 5000:
            ans[1,0,2] = 5

    if ans[0,1,1] == 0 and ans[1,1,1] == 0:
        if numpy.sum(gray_2_4_1) > 5000:
            ans[1,1,0] = 4
        if numpy.sum(green_2_4_1) > 5000:
            ans[1,1,0] = 3
        if numpy.sum(red_2_4_1) > 5000:
            ans[1,1,0] = 2
        if numpy.sum(orange_2_4_1) > 5000:
            ans[1,1,0] = 5

    if ans[0,1,1] == 0 and ans[1,1,1] == 0:
        if numpy.sum(gray_2_6_1) > 5000:
            ans[1,1,2] = 4
        if numpy.sum(green_2_6_1) > 5000:
            ans[1,1,2] = 3
        if numpy.sum(red_2_6_1) > 5000:
            ans[1,1,2] = 2
        if numpy.sum(orange_2_6_1) > 5000:
            ans[1,1,2] = 5

    if ans[0,1,0] == 0 and ans[1,1,0] == 0:
        if numpy.sum(gray_2_7_1) > 5000:
            ans[1,2,0] = 4
        if numpy.sum(green_2_7_1) > 5000:
            ans[1,2,0] = 3
        if numpy.sum(red_2_7_1) > 5000:
            ans[1,2,0] = 2
        if numpy.sum(orange_2_7_1) > 5000:
            ans[1,2,0] = 5

    if ans[0,2,1] == 0 and ans[1,2,1] == 0:
        if numpy.sum(gray_2_7_2) > 5000:
            ans[1,2,0] = 4
        if numpy.sum(green_2_7_2) > 5000:
            ans[1,2,0] = 3
        if numpy.sum(red_2_7_2) > 5000:
            ans[1,2,0] = 2
        if numpy.sum(orange_2_7_2) > 5000:
            ans[1,2,0] = 5

    if ans[0,1,1] == 0 and ans[1,1,1] == 0:
        if numpy.sum(gray_2_8_1) > 5000:
            ans[1,2,1] = 4
        if numpy.sum(green_2_8_1) > 5000:
            ans[1,2,1] = 3
        if numpy.sum(red_2_8_1) > 5000:
            ans[1,2,1] = 2
        if numpy.sum(orange_2_8_1) > 5000:
            ans[1,2,1] = 5

    if ans[0,1,2] == 0 and ans[1,1,2] == 0:
        if numpy.sum(gray_2_9_1) > 5000:
            ans[1,2,2] = 4
        if numpy.sum(green_2_9_1) > 5000:
            ans[1,2,2] = 3
        if numpy.sum(red_2_9_1) > 5000:
            ans[1,2,2] = 2
        if numpy.sum(orange_2_9_1) > 5000:
            ans[1,2,2] = 5

    if ans[0,2,1] == 0 and ans[1,2,1] == 0:
        if numpy.sum(gray_2_9_2) > 5000:
            ans[1,2,2] = 4
        if numpy.sum(green_2_9_2) > 5000:
            ans[1,2,2] = 3
        if numpy.sum(red_2_9_2) > 5000:
            ans[1,2,2] = 2
        if numpy.sum(orange_2_9_2) > 5000:
            ans[1,2,2] = 5

    if ans[0,0,0] != 0 and ans[0,0,1]  != 0 and ans[0,1,0] !=0:
        ans[1,0,0] = 1

    if ans[0,0,0] != 0 and ans[1,0,1]  != 0 and ans[0,1,0] !=0:
        ans[1,0,0] = 1  

    if ans[0,0,0] != 0 and ans[0,0,1]  != 0 and ans[1,1,0] !=0:
        ans[1,0,0] = 1 

    if ans[0,0,0] != 0 and ans[1,0,1]  != 0 and ans[1,1,0] !=0:
        ans[1,0,0] = 1



    if ans[0,0,1] != 0 and ans[0,1,1]  != 0 :
        ans[1,0,1] = 1 
    if ans[0,0,0] != 0 and ans[1,1,1]  != 0 :
        ans[1,0,1] = 1   



    if ans[0,0,2] != 0 and ans[0,0,1]  != 0 and ans[0,1,2] !=0:
        ans[1,0,2] = 1 
    if ans[0,0,2] != 0 and ans[1,0,1]  != 0 and ans[0,1,2] !=0:
        ans[1,0,2] = 1 
    if ans[0,0,2] != 0 and ans[0,0,1]  != 0 and ans[1,1,2] !=0:
        ans[1,0,2] = 1  
    if ans[0,0,2] != 0 and ans[1,0,1]  != 0 and ans[1,1,2] !=0:
        ans[1,0,2] = 1    



    if ans[0,1,0] != 0 and ans[0,1,1]  != 0 :
        ans[1,1,0] = 1  
    if ans[0,1,0] != 0 and ans[1,1,1]  != 0 :
        ans[1,1,0] = 1 


    if ans[0,1,1] != 0 :
        ans[1,1,1] = 1


    if ans[0,1,2] != 0 and ans[0,1,1]  != 0 :
        ans[1,1,2] = 1
    if ans[0,1,2] != 0 and ans[1,1,1]  != 0:
        ans[1,1,2] = 1    


    if ans[0,2,0] != 0 and ans[0,1,0]  != 0 and ans[0,2,1] !=0:
        ans[1,2,0] = 1
    if ans[0,2,0] != 0 and ans[1,1,0]  != 0 and ans[0,2,1] !=0:
        ans[1,2,0] = 1 
    if ans[0,2,0] != 0 and ans[0,1,0]  != 0 and ans[1,2,1] !=0:
        ans[1,2,0] = 1   
    if ans[0,2,0] != 0 and ans[1,1,0]  != 0 and ans[1,2,1] !=0:
        ans[1,2,0] = 1    



    if ans[0,2,1] != 0 and ans[0,1,1]  != 0 :
        ans[1,2,1] = 1
    if ans[0,2,1] != 0 and ans[1,1,1]  != 0:
        ans[1,2,1] = 1  

    if ans[0,2,2] != 0 and ans[0,1,2]  != 0 and ans[0,2,1] !=0:
        ans[1,2,2] = 1
    if ans[0,2,2] != 0 and ans[1,1,2]  != 0 and ans[0,2,1] !=0:
        ans[1,2,2] = 1 
    if ans[0,2,2] != 0 and ans[0,1,2]  != 0 and ans[1,2,1] !=0:
        ans[1,2,2] = 1   
    if ans[0,2,2] != 0 and ans[1,1,2]  != 0 and ans[1,2,1] !=0:
        ans[1,2,2] = 1
    result[0,0,0] = ans[1,0,0]
    result[0,0,1] = ans[1,0,1]
    result[0,0,2] = ans[1,0,2]
    result[0,1,0] = ans[1,1,0]
    result[0,1,1] = ans[1,1,1]
    result[0,1,2] = ans[1,1,2]
    result[0,2,0] = ans[1,2,0]
    result[0,2,1] = ans[1,2,1]
    result[0,2,2] = ans[1,2,2]

    result[1,0,0] = ans[0,0,0]
    result[1,0,1] = ans[0,0,1]
    result[1,0,2] = ans[0,0,2]
    result[1,1,0] = ans[0,1,0]
    result[1,1,1] = ans[0,1,1]
    result[1,1,2] = ans[0,1,2]
    result[1,2,0] = ans[0,2,0]
    result[1,2,1] = ans[0,2,1]
    result[1,2,2] = ans[0,2,2]
    cv2.imshow('ra', kub_2_9_2)
    print(result)
         
    return result

count_the_types_of_cubes('stage2/task 4/images/40074acb-cabe-49ac-9b9e-a010c189c3c9.jpg')