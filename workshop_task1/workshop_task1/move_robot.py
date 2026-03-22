#!/usr/bin/env python3

# =============================================================
#  ROS 2 Workshop — Drive TurtleBot3 to a Goal
# =============================================================
#
#  NAME : ___________________________
#
#  Fill in the 2 functions below.
#  Do NOT change anything else.
#
#  Run:
#    Terminal 1: ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
#    Terminal 2: ros2 run workshop_robot_task move_robot.py
# =============================================================

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math

GOAL_DISTANCE = 1.5   # metres — how far the robot should travel
SPEED         = 0.1   # m/s   — forward speed (keep between 0.05 and 0.20)


class MoveRobot(Node):

    def __init__(self):
        super().__init__('move_robot')
        self.publisher  = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscriber = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.timer      = self.create_timer(0.1, self.control_loop)

        self.start_x   = None
        self.start_y   = None
        self.current_x = 0.0
        self.current_y = 0.0

    # ── DO NOT CHANGE ─────────────────────────────────────────
    def odom_callback(self, msg):
        self.current_x = msg.pose.pose.position.x
        self.current_y = msg.pose.pose.position.y
        if self.start_x is None:
            self.start_x = self.current_x
            self.start_y = self.current_y

    # ── DO NOT CHANGE ─────────────────────────────────────────
    def stop_robot(self):
        msg = Twist()
        msg.linear.x  = 0.0
        msg.angular.z = 0.0
        return msg

    # ==========================================================
    #  TASK 1 — How far has the robot travelled?
    # ==========================================================
    #  Use Pythagoras:
    #    distance = euclideian

    #
    #  You have:
    #    self.start_x / self.start_y    ← where robot started
    #    self.current_x / self.current_y ← where robot is now
    # ==========================================================
    def calculate_distance(self):

        distance = 0.0   # ← replace with your formula

        return distance

    # ==========================================================
    #  TASK 2 — Make the robot move forward
    # ==========================================================
    #  msg.linear.x  = forward speed  
    #  msg.angular.z = turning speed  
    # ==========================================================
    def drive_forward(self):
        msg = Twist()

        msg.linear.x  = 0.0   
        msg.angular.z = 0.0   
        return msg

    # ── DO NOT CHANGE ─────────────────────────────────────────
    def control_loop(self):
        if self.start_x is None:
            return

        if self.calculate_distance() >= GOAL_DISTANCE:
            self.publisher.publish(self.stop_robot())
            self.get_logger().info('Goal reached!')
        else:
            self.publisher.publish(self.drive_forward())


# ── DO NOT CHANGE ─────────────────────────────────────────────
def main(args=None):
    rclpy.init(args=args)
    node = MoveRobot()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.publisher.publish(Twist())
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()