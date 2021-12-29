import cv2 as cv
import numpy as np  


real = cv.VideoCapture(1)

while True :
    
    ret,frame = real.read()
    frame = cv.flip(frame,1)
    kernel = np.zeros((3,3),dtype='uint8')


    box = frame[200:500, 200:500]

    cv.rectangle(frame,(200,200),(500,500),(255,0,0),0)
    hsv = cv.cvtColor(box,cv.COLOR_BGR2HSV)
    
    lowerHS = np.array([0,20,70], dtype="uint8")
    upperHS = np.array([20,255,255], dtype="uint8")

    msk = cv.inRange(hsv,lowerHS,upperHS)
    msk = cv.dilate(msk,kernel , iterations=10)

    msk = cv.GaussianBlur(msk,(3,3),200)

    cv.imshow('Mask',msk)
    cv.imshow('frame',frame)

    if cv.waitKey(1) & 0XFF == ord('q'):
        break

real.release()
cv.destroyAllWindows()