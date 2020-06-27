#!/usr/bin/env python

from __future__ import print_function
import numpy as np
import math
from numpy.linalg import inv
import serial




import rospy

from geometry_msgs.msg import Twist

import sys, select, termios, tty



if __name__=="__main__":

	pub = rospy.Publisher('/Ik_result', Twist, queue_size = 1)
	rospy.init_node('arm_angle')

	with open('pick_ik.dat','r') as f:
		pick_angles = f.read().strip().split(',')
		s0_pick, s1_pick, s2_pick = float(pick_angles[1]) ,float(pick_angles[2]) , float(pick_angles[3])

	'''

	with open('place_ik.dat','r') as f:
		place_angles = f.read().strip().split(',')
		s0_place, s1_place, s2_place = float(place_angles[1]) ,float(place_angles[2]) , float(place_angles[3])

	'''

	#print(s0_pick, s1_pick, s2_pick  ,  s0_place, s1_place, s2_place  )
	twist = Twist()
	twist.linear.x = s0_pick; 
	twist.linear.y = s1_pick; 
	twist.linear.z = s2_pick;
	twist.angular.x = 0#s0_place; 
	twist.angular.y = 0#s1_place; 
	twist.angular.z = 0#s2_place
	pub.publish(twist)


