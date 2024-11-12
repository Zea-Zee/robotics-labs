#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math


class FigureEightNode(Node):
    def __init__(self):
        super().__init__('figure_eight_node')
        self.publisher_ = self.create_publisher(Twist, '/robot/cmd_vel', 10)
        self.timer_period = 0.001  # период таймера в секундах
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

        self.circle_duration = 3.1415
        self.time_elapsed = 0.0
        self.state = 0

    def timer_callback(self):
        twist_msg = Twist()

        if self.state == 0:
            # print(f"first circle")
            twist_msg.linear.x = 2.0
            twist_msg.angular.z = 2.0
        elif self.state == 1:
            # print(f"second circle")
            twist_msg.linear.x = 2.0
            twist_msg.angular.z = -2.0

        self.publisher_.publish(twist_msg)
        
        self.time_elapsed += self.timer_period

        if self.time_elapsed >= self.circle_duration:
            self.time_elapsed = 0.0
            self.state = (self.state + 1) % 2


def main(args=None):
    rclpy.init(args=args)
    node = FigureEightNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
