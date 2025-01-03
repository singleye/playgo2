import argparse
import sys
import time

from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactoryInitialize
from unitree_sdk2py.idl.sensor_msgs.msg.dds_ import PointCloud2_
from unitree_sdk2py.idl.unitree_go.msg.dds_ import LowState_

def build_message_map():
    message_map = {}
    message_map['LowState'] = {'type': LowState_, 'topic': 'rt/lowstate'}
    message_map['PointCloud2'] = {'type': PointCloud2_, 'topic': 'rt/utlidar/cloud'}
    return message_map


def PointCloud2Callback(msg: PointCloud2_):
    print('PointCloud2_ received:', msg)

def msg_callback(msg):
    print(f'{msg}')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', type=str, dest='interface', help='network interface')
    parser.add_argument('-d', '--domain', type=int, dest='domain', default=0, help='domain id')
    parser.add_argument('-t', '--topic', type=str, dest='topic', help='topic to be subscribed to')
    parser.add_argument('-m', '--message', type=str, dest='message', help='message type of the topic to be subscribed to')
    parser.add_argument('-s', '--show', action='store_true', dest='show', default=False, help='show the message map')
    args = parser.parse_args()

    message_map = build_message_map()
    if args.show:
        for key, value in message_map.items():
            print(f'{key}')
        sys.exit(0)

    if not args.interface:
        print(parser.print_help())
        print('Please specify the network interface')
        sys.exit(1)

    ChannelFactoryInitialize(args.domain, args.interface)

    msg = message_map[args.message]
    sub = ChannelSubscriber(msg['topic'], msg['type'])
    sub.Init(msg_callback, 10)
    while True:
        time.sleep(3)


if __name__ == '__main__':
    main()
