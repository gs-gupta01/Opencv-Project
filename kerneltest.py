import cv2
import numpy as np

img = cv2.imread("1.jpeg",1)

kernel = np.array([[0,1,0],[1,-4,1],[0,1,0]])

img = cv2.GaussianBlur(img,-1,kernel=kernel)

cv2.imshow("image",img)
cv2.waitKey(20000)