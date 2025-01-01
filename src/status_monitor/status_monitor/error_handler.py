

import rclpy
from rclpy.node import Node

class ErrorHandler(Node):
    def __init__(self):
        super().__init__('error_handler')
        self.get_logger().info("Error Handler est lancé")

def main(args=None):
    rclpy.init(args=args)
    node= ErrorHandler()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
