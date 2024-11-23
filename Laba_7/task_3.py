import cv2, sys, math
import numpy as np

cap = cv2.VideoCapture('Laba_5\\video_1.mp4')

while 1:
    _, frame = cap.read()
    frame_filt= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    _, frame_filt= cv2.threshold(frame_filt, 30, 255, type = cv2.THRESH_BINARY_INV)
    lines = cv2.HoughLinesP(frame_filt, rho = 1, theta = math.pi/180, threshold = 200, maxLineGap = 5, minLineLength = 50)
    
    if not(lines is None):
        for i in range(0,len(lines)): 
            cv2.line(frame, (lines[i,0,0], lines[i,0,1]), (lines[i,0,2], lines[i,0,3]),(0,0,255), thickness=5, lineType=cv2.LINE_AA)
    cv2.imshow('video', frame) 
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()