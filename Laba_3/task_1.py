import cv2, sys
import numpy as np

def save_or_break(img,number):
    name=['Photo\\3-1_color.png','Photo\\3-1_grey.png',
          'Photo\\3-2_color.png','Photo\\3-2_grey.png']
    key=cv2.waitKey(0)
    if key == 121: # Нажали Y - сохранить
        cv2.imwrite(name[number-1],img) 
    elif key==27: # Нажали ESC - выйти
        cv2.destroyAllWindows()
        sys.exit(1)

def filt_img(img,d,number):
    font = cv2.FONT_HERSHEY_DUPLEX
    fontScale = 1
    thick=2
    color=(255,255,255)
    filter=(d,d) # Задание ядра фильтра

    img_new_0 = np.copy(img)
    cv2.putText(img_new_0,'origin',(0,25),font,fontScale,color,thick)

    img_new_1 = cv2.blur(img,filter)
    cv2.putText(img_new_1,'blur',(0,25),font,fontScale,color,thick)

    img_new_2 = cv2.boxFilter(img,-1,filter)
    cv2.putText(img_new_2,'boxFilter',(0,25),font,fontScale,color,thick)

    img_new_3 = cv2.medianBlur(img,d)
    cv2.putText(img_new_3,'medianBlur',(0,25),font,fontScale,color,thick)

    img_new_4 = cv2.GaussianBlur(img,filter,0)
    cv2.putText(img_new_4,'GaussianBlur',(0,25),font,fontScale,color,thick)

    img_new_5 = cv2.bilateralFilter(img,d,0,0)
    cv2.putText(img_new_5,'bilateralFilter',(0,25),font,fontScale,color,thick)

    img_new = np.vstack((np.hstack((img_new_0,img_new_1,img_new_2)),np.hstack((img_new_3,img_new_4,img_new_5))))
    cv2.imshow(window,img_new)
    save_or_break(img_new,number)

path = ['Laba_3\\3-1.PNG','Laba_3\\3-2.PNG']
window = 'figure 1'
# Открытие изображений в разном формате
img_1c = cv2.imread(path[0],cv2.IMREAD_REDUCED_COLOR_2)
img_1g = cv2.imread(path[0],cv2.IMREAD_REDUCED_GRAYSCALE_2)
img_2c = cv2.imread(path[1],cv2.IMREAD_REDUCED_COLOR_2)
img_2g = cv2.imread(path[1],cv2.IMREAD_REDUCED_GRAYSCALE_2)
# Создание окна
cv2.namedWindow(window,cv2.WINDOW_GUI_EXPANDED)
while(1):
    filt_img(img_1c,15,1)
    filt_img(img_1g,15,2)
    filt_img(img_2c,13,3)
    filt_img(img_2g,13,4)   