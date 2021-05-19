# -*- coding: utf-8 -*-
"""
Created on Tue May 18 18:53:17 2021

@author: precalde
"""

import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("No se puede abrir la camara")
    exit()
while True:
    # Capturar frame-by-frame
    ret, frame = cap.read()
    # Si el frame se lee bien ret es True
    if not ret:
        print("No se puede leer el straming, salir? ...")
        break
    # Las operaciones sobre el streaming van aquí
    enGris = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Mostrar el frame resultante
    cv.imshow('Venta del streaming', frame) #enGris)
    if cv.waitKey(1) == ord('q'):
        break
# Cuando se haya hecho todo, salir 
cap.release()
cv.destroyAllWindows()