# This file contains the AttractState class, which is a subclass of BaseState.

from logger import get_logger
from .base_state import BaseState


logger = get_logger(__name__)

STATE_ATTRACT = "attract"

class AttractState(BaseState):
    """
    Doggy will try to attract the player's attention.
    """

    def __init__(self):
        super(AttractState, self).__init__()

    def enter(self):
        logger("Entering attract state...")

    def do_action(self):
        logger("Attracting...")

    def leave(self):
        logger("Leaving attract state...")
