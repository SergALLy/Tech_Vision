import cv2
import numpy as np

path = 'Laba_2\\2-3.png'
path_1 = 'Laba_2\\2-4.png'
window_name = 'figure_1'
window_name_2 = 'figure_2'
window_name_3 = 'figure_3'
window_name_4 = 'figure_4'
img=cv2.imread(path,flags=cv2.IMREAD_REDUCED_GRAYSCALE_2) # Считать фото в ЧБ 1:2
img1=cv2.imread(path_1,cv2.IMREAD_REDUCED_GRAYSCALE_2)
# Адаптивное преобразования
img_n = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,13)
img_n1 = cv2.adaptiveThreshold(img1,255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,28)
# _,img_n1 = cv2.threshold(img1,100,255,cv2.THRESH_BINARY) 
# Создание окон 
cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(window_name_2,cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(window_name_3,cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(window_name_4,cv2.WINDOW_AUTOSIZE)
# Показать изображения
cv2.imshow(window_name,img)
cv2.imshow(window_name_2,img_n )
cv2.imshow(window_name_3,img1 )
cv2.imshow(window_name_4,img_n1 )
# Нажали Y - сохранить img_n и img_n1
if cv2.waitKey(0)==121:
    cv2.imwrite('Photo\\task_3_1.jpg',img_n)
    cv2.imwrite('Photo\\task_3_2.jpg',img_n1)
cv2.destroyAllWindows() # Удалить окна