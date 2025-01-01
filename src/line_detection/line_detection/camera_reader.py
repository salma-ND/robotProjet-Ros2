import rclpy
from rclpy.node import Node


class CameraReader(Node):
    def __init__(self):
        super().__init__('camera_reader')
        self.get_logger().info("Camera Reader Node Started")

   

def main(args=None):
    rclpy.init(args=args)
    node = CameraReader()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
