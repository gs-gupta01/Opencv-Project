import cv2

img = cv2.imread("1.jpeg", 0)

ret,thr = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)
cv2.imshow("original", img)
cv2.imshow("Thresholded", thr)
cv2.imwrite("thresholded.jpeg", thr)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
