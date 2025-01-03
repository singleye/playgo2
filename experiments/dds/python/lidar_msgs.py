import argparse
import sys
import time

from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactoryInitialize
from unitree_sdk2py.idl.sensor_msgs.msg.dds_ import PointCloud2_

TOPIC_RAW = 'rt/utlidar/cloud'
TOPIC_CALIBRATED = 'rt/utlidar/cloud_deskewed'

def PointCloud2Callback(msg: PointCloud2_):
    print('PointCloud2_ received:', msg)

def main():
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
    sub.Init(PointCloud2Callback, 10)
    while True:
        time.sleep(3)


if __name__ == '__main__':
    main()
