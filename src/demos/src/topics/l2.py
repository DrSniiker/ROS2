import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from std_msgs.msg import String


class L2(Node):
    def __init__(self):
        super().__init__("l2")
        self.sub = self.create_subscription(
            String, "Niklas", self.chatter_callback, 10
        )
        self.sub = self.create_subscription(
            String, "Emil", self.chatter_callback, 10
        )

    def chatter_callback(self, msg):
        self.get_logger().info("I heard: [%s]" % msg.data)


def main(args=None):
    rclpy.init(args=args)
    
    node2 = L2()
    
    try:
        rclpy.spin(node2)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node2.destroy_node()
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()