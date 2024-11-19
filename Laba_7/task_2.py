import cv2, sys, math
import numpy as np

# НЕ ДОДЕЛАНО!!!

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

def draw_line_P(x0, y0, x1, y1, img, color=(0, 0, 255),
    thickness=1, lineType=cv2.LINE_AA):
    cv2.line(img, (x0, y0), (x1, y1),color, thickness, lineType)

window = "image"
img = cv2.imread("Laba_4\\4-1.jpg", cv2.IMREAD_COLOR)
cv2.namedWindow(window, cv2.WINDOW_GUI_EXPANDED)

img = cv2.morphologyEx(img, cv2.MORPH_OPEN, np.full((3,3),1), iterations=2) # Размыкание
img_H = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_H = cv2.Canny(img, 50,150)
lines = cv2.HoughLinesP(img_H, 1, np.pi/180, 25)
cv2.imshow(window,img_H)
cv2.waitKey(0)

for i in range(0, len(lines)):
    draw_line_P(lines[i,0,0],lines[i,0,1],lines[i,0,2],lines[i,0,3],img,thickness=3)

cv2.imshow(window,img)
save_or_break(img, 'Photo\\7-2.png')