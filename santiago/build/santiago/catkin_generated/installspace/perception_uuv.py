#!/usr/bin/env python2
# license removed for brevity
import rospy
from geometry_msgs.msg import Point

def talker():
    pub = rospy.Publisher('perception_to_control', Point, queue_size=10)
    rospy.init_node('perception_uuv', anonymous=True)
    if not rospy.is_shutdown():
        coord = Point(1, 2, 3)
        rospy.loginfo("Coordenada enviada: " + coord.data)
        pub.publish(coord)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass