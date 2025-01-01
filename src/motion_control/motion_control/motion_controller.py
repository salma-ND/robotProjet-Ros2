

import rclpy
from rclpy.node import Node


class MotionController(Node):
    def __init__(self):
        super().__init__('motion_controller')
        self.get_logger().info("Motion Controller lancé")
        
def main(args=None):
    rclpy.init(args=args)
    node = MotionController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
