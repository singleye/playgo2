import time

from logger import get_logger
from .base_state import BaseState


logger = get_logger(__name__)

STATE_STROLL = "stroll"

class StrollState(BaseState):
    """
    Doggy will stroll around.
    """

    def __init__(self):
        super(StrollState, self).__init__()
        self.last_stand = time.time()
        self.stand = False

    def enter(self):
        logger.info("Strolling...")

    def do_action(self, controller):
        now = time.time()
        if now - self.last_stand > 5:
            self.last_stand = now
            self.stand = not self.stand
            if self.stand:
                logger.info("Standing up...")
                controller.standup()
            else:
                logger.info("Standing down...")
                controller.standdown()

    def leave(self):
        logger.info("Leaving stroll state...")
