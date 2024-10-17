import cv2, sys
import numpy as np

def save_or_break(img):
    name='Photo\\3-4.jpg'
    key=cv2.waitKey(0)
    if key == 121: # Нажали Y - сохранить кадр
        cv2.imwrite(name,img) 
        sys.exit(1)
    elif key==27: # Нажали ESC - выйти
        cv2.destroyAllWindows()
        sys.exit(1)

path = "Laba_3\\3-4.jpg"
window = 'image'
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
fontScale = 1.5
h=100
thick=2
color=(0,0,0)
img=cv2.imread(path,cv2.IMREAD_REDUCED_COLOR_8)
cv2.namedWindow(window,cv2.WINDOW_GUI_EXPANDED)
height, weight= img.shape[0:2]
img_1=cv2.resize(img, (height//2+200,weight//2+200))
img =cv2.resize(img, (height//2,weight//2)) 
while True:
    img_new_0=np.copy(img_1)
    cv2.putText(img_new_0,'ORIGIN',(100,200),font,fontScale,color,thick)

    img_new_1=cv2.copyMakeBorder(img,h,h,h,h,cv2.BORDER_DEFAULT)
    cv2.putText(img_new_1,'BORDER_DEFAULT',(100,200),font,fontScale,color,thick)

    img_new_2=cv2.copyMakeBorder(img,h,h,h,h,cv2.BORDER_CONSTANT,value=(0,0,255))
    cv2.putText(img_new_2,'BORDER_CONSTANT',(100,200),font,fontScale,color,thick)

    img_new_3=cv2.copyMakeBorder(img,h,h,h,h,cv2.BORDER_REFLECT)
    cv2.putText(img_new_3,'BORDER_REFLECT',(100,200),font,fontScale,color,thick)

    img_new_4=cv2.copyMakeBorder(img,h,h,h,h,cv2.BORDER_REFLECT101)
    cv2.putText(img_new_4,'BORDER_REFLECT101',(100,200),font,fontScale,color,thick)

    img_new_5=cv2.copyMakeBorder(img,h,h,h,h,cv2.BORDER_REFLECT_101)
    cv2.putText(img_new_5,'BORDER_REFLECT_101',(100,200),font,fontScale,color,thick)

    img_new_6=cv2.copyMakeBorder(img,h,h,h,h,cv2.BORDER_REPLICATE)
    cv2.putText(img_new_6,'BORDER_REPLICATE',(100,200),font,fontScale,color,thick)

    img_new_7=cv2.copyMakeBorder(img,h,h,h,h,cv2.BORDER_WRAP)
    cv2.putText(img_new_7,'BORDER_WRAP',(100,200),font,fontScale,color,thick)
    
    img_new = np.vstack((np.hstack((img_new_0,img_new_1,img_new_2,img_new_3)),np.hstack((img_new_4,img_new_5,img_new_6,img_new_7))))
    cv2.imshow(window,img_new)
    save_or_break(img_new)