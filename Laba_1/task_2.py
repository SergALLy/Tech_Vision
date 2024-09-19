import cv2
import numpy as np

path = 'Paint.jpg'
window_name = 'figure 2'
font = cv2.FONT_HERSHEY_COMPLEX
fontScale = 0.8
img = np.full((500,500,3),255,dtype='uint8') # Создаём белый холст
cv2.line(img,pt1=(500,0),pt2=(0,500),color=(255,191,0), thickness=3) # Рисуем голубую линию
cv2.putText(img,'Line',(50,380),font,fontScale,color=(0,0,0))
cv2.rectangle(img,pt1=(100,100),pt2=(200,150), color=(255,0,139),thickness=3) # Рисуем фиолетовый прямоугольник
cv2.putText(img,'Restangle',(90,90),font,fontScale,color=(0,0,0))
cv2.circle(img,center=(350,400),radius=50,color=(0,0,255),thickness=3) # Рисуем красный круг
cv2.putText(img,'Circle',(310,340),font,fontScale,color=(0,0,0))
cv2.namedWindow(window_name, flags=cv2.WINDOW_AUTOSIZE) # Создание окна
cv2.imshow(window_name,img) # Вывод изображения на экран
if cv2.waitKey(0)==121: # Если нажата "Y", то сохраняем
    cv2.destroyWindow(window_name) # Удалить окно
    res=cv2.imwrite(path,img) # Сохранить изображение