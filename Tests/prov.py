"""ЧТОБЫ НИЧЕГО НЕ МЕНЯТЬ МОЖНО ЗАКИНУТЬ ЭТОТ ФАЙЛ В ОДНУ ДИРЕКТОРИЮ С ПАПКОЙ ФОТОГРАФИЙ"""
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
    
    #дальше обычная прога
    frame = cv2.imread(frame_input)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray,100,200)
    thresh = 92
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

    
    true_ans = list(enumerate(data.itertuples()))[pos][1][2] # берем правильный ответ из таблицы
    print(f"{img[7:]}, conturs={num_shapes}, {true_ans=}")
        
    #print("Типы фигур: ", shapes) 

    # # min_dist =1000
    # # k=0
    # # for cnt_1 in contours[6]:
    # #         x1, y1 = cnt_1[0]
    # #         for cnt_2 in contours[3]:
    # #             x2,y2 = cnt_2[0]
    # #             dist = np.sqrt((x1-x2)**2+(y1-y2)**2)
    # #             if dist < min_dist:
    # #                 min_dist = dist
    # #                 min_dist = float(min_dist) 
    # # if min_dist < 10:
    # #     	k+=1
    # # print('kol',k)
    # # print(min_dist)    
    # for hi in hierarchy:
    #     print(hi)                       
    
    cv2.drawContours(frame, contours, -1, (0,255,0), 1)
    # cv2.imshow('frame', frame)
    
    while True:
        cv2.imshow('frame', frame)
        cv2.imshow('canny', canny)

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

    