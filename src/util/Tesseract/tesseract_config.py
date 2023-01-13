import cv2 
import pytesseract

img = cv2.imread('data\\imagens\\input\\ocr\\biblioteca.jpg')

# Adding custom options
custom_config = r'--oem 3 --psm 6'
result = pytesseract.image_to_string(img, config=custom_config)

print(result)

