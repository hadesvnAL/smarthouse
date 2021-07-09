import cv2
import sys
import numpy as np # truy suat nhanh hon, toi uu hoa
#khai bao thu vien khuon mat

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascades_frontalface_default.xml")

#truy cap webcame
vid = cv2.VideoCapture(0)
#hien thi lien tuc va tat
while(True):
    #lay du lieu tu webcame, ret tra va true neu thanh cong, frame data du lieu
    ret, frame = vid.read()
    #lay dl chuyen ve anh xam, frame dl tu webcame, cv2. chuyen tu BGR sang GRAY
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #lay thu vien khuon mat
    faces = face_cascade.detectMultiScale(gray)
    #ve hinh vuong, x , y toa do diem
    for (x, y, w, h) in faces:
        #ve hinh vuong, frame dl lay webcame, x,y toa do diem dau tien, tinh tien trong khong gian; w wight vs high; 0, 0 , 225 mau rgb; 2 do day hinh vuong 
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,225), 2)
    #show hinh vuong len man hinh 2 ham imshow va imread
    cv2.imshow('DETECTING FACE', gray)   
    #ket thuc chuong trinh,waitKEY muon cho hien ko tat luon, con ord là tat chuong trình
    if cv2.waitKEY(1) & 0xFF == ord('q'):
        break
#giai phong bo nho   
vid.release()
#huy chuong trinh
cv2.destroyAllWindows()

