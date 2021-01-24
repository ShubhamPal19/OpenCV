import cv2

x1=0
x2=100
y1=100
y2=500
image =   cv2.imread("img/building.jpg")

while True:
    frame =image[x1:y1,x2:y2]
    x1=x1+1
    x2=x2+1
    cv2.imshow("video",frame)
    cv2.waitKey(1000)
