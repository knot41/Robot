import cv2 as cv
import numpy as np

img = cv.imread('f3.jpg')
img0 = cv.imread('f3.jpg')
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
lower1 = np.array([0, 100, 100])
upper1 = np.array([10, 255, 255])
mask1 = cv.inRange(hsv, lower1, upper1)  # mask1 为二值图像
lower2 = np.array([156, 100, 100])
upper2 = np.array([180, 255, 255])
mask2 = cv.inRange(hsv, lower2, upper2)
mask3 = mask1 + mask2
num_labels,labels,stats,centroids = cv.connectedComponentsWithStats(mask3,connectivity=8,ltype=None)
for i in range(0,num_labels):
    if stats[i][0] !=0 and 9000<stats[i][4]<10000:
        x = stats[i][0]
        y = stats[i][1]
        w = stats[i][2]
        h = stats[i][3]
        cv.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
cv.imshow("origin", img0)
cv.imshow("now",img)
cv.waitKey(0)
cv.destroyAllWindows()