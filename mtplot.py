import matplotlib.pyplot as plt
import cv2
img1 = cv2.imread("1.jpeg",1)
img2 = cv2.imread("2.jpeg",1)
img3=cv2.imread("thresholded.jpeg",1)
img4 = cv2.imread("newimg.jpeg",1)

titles = ["First","Second","Third","Fourth"]
imgs = [img1,img2,img3,img4]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(imgs[i],"gray")
    plt.title(titles[i])
plt.show()