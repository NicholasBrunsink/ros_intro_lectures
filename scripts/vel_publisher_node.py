#!/usr/bin/env python3

# import ROS for developing the node
import rospy

# import geometry_msgs/Twist for control commands
from geometry_msgs.msg import Twist

if __name__ == '__main__':
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	rospy.init_node('vel_publisher_node', anonymous = True)
	loop_rate = rospy.Rate(10)
	vel_cmd = Twist()
	
	While not rospy.is_shutdown():
		vel_cmd.linear.x = 0.5
		vel_cmd.angular.z = 0.5
		cmd_pub.publish(vel_cmd)
		loop_rate.sleep()
		
