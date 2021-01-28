#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897



def rotate(angle):
		velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
		vel_msg = Twist()
		vel_msg.linear.x = 0
		vel_msg.angular.z = 0.2
		rel_angle = angle * 2 * PI/360
		traveled = 0
		t0 = rospy.Time.now().to_sec()
		while(traveled < rel_angle) :
			velocity_publisher.publish(vel_msg)
			t1 = rospy.Time.now().to_sec()
			traveled = vel_msg.angular.z * (t1 - t0)	
		
		vel_msg.linear.x = 0
		vel_msg.angular.z = 0
		velocity_publisher.publish(vel_msg)

def straightline(dist):
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()
	vel_msg.linear.x = 0.2
	vel_msg.angular.z = 0
	
	distance = dist
	traveled = 0
	t0 = rospy.Time.now().to_sec()
	while(traveled < distance):
		velocity_publisher.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		traveled = vel_msg.linear.x * (t1 - t0)
	
	vel_msg.linear.x = 0
	vel_msg.angular.z = 0
	velocity_publisher.publish(vel_msg)

	
		
if __name__ == '__main__':
	try:
		rospy.init_node('robot_cleaner', anonymous=True)
		straightline(2)
		rotate(90)
		straightline(2)
		rotate(90)
		straightline(2)
		rotate(90)
		straightline(2)
	except rospy.ROSInterruptException: pass
