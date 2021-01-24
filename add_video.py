import cv2


video= cv2.VideoCapture("video/sample_video.mp4")

while True:
    success,image=video.read()
    cv2.imshow("video",image)
    if cv2.waitkey(1) & 0xFF == ord('q'):
        break