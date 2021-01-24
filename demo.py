import cv2


img= cv2.imread("img/photo1.jpg")

imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(img,(19,19),0)
imgcanny= cv2.Canny(img,100,100)

cv2.imshow("IMG1",imgGray)
cv2.imshow("output",img)
cv2.imshow("blur",imgblur)
cv2.imshow("canny",imgcanny)



img2=cv2.imread("img/847723.jpg")
img2canny= cv2.Canny(img2,100,100)
cv2.imshow("canny",img2canny)

cv2.waitKey(0)