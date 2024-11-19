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

def draw_line_P(x0, y0, x1, y1, img, color=(0, 0, 255),
    thickness=1, lineType=cv2.LINE_AA):
    cv2.line(img, (x0, y0), (x1, y1),color, thickness, lineType)

img_1 = cv2.imread('Laba_7\\7_5_1.jpg')
img_2 = cv2.imread('Laba_7\\7_5_2.jpg')
img_3 = cv2.imread('Laba_7\\7_5_3.jpg')
img_4 = cv2.imread('Laba_7\\7_5_4.jpg')
img_5 = cv2.imread('Laba_7\\7_5_5.jpg')
img_6 = cv2.imread('Laba_7\\7_5_6.jpg')
window = 'image'
cv2.namedWindow(window, cv2.WINDOW_GUI_EXPANDED)

img_1_g = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
img_2_g = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)
img_3_g = cv2.cvtColor(img_3, cv2.COLOR_BGR2GRAY)
img_4_g = cv2.cvtColor(img_4, cv2.COLOR_BGR2GRAY)
img_5_g = cv2.cvtColor(img_5, cv2.COLOR_BGR2GRAY)
img_6_g = cv2.cvtColor(img_6, cv2.COLOR_BGR2GRAY)

