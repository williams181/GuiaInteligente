import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread('data\\imagens\\input\\ocr\\ifpe.png')

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(pytesseract.image_to_string(img))

n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

imS = cv2.resize(img, (960, 540)) 
cv2.imshow("img", imS)  
cv2.waitKey(0) 