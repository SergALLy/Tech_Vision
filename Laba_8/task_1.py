import cv2, math, sys
import numpy as np

def save_or_break(img, path): # Сохранение
    key=cv2.waitKey(0)
    if key == 121: # Нажали Y - сохранить
        cv2.imwrite(path,img) 
    elif key==27: # Нажали ESC - выйти
        cv2.destroyAllWindows()
        sys.exit(1)

img = cv2.imread('Laba_8\\task.png')
window='image'
cv2.namedWindow(window, cv2.WINDOW_GUI_EXPANDED)

img_c = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,img_c = cv2.threshold(img_c, 80,255, cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(img_c, mode=cv2.RETR_CCOMP, method=cv2.CHAIN_APPROX_SIMPLE)
# нужный контур индекс 1
# cv2.drawContours(img, contours,contourIdx=1, color=(255,0,0), thickness=3)

moments=[]
hu_moments=[]
# ищем 4, 13, 14

for i in range(0,len(contours)-1):
    moments.append(cv2.moments(contours[i+1], False))
    hu_moments.append(cv2.HuMoments(moments[i]))

stars=[]
pattern = moments[0]
hu_pattern = hu_moments[0]
# print(hu_pattern[0])
print(pattern['nu20'])
for i in range(1,len(moments)):
    print(moments[i]['nu20'])
    # print(hu_moments[i][0])
    if hu_pattern[0]*0.99<=hu_moments[i][0]<=hu_pattern[0]*1.01 and pattern['m00']*0.96<=moments[i]['m00']<=pattern['m00']*1.04:
          stars.append(contours[i+1])

# print(stars)

for i in range(len(stars)):
      cv2.drawContours(img, stars,contourIdx=i, color=(0,0,0), thickness=5)

cv2.imshow(window, img)
save_or_break(img, "Photo\\8.png")