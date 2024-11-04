import cv2, sys
import numpy as np

def save_or_break(img,number): # Сохранение
    name=['Photo\\5-1.png', 'Photo\\5-2.png', 'Photo\\5-3.png']
    key=cv2.waitKey(0)
    if key == 121: # Нажали Y - сохранить
        cv2.imwrite(name[number],img) 
    elif key==27: # Нажали ESC - выйти
        cv2.destroyAllWindows()
        sys.exit(1)

name = ['Laba_5\\5-1.jpg', 'Laba_5\\5-2.jpg', 'Laba_5\\5-3.jpg']
window = 'image'
