import cv2, sys, math
import numpy as np

def save_or_break(img, path): # Сохранение
    key=cv2.waitKey(0)
    if key == 121: # Нажали Y - сохранить
        cv2.imwrite(path,img) 
    elif key==27: # Нажали ESC - выйти
        cv2.destroyAllWindows()
        sys.exit(1)

window = "image"
img = cv2.imread("Laba_4\\4-1.jpg", cv2.IMREAD_COLOR)
cv2.namedWindow(window, cv2.WINDOW_AUTOSIZE)

img = cv2.morphologyEx(img, cv2.MORPH_OPEN, np.full((3,3),0.1), iterations=2) # Размыкание
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_,img_b = cv2.threshold(img_g, 75, 255, cv2.THRESH_BINARY_INV)

lines = cv2.HoughLinesP(img_b, rho = 4, theta = math.pi/180, threshold = 800, minLineLength = 100,maxLineGap= 5)
circles = cv2.HoughCircles(img_g, method=cv2.HOUGH_GRADIENT, dp=2, minDist=10, param1=100,param2=50, minRadius=20, maxRadius=60)

max_len = 0
max_lines = [0,0,0,0]
for i in range(0, len(lines)):
    len = ((lines[i,0,0] - lines[i,0,2])**2 + (lines[i,0,1] - lines[i,0,3])**2)**(1/2)
    if len >max_len:
        max_len = len
        max_line = lines[i,0,:]

max_r = 0
max_circle = [0,0,0]
for i in range(0, circles.shape[1]):
    if circles[0,i,2]>max_r:
        max_r=circles[0,i,2]
        max_circle = circles[0,i,:]
cv2.circle(img, center=(int(max_circle[0]),int(max_circle[1])), radius=int(max_circle[2]), color=(0,0,255), thickness=3, lineType=cv2.LINE_AA)
cv2.line(img, (max_line[0], max_line[1]), (max_line[2], max_line[3]),(255,0,0), thickness=3, lineType=cv2.LINE_AA)

cv2.imshow(window,img)
save_or_break(img, 'Photo\\7-2.png')