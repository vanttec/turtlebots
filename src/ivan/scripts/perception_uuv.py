#!/usr/bin/env python

import rospy 
from geometry_msgs.msg import Point

def perception_uuv():
    pub = rospy.Publisher('perception_to_control', Point, queue_size=10)
    rospy.init_node('perception_uuv', anonymous=False)
    while not rospy.is_shutdown():
        coordenadas = Point(1,1,1)
        pub.publish(coordenadas)
        rospy.loginfo(coordenadas)
        

if __name__ == '__main__':
    try:
        perception_uuv()
    except rospy.ROSInterruptException:
        pass
