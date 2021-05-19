import cv2
import numpy as np 


#leer imagen
img = cv2.imread("florroja.jpg")


#Ver que hay en img
#print(type(img))
#cv2.imshow('Imagen original', img) 

#Tamaños de la imagen
alto, ancho = img.shape[0:2]
#print(img.shape[0:2])

#rotar la imagen 90
matrizRotacion = cv2.getRotationMatrix2D((ancho/2, alto/2), 90, .5) 
                                          #(centro, angulo, escala)
imagenRotada   = cv2.warpAffine(img, matrizRotacion, (ancho, alto))
#cv2.imshow('Imagen rotada 90º', imagenRotada)

#rotar la imagen 90
matrizRotacion = cv2.getRotationMatrix2D((ancho/2, alto/2), 90, .5) #(centro, angulo, escala)
imagenRotada   = cv2.warpAffine(img, matrizRotacion, (ancho, alto))
#cv2.imshow('Imagen rotada 90º', imagenRotada)

#recortar la imagen
filaInicio = int(alto*.15)
columnaInicio = int(ancho*.15)

filaFin = int(alto*.85)
columnaFin = int(ancho*.85)

imgCortada = img[filaInicio:filaFin, columnaInicio:columnaFin]
#cv2.imshow('Imagen recortada', imgCortada)

#cambiar tamaño de imagen
nuevoTamanio = cv2.resize(img, (550, 350))
cv2.imshow('Imagen con cambio de tamaño', nuevoTamanio)


#Ajustar contrastes
'''
nuevaImagen = alfa * imgOriginal + beta

alfa: define el contraste de la imagen. 

Si alfa > 1 mayor contraste 
Si 0 < alfa < 1  menosr contraste
Si alfa = 1 no hay contraste
beta: [-127 , 127]

Para implementar esta ecuación en Python OpenCV, puedes usar el 
método addWeighted(). Usamos el método addWeighted() ya que genera la 
salida en el rango de 0 y 255 para una imagen en color de 24 bits.
cv2.addWeighted(source_img1, alpha1, source_img2, alpha2, beta)

'''
imgContraste = cv2.addWeighted(img, 2.5, np.zeros(img.shape, img.dtype), 0, 0)
#cv2.imshow('Imagen con contraste', imgContraste)


#Imagen difuminada
imgDifuminada = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow('Imagen difuminada', imgDifuminada)

#detectar bordes
imgBordes= cv2.Canny(img, 100, 200)
#cv2.imshow('Los bordes', imgBordes)


#convertir a escala de grises
imgGris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagen en gris", imgGris)


#detectar el centro de la imagen
momentos = cv2.moments(imgGris)
#--- calcular las coordenadas x y y
X = int(momentos ["m10"] / momentos["m00"])
Y = int(momentos ["m01"] / momentos["m00"])
cv2.circle(img, (X, Y), 15, (205, 114, 101), 1)
cv2.imshow("Centro de la Imagen", img)






cv2.waitKey(0)





