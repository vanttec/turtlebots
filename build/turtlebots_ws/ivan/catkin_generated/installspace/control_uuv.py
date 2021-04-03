#!/usr/bin/env python2

import rospy 
from geometry_msgs.msg import Point

def callback (data):
    print("La coordenada es")
    rospy.loginfo(data)

def control_uuv():
    rospy.init_node('control_uuv',anonymous=False)
    rospy.Subscriber('perception_to_control', Point, callback)
    rospy.spin()

if __name__ == '__main__':
    control_uuv()
