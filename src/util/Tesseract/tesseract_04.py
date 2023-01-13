import pytesseract
import cv2
img = cv2.imread('data\\imagens\\input\\ocr\\ifpe.png')
img = cv2.resize(img, (960, 540)) 
hImg, wImg, _ = img.shape

boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
  b = b.split(' ')
print(b)
x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 1)
cv2.putText(img, b[0], (x, hImg - y + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50, 205, 50), 1)

cv2.imshow('ifpe_detected_text', img)
cv2.waitKey(0)