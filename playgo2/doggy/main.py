import sys
import argparse

from logger import get_logger
from doggy import Doggy


logger = get_logger(__name__)

def main():
    parser = argparse.ArgumentParser(description='Doggy')
    parser.add_argument('-i', '--interface', type=str, dest='interface', help='Network interface to use')
    parser.add_argument('-n', '--name', type=str, default='doggy', dest='name', help='Name of the doggy')
    args = parser.parse_args()

    logger.info(f'name: {args.name}')
    logger.info(f'interface: {args.interface}')
    doggy = Doggy(args.name, args.interface)
    doggy.play()


if __name__ == '__main__':
    main()
