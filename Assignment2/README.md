Folder Description:
The turtlesim_cleaner folder contains all of my assingments for Assignment 2. It contains 3 python files: circle.py, square_openloop.py, and square_closedloop.py. Their descriptions are as followed:

circle.py:
This script is based on the 'Rotating Left/Right' ROS tutorial (http://wiki.ros.org/turtlesim/Tutorials/Rotating%20Left%20and%20Right) that moves the turtlesim in a circle. Because I want to move in a circle, i set the linear and angular velocities to the same number. Distance calculation is similar to the tutorial, instead of asking for a numbers of degrees to rotate, I know that I want to spin a full 360 circle. ROS angular velocities are in radians, so I convert 360 to radians to get the relative angle, w, and distance. Then run in a while loop until the traveled_distance is greater than the calculated distance.


![Alt text](https://github.com/mikail-g/git_ws_AuE893/blob/main/Assignment2/Pictures/circle.png)

square_openloop.py
The script makes the turtlesim move in a 2x2 square at a speed of 0.2. This file contains two main functions: rotate and drive. Following the 'Moving in a Straight Line' ROS tutorial (http://wiki.ros.org/turtlesim/Tutorials/Moving%20in%20a%20Straight%20Line). Drive sets the linear velocity to the specified 0.2, and the distance at 2. The rotate function follows the same idea from the circle.py file where the desired turning angle is set to 90 instead of 360. Then I call the two functions for each side: drive, rotate, drive, rotate...


![Alt text](https://github.com/mikail-g/git_ws_AuE893/blob/main/Assignment2/Pictures/square_openloop.png)

square_closedloop.py
This script moves the turtlebot in a 3x3 square but instead of setting distances, it moves based on cartesian coordinates. Using the 'Go to Goal' ROS tutorial (http://wiki.ros.org/turtlesim/Tutorials/Go%20to%20Goal). I basically just used this code, with some minor changes to work with python3 rather than python. __init__ sets up the communication channels and data structures. update_pose updates the position data structure. euclid_dist calculates the euclidean distance between two points via the distance formula. steering angle calculate the angle to turn the turtlesim, linear_vel and angular_vel determine the respective velocities. I added the rotate function from square_openloop and modified it to take in a desired angle as an argument. move2goal moves the turtlesim to the specified location via the tutorials method. I call move2goal and rotate in succession through the coordinates (5,5)-->(8,5)-->(8,8)-->(5,8)-->(5,5) 


![Alt text](https://github.com/mikail-g/git_ws_AuE893/blob/main/Assignment2/Pictures/square_closedloop.png)
