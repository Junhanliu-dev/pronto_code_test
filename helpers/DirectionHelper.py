from Command import Command
from utils.Direction import Direction


class DirectionHelper:
    """
    Helper class that helps robot turn left or right
    """
    @classmethod
    def turn(cls, current_direction: Direction, instruction: tuple[Command, int]) -> Direction:
        """
        It uses robot`s current direction as base direction, and uses instruction to help the robot towards
        the right direction
        :param current_direction:
        :param instruction:
        :return: The right direction enum
        """
        current_direction_enum_value = current_direction.value
        target_direction: Command = instruction[0]
        steps: int = instruction[1]

        if target_direction is Command.RIGHT:
            total_steps = current_direction_enum_value + steps

            final_direction_value = total_steps % 4

            if final_direction_value == 0:
                return Direction(4)
            else:
                return Direction(final_direction_value)

        if target_direction is Command.LEFT:
            final_steps = current_direction_enum_value - steps

            if final_steps % 4 == 0:
                return Direction(4)

            # the left turn based on deduction of the direction enum. That if the final steps > 0 means
            # the final steps must fall into one of the direction enum values, so that would be the right
            # direction
            if final_steps > 0:
                return Direction(final_steps)

            # transfer the left turn to right turn. For example, if the current direction is East (enum val = 2),
            # the instruction is turn left 3 times, the final steps would be -1, it means we only need to turn right
            # once to get the final direction, South in this case.
            final_direction = current_direction_enum_value + (abs(final_steps)) % 4

            return Direction(final_direction)
