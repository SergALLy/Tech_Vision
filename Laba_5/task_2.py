import cv2, sys
import numpy as np

def save_or_break(img, pyth): # Сохранение
    key=cv2.waitKey(0)
    if key == 121: # Нажали Y - сохранить
        cv2.imwrite(pyth,img) 
    elif key==27: # Нажали ESC - выйти
        cv2.destroyAllWindows()
        sys.exit(1)

name = ['Laba_5\\5-4.png', 'Laba_5\\5-5.jpg']
window = 'image'

img_1 = cv2.imread(name[0], cv2.IMREAD_GRAYSCALE)
img_2 = cv2. imread(name[1], cv2.IMREAD_GRAYSCALE)
cv2.namedWindow(window, cv2.WINDOW_GUI_EXPANDED)

img_1_filt = cv2.GaussianBlur(img_1,ksize=(21,21),sigmaX=4)
img = cv2.Canny(img_1_filt, 11, 33, 3)
cv2.imshow(window,img)
save_or_break(img, 'Photo\\5-4.png')

img_2_filt = cv2.GaussianBlur(img_2,ksize=(15,15),sigmaX=0)
img = cv2.Canny(img_2_filt, 11, 33, 7)
cv2.imshow(window,img)
save_or_break(img, 'Photo\\5-5.png')