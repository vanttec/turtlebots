#!/usr/bin/env python

#dependencia 
import rospy 
#tipo de mensaje
from geometry_msgs.msg import Point

#lo que hace cuando reciba el mensaje
def callback (data):
    print("La coordenada es")
    rospy.loginfo(data)

def listener():
    rospy.init_node('listener',anonymous=True)
    rospy.Subscriber('perception_to_control', Point, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()