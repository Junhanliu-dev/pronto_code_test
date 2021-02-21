from helpers.PathFinderBase import PathFinderBase
from utils.Coordination import Coordination
from utils.Direction import Direction


class DefaultPathFinder(PathFinderBase):

    """
    Helper class to help robot find way back
    """
    @classmethod
    def find_minimum_path_with_turn_amount(cls, start_point: Coordination,
                                           current_point: Coordination,
                                           current_direction: Direction) -> int:
        """
        Calculate how many turns are needed in order to go back to the original coordination
        :param start_point:
        :param current_point:
        :param current_direction:
        :return: The total number of turns needed to go back its start coordination
        """

        if start_point == current_point:
            return 0

        # To decide the robot heading to x axis first or y axis, with minimum turn
        min_turn = min(cls.cost_toward_x_axis(current_point, current_direction),
                       cls.cost_toward_y_axis(current_point, current_direction))

        # in the coordinate axis, the shortest steps between two coordinates is units to x axis plus units to y axis,
        # without go diagonally
        steps = abs(current_point.x) + abs(current_point.y)

        # + 1 is the final turn toward the original coordination
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
    def find_minimum_path_cost(cls, start_point: Coordination, current_point: Coordination) -> int:
        """
        The example, provided by the code challenge mark down file, indicates that the minimum cost turning back
        to original position excludes the turning cost, so the minimum steps to original coordination is the distance
        x axis + y axis distance between two points
        :param start_point:
        :param current_point:
        :return:
        """
        return abs(start_point.x - current_point.x) + abs(start_point.y - current_point.y)

    @classmethod
    def find_path(cls, start_point: Coordination, current_position: Coordination):
        return cls.find_path_recursion(start_point, current_position)

    @classmethod
    def find_path_recursion(cls, start_point: Coordination, current_point: Coordination,
                            path_list: list[Coordination] = None):
        """
        Using recursion style.
        list each coordination that robot should step, in order to go back with minimum effort.
        :param start_point:
        :param current_point:
        :param path_list:
        :return:
        """
        if path_list is None:
            path_list = [current_point]

        # the robot will keep going parallel to x-axis until it hits the x point of the start point
        if current_point.x != start_point.x:
            next_y = current_point.y

            if current_point.x > start_point.x:
                next_x = current_point.x - 1
            else:
                next_x = current_point.x + 1

            next_coordination = Coordination(next_x, next_y)
            path_list.append(next_coordination)
            cls.find_path_recursion(start_point=start_point, current_point=next_coordination, path_list=path_list)

        # the robot will keep going parallel to y-axis until it hits the y point of the start point
        elif current_point.y != start_point.y:
            next_x = current_point.x

            if current_point.y > start_point.y:
                next_y = current_point.y - 1
            else:
                next_y = current_point.y + 1

            next_coordination = Coordination(next_x, next_y)
            path_list.append(next_coordination)
            cls.find_path_recursion(start_point=start_point, current_point=next_coordination, path_list=path_list)

        return path_list
