import cv2, sys
import numpy as np

def save_or_break(img, pyth): # Сохранение
    key=cv2.waitKey(0)
    if key == 121: # Нажали Y - сохранить
        cv2.imwrite(pyth,img) 
    elif key==27: # Нажали ESC - выйти
        cv2.destroyAllWindows()
        sys.exit(1)

name = ['Laba_5\\5-1.jpg', 'Laba_5\\5-2.jpg', 'Laba_5\\5-3.jpg']
window = 'image'
font = cv2.FONT_HERSHEY_COMPLEX
color=(0,255,0)

img_1 = cv2.imread(name[0], cv2.IMREAD_COLOR)
img_2 = cv2.imread(name[1], cv2.IMREAD_COLOR)
img_3 = cv2.imread(name[2], cv2.IMREAD_COLOR)
cv2.namedWindow(window, cv2.WINDOW_GUI_EXPANDED)

while 1:
    img_1_Sob = cv2.Sobel(img_1, 0, 2, 2, scale=2, ksize=5, delta=10)
    img_1_Lap = cv2.Laplacian(img_1, 0, scale=2, ksize=5, delta=10)
    cv2.putText(img_1_Sob,'Sobel',(10,100),font,fontScale=3,color=color,thickness=5)
    cv2.putText(img_1_Lap,'Laplacian',(10,100),font,fontScale=3,color=color,thickness=5)
    height= img_1_Sob.shape[0]
    line = np.full((height, 10, 3),color,dtype='uint8')
    img = np.hstack((img_1_Sob,line, img_1_Lap))
    cv2.imshow(window,img)
    save_or_break(img, 'Photo\\5-1.png')

    img_2_Sob = cv2.Sobel(img_2, 0, 2, 2, scale=2, ksize=5, delta=10)
    img_2_Lap = cv2.Laplacian(img_2, 0, scale=2, ksize=5, delta=10)
    cv2.putText(img_2_Sob,'Sobel',(10,150),font,fontScale=5,color=color,thickness=5)
    cv2.putText(img_2_Lap,'Laplacian',(10,150),font,fontScale=5,color=color,thickness=5)
    height= img_2_Sob.shape[0]
    line = np.full((height, 10, 3),color,dtype='uint8')
    img = np.hstack((img_2_Sob,line, img_2_Lap))
    cv2.imshow(window,img)
    save_or_break(img, 'Photo\\5-2.png')

    img_3_Sob = cv2.Sobel(img_3, 0, 2, 2, scale=1, ksize=5, delta=10)
    img_3_Lap = cv2.Laplacian(img_3, 0, scale=1, ksize=5, delta=10)
    cv2.putText(img_3_Sob,'Sobel',(10,30),font,fontScale=1,color=color,thickness=1)
    cv2.putText(img_3_Lap,'Laplacian',(10,30),font,fontScale=1,color=color,thickness=1)
    height= img_3_Sob.shape[0]
    line = np.full((height, 10, 3),color,dtype='uint8')
    img = np.hstack((img_3_Sob,line, img_3_Lap))
    cv2.imshow(window,img)
    save_or_break(img, 'Photo\\5-3.png')