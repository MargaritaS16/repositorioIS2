import cv2
import mediapipe as mp
from Funciones.condicionales import condicionalesLetras
from Funciones.normalizacionCords import obtenerAngulos
from Funciones.condicionales import validarLetras
import random
from tkinter import *
import tkinter as tk
from tkinter import ttk
import time

global letra_azar


def letra_aleatoria():
    letras = "ABCDEFGHIKLOWYX"
    return random.choice(letras)



lectura_actual = 0
     # se elige una letra al azar
letra_azar = letra_aleatoria()
    # cap almacenara la imagen de la camara
cap = cv2.VideoCapture(0)
    #establecemos la dimension de la camara
wCam, hCam = 1280, 720
cap.set(3, wCam)
cap.set(4, hCam)
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
mp_drawing_styles = mp.solutions.drawing_styles
with mp_hands.Hands(
static_image_mode=False,                        #imagen estatica
max_num_hands=2,                                #numero maximo de manos
min_detection_confidence=0.65) as hands:         #confianza de deteccion de manos
  while True:
    ret, frame = cap.read()
    if ret == False:
        break
    height, width, _ = frame.shape
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    #si quiero añadir mas puntos de referencias debo cambiar esta funcion
    if results.multi_hand_landmarks is not None:
        # Accediendo a los puntos de referencia, de acuerdo a su nombre
            angulosid = obtenerAngulos(results, width, height)[0]
            dedos = []
            # pulgar externo angle
            if angulosid[5] > 125:
                dedos.append(1)
            else:
                dedos.append(0)

            # pulgar interno
            if angulosid[4] > 150:
                dedos.append(1)
            else:
                dedos.append(0)

            # 4 dedos
            for id in range(0, 4):
                if angulosid[id] > 90:
                    dedos.append(1)
                else:
                    dedos.append(0)

            TotalDedos = dedos.count(1)
            condicionalesLetras(dedos, frame)
        #VALIDA SI LA LETRA ALEATORIA ES LA MISMA QUE LA QUE SE LE PIDE
            valResp = validarLetras(dedos)
            while(valResp == letra_azar):
                if valResp == letra_azar:
                    #hacer que demore unos segundos que hiciste la seña correcta
                    cv2.rectangle(frame, (500, 600), (850, 700), (255, 255, 255), cv2.FILLED)
                    cv2.putText(frame, "Correcto", (550, 660), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 5, cv2.LINE_AA)
                valResp=validarLetras(dedos)
                letra_azar=letra_aleatoria()
            #hacer que retrase el proceso de elegir otra letra
        #PREGUNTA SI QUIERES REPETIR
            pinky = obtenerAngulos(results, width, height)[1]
            pinkY=pinky[1] + pinky[0]
            resta = pinkY - lectura_actual
            lectura_actual = pinkY
            print(abs(resta), pinkY, lectura_actual)

            if dedos == [0, 0, 1, 0, 0, 0]:
                if abs(resta) > 30:
                    print("jota en movimento")
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
                    cv2.putText(frame, 'J', (20, 80), font, 3, (0, 0, 0), 5, cv2.LINE_AA)

            #dibuja las lineas entre los landmarks
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())

                #cabecera del frame
    cv2.rectangle(frame, (110, 20), (800, 100), (255, 255, 255), cv2.FILLED)
    cv2.putText(frame, "Indique la letra ", (120, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 5, cv2.LINE_AA)
    cv2.putText(frame, letra_azar, (700, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 5, cv2.LINE_AA)
    cv2.imshow('Frame', frame)
    #elige otra letra aleatoria
    if cv2.waitKey(1) & 0xFF == ord('q'):
        letra_azar = letra_aleatoria()
    #Para que se cierre la ventana se presiona esc
    if cv2.waitKey(1) & 0xFF == 27:
        break


        cv2.destroyAllWindows()