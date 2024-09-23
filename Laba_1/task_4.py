# Bмпорт библиотеки
import cv2, datetime

cap = cv2.VideoCapture(0) # Cоздание экземпляра класса для захвата видео с камеры 0
font = cv2.FONT_HERSHEY_COMPLEX
fontScale = 0.8
while(True):
    date=datetime.datetime.today() # Определение даты и времени
    date=str(date)
    # date=date.strftime("%Y-%m-%d %H:%M:%S") # Дата в формате YYYY-MM-DD HH:MM:SS
    ret, frame = cap.read() # Чтение одного кадра
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # Перевод кадра в чб
    cv2.putText(frame,date,(200,450),font,fontScale,color=(255,255,255)) # Добавление текста
    cv2.imshow('frame', frame)  # Отображение кадра
    # Ожидание нажатия на q в течение 1 мс
    if cv2.waitKey(1) == 113:
        break

