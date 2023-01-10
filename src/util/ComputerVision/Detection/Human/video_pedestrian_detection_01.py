import cv2

print("Versão do OpenCV:", cv2.__version__)

# Utilização do Classificador para detecção de todo o corpo
classificador = cv2.CascadeClassifier("data\\cascades\\haarcascade_fullbody.xml")
# Video de referência
webCam = cv2.VideoCapture("data\\videos\\input\\ifpe (1).mp4")

while(True):
    conectou, imagem = webCam.read()
    converteuCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    encontrarFaces = classificador.detectMultiScale(converteuCinza,
                                                    scaleFactor=1.5,
                                                    minSize=(150,150),
                                                    maxSize=(200,200))
    cor = (0,0,255)
    for(origemX, origemY, largura, altura) in encontrarFaces:
        cv2.rectangle(imagem,(origemX,origemY),
                      (origemX + largura, origemY + altura),
                      cor,2)
        print("Largura", largura, "Altura", altura)
    cv2.imshow("Rosto", imagem)

    teclou = cv2.waitKey(20) & 0xFF
    if teclou == ord('q') or teclou == 27: # se apertar q ou ESC
        break

webCam.release()
cv2.destroyAllWindows()



