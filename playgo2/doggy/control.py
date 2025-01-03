

from unitree_sdk2py.go2.sport.sport_client import SportClient

class Controller(object):
    def __init__(self: object) -> None:
        self.client = SportClient()
        self.client.SetTimeout(10.0)
        self.client.Init()

    def standup(self: object) -> None:
        self.client.StandUp()

    def standdown(self: object) -> None:
        self.client.StandDown()
