import cv2
import numpy as np

path = 'Laba_0\\photo.jpg'
window_name = 'figure 1'
while (True):
    img = cv2.imread(path, flags=cv2.IMREAD_COLOR) # Чтение в формате BGR
    cv2.namedWindow(window_name, flags=cv2.WINDOW_AUTOSIZE) # Создание окна
    cv2.imshow(window_name,img) # Вывод изображения на экран
    if cv2.waitKey(5000)==27: # Если в течение 5с нажат ESC, то выходим и закрываем окна
        cv2.destroyAllWindows(window_name) # Удаление окна window_name
        break # Выход из цикла
    img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Из BGR в чб
    cv2.imshow(window_name,img2)
    if cv2.waitKey(7000)==27: 
        cv2.destroyAllWindows(window_name)
        break
    img3 = cv2.imread(path, flags=cv2.IMREAD_REDUCED_COLOR_2) # Чтение bgr, уменьшенное в 2 раза
    cv2.imshow(window_name,img3)
    if cv2.waitKey(9000)==27: 
        cv2.destroyAllWindows(window_name)
        break
    img4 = cv2.imread(path, flags=cv2.IMREAD_REDUCED_GRAYSCALE_4) # Чтение чб, уменьшенное в 4 раза
    cv2.imshow(window_name,img4)
    if cv2.waitKey(11000)==27: 
        cv2.destroyAllWindows(window_name)
        break
    b,g,r = cv2.split(img) # Делим на отдельные каналы
    img_n = cv2.merge([b,r,g]) # Собираем BRG 
    cv2.imshow(window_name,img_n)
    if cv2.waitKey(4000)==27: 
        cv2.destroyAllWindows(window_name)
        break
