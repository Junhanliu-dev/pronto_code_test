from enum import Enum


class Command(Enum):
    # turn left 90 deg
    LEFT = 'L'
    # turn right 90 deg
    RIGHT = 'R'
    # forward 1 unit
    FORWARD = 'F'
    # backward 1 unit
    BACKWARD = 'B'