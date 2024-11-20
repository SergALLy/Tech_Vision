import cv2, sys, math
import numpy as np

def save_or_break(img, path): # Сохранение
    key=cv2.waitKey(0)
    if key == 121: # Нажали Y - сохранить
        cv2.imwrite(path,img) 
    elif key==27: # Нажали ESC - выйти
        cv2.destroyAllWindows()
        sys.exit(1)

def draw_line(rho, theta, img, color=(0, 0, 255), 
              thickness=1, lineType=cv2.LINE_AA):
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    x0 = cos_t * rho
    y0 = sin_t * rho
    pt1 = int(x0 - 1000 * sin_t), int(y0 + 1000 * cos_t)
    pt2 = int(x0 + 1000 * sin_t), int(y0 - 1000 * cos_t)
    cv2.line(img, pt1, pt2, color, thickness, lineType)

img = cv2.imread('Laba_7\\7_1.jpg', cv2.IMREAD_COLOR)
window = 'image'
cv2.namedWindow(window,cv2.WINDOW_AUTOSIZE)

img = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT,value=(255,255,255))
img_t = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_t = cv2.Canny(img, 50, 150)
lines = cv2.HoughLines(img_t, 1,math.pi/4, 150)

for i in range(0, len(lines)):
     draw_line(lines[i,0,0],lines[i,0,1], img, thickness=7, color=(255,255,255))

cv2.imshow(window, img)
save_or_break(img, 'Photo\\7-1')