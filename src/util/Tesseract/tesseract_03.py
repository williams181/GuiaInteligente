import cv2
import pytesseract

img = cv2.imread('data\\imagens\\input\\ocr\\biblioteca.jpg')

h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img) 
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

imS = cv2.resize(img, (960, 540)) 
cv2.imshow("img", imS)  
cv2.waitKey(0) 
