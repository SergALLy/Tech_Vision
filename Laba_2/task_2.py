import cv2
import numpy as np
path = 'Laba_2\\2-1.jpg'
window_name = 'figure_1'
window_name_2 = 'figure_2'
img=cv2.imread(path,flags=cv2.IMREAD_REDUCED_GRAYSCALE_2)
img_n = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,47,55)
cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(window_name_2,cv2.WINDOW_AUTOSIZE)
cv2.imshow(window_name,img)
cv2.imshow(window_name_2,img_n )
if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()