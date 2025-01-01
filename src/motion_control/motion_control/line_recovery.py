

import rclpy
from rclpy.node import Node

class LineRecovery(Node):
    def __init__(self):
         super().__init__('line_recovery')
         self.get_logger().info("line Recovery Node lancé")

def main(args=None):
    rclpy.init(args=args)
    node = LineRecovery()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
