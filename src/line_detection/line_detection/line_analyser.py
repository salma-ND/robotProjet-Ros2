

import rclpy
from rclpy.node import Node


class LineAnalyser(Node):
    def __init__(self):
        super().__init__('line_analyser')
        self.get_logger().info("line anlyserNode Started")
           

           
def main(args=None):
    rclpy.init(args=args)
    node = LineAnalyser()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
