

import rclpy
from rclpy.node import Node

class StatusPublisher(Node):
    def __init__(self):
        super().__init__('status_publisher')
        self.get_logger().info("status publisher Node lancé")

def main(args=None):
    rclpy.init(args=args)
    node = StatusPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
