#!/usr/bin/env python

#<!--////////////////////////////////////////////////////////////////////////////// -->
#<!--//////////////////////////////INICIO NO MOVER///////////////////////////////// -->
#<!--////////////////////////////////////////////////////////////////////////////// -->
import rospy #Importa rospy
import keyboard #Importa keyboard
from geometry_msgs.msg import Twist #Importa tipo ros msg tipo Twist
from sensor_msgs.msg import Image #Importa ros msg tipo Imagen
from cv_bridge import CvBridge, CvBridgeError #Importa opencv_bridge
import cv2 #Importa opencv
import random

import sys, select, os
if os.name == 'nt':
    import msvcrt
else:
    import tty, termios

counter = 0

def getKey():
    '''Esta funcion recibe la tecla del keyboard, no modificar'''
    if os.name == 'nt':
        return msvcrt.getch()
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def add_noise(img):
    '''Esta funcion agrega el salt and pepper noise, no modificar'''
    # Getting the dimensions of the image
    row, col, a= img.shape
    # Randomly pick some pixels in the
    # image for coloring them white
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)
        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)
        # Color that pixel to white
        img[y_coord][x_coord] = 255
    # Randomly pick some pixels in
    # the image for coloring them black
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300 , 10000)
    for j in range(number_of_pixels):
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)
        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)
        # Color that pixel to black
        img[y_coord][x_coord] = 0

    return img

#<!--////////////////////////////////////////////////////////////////////////////// -->
#<!--/////////////////////////////FIN NO MOVER///////////////////////////////////// -->
#<!--////////////////////////////////////////////////////////////////////////////// -->

def opencv_bridge(ros_msg_imagen, tecla_keyboard):
    '''Esta funcion crea el bridge para poder convertir el ROS msg/imagen a una
    imagen que puede ser modificada por opencv'''

    #Crea un objeto llamado <<bridge>> que adquiera las caracteristicas de la clase CvBridge()
    #-Escribe aqui

    #Convierte el ros msg/imagen en una imagen bgr8 (blue, green,red, 8 bits),
    # guarda esa imagen en la variable <<cv_image>>
    #-Escribe aqui

    cv_image_with_noise = add_noise(cv_image) #opencv image con salt and pepper noise

    # Muestra la opencv_image con ruido con .imshow de opencv
    #-Escribe aqui

    # Aplica un filtro medianBlur de opencv con los parametros (cv_image_with_noise, 5) y
    # guarda el resultado en la variable <<cv_image_filtered>>
    #-Escribe aqui

    # Muestra la opencv image filtrada con .imshow
    #-Escribe aqui

    if cv2.waitKey(10) & (tecla_keyboard =='p'): #Espera 10 milisegundos y con la tecla p toma foto.
        global counter
        counter +=1
        #usa .imwrite de opencv (cv2) para guardar la cv_image_filtered, este metodo 
        # tiene dos argumentos (path, imagen_a_guardar)
        #-Escribe aqui

def callback(ros_msg_imagen):
    '''Esta funcion recibe una imagen y llama el opencv_bridge, ademas desde 
    aqui se opera el submarino desde la terminal (teleop)''' 
    
    #Crea un objeto llamado <<twist>> que adquiera las caracteristicas de la clase Twist()
    # este es el tipo de mensaje que el submarino necesita para moverse por gazebo
    #-Escribe aqui 
    
    msg = """

    ---------------------------
    Teleop vtec_u3 

    1) Lineal:
        a = left
        d = rights
        w = forwards
        s = backwards
    2) Angular:
        i = right yaw 
        o = left yaw
    3) Picture: 
        p = take picture

    CTRL-C to quit

    """
    tecla_keyboard = getKey() #Recibe la tecla seleccionada del keyboard
    v_lin = 0.8 #Velocidad lineal 
    v_ang = 0.8 #Velocidad angular
    
    #Submarino hacia la izquierda 
    if tecla_keyboard=='a':
        #objeto.tipo_de_movimiento.componente_y = v_lin
        #-Escribe aqui
    #Submarino hacia la derecha
    elif tecla_keyboard=='d':
        #-Escribe aqui
    #Submarino hacia enfrente
    elif tecla_keyboard=='w':
    #objeto.tipo_de_movimiento.componente_x = v_lin
        #-Escribe aqui
    #Submarino hacia atras
    elif tecla_keyboard=='s':
        #-Escribe aqui   
    #Submarino gira hacia la izquierda
    elif tecla_keyboard=='i':
    #objeto.tipo_de_movimiento.componente_z = v_ang    
        #-Escribe aqui
    #Submarino gira hacia la derecha
    elif tecla_keyboard=='o':
        #-Escribe aqui
    print (msg) #Printea el mensaje en la terminal 

    #Crea un objeto <<pub>> con pub = rospy.Publisher (/topico, tipo de mensaje, queue_size=10)
    #-Escribe aqui

    rate = rospy.Rate(10) #10 Hz

    #publicar con pub.publish(tipo de mensaje)
    #-Escribe aqui
    
    #Llama la funcion opencv_bridge con los parametros <<ros_msg_imagen>> y <<tecla_keyboard>>
    #-Escribe aqui
    
    rate.sleep() #sleep

def image_subscriber():
    ''' Funcion principal, aqui se define el nodo subscriber y el topico usado
    para recibir esa informacion''' 
    #Inicializa el nodo con el parametro anonymous=True
    #-Escribe aqui

    #Subscribete al topico: /frontr200/camera/color/image_raw, recibe un ROS msg tipo [sensor_msgs/Image]
    #recuerda que cuando se recibe un mensaje se activa la funcion callback.
    #-Escribe aqui
    
    rospy.spin() #Evita que el nodo se cierre

#<!--////////////////////////////////////////////////////////////////////////////// -->
#<!--//////////////////////////INICIO NO MOVER///////////////////////////////////// -->
#<!--////////////////////////////////////////////////////////////////////////////// -->

#Linea 143 y 144 son utilizadas para poder usar las teclas de la computadora.
if __name__ == '__main__':
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)
    try:
        image_subscriber() #Corre la funcion principal
    except rospy.ROSInterruptException:
        pass
#<!--////////////////////////////////////////////////////////////////////////////// -->
#<!--/////////////////////////////FIN NO MOVER///////////////////////////////////// -->
#<!--////////////////////////////////////////////////////////////////////////////// -->