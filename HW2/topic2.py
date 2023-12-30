import cv2 as cv

img = cv.imread("f2.jpg")
img0 = cv.imread("f2.jpg")
kernel = cv.getStructuringElement(cv.MORPH_RECT,(9,9))
img1 = cv.morphologyEx(img,cv.MORPH_OPEN,kernel)
img2 = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
retval,img3 = cv.threshold(img2,150,255,cv.THRESH_BINARY)
num_labels,labels,stats,centroids = cv.connectedComponentsWithStats(img3,connectivity=8,ltype=None)
for i in range(0,num_labels):
    if stats[i][0] != 0:
        x = stats[i][0]
        y = stats[i][1]
        w = stats[i][2]
        h = stats[i][3]
        cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

cv.imshow('origin',img0)
cv.imshow('now',img)
cv.waitKey(0)
cv.destroyAllWindows()