import cv2, sys
import numpy as np

def save_or_break(img, path): # Сохранение
    key=cv2.waitKey(0)
    if key == 121: # Нажали Y - сохранить
        cv2.imwrite(path,img) 
    elif key==27: # Нажали ESC - выйти
        cv2.destroyAllWindows()
        sys.exit(1)

img = cv2.imread('Laba_6\\6-1.png',cv2.IMREAD_GRAYSCALE)
window = 'image'
cv2.namedWindow(window, cv2.WINDOW_GUI_EXPANDED)

_, img2 = cv2.threshold(img, 75, 255, cv2.THRESH_BINARY)
img2 = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, np.full((2,2),1), iterations=1) # Замыкание

contours, hierarchy = cv2.findContours(img2, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)

img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
for i in range (0, len(contours)-1):
    _,_,w,h=cv2.boundingRect(contours[i])
    _, r = cv2.minEnclosingCircle(contours[i])
    
    if (w*h*0.95 <= cv2.contourArea(contours[i]) <= w*h*1.05) and (2*(w+h)*0.95 <= cv2.arcLength(contours[i], True) <= 2*(w+h)*1.05):
        cv2.drawContours(img, contours,contourIdx=i, color=(0,0,255), thickness=3)
    elif (2*3.14*(r**2)*0.4875 <= cv2.contourArea(contours[i]) <= 3.14*(r**2)*1.5125)  and  (2*3.14*r*0.9 <= cv2.arcLength(contours[i], True) <= 2*3.14*r*1.1):
        cv2.drawContours(img, contours,contourIdx=i, color=(255,0,0), thickness=3)
    else:
        cv2.drawContours(img, contours,contourIdx=i, color=(255,0,139), thickness=3)
        
cv2.imshow(window, img)
save_or_break(img, 'Photo\\6-1.png')