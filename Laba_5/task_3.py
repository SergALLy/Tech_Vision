import cv2

cap = cv2.VideoCapture('Laba_5\\video_1.mp4')
while 1:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_filt = cv2.GaussianBlur(frame,ksize=(15,15),sigmaX=0)
    frame_filt = cv2.Canny(frame_filt, 50, 150, 7)
    cv2.imshow('video', frame_filt) 
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()