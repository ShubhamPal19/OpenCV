import cv2
import numpy


image= cv2.imread("img/building.jpg")
print(image.shape)


pts1= numpy.float32([[1000,100],[1400,100],[700,600],[1400,500]])
pts2=  numpy.float32([[0,0],[400,0],[0,400],[400,400]])
matrix= cv2.getPerspectiveTransform(pts1,pts2)
output =cv2.warpPerspective(image,matrix,(400,400))
cv2.imshow("original",image)
cv2.imshow("output",output)

cv2.waitKey(0)