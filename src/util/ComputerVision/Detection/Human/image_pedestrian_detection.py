import cv2
import imutils

# Inicializando a pessoa HOG
# detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Lendo a imagem
image = cv2.imread('data\\imagens\\input\\1\\1.jpg')

# Redimensionando a imagem
image = imutils.resize(image,
					width=min(800, image.shape[1]))

# Detectando todas as regiões do
# Imagem que tem um pedestre dentro dela
(regions, _) = hog.detectMultiScale(image,
									winStride=(4, 4),
									padding=(4, 4),
									scale=1.05)

# Desenhando as regiões na imagem
for (x, y, w, h) in regions:
	cv2.rectangle(image, (x, y),
				(x + w, y + h),
				(0, 0, 255), 2)

# Mostrando a imagem de saída
cv2.imshow("Image", image)
cv2.waitKey(0)

cv2.destroyAllWindows()



