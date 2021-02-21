from utils.Coordination import Coordination
from utils.Direction import Direction


class Position:
    """
    store the coordination and direction the robot has been to.
    """
    def __init__(self, coordination: Coordination, direction: Direction):
        self.coordination: Coordination = coordination
        self.direction: Direction = direction

    def __str__(self):
        return str(self.coordination) + " dir: " + str(self.direction)