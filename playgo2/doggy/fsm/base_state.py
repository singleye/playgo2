
class BaseState(object):
    """
    BaseState defines the state interface
    """

    def __init__(self):
        pass

    def enter(self):
        """
        This method is called when the state is entered.
        """
        raise NotImplementedError

    def do_action(self):
        """
        This method is called when the state is active.
        """
        raise NotImplementedError

    def leave(self):
        """
        This method is called when the state is exited.
        """
        raise NotImplementedError
