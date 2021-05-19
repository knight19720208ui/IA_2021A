# -*- coding: utf-8 -*-
"""
Created on Tue May 18 18:01:26 2021
@author: precalde
"""

import cv2
import numpy as np 


#leer imagen
img = cv2.imread("florroja.jpg")
imgGris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #a gris

#encontrar umbrales
_, thresh = cv2.threshold(imgGris, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

#encontrar contornos
imgContorno = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]

#ordenar contornos
imgContorno = sorted(imgContorno, key=cv2.contourArea)

for i in imgContorno:
    if cv2.contourArea(i) > 100:
        break
    
#generar mascara con ceros
mask = np.zeros(img.shape[:2], np.uint8)

#dibujar esos contornos
cv2.drawContours(mask, [i],-1, 255, -1)

#aplicar el bitwise_and
imgNueva = cv2.bitwise_and(img, img, mask=mask)

#mostrar la imagen original
cv2.imshow("Imagen Original", img)

#mostrar la imagen restada
cv2.imshow("Imagen sin el fondo", imgNueva)

cv2.waitKey(0)