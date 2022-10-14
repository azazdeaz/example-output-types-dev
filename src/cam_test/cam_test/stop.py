import rclpy
from rclpy.node import Node

def main(args=None):

    print("??1")
    rclpy.init(args=args)
    node = Node('my_node_name')
    print("??")
    rclpy.spin_once(node, timeout_sec=15)
    node.get_logger().debug("Stopping.............")
    rclpy.shutdown()
if __name__ == '__main__':
    main()