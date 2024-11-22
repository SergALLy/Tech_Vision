import cv2, sys, math
import numpy as np

def draw_line(rho, theta, img, color=(0, 0, 255), 
              thickness=1, lineType=cv2.LINE_AA):
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    x0 = cos_t * rho
    y0 = sin_t * rho
    pt1 = int(x0 - 1000 * sin_t), int(y0 + 1000 * cos_t)
    pt2 = int(x0 + 1000 * sin_t), int(y0 - 1000 * cos_t)
    cv2.line(img, pt1, pt2, color, thickness, lineType)

cap = cv2.VideoCapture('Laba_5\\stop_line_1.mp4')
while 1:
    ret, frame = cap.read()
    frame_filt= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_filt = cv2.GaussianBlur(frame,ksize=(15,15),sigmaX=0)
    frame_filt = cv2.Canny(frame_filt, 35, 75, 7)
    lines = cv2.HoughLinesP(frame_filt, rho = 5, theta = math.pi/180, threshold = 500,maxLineGap=0, minLineLength= 0)
    if not(lines is None):
        for i in range(0,len(lines)): 
            draw_line(lines[i,0,0],lines[i,0,1], frame, thickness=3, color=(0,0,255))
    cv2.imshow('video', frame) 
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()