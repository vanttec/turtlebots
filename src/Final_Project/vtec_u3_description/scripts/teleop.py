#!/usr/bin/env python

#<!--////////////////////////////////////////////////////////////////////////////// -->
#<!--//////////////////////////////INICIO NO MOVER///////////////////////////////// -->
#<!--////////////////////////////////////////////////////////////////////////////// -->
import rospy
import keyboard 
from geometry_msgs.msg import Twist #Importa tipo ros msg tipo Twist
from sensor_msgs.msg import Image #Importa ros msg tipo Imagen
from cv_bridge import CvBridge, CvBridgeError
import cv2
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
    #Crea un objeto que adquiera las caracteristicas de la clase CvBridge()
    bridge = CvBridge()
    #Convierte el ros msg/imagen en una imagen bgr8 (blue, green,red, 8 bits) 
    cv_image = bridge.imgmsg_to_cv2(ros_msg_imagen, "bgr8")
    cv_2 = add_noise(cv_image) #opencv image con salt and pepper noise
    #Despliega la opencv image con ruido 
    cv2.imshow("Image w/noise", cv_2)
    #Aplica un filtro medianBlur de opencv con los parametros (imagen, 5) 
    median = cv2.medianBlur(cv_image, 5)
    #DEspliega la opencv image sin ruido
    cv2.imshow("Image filtered", median)
    if cv2.waitKey(10) & (tecla_keyboard =='p'): #Espera 10 milisegundos y con la tecla p toma foto.
        global counter
        counter +=1
        #usa la funcion imwrite de cv2 (opencv) y modifica el path para ti.
        # cv2.imwrite(path, imagen_a_guardar) 
        cv2.imwrite('/home/ivan5d/Pictures/VantTec/foto_' +str(counter) + '.jpg', median)

def callback(ros_msg_imagen):
    '''Esta funcion recibe una imagen y llama el opencv_bridge, ademas desde 
    aqui se opera el submarino desde la terminal (telleop)''' 
    
    #Crea un objeto que adquiera las caracteristicas de la clase Twist()
    twist=Twist() 
    
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
        twist.linear.y = v_lin 
    #Submarino hacia la derecha
    elif tecla_keyboard=='d':
        twist.linear.y = -1*v_lin 
    #Submarino hacia enfrente
    elif tecla_keyboard=='w':
    #objeto.tipo_de_movimiento.componente_x = v_lin
        twist.linear.x = v_lin
    #Submarino hacia atras
    elif tecla_keyboard=='s':
        twist.linear.x = -1*v_lin    
    #Submarino gira hacia la izquierda
    elif tecla_keyboard=='i':
        twist.angular.z = v_ang
    #Submarino gira hacia la derecha
    elif tecla_keyboard=='o':
        twist.angular.z = -1*v_ang
    print (msg) #Printea el mensaje en la terminal 

    #Crea un objeto pub = rospy.Publisher (/topico, tipo de mensaje, queue_size=10)
    pub = rospy.Publisher('/teleop', Twist, queue_size=10)

    rate = rospy.Rate(10) #10 Hz

    #publica con pub.publish(tipo de mensaje)
    pub.publish(twist)
    
    #Llama la funcion opencv_bridge con los parametros imagen y tecla_keyboard
    opencv_bridge(ros_msg_imagen, tecla_keyboard)
    
    rate.sleep() 

def image_subscriber():
    ''' Funcion principal, aqui se define el nodo subscriber y el topico usado
    para recibir esa informacion''' 
    #Define el nodo con el parametro anonymous=True
    rospy.init_node('Teleop', anonymous=True)
    #Subscribete al topico: /frontr200/camera/color/image_raw, recibe un ROS msg tipo [sensor_msgs/Image]
    #recuerda que cuando se recibe un mensaje se activa la funcion callback.
    rospy.Subscriber("/frontr200/camera/color/image_raw", Image, callback) #Callback
    #Evita que el nodo se cierre
    rospy.spin()

#<!--////////////////////////////////////////////////////////////////////////////// -->
#<!--//////////////////////////INICIO NO MOVER///////////////////////////////////// -->
#<!--////////////////////////////////////////////////////////////////////////////// -->

#Linea 143 y 144 son utilizadas para poder usar las teclas de la computadora.
if __name__ == '__main__':
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)
    try:
        #Corre la funcion principal
        image_subscriber()
    except rospy.ROSInterruptException:
        pass
#<!--////////////////////////////////////////////////////////////////////////////// -->
#<!--/////////////////////////////FIN NO MOVER///////////////////////////////////// -->
#<!--////////////////////////////////////////////////////////////////////////////// -->