#!/usr/bin/env python3

# import ROS for developing the node
import rospy

# import turtlesim import pose message
from turtlesim.msg import Pose

# importing the new message from our package
from ros_intro_lectures.msg import Shortpose

#math module
import math

ROTATION_SCALE = 180.0/math.pi

pos_msg = Shortpose()

def pose_callback(data):
	global pos_msg
	# convert angular position to degrees
	pos_msg.theta = data.theta * ROTATION_SCALE
	# convert x and y to cm
	pos_msg.x = data.x * 100
	pos_msg.y = data.y * 100 
	
	
	
if __name__== "__main__":

	# initialized the node
	rospy.init_node('pos_converter', anonymous = True)
	# add subscriber to the node
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	# add a publisher with a new topic using the Shortpose message
	pos_pub = rospy.Publisher('/turtle1/shortpose', Shortpose, queue_size=10)
	# set a 10Hz freq for this loop
	loop_rate=rospy.Rate(10)
	
	while not rospy.is_shutdown():
		# publish the message
		pos_pub.publish(pos_msg)
		# wait for 0.1 seconds until next loop and repeat
		loop_rate.sleep()
	

	
