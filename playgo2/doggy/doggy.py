import signal

from logger import get_logger
from fsm import (
    FSM,
    STATE_STROLL,
)

logger = get_logger(__name__)

class Doggy(object):
    def __init__(self, name, net_interface):
        self.name = name
        self.net_interface = net_interface
        self.fsm = FSM()
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
        self._alive = True

    def signal_handler(self, sig, frame):
        self.stop_play()

    def initialize(self):
        self.fsm.set_state(STATE_STROLL)

    def play(self):
        logger.info(f'{self.name} is playing...')
        self.initialize()
        while self._alive:
            self.fsm.update()

    def stop_play(self):
        logger.info(f'{self.name} stopped playing...')
        self._alive = False
