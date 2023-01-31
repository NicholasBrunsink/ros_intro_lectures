#!/usr/bin/env python3

# import ROS for developing the node
import rospy

# import geometry_msgs/Twist for control commands
from geometry_msgs.msg import Twist

if __name__ == '__main__':
	# decalre a publisher to publish velocity commands
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	# initialized the node
	rospy.init_node('vel_publisher_node', anonymous = True)
	# set up a loop frequency for the control loop (10Hz)
	loop_rate = rospy.Rate(10)
	# define a Twist message to use in the loop
	vel_cmd = Twist()
	
	# set up a loop that runs at a 10Hz frequency
	while not rospy.is_shutdown():
		# set the linear velocity to 1 m/s
		vel_cmd.linear.x = 1
		# set the angular velocity to 1 rad/s
		vel_cmd.angular.z = -1
		# publish the command to the sim
		cmd_pub.publish(vel_cmd)
		# wait for 0.1 of second until the next loop
		loop_rate.sleep()

