import cv2



image= cv2.imread("building.jpg")

print(image.shape)
imgresize=cv2.resize(image,(1000,700))
print(imgresize.shape)




cv2.imshow("image_resized",imgresize)
cv2.waitKey(10)


cropped_img= image[200:400,0:300]

cv2.imshow("cropped",cropped_img)

cv2.waitKey(0)
