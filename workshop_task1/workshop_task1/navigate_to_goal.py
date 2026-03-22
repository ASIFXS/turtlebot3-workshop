#!/usr/bin/env python3

# Workshop Task 3 — Navigate to Goal using Nav2
# NAME: ___________________________
#
# BEFORE RUNNING:
#   1. Launch Gazebo + Nav2:  ros2 launch workshop_robot_task task3.launch.py
#   2. In RViz2 → click "2D Pose Estimate" → click robot's position on map
#   3. In RViz2 → click "Publish Point"    → click your goal on the map
#   4. Copy the X, Y printed in terminal → paste into TODO 1 below
#   5. Fill TODOs 2, 3, 4 then run:  ros2 run workshop_robot_task navigate_to_goal.py

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose
from action_msgs.msg import GoalStatus

# TODO 1 — paste your X, Y from Publish Point
GOAL_X = 0.0   # ← your X
GOAL_Y = 0.0   # ← your Y


class NavigateToGoal(Node):

    def __init__(self):
        super().__init__('navigate_to_goal')

        # TODO 2 — create ActionClient
        # ActionClient(self, NavigateToPose, 'navigate_to_pose')
        self.client = None   # ← replace None

        self.send_goal()

    def send_goal(self):
        self.client.wait_for_server()

        goal = NavigateToPose.Goal()

        # TODO 3 — fill in 4 fields:
        # goal.pose.header.frame_id        = 'map'
        # goal.pose.pose.position.x        = GOAL_X
        # goal.pose.pose.position.y        = GOAL_Y
        # goal.pose.pose.orientation.w     = 1.0

        # TODO 4 — send goal
        # future = self.client.send_goal_async(goal, feedback_callback=self.feedback_cb)
        # future.add_done_callback(self.response_cb)
        self.get_logger().info(f'Sending goal x={GOAL_X} y={GOAL_Y}')

    # ── DO NOT CHANGE ─────────────────────────────────────────
    def response_cb(self, future):
        gh = future.result()
        if not gh.accepted:
            self.get_logger().info('Rejected!')
            return
        self.get_logger().info('Moving...')
        gh.get_result_async().add_done_callback(self.result_cb)

    def feedback_cb(self, feedback):
        self.get_logger().info(
            f'Remaining: {feedback.feedback.distance_remaining:.2f} m',
            throttle_duration_sec=1.0)

    def result_cb(self, future):
        if future.result().status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info('=== GOAL REACHED! ===')
        else:
            self.get_logger().info('Failed.')


def main(args=None):
    rclpy.init(args=args)
    node = NavigateToGoal()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
