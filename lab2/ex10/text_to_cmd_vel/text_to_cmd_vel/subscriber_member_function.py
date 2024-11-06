import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from math import pi


class TextToCmdVel(Node):

    def __init__(self):
        super().__init__('text_to_cmd_vel')
        self.subscriber = self.create_subscription(
            String,
            'cmd_text',
            self.listener_callback,
            10)
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def listener_callback(self, msg):
        command = msg.data
        twist = Twist()

        if command == "turn_right":
            twist.angular.z = -pi / 2  # negative value to turn right
        elif command == "turn_left":
            twist.angular.z = pi / 2  # positive value to turn left
        elif command == "move_forward":
            twist.linear.x = 2.0  # move forward
        elif command == "move_backward":
            twist.linear.x = -2.0  # move backward
        else:
            self.get_logger().warning(f"Unknown command: {command}")

        self.publisher.publish(twist)
        self.get_logger().info(f'Publishing: "{command}" -> Twist: {twist}')

def main(args=None):
    rclpy.init(args=args)
    text_to_cmd_vel = TextToCmdVel()
    rclpy.spin(text_to_cmd_vel)
    text_to_cmd_vel.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
