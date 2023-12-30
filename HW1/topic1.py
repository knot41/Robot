import cv2 as cv

img = cv.imread("f1.jpg")
kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
img = cv.morphologyEx(img,cv.MORPH_OPEN,kernel)
img1 = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
retval,img2 = cv.threshold(img1,0,255,cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
num_labels, labels ,stats , centroids = cv.connectedComponentsWithStats(img2, connectivity=8, ltype=None)
for i in range(1,num_labels):
    mask = labels == i
    if stats[i-1][2]-10 < stats[i-1][3] < stats[i-1][2]+10 and stats[i-1][4] < 20:
        img[:, :, 0][mask] = 0
        img[:, :, 1][mask] = 255
        img[:, :, 2][mask] = 255
img = cv.morphologyEx(img,cv.MORPH_OPEN,kernel)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
