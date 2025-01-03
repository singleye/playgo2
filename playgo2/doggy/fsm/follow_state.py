# Description: This file contains the FollowState class, which is a subclass of the BaseState class.

from logger import get_logger
from .base_state import BaseState


logger = get_logger(__name__)

STATE_FOLLOW = "follow"

class FollowState(BaseState):
    """
    Doggy will follow the player.
    """

    def __init__(self):
        super(FollowState, self).__init__()

    def enter(self):
        logger("Entering follow state...")

    def do_action(self, controller):
        logger("Following...")

    def leave(self):
        logger("Leaving follow state...")
