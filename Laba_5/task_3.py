import cv2, sys
import numpy as np

cap = cv2.VideoCapture('Laba_5\\stop_line_1.mp4')
while 1:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_filt = cv2.GaussianBlur(frame,ksize=(15,15),sigmaX=0)
    frame_filt = cv2.Canny(frame_filt, 7, 21, 7)
    cv2.imshow('video', frame_filt) 
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()