import cv2, sys
import numpy as np

def save_or_break(img): # Выход или сохранить
    name='Photo\\4-2.png'
    key=cv2.waitKey(0)
    if key == 121: # Нажали Y - сохранить
        cv2.imwrite(name,img) 
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
h = 3

while 1:
    img_new = cv2.morphologyEx(img_new, cv2.MORPH_OPEN, ksize, iterations=1,borderType=cv2.BORDER_CONSTANT,borderValue=(255,255,255)) # Размыкание
    img_new = cv2.medianBlur(img_new,h) # Медианный фильтр
    cv2.imshow(window, img_new)
    save_or_break(img_new)