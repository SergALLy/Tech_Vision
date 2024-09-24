# Bмпорт библиотеки
import cv2

cap = cv2.VideoCapture(0) # Cоздание экземпляра класса для захвата видео с камеры 0
while(True):
    # date=date.strftime("%Y-%m-%d %H:%M:%S") # Дата в формате YYYY-MM-DD HH:MM:SS
    ret, frame = cap.read() # Чтение одного кадра
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # Перевод кадра в чб
    # frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,21,13)
    frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,21,8)
    cv2.imshow('frame', frame)  # Отображение кадра
    # Ожидание нажатия на q в течение 1 мс
    if cv2.waitKey(1) == 113:
        break