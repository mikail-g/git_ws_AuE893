#!/usr/bin/env python3
import rospy
from geometry_msgs.msg  import Twist
from turtlesim.msg import Pose
from math import pow,atan2,sqrt
PI = 3.1415926535897
class turtlebot():

    def __init__(self):
        #Creating our node,publisher and subscriber
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)
        self.pose = Pose()
        self.rate = rospy.Rate(10)
        
    def update_pose(self, data):
    	self.pose = data
    	self.pose.x = round(self.pose.x, 4)
    	self.pose.y = round(self.pose.y, 4)
        
    def euclid_dist(self, goal_pose):
    	return sqrt(pow((goal_pose.x - self.pose.x),2) + pow((goal_pose.y - self.pose.y),2))
    	
    def linear_vel(self, goal_pose):
    	return 2 * 0.5 * self.euclid_dist(goal_pose)
    	
    def steering_angle(self, goal_pose):
    	return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)
    
    def angular_vel(self, goal_pose):
    	return 3 * (self.steering_angle(goal_pose) - self.pose.theta)
    
    def rotate(self, angle):
    	vel_msg = Twist()
    	vel_msg.linear.x = 0
    	vel_msg.angular.z = 0.2
    	rel_angle = angle * 2 * PI/360
    	traveled = 0
    	t0 = rospy.Time.now().to_sec()
    	while(traveled < rel_angle) :
    		self.velocity_publisher.publish(vel_msg)
    		t1 = rospy.Time.now().to_sec()
    		traveled = vel_msg.angular.z * (t1 - t0)
		
    	vel_msg.linear.x = 0
    	vel_msg.angular.z = 0
    	self.velocity_publisher.publish(vel_msg)	

    def move2goal(self, x, y, tol):
        goal_pose = Pose()
        goal_pose.x = x
        goal_pose.y = y
        distance_tolerance = tol
        vel_msg = Twist()
        
      
        while self.euclid_dist(goal_pose) >= distance_tolerance:
        	print("distance: " + str(self.euclid_dist(goal_pose)))
        	print("linear vel: " + str(self.linear_vel(goal_pose)))
        	print("angular vel: " + str(self.angular_vel(goal_pose)))
        	vel_msg.linear.x = abs(self.linear_vel(goal_pose))
        	vel_msg.angular.z = self.angular_vel(goal_pose)
        	self.velocity_publisher.publish(vel_msg)
        	self.rate.sleep()
            
            
        #Stopping our robot after the movement is over
        vel_msg.linear.x = 0
        vel_msg.angular.z =0
        self.velocity_publisher.publish(vel_msg)
        
        
        

if __name__ == '__main__':
    try:
        #Testing our function
        x = turtlebot()
        print("moving to point (5,5)")
        x.move2goal(5,5,.1)
        x.rotate(180)
        x.move2goal(8,5,.1)
        x.rotate(90)
        x.move2goal(8,8,.1)
        x.rotate(90)
        x.move2goal(5,8,.1)
        x.rotate(90)
        x.move2goal(5,5,.1)
        
        
        


    except rospy.ROSInterruptException: pass
