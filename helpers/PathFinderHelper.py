from Robot import Robot
from utils.Coordination import Coordination
from utils.Direction import Direction


class PathFinderHelper:

    @classmethod
    def find_minimum_path(cls, robot: Robot) -> int:
        starting_point: Coordination = robot.path[0].coordination
        current_point: Coordination = robot.current_coordination
        if starting_point == current_point:
            return 0



        return 0

    def cost_toward_x(self, current_point: Coordination, direction: Direction) -> int:

        if current_point.x != 0 and current_point.y > 0:
            current_direction_value = direction.value
            south_direction_value = Direction.SOUTH.value
            return abs(current_direction_value - south_direction_value)