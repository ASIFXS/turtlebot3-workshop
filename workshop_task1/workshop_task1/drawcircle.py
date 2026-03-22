#!/usr/bin/env python3

# Workshop Task 2 — Draw a Circle
# NAME: ___________________________

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

LINEAR_SPEED  = 0.2   # m/s
ANGULAR_SPEED = 0.0   # rad/s 

# radius = LINEAR_SPEED / ANGULAR_SPEED


class DrawCircle(Node):

    def __init__(self):
        super().__init__('draw_circle')

        #  create a publisher to 'command velocity' with Twist and queue 10
        self.publisher = None

        self.timer = self.create_timer(0.1, self.drive)

    def drive(self):
        msg = Twist()

        msg.linear.x  = 0.0   
        msg.angular.z = 0.0   
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = DrawCircle()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.publisher.publish(Twist())
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()