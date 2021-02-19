import unittest

from Command import Command
from utils.Direction import Direction
from helpers.DirectionHelper import DirectionHelper


class TestDirectionHelper(unittest.TestCase):

    def test_left_turn_1(self):
        current_direction = Direction.EAST
        instruction: tuple[Command, int] = (Command.LEFT, 15)
        self.assertEqual(DirectionHelper.turn(current_direction, instruction), Direction.SOUTH)

    def test_left_turn_2(self):
        current_direction = Direction.WEST
        instruction: tuple[Command, int] = (Command.LEFT, 3)
        self.assertEqual(DirectionHelper.turn(current_direction, instruction), Direction.NORTH)

    def test_left_turn_3(self):
        current_direction = Direction.WEST
        instruction: tuple[Command, int] = (Command.LEFT, 4)
        self.assertEqual(DirectionHelper.turn(current_direction, instruction), Direction.WEST)

    def test_right_turn_1(self):
        current_direction = Direction.WEST
        instruction: tuple[Command, int] = (Command.RIGHT, 2)
        self.assertEqual(DirectionHelper.turn(current_direction, instruction), Direction.EAST)

    def test_right_turn_2(self):
        current_direction = Direction.NORTH
        instruction: tuple[Command, int] = (Command.RIGHT, 20)
        self.assertEqual(DirectionHelper.turn(current_direction, instruction), Direction.NORTH)

    def test_right_turn_3(self):
        current_direction = Direction.EAST
        instruction: tuple[Command, int] = (Command.RIGHT, 1)
        self.assertEqual(DirectionHelper.turn(current_direction, instruction), Direction.SOUTH)