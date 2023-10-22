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
    contours =[]

    img = list(enumerate(data.itertuples()))[pos][1][1] #из таблицы берем название файла
    frame_input = os.path.join(dir_images, img[7:] )#соединяем путь до папки с фотографиями с названием фотографии
    frame = cv2.imread(frame_input) 
    canny = cv2.Canny(frame,100,100)
    cnt, h = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in cnt:
        rect = cv2.minAreaRect(c)   
        area = int(rect[1][0]*rect[1][1])
        if len(c)>31 and area>4500:    
            contours.append(c)
    cv2.waitKey()
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