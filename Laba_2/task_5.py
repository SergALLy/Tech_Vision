import cv2
import numpy as np

path = 'Laba_2\\2-2.jpg'
window_name = 'figure_1'
window_name_2 = 'figure_2'
img=cv2.imread(path,flags=cv2.IMREAD_REDUCED_GRAYSCALE_4) #Прочесть фото в ЧБ 1:4
# Адаптивное преобразование
img_n = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,35)
# Создание окон
cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(window_name_2,cv2.WINDOW_AUTOSIZE)
# Показать изображения
cv2.imshow(window_name,img)
cv2.imshow(window_name_2,img_n )
# Нажата Y - сохранить img_n
if cv2.waitKey(0)==121:
    cv2.imwrite('Photo\\task_5.jpg',img_n)
cv2.destroyAllWindows()
