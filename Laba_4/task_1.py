import cv2, sys
import numpy as np

def my_morph_open(img,filter,n=1): # Размыкание
    img_new = cv2.erode(img, filter,iterations=n) # Эрозия
    img_new = cv2.dilate(img_new, filter, iterations=n) # Наращивание
    return img_new

def my_morph_close(img,filter,n): # Замыкание
    img_new = cv2.dilate(img, filter, iterations=n) # Наращивание
    img_new = cv2.erode(img_new, filter,iterations=n) # Эрозия
    return img_new

def save_or_break(img,number): # Сохранение
    name=['Photo\\4-1_1.png', 'Photo\\4-1_2.png' ]
    key=cv2.waitKey(0)
    if key == 121: # Нажали Y - сохранить
        cv2.imwrite(name[number],img) 
    elif key==27: # Нажали ESC - выйти
        cv2.destroyAllWindows()
        sys.exit(1)

name = "Laba_4\\4-1.jpg"
window = "image"
img = cv2.imread(name, cv2.IMREAD_COLOR)
cv2.namedWindow(window, cv2.WINDOW_GUI_EXPANDED)
height= img.shape[0]

font = cv2.FONT_HERSHEY_COMPLEX_SMALL
fontScale = 1
thick=1
color=(0,0,255)

ksize = np.array([[0.5, 0.75, 0.5],
                  [0.75, 1.0, 0.75],
                  [0.5, 0.75, 0.5]])

while 1:
    img_new_1 = cv2.morphologyEx(img, cv2.MORPH_OPEN, ksize, iterations=2) # Размыкание

    img_new_2 = my_morph_open(img, ksize, 2) # Моё размыкание

    print(np.array_equal(img_new_1, img_new_2)) # Сравниваем изображения

    cv2.putText(img_new_1,'origin_function',(20,40),font,fontScale,color,thick)
    cv2.putText(img_new_2,'my_function',(20,40),font,fontScale,color,thick)
    img_2 = np.full((height, 10, 3),(0,0,255),dtype='uint8')

    img_2 = np.hstack((img_new_1, img_2, img_new_2)) # Объединение по горизонтали
    cv2.imshow(window,img_2)
    save_or_break(img_2,0)

    img_new_1 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, ksize, iterations=2) # Замыкание

    img_new_2 = my_morph_close(img, ksize, 2) # Моё замыкание

    print(np.array_equal(img_new_1, img_new_2))

    cv2.putText(img_new_1,'origin_function',(20,40),font,fontScale,color,thick)
    cv2.putText(img_new_2,'my_function',(20,40),font,fontScale,color,thick)
    img_2 = np.full((height, 10, 3),(0,0,255),dtype='uint8')

    img_2 = np.hstack((img_new_1, img_2, img_new_2))
    cv2.imshow(window,img_2)
    save_or_break(img_2,1)