import cv2
import serial

print("Versão do OpenCV:", cv2.__version__)

classificador = cv2.CascadeClassifier('data\\opencv\\cascades\\haarcascade_frontalface_default.xml')
webCam = cv2.VideoCapture('data\\videos\\input\\ifpe (28).mp4')

while(True):
    conectou, imagem = webCam.read()
    
    imagem = cv2.flip(imagem, 1) # inverte imagem (opcional)
    alturaImagem, larguraImagem = imagem.shape[:2]
    
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
        #print("Largura", largura, "Altura", altura)
        
        raio = 4
        centroRosto = (origemX + int(largura/2),origemY + int(altura/2))
        cv2.circle(imagem, centroRosto, raio, cor)
        
        # Normalizar = deixa valores entre zero até um
        normalizarZeroAteUm = int(larguraImagem/2)
        # Correção = transforma valores para 1 até 10
        fatorDeCorrecao = 10
        
        erroCentro = (((centroRosto[0] - (larguraImagem/2))
        /normalizarZeroAteUm) * fatorDeCorrecao)
        print(erroCentro)
        erroCentro = int(erroCentro)

    # desenha linha central
    cv2.line(imagem,(int(larguraImagem/2),0),
             (int(larguraImagem/2),alturaImagem),
             cor, 2)
    
    cv2.imshow("Rosto", imagem)
    
    teclou = cv2.waitKey(5) & 0xFF
    if teclou == ord('q') or teclou == 27: # se apertar q ou ESC
        webCam.release()
        cv2.destroyAllWindows()
