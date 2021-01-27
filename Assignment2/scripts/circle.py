#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def move():
	rospy.init_node('robot_cleaner', anonymous=True)
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()
	
	vel_msg.linear.x = 10
	vel_msg.angular.z = 10
	
	w = 360 * 2 * PI/360
	distance = 360 * 2 * PI/360
	print(distance)
	traveled = 0
	t0 = rospy.Time.now().to_sec()
	
	while(traveled < distance):
		velocity_publisher.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		traveled = w * (t1 - t0)
		
	vel_msg.linear.x = 0
	vel_msg.angular.z = 0
	velocity_publisher.publish(vel_msg)
	
		
if __name__ == '__main__':
	try:
		move()
	except rospy.ROSInterruptException: pass
