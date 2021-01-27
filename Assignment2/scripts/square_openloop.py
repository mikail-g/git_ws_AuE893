#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def move():
	rospy.init_node('robot_cleaner', anonymous=True)
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()
	
	
	#step 1:
	vel_msg.linear.x = 0.2
	vel_msg.angular.z = 0
	
	distance = 2
	traveled = 0
	t0 = rospy.Time.now().to_sec()
	while(traveled < distance):
		velocity_publisher.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		traveled = vel_msg.linear.x * (t1 - t0)
	
	vel_msg.linear.x = 0
	vel_msg.angular.z = 0
	velocity_publisher.publish(vel_msg)
		
	#step 2:
	vel_msg.linear.x = 0
	vel_msg.angular.z = 0.2
	
	rel_angle = 90 * 2 * PI/360
	traveled = 0
	t0 = rospy.Time.now().to_sec()
	while(traveled < rel_angle):
		velocity_publisher.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		traveled = vel_msg.angular.z * (t1 - t0)
		
	vel_msg.linear.x = 0
	vel_msg.angular.z = 0
	velocity_publisher.publish(vel_msg)
	
	#step 3:
	vel_msg.linear.x = 0.2
	vel_msg.angular.z = 0
	distance = 2
	traveled = 0
	t0 = rospy.Time.now().to_sec()
	while(traveled < distance):
		velocity_publisher.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		traveled = vel_msg.linear.x * (t1 - t0)
	
	vel_msg.linear.x = 0
	vel_msg.angular.z = 0
	velocity_publisher.publish(vel_msg)
	
	#step 4:
	vel_msg.linear.x = 0
	vel_msg.angular.z = 0.2
	
	rel_angle = 90 * 2 * PI/360
	traveled = 0
	t0 = rospy.Time.now().to_sec()
	while(traveled < rel_angle):
		velocity_publisher.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		traveled = vel_msg.angular.z * (t1 - t0)
		
	vel_msg.linear.x = 0
	vel_msg.angular.z = 0
	velocity_publisher.publish(vel_msg)
	
	#Step 5:
	vel_msg.linear.x = 0.2
	vel_msg.angular.z = 0
	distance = 2
	traveled = 0
	t0 = rospy.Time.now().to_sec()
	while(traveled < distance):
		velocity_publisher.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		traveled = vel_msg.linear.x * (t1 - t0)
	
	vel_msg.linear.x = 0
	vel_msg.angular.z = 0
	velocity_publisher.publish(vel_msg)
	
	#step 6:
	vel_msg.linear.x = 0
	vel_msg.angular.z = 0.2
	
	rel_angle = 90 * 2 * PI/360
	traveled = 0
	t0 = rospy.Time.now().to_sec()
	while(traveled < rel_angle):
		velocity_publisher.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		traveled = vel_msg.angular.z * (t1 - t0)
		
	vel_msg.linear.x = 0
	vel_msg.angular.z = 0
	velocity_publisher.publish(vel_msg)
	
	#step 7:
	vel_msg.linear.x = 0.2
	vel_msg.angular.z = 0
	distance = 2
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
		move()
	except rospy.ROSInterruptException: pass
