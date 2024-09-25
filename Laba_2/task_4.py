import cv2

cap = cv2.VideoCapture(0) # Cоздание экземпляра класса для захвата видео с камеры 0
while(True):
    _, frame = cap.read() # Чтение одного кадра
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # Перевод кадра в чб
    # Адаптивное изображение
    frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,21,8)
    cv2.imshow('frame', frame)  # Отображение кадра
    # Ожидание нажатия на клавиши в течение 1 мс
    key=cv2.waitKey(1)
    # Нажали Y - сохранить кадр
    if key == 113:
        cv2.imwrite('task_4.jpg',frame)
    # Нажали ESC - выйти
    elif key==27:
        cv2.destroyAllWindows()
        break