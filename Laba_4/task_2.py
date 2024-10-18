import cv2, sys
import numpy as np

def save_or_break(img):
    name='Photo\\4-1.png'
    key=cv2.waitKey(0)
    if key == 121: # Нажали Y - сохранить
        cv2.imwrite(name,img) 
        sys.exit(1)
    elif key==27: # Нажали ESC - выйти
        cv2.destroyAllWindows()
        sys.exit(1)

name = "Laba_4\\4-2.jpg"
window = "image"

img = cv2.imread(name, cv2.IMREAD_COLOR)
cv2.namedWindow(window, cv2.WINDOW_GUI_EXPANDED)
img_new = np.copy(img)
ksize = np.array([[0.5, 0.75, 0.5],
                  [0.75, 1.0, 0.75],
                  [0.5, 0.75, 0.5]])

while 1:
    img_new = cv2.morphologyEx(img_new, cv2.MORPH_OPEN, ksize, iterations=1)
    img_new = cv2.erode(img_new, ksize,iterations=1)
    # img_new = cv2.morphologyEx(img_new, cv2.MORPH_CLOSE, ksize, iterations=1)    
    img_new = cv2.dilate(img_new, ksize,iterations=1)
    img_new = cv2.erode(img_new, ksize,iterations=1)
    img_new = cv2.morphologyEx(img_new, cv2.MORPH_CLOSE, ksize, iterations=1)
    img_new = cv2.dilate(img_new, ksize,iterations=1)
    cv2.imshow(window, img_new)
    save_or_break(img_new)