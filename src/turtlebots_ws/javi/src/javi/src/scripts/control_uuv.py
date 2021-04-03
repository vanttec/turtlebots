#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point

# Format the point so it can be printed
def inline_point(point):
    return "[{},{},{}]".format(point.x,point.y,point.z)

def callback(data):
    # Print the buoy position sent by the 'perception_uuv' node
    rospy.loginfo("La coordenada es: %s",inline_point(data))
    
def listener():
    rospy.init_node('contro_uuv', anonymous=True)
    rospy.Subscriber('perception_to_control', Point, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()