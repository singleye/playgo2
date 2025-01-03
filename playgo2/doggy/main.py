import sys
import argparse

from logger import get_logger
from doggy import Doggy


logger = get_logger(__name__)

def main():
    parser = argparse.ArgumentParser(description='Doggy')
    parser.add_argument('-d', '--domain', type=int, dest='domain', default=0, help='domain id')
    parser.add_argument('-i', '--interface', type=str, dest='interface', help='Network interface to use')
    parser.add_argument('-n', '--name', type=str, default='doggy', dest='name', help='Name of the doggy')
    parser.add_argument('-m', '--mode', type=str, dest='mode', default='normal', help='motion mode: normal, ai, Advanced')
    args = parser.parse_args()

    logger.info(f'name: {args.name}')
    logger.info(f'interface: {args.interface}')
    doggy = Doggy(args.name, args.domain, args.interface)
    doggy.switch_motion_mode(args.mode)
    doggy.play()


if __name__ == '__main__':
    main()
