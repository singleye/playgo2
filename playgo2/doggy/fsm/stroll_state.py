
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

    def enter(self):
        logger.info("Strolling...")

    def do_action(self):
        logger.info("Still strolling...")

    def leave(self):
        logger.info("Leaving stroll state...")
