#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Point

# simulate the buoy's y-position influenced by a wave
def wave_sim():
    return math.sin(rospy.get_time()*math.pi*2.0/10.0)

def talker():
    pub = rospy.Publisher('perception_to_control', Point, queue_size=10)
    rospy.init_node('perception_uuv', anonymous=True)
    rate = rospy.Rate(15) # 15hz
    
    while not rospy.is_shutdown():
        
        # Publish position: 1.0, x, 5.0
        point=Point(1.0, wave_sim(), 5.0)
        pub.publish(point)
        
        rate.sleep()
 
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass