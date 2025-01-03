import signal

from unitree_sdk2py.core.channel import ChannelFactoryInitialize
from unitree_sdk2py.comm.motion_switcher.motion_switcher_client import MotionSwitcherClient

from logger import get_logger
from fsm import (
    FSM,
    STATE_STROLL,
)
from control import Controller

logger = get_logger(__name__)

class Doggy(object):
    def __init__(self: object, name: str, domain_id: int, net_interface: str):
        self.name = name
        self.domain_id = domain_id
        self.net_interface = net_interface
        ChannelFactoryInitialize(self.domain_id, self.net_interface)
        self.controller = Controller()
        self.fsm = FSM(self.controller)
        self.fsm.set_state(STATE_STROLL)
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
        self._alive = True

    def signal_handler(self: object, sig: int, frame: object) -> None:
        self.stop_play()

    def switch_motion_mode(self, mode: str) -> None:
        """
        switch motion mode
        * normal: normal mode
        * ai: ai mode
        * advanced: advanced mode
        """
        if mode not in ['normal', 'ai', 'advanced']:
            logger.error(f'Invalid motion mode: {mode}')
            return
        switcher = MotionSwitcherClient()
        logger.info(f'Switching motion to {mode} mode...')
        switcher.SelectMode(mode)

    def play(self: object) -> None:
        logger.info(f'{self.name} is playing...')
        while self._alive:
            self.fsm.update()

    def stop_play(self: object) -> None:
        logger.info(f'{self.name} stopped playing...')
        self._alive = False
