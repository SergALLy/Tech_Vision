import cv2, numpy, sys

def save_or_break(img):
    name='Photo\\3-3.png'
    key=cv2.waitKey(0)
    if key == 121: # Нажали Y - сохранить кадр
        cv2.imwrite(name,img) 
    elif key==27: # Нажали ESC - выйти
        cv2.destroyAllWindows()
        sys.exit(1)

path = 'Laba_3\\3-3.jpg'
window = 'image'
img = cv2.imread(path, cv2.IMREAD_COLOR)
cv2.namedWindow(window,cv2.WINDOW_GUI_EXPANDED)

img = cv2.medianBlur(img,15)
# img = cv2.blur(img,(3,3))
# img = cv2.bilateralFilter(img,7,1,1)
# img = cv2.GaussianBlur(img,(7,7),0)


cv2.imshow(window, img)
save_or_break(img)