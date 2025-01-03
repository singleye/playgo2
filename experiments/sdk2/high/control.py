import sys
import time
import argparse

from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactoryInitialize
from unitree_sdk2py.go2.sport.sport_client import (
    SportClient
)


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

    client = SportClient()
    client.SetTimeout(10.0)
    client.Init()

    print('Stand up')
    client.StandUp()
    time.sleep(3)

    print('Stand down')
    client.StandDown()
    time.sleep(3)


if __name__ == '__main__':
    main()
