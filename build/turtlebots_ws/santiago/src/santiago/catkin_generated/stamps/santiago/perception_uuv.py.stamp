#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Point

def talker():
    pub = rospy.Publisher('perception_to_control', Point, queue_size=10)
    rospy.init_node('perception_uuv', anonymous=True)
    while not rospy.is_shutdown():
        print("Introduce los valores de la coordenada: ")
        x = input("x: ")
        y = input("y: ")
        z = input("z: ")
        coord = Point(x, y, z)
        coord_text = "(" + str(coord.x) + \
                     ", " + str(coord.y) + \
                     ", " + str(coord.z) + ")"
        rospy.loginfo("Coordenada enviada: " + coord_text)
        pub.publish(coord)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass