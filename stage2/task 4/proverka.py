import cv2
import numpy as np
import math
import os
import pandas as pd
pos = 0 
breaking_bad = False

images = "images"

main_dir = os.path.dirname(__file__) #полный путь до файла
dir_images = os.path.join(main_dir, images) #путь до папки с фотографиями

csv = "annotations.csv"
csv_file = os.path.join(main_dir, csv)  #полный путь до таблицы ексель
data = pd.read_csv(csv_file, sep=',')
data = data.sample(frac=1) #парсинг данных таблицы
number_of_files = len(data) #количество фотографий


while True:

    if breaking_bad:
        break
    img = list(enumerate(data.itertuples()))[pos][1][1] #из таблицы берем название файла
    frame_input = os.path.join(dir_images, img[7:] )#соединяем путь до папки с фотографиями с названием фотографии
    frame = cv2.imread(frame_input) 
    canny = cv2.Canny(frame,100,100)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.line(frame, (75,75),(525,75),(0,255,0),3)
    cv2.line(frame, (75,75),(75,525),(0,255,0),3)
    cv2.line(frame, (525,525),(525,75),(0,255,0),3)
    cv2.line(frame, (75,525),(525,525),(0,255,0),3)

    cv2.line(frame, (75,225),(525,225),(0,255,0),3)
    cv2.line(frame, (75,375),(525,375),(0,255,0),3)

    cv2.line(frame, (225,75),(225,525),(0,255,0),3)
    cv2.line(frame, (375,75),(375,525),(0,255,0),3)
    kub_1_1 = frame[75:225, 75:225]
    kub_1_2 = frame[75:225, 225:375]
    kub_1_3 = frame[75:225, 375:525]
    kub_1_4 = frame[225:375, 75:225]
    kub_1_5 = frame[225:375, 225:375]
    kub_1_6 = frame[225:375, 375:525]
    kub_1_7 = frame[375:525, 75:225]
    kub_1_8 = frame[375:525, 225:375]
    kub_1_9 = frame[375:525, 375:525]
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask_green = cv2.inRange(hsv,(50,83,26),(95,255,110))
    mask_gray = cv2.inRange(hsv,(0,0,17),(179,26,71))
    mask_orange = cv2.inRange(hsv,(0,120,150),(164,230,255))
    mask_red = cv2.inRange(hsv,(156,203,113),(255,255,255))
    green = cv2.bitwise_and(frame,frame,mask=mask_green)
    gray = cv2.bitwise_and(frame,frame,mask=mask_gray)
    orange = cv2.bitwise_and(frame,frame,mask=mask_orange)
    red = cv2.bitwise_and(frame,frame,mask=mask_red)
   
    cv2.waitKey()
    while True:
        cv2.imshow("kub1", kub_1_1)
        cv2.imshow("kub2", kub_1_2)
        cv2.imshow("kub3", kub_1_3)
        cv2.imshow("kub4", kub_1_4)
        cv2.imshow("kub5", kub_1_5)
        cv2.imshow("kub6", kub_1_6)
        cv2.imshow("kub7", kub_1_7)
        cv2.imshow("kub8", kub_1_8)
        cv2.imshow("kub9", kub_1_9)
        cv2.imshow('frame',frame)

        k = cv2.waitKey(1)

        if k == ord('a'):
            pos=pos-1

            if pos < 0:
                pos = 0
                print("the first file is open")
            else: cv2.destroyAllWindows()
            break
        
        
        elif k == ord('d'):
            pos=pos+1
            print(pos)

            if pos == number_of_files:
                pos = number_of_files - 1
                print("files are over")
            else: cv2.destroyAllWindows()
            break

        elif k == ord('q'):
            cv2.destroyAllWindows()
            breaking_bad = True
            break