import cv2
import numpy as np

pts = []
print(cv2.__version__)


def handle_events(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # rbg = str(img[y, x, 0]) + " , " + str(img[y, x, 1]) + " , " + str(img[y, x, 2])
        # font = cv2.FONT_ITALIC
        # cv2.putText(img, rbg, (x, y), font, 0.5, (255, 0, 10), 2)
        # cv2.imshow("image", img)
        # r = abcd[y,x,2]
        # g = abcd[y,x,1]
        # b = abcd[y,x,0]
        #
        # mci = np.zeros((512, 512, 3), np.uint8)
        # mci[:] = [b, g, r]
        # cv2.imshow("color", mci)
        coor = str(x) + " , " + str(y)
        font = cv2.FONT_ITALIC
        cv2.putText(abcd, coor, (x, y), font, 0.5, (255, 0, 0), 2)
        cv2.imshow("image", abcd)
    if event == cv2.EVENT_RBUTTONDOWN:
        pts.append((x, y))
        cv2.circle(abcd, (x, y), 5, (255, 0, 0), -1)
        if len(pts) >= 2:
            cv2.line(abcd, pts[-1], pts[-2], (145, 255, 255), 3)
        cv2.imshow("image", abcd)


cv2.namedWindow("image")
cv2.setMouseCallback("image", handle_events)

abcd = cv2.imread("1.jpeg", 1)
img = abcd[16:194, 319:686]

cv2.imshow("ja", img)

cv2.imshow("image", abcd)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
