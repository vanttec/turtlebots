#!/usr/bin/env python

#---------------------------No mover--------------------
import rospy
import keyboard 
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
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

#-------------------------------------------No mover---------------------

def opencv_bridge(data, key):

    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    #Imagen opencv con noise
    cv_2 = add_noise(cv_image)
    cv2.imshow("Image w/noise", cv_2)
    median = cv2.medianBlur(cv_image, 5)
    cv2.imshow("Image filtered", median)
    if cv2.waitKey(10) & (key =='p'):
        global counter
        counter +=1
        cv2.imwrite('/home/ivan5d/Pictures/VantTec/foto_' +str(counter) + '.jpg', cv_image)

#--------------------------------------------
#Publisher
def callback(data):
    v_lin = 0.8
    v_ang = 0.8
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
    key = getKey()
    #Left
    if key=='a':
        twist.linear.y = v_lin 
    #Right
    elif key=='d':
        twist.linear.y = -1*v_lin 
    #Forward
    elif key=='w':
        twist.linear.x = v_lin
    #Backwards
    elif key=='s':
        twist.linear.x = -1*v_lin    
    #Right yaw
    elif key=='i':
        twist.angular.z = v_ang
    #Left yaw 
    elif key=='o':
        twist.angular.z = -1*v_ang
    print (msg)
    pub = rospy.Publisher('/teleop', Twist, queue_size=10)
    rate = rospy.Rate(10)
    pub.publish(twist)
    opencv_bridge(data, key)
    rate.sleep()    

def image_subscriber():
    #Topic: /frontr200/camera/color/image_raw [sensor_msgs/Image]
    rospy.init_node('Teleop', anonymous=True)
    rospy.Subscriber("/frontr200/camera/color/image_raw", Image, callback) #Callback
    rospy.spin()

if __name__ == '__main__':
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)
    try:
        image_subscriber()
    except rospy.ROSInterruptException:
        pass