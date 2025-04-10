import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from std_msgs.msg import String


class L1(Node):
    def __init__(self):
        super().__init__("listener")
        self.sub = self.create_subscription(
            String, "Emil", self.chatter_callback, 10
        )

    def chatter_callback(self, msg):
        self.get_logger().info("I heard: [%s]" % msg.data)
        
class L2(Node):
    def __init__(self):
        super().__init__("listener")
        self.sub = self.create_subscription(
            String, "Niklas", self.chatter_callback, 10
        )

    def chatter_callback(self, msg):
        self.get_logger().info("I heard: [%s]" % msg.data)
        
class L3(Node):
    def __init__(self):
        super().__init__("listener")
        self.sub = self.create_subscription(
            String, "Jonas", self.chatter_callback, 10
        )

    def chatter_callback(self, msg):
        self.get_logger().info("I heard: [%s]" % msg.data)


def main(args=None):
    rclpy.init(args=args)

    node1 = L1()
    node2 = L2()
    node3 = L3()
    
    try:
        rclpy.spin(node1)
        rclpy.spin(node2)
        rclpy.spin(node3)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node1.destroy_node()
        node2.destroy_node()
        node3.destroy_node()
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()