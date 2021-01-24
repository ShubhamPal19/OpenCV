import cv2
import numpy as np 


image=np.zeros((512,1024,3),np.uint8)
print(image)

image[200:400,400:900]= 100,255,0

cv2.line(image,(0,0),(900,400),(255,255,255),5)
cv2.rectangle(image,(100,100),(200,400),(0,0,200),cv2.FILLED)
cv2.circle(image,(700,0),200,(122,177,42),2)
cv2.imshow("image",image)
cv2.waitKey(0)

