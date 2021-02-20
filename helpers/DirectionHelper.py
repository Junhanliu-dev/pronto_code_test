from Command import Command
from utils.Direction import Direction


class DirectionHelper:

    @classmethod
    def turn(cls, current_direction: Direction, instruction: tuple[Command, int]) -> Direction:
        current_direction_enum_value = current_direction.value
        target_direction: Command = instruction[0]
        steps: int = instruction[1]

        if target_direction is Command.RIGHT:
            total_steps = current_direction_enum_value + steps

            if total_steps % 4 == 0:
                return Direction(4)
            else:
                final_direction = total_steps % 4
                return Direction(final_direction)

        if target_direction is Command.LEFT:
            final_steps = current_direction_enum_value - steps

            if final_steps % 4 == 0:
                return Direction(4)

            if final_steps > 0:
                return Direction(final_steps)

            final_direction = current_direction_enum_value + (abs(final_steps)) % 4

            return Direction(final_direction)
