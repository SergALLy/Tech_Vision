import cv2
import numpy as np

path = 'Laba_2\\2-1.jpg'
window_name = 'figure_1'
window_name_2 = 'figure_2'
img=cv2.imread(path,flags=cv2.IMREAD_REDUCED_GRAYSCALE_2) # Прочитать фото в ЧБ 1:2
# Ручной поиск: Обнуление яркости части пикселей изображения
_,img_n = cv2.threshold(img,80,255,cv2.THRESH_TOZERO)
cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE) # Создать окно window_name
cv2.namedWindow(window_name_2,cv2.WINDOW_AUTOSIZE)
# Показать изображения
cv2.imshow(window_name,img)
cv2.imshow(window_name_2,img_n )
# При нажатии на Y сохранить img_n
if cv2.waitKey(0)==121:
    cv2.imwrite('Photo\\task_2.jpg',img_n)
cv2.destroyAllWindows() # Удалить все окна