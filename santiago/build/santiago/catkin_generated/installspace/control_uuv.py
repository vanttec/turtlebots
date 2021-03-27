#!/usr/bin/env python2
import rospy
from geometry_msgs.msg import Point

def callback(data):
    rospy.loginfo("La coordenada es: " + data.data)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('control_uuv', anonymous=True)

    rospy.Subscriber("perception_to_control", Point, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()