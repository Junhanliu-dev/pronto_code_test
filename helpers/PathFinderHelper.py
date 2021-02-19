from Robot import Robot
from utils.Coordination import Coordination
from utils.Direction import Direction


class PathFinderHelper:

    @classmethod
    def find_minimum_path_with_turn_amount(cls, start_point: Coordination, current_point: Coordination, current_direction: Direction) -> int:

        if start_point == current_point:
            return 0

        min_turn = min(cls.cost_toward_x_axis(current_point, current_direction),
                       cls.cost_toward_y_axis(current_point, current_direction))

        steps = abs(current_point.x) + abs(current_point.y)

        minimum_path = min_turn + steps + 1

        return minimum_path

    @classmethod
    def cost_toward_x_axis(cls, current_point: Coordination, current_direction: Direction) -> int:
        if current_point.x == 0:
            return 0

        current_direction_value = current_direction.value

        if current_point.x != 0:
            if current_point.y >= 0:
                south_direction_value = Direction.SOUTH.value
                return abs(current_direction_value - south_direction_value)

            if current_point.y < 0:
                north_direction_value = Direction.NORTH.value
                if current_direction is Direction.WEST:
                    return 1
                else:
                    return abs(current_direction_value - north_direction_value)

    @classmethod
    def cost_toward_y_axis(cls, current_point: Coordination, current_direction: Direction) -> int:
        if current_point.y == 0:
            return 0

        current_direction_value = current_direction.value

        if current_point.y != 0:
            if current_point.x >= 0:
                west_direction_value = Direction.WEST.value
                if current_direction_value == Direction.NORTH.value:
                    return 1
                else:
                    return abs(current_direction_value - west_direction_value)

            if current_point.x < 0:
                east_direction_value = Direction.EAST.value
                return abs(current_direction_value - east_direction_value)

    @classmethod
    def find_minimum_path_without_turn(cls, start_point: Coordination, current_point: Coordination) -> int:

        return abs(start_point.x - current_point.x) + abs(start_point.y - current_point.y)

