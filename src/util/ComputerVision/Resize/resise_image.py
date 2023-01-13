import cv2

img = cv2.imread('data\\imagens\\input\\pisos tateis\\png\\1.png')

imS = cv2.resize(img, (960, 540)) 
cv2.imwrite('data\\imagens\\input\\pisos tateis\\lineDetected\\resized.png', imS)
cv2.imshow("img", imS)  
cv2.waitKey(0) 
