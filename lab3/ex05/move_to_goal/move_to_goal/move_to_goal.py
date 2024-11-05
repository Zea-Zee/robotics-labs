import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import sys


class MoveToGoalNode(Node):
    def __init__(self, goal_x, goal_y, goal_theta):
        super().__init__('move_to_goal')

        self.goal_x = goal_x
        self.goal_y = goal_y
        self.goal_theta = math.radians(goal_theta)

        self.destinated_spot = False

        # Подписка на текущую позу черепахи
        self.pose_subscription = self.create_subscription(
            Pose, 'turtle1/pose', self.update_pose, 10)
        self.pose = Pose()

        # Публикация в топик для управления скоростью
        self.cmd_vel_publisher = self.create_publisher(
            Twist, 'turtle1/cmd_vel', 10)

        # Частота обновления
        self.timer = self.create_timer(0.01, self.move_to_goal)

    def update_pose(self, msg):
        self.pose = msg

    def normalize_angle(self, angle):
        # Приведение угла в диапазон от -pi до pi
        while angle > math.pi:
            angle -= 2 * math.pi
        while angle < -math.pi:
            angle += 2 * math.pi
        return angle

    def move_to_goal(self):
        msg = Twist()

        if self.destinated_spot is True:
            angle_diff = self.normalize_angle(self.goal_theta - self.pose.theta)
            # print(angle_diff)
            if abs(angle_diff) < 0.01:
                self.destroy_timer(self.timer)
                self.stop()
                return
            self.get_logger().info('Черепаха "поворачивается"')
            distance = 0.0
            angle_coeff = 3.0
        else:
            angle_to_goal = math.atan2(self.goal_y - self.pose.y, self.goal_x - self.pose.x)
            angle_diff = self.normalize_angle(angle_to_goal - self.pose.theta)

            if abs(angle_diff) < 0.01:
                self.get_logger().info('Черепаха "двигается"')
                angle_coeff = 0
                # Рассчитываем расстояние до цели
                distance = math.sqrt((self.goal_x - self.pose.x) ** 2 + (self.goal_y - self.pose.y) ** 2)

                # Порог для остановки по достижении цели
                if distance < 0.005:
                    self.destinated_spot = True
            else:
                self.get_logger().info('Черепаха "прицеливается"')
                angle_coeff = 3
                distance = 0

        msg.linear.x = 2.0 * distance
        msg.angular.z = angle_coeff * angle_diff  # Скорость поворота

        # Публикуем сообщение
        self.cmd_vel_publisher.publish(msg)

    def stop(self):
        # Останавливаем черепаху
        stop_msg = Twist()
        self.cmd_vel_publisher.publish(stop_msg)
        self.get_logger().info("\nЦель достигнута\n")
        cur_theta = math.degrees(self.pose.theta)
        if cur_theta < 0:
            cur_theta += 360
        s = f"\nЧерепаха находися в точке ({self.pose.x};{self.pose.y} и повернута на {cur_theta} градусов)"
        self.get_logger().info(s)
        rclpy.shutdown()

    # def rotate(self):


def main(args=None):
    try:
        rclpy.init(args=args)
        if len(sys.argv) < 4:
            print("Enter x y and theta")
            return

        goal_x = float(sys.argv[1])
        goal_y = float(sys.argv[2])
        goal_theta = float(sys.argv[3])

        # Запуск ноды
        move_to_goal_node = MoveToGoalNode(goal_x, goal_y, goal_theta)

        rclpy.spin(move_to_goal_node)

        move_to_goal_node.destroy_node()
    except KeyboardInterrupt:
        print("Программа завершена пользователем.")
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
