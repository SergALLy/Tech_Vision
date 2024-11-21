import cv2, sys, math
import numpy as np

def save_or_break(img, path): # Сохранение
    key=cv2.waitKey(0)
    if key == 121: # Нажали Y - сохранить
        cv2.imwrite(path,img) 
    elif key==27: # Нажали ESC - выйти
        cv2.destroyAllWindows()
        sys.exit(1)

def road_sign(img, dp, minDist, param1, param2,metod = cv2.HOUGH_GRADIENT, minRadius = 0, maxRadius = 0):
    flag = 0
    circles = cv2.HoughCircles(image=img, method = metod, dp = dp, minDist = minDist, param1 = param1, param2 = param2, minRadius = minRadius, maxRadius = maxRadius)
    print(circles)
    if circles is None: 
        flag = 1
        print('Circles not found')
    return (circles, flag)

img_1 = cv2.imread('Laba_7\\7_5_1.jpg', cv2.IMREAD_REDUCED_COLOR_4)
img_2 = cv2.imread('Laba_7\\7_5_2.jpg', cv2.IMREAD_REDUCED_COLOR_4)
img_3 = cv2.imread('Laba_7\\7_5_3.jpg', cv2.IMREAD_REDUCED_COLOR_4)
# img_4 = cv2.imread('Laba_7\\7_5_4.jpg', cv2.IMREAD_REDUCED_COLOR_4)
# img_5 = cv2.imread('Laba_7\\7_5_5.jpg', cv2.IMREAD_REDUCED_COLOR_4)
# img_6 = cv2.imread('Laba_7\\7_5_6.jpg', cv2.IMREAD_REDUCED_COLOR_4)

# print(img_4.shape)
# print(img_5.shape)
# print(img_6.shape)

window = 'image'
cv2.namedWindow(window, cv2.WINDOW_GUI_NORMAL)

img_1_g = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
img_2_g = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)
img_3_g = cv2.cvtColor(img_3, cv2.COLOR_BGR2GRAY)
# img_4_g = cv2.cvtColor(img_4, cv2.COLOR_BGR2GRAY)
# img_5_g = cv2.cvtColor(img_5, cv2.COLOR_BGR2GRAY)
# img_6_g = cv2.cvtColor(img_6, cv2.COLOR_BGR2GRAY)

# image 1
circles, flag = road_sign(img_1_g, dp=1, minDist=10, param1=100,param2=200, minRadius=50, maxRadius=200)
if flag != 1:
    for i in range (0, circles.shape[1]):
        cv2.circle(img_1, center=(int(circles[0,i,0]),int(circles[0,i,1])), radius=int(circles[0,i,2]), color=(255,0,0), thickness=10, lineType=cv2.LINE_AA)
cv2.imshow(window, img_1)
save_or_break(img_1, 'Photo\\7-5-1.png')

# image 2
circles, flag = road_sign(img_2_g, dp=1, minDist=5, param1=100,param2=150, minRadius=200, maxRadius=260)
if flag != 1:
    for i in range (0, circles.shape[1]):
        cv2.circle(img_2, center=(int(circles[0,i,0]),int(circles[0,i,1])), radius=int(circles[0,i,2]), color=(255,0,0), thickness=15, lineType=cv2.LINE_AA)
cv2.imshow(window, img_2)
save_or_break(img_2, 'Photo\\7-5-2.png')

# image 3
circles, flag = road_sign(img_3_g, dp=1, minDist=15, param1=100,param2=80, minRadius=200, maxRadius=250)
if flag != 1:
    for i in range (0, circles.shape[1]):
        cv2.circle(img_3, center=(int(circles[0,i,0]),int(circles[0,i,1])), radius=int(circles[0,i,2]), color=(255,0,0), thickness=15, lineType=cv2.LINE_AA)
cv2.imshow(window, img_3)
save_or_break(img_3, 'Photo\\7-5-3.png')

# image 4
# circles, flag = road_sign(img_4_g, dp=1, minDist=1, param1=100, param2=40 , minRadius=70, maxRadius=100)
# if flag != 1:
#     for i in range (0, circles.shape[1]):
#         cv2.circle(img_4, center=(int(circles[0,i,0]),int(circles[0,i,1])), radius=int(circles[0,i,2]), color=(255,0,0), thickness=3, lineType=cv2.LINE_AA)
# cv2.imshow(window, img_4)
# save_or_break(img_2, 'Photo\\7-5-3.png')