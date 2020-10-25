
import cv2
import numpy as np

img = cv2.imread("2.jpeg",1)
hsvimg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow("original",img)
cv2.imshow("HSV",hsvimg)

lb=np.array([110,50,50])
ub=np.array([130,255,255])

mask = cv2.inRange(hsvimg,lb,ub)
cv2.imshow("mask",mask)

resimg = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("resimg",resimg)

if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()