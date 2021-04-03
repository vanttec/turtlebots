#!/usr/bin/env python2

import rospy
from geometry_msgs.msg import Point

def talker():
    pub = rospy.Publisher('perception_to_control', Point, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        #rospy.loginfo(hello_str)
        pub.publish((1.0, 2.0, 5.0))
        rate.sleep()
 
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass