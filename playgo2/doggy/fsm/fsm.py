# Description: Finite State Machine class for the robot


from logger import get_logger
from .attract_state import AttractState, STATE_ATTRACT
from .follow_state import FollowState, STATE_FOLLOW
from .stroll_state import StrollState, STATE_STROLL


logger = get_logger(__name__)

class FSM(object):
    def __init__(self: object, controller: object) -> None:
        self.states = {
                STATE_ATTRACT: AttractState(),
                STATE_FOLLOW: FollowState(),
                STATE_STROLL: StrollState(),
            }
        self.cur_state = None
        self.controller = controller

    def set_state(self: object, state: str) -> None:
        """
        Set the current state of the FSM.
        May raise KeyError if the state is not found.
        """
        self.cur_state = self.states.get(state)

    def get_state(self: object) -> str:
        return self.cur_state

    def update(self: object) -> None:
        """
        Update the current state.
        """
        self.cur_state.do_action(self.controller)
