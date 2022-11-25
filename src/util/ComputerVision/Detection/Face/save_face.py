import numpy as np

import cv2

detector= cv2.CascadeClassifier('data\\opencv\\cascades\\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while(True):

    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = detector.detectMultiScale(gray, 1.3, 5)
    count = 0
    for (x,y,w,h) in faces:
        face = img[y:y+h, x:x+w] #slice the face from the image
        cv2.imwrite('data\\imagens\\output\\'+ str(count)+'.jpg', face) #save the image
        count+=1
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('frame',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

cap.release()

cv2.destroyAllWindows()