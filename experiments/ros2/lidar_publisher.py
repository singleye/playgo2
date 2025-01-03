import argparse
import sys
import time

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2

from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactoryInitialize
from unitree_sdk2py.idl.sensor_msgs.msg.dds_ import PointCloud2_

TOPIC_RAW = 'rt/utlidar/cloud'
TOPIC_CALIBRATED = 'rt/utlidar/cloud_deskewed'

class LidarPublisher(Node):
    def __init__(self):
        super().__init__('lidar_publisher')
        #self.publisher_ = self.create_publisher(PointCloud2, '/playgo2/rt/utlidar/cloud', 10)
        self.pub = self.create_publisher(PointCloud2, 'topic', 10)

    def dds_msg_callback(self: object, msg: PointCloud2_):
        ros_msg = PointCloud2()
        ros_msg.header.frame_id = 'utlidar'
        ros_msg.height = msg.height_
        ros_msg.width = msg.width_
        ros_msg.fields = msg.fields_
        ros_msg.is_bigendian = msg.is_bigendian_
        ros_msg.point_step = msg.point_step_
        ros_msg.row_step = msg.row_step_
        ros_msg.data = msg.data_
        ros_msg.is_dense = msg.is_dense_

        self.pub.publish(ros_msg)
        #self.publisher_.publish(msg)


def main(ros_args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', type=str, dest='interface', help='network interface')
    parser.add_argument('-d', '--domain', type=int, dest='domain', default=0, help='domain id')
    args = parser.parse_args()

    if not args.interface:
        print(parser.print_help())
        print('Please specify the network interface')
        sys.exit(1)


    ChannelFactoryInitialize(args.domain, args.interface)
    sub = ChannelSubscriber(TOPIC_RAW, PointCloud2_)

    rclpy.init(args=ros_args)
    lidar_publisher = LidarPublisher()
    sub.Init(lidar_publisher.dds_msg_callback, 10)

    rclpy.spin(lidar_publisher)
    lidar_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
