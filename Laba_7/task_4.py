import cv2, sys, math
import numpy as np

def save_or_break(img, path): # Сохранение
    key=cv2.waitKey(0)
    if key == 121: # Нажали Y - сохранить
        cv2.imwrite(path,img) 
    elif key==27: # Нажали ESC - выйти
        cv2.destroyAllWindows()
        sys.exit(1)

# img_1 = cv2.imread('Laba_7\\7_5_1.jpg')
img_2 = cv2.imread('Laba_7\\7_5_2.jpg')
# img_3 = cv2.imread('Laba_7\\7_5_3.jpg')
# img_4 = cv2.imread('Laba_7\\7_5_4.jpg')
# img_5 = cv2.imread('Laba_7\\7_5_5.jpg')
# img_6 = cv2.imread('Laba_7\\7_5_6.jpg')
window = 'image'
cv2.namedWindow(window, cv2.WINDOW_GUI_EXPANDED)

# img_1_g = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
img_2_g = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)
# img_3_g = cv2.cvtColor(img_3, cv2.COLOR_BGR2GRAY)
# img_4_g = cv2.cvtColor(img_4, cv2.COLOR_BGR2GRAY)
# img_5_g = cv2.cvtColor(img_5, cv2.COLOR_BGR2GRAY)
# img_6_g = cv2.cvtColor(img_6, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(img_2_g, method = cv2.HOUGH_GRADIENT, dp = 2, minDist = 1, param1 = 80, param2 = 50, minRadius = 0, maxRadius = 0)

for i in range (0, circles.shape[0]):
    cv2.circle(img_2, center=(int(circles[0,i,0]),int(circles[0,i,1])), radius=int(circles[0,i,2]), color=(255,0,0), thickness=3, lineType=cv2.LINE_AA)

cv2.imshow(window, img_2)
save_or_break()