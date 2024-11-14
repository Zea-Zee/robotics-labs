import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
import numpy as np
import cv2


class Happy(Node):
    def __init__(self):
        super().__init__('happy')

        self.velocity_publisher = self.create_publisher(
            Twist, '/robot/cmd_vel', 10)

        self.pose_subscriber = self.create_subscription(
            Image, '/depth/image', self.update_pose, 10)
        self.scan = None
        self.timer = self.create_timer(0.01, self.move)

    def update_pose(self, data):
        self.scan = data

    def move(self):
        vel_msg = Twist()

        # Проверка наличия данных глубины
        if self.scan is None or len(self.scan.data) == 0:
            vel_msg.linear.x = 0.0
            self.velocity_publisher.publish(vel_msg)
            return

        try:
            # Конвертируем данные в numpy array
            height = self.scan.height
            width = self.scan.width
            depth_array = np.frombuffer(self.scan.data, dtype=np.float32).reshape((height, width))
            depth_array = np.nan_to_num(depth_array, nan=0.0, posinf=2.0, neginf=0.1)

            # Определяем области:
            left_region = depth_array[height // 3: 2 * height // 3, :width // 3]
            center_region = depth_array[height // 3: 2 * height // 3, width // 3: 2 * width // 3]
            right_region = depth_array[height // 3: 2 * height // 3, 2 * width // 3:]

            left_mean_depth = np.mean(left_region)
            center_mean_depth = np.mean(center_region)
            right_mean_depth = np.mean(right_region)

            self.get_logger().info(
                f'Средняя глубина (Левая: {left_mean_depth:.2f}, Центр: {center_mean_depth:.2f}, Правая: {right_mean_depth:.2f})')

            stop_threshold = 0.25  # Остановка при расстоянии < 0.25 метра
            slow_threshold = 1.0  # Замедление, когда ближе 1 метра

            # Если хотя бы в одном из регионов глубина ниже порога остановки
            if (left_mean_depth <= stop_threshold or center_mean_depth <= stop_threshold or right_mean_depth <= stop_threshold):
                vel_msg.linear.x = 0.0
                print(f"Остановка")
            elif (left_mean_depth <= slow_threshold or
                  center_mean_depth <= slow_threshold or
                  right_mean_depth <= slow_threshold):
                # Линейное замедление
                min_depth = min(left_mean_depth, center_mean_depth, right_mean_depth)
                vel_msg.linear.x = 1.0 * (min_depth - stop_threshold) / (slow_threshold - stop_threshold)
                print(f"Снижение скорости")
            else:
                vel_msg.linear.x = 1.0  # Максимальная скорость
            vel_msg.angular.z = 0.0
            self.velocity_publisher.publish(vel_msg)

        except Exception as e:
            self.get_logger().error(f"Error processing depth data: {str(e)}")
            vel_msg.linear.x = 0.0
            self.velocity_publisher.publish(vel_msg)


def main(args=None):
    rclpy.init(args=args)
    node = Happy()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
