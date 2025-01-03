import argparse
import sys
import time

from unitree_sdk2py.core.channel import ChannelFactoryInitialize
from unitree_sdk2py.comm.motion_switcher.motion_switcher_client import MotionSwitcherClient

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', type=str, dest='interface', help='network interface')
    parser.add_argument('-d', '--domain', type=int, dest='domain', default=0, help='domain id')
    parser.add_argument('-m', '--mode', type=str, dest='mode', default='normal', help='motion mode: normal, ai, Advanced')
    args = parser.parse_args()

    if not args.interface:
        print(parser.print_help())
        print('Please specify the network interface')
        sys.exit(1)

    ChannelFactoryInitialize(args.domain, args.interface)

    client = MotionSwitcherClient()
    client.SetTimeout(10.0)
    client.Init()

    #print('Silent statue: ', client.GetSilent())
    print('current mode: ', client.CheckMode())
    print('switching to mode: ', args.mode)

    client.SelectMode(args.mode)
    print('current mode: ', client.CheckMode())
    time.sleep(3)

if __name__ == '__main__':
    main()
