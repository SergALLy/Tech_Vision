import cv2
import numpy as np
path = 'Desk.jpg'
window_name= 'figure 3'
hight = 400
widht = 150
img = np.full((hight,widht,3),255,dtype='uint8') # Создаём белый холст
x=0
y=0
while(y<hight):
    cv2.rectangle(img,pt1=(x,y),pt2=(x+10,y+10), color=(255,0,139),thickness=-1) # Рисуем фиолетовый прямоугольник
    x=x+20
    y=y+x//widht*10
    x=x%widht
cv2.namedWindow(window_name, flags=cv2.WINDOW_AUTOSIZE) # Создание окна
cv2.imshow(window_name,img) # Вывод изображения на экран
if cv2.waitKey(5000)==121: # Если нажата "Y", то сохраняем
    cv2.destroyWindow(window_name) # Удалить окно figure 2
    cv2.imwrite(path,img) # Сохранить изображение