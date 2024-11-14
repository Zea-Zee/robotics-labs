import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import numpy as np
import cv2

class DepthStreamer(Node):
    def __init__(self):
        super().__init__('depth_streamer')
        self.subscription = self.create_subscription(
            Image,
            '/depth/image',
            self.image_callback,
            10
        )
        self.get_logger().info("DepthStreamer node has been started")

    def image_callback(self, msg):
        try:
            # Получаем размеры изображения из сообщения
            height = msg.height
            width = msg.width
            step = msg.step

            # Проверка размера данных
            data_size = len(msg.data)
            expected_size = height * width * 4  # 4 байта на пиксель (float32)
            if data_size != expected_size:
                self.get_logger().error(f"Data size does not match expected size: {data_size} != {expected_size}")
                return

            # Преобразуем данные изображения в numpy array (тип данных float32)
            depth_image = np.frombuffer(msg.data, dtype=np.float32).reshape((height, width))

            # Нормализуем изображение для отображения
            depth_display = cv2.normalize(depth_image, None, 0, 255, cv2.NORM_MINMAX)
            depth_display = np.uint8(depth_display)

            # Отображаем изображение глубины
            cv2.imshow("Depth Camera", depth_display)
            cv2.waitKey(1)

        except Exception as e:
            self.get_logger().error(f"Error processing depth image: {str(e)}")

def main(args=None):
    rclpy.init(args=args)
    node = DepthStreamer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("Shutting down depth streamer...")
    finally:
        node.destroy_node()
        rclpy.shutdown()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
