import cv2
import numpy as np
from pyzbar.pyzbar import decode
from pytube import YouTube
import glob
import os
from termcolor import cprint as c
for file in glob.glob("*.webm"):
    os.remove(file)
video_url=input(">")
os.system(f'yt-dlp {video_url} -o "vid.webm"')
cap=cv2.VideoCapture(glob.glob("*.webm")[0])
while True:
    image = cap.read()
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)
    for obj in barcode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
        
        #cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
        c(barcodeData,'blue')
        print("Barcode: "+barcodeData +" | Type: "+barcodeType)
        quit()
