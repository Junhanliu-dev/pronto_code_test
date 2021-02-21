import unittest

from helpers.DefaultPathFinder import PathFinderHelper
from utils.Coordination import Coordination
from utils.Direction import Direction


class TestPathFinder(unittest.TestCase):

    def test_path_1(self):
        start_coord = Coordination(0, 0)
        current_position: Coordination = Coordination(3, 2)
        current_direction: Direction = Direction.NORTH

        result = PathFinderHelper.find_minimum_path_with_turn_amount(start_coord, current_position, current_direction)
        self.assertEqual(result, 7)

    def test_path_2(self):
        start_coord = Coordination(0, 0)
        current_position: Coordination = Coordination(-2, 2)
        current_direction: Direction = Direction.EAST

        result = PathFinderHelper.find_minimum_path_with_turn_amount(start_coord, current_position, current_direction)
        self.assertEqual(result, 5)

    def test_path_3(self):
        start_coord = Coordination(-5, -4)
        current_coord = Coordination(-2, -2)
        print(PathFinderHelper.find_path(start_coord, current_coord))
