#!/usr/bin/env python3

# import ROS for developing the node
import rospy

# import turtlesim import pose message
from turtlesim.msg import Pose

#math module
import math

ROTATION_SCALE = 180.0/math.pi

def pose_callback(data):
	# convert angular position to degrees
	rot_in_degree = data.theta * ROTATION_SCALE
	# convert x and y to cm
	x_in_cm = data.x * 100
	y_in_cm = data.y * 100 
	# show results
	rospy.loginfo("x is %0.2f cm, y is %0.2f cm, theta is %0.2f degrees", x_in_cm, y_in_cm, rot_in_degree)
	
if __name__== "__main__":

	# initialized the node
	rospy.init_node('pos_converter', anonymous = True)
	# add subscriber to the node
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	# spin means keep the python node running until force stop
	rospy.spin()
	

	
