import cv2
import numpy as np

path = 'Laba_2\\2-0.jpg'
window_name = 'figure_1'
window_name_2 = 'figure_2'
img=cv2.imread(path,flags=cv2.IMREAD_REDUCED_GRAYSCALE_4) # Прочитать в ЧБ 1:4
# Адаптивное пороговое преобразование
img_n = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,47,55) 
cv2.namedWindow(window_name,cv2.WINDOW_GUI_EXPANDED) # Создать окно масштабируемое
cv2.namedWindow(window_name_2,cv2.WINDOW_GUI_EXPANDED)
cv2.imshow(window_name,img) # Показать изображение в окне wimdow_name
cv2.imshow(window_name_2,img_n )
if cv2.waitKey(0)==121: # При нажатии на Y сохранить img_n
    cv2.imwrite('task_1.jpg',img_n)
cv2.destroyAllWindows() # Удвлить все окна