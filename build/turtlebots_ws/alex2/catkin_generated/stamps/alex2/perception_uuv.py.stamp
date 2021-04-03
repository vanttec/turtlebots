#!/usr/bin/env python

#dependencia 
import rospy 
#tipo de mensaje
from geometry_msgs.msg import Point


def talker():
    #publisher
    pub = rospy.Publisher('perception_to_control', Point, queue_size=10)
    #anonimo x si hay otro nodo con el mismo nombre
    rospy.init_node('perception_uuv', anonymous=True)

    #mientras no se cierre rospy
    while not rospy.is_shutdown():

        coordenadas = Point(1,1,1)
        pub.publish(coordenadas)

        coordenadas_string = "(1,1,1)"
        rospy.loginfo(coordenadas)
        

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

