from typing import List
from Command import Command
from helpers.PathFinderHelper import PathFinderHelper
from utils.Coordination import Coordination
from utils.Direction import Direction
from helpers.DirectionHelper import DirectionHelper
from utils.Position import Position


class Robot:
    def __init__(self):
        self.path: List[Position] = []
        self.current_direction: Direction = Direction.EAST
        self.current_coordination: Coordination = Coordination(0, 0)
        self.path.append(Position(self.current_coordination, self.current_direction))

    def move(self, instruction: tuple[Command, int]):
        command = instruction[0]

        if command in (Command.LEFT, Command.RIGHT):
            new_direction: Direction = DirectionHelper.turn(self.current_direction, instruction)
            self.current_direction = new_direction
            new_position = Position(direction=new_direction, coordination=self.current_coordination)
            self.path.append(new_position)
            return

        if command in (Command.FORWARD, Command.BACKWARD):
            command = instruction[0]
            steps = instruction[1]
            new_coordination: Coordination = self.get_new_coordination(command=command, steps=steps)
            self.current_coordination = new_coordination
            new_position = Position(direction=self.current_direction, coordination=new_coordination)
            self.path.append(new_position)
            return

    def get_current_direction(self):
        return self.current_direction

    def get_current_coordination(self):
        return self.current_coordination

    def find_minimum_path(self) -> int:
        start_point = self.path[0].coordination
        current_point = self.current_coordination
        minimum_unit = PathFinderHelper.find_minimum_path_without_turn(start_point, current_point)
        return minimum_unit

    def get_new_coordination(self, command: Command, steps: int) -> Coordination:

        if self.current_direction is Direction.NORTH:
            new_x = self.current_direction.x
            if command is Command.FORWARD:
                new_y = self.current_coordination.y + steps
                return Coordination(new_x, new_y)
            if command is Command.BACKWARD:
                new_y = self.current_coordination.y - steps
                return Coordination(new_x, new_y)
        if self.current_direction is Direction.SOUTH:
            new_x = self.current_coordination.x
            if command is Command.FORWARD:
                new_y = self.current_coordination.y - steps
                return Coordination(new_x, new_y)
            if command is Command.BACKWARD:
                new_y = self.current_coordination.y + steps
                return Coordination(new_x, new_y)
        if self.current_direction is Direction.WEST:
            new_y = self.current_coordination.y
            if command is Command.FORWARD:
                new_x = self.current_coordination.x - steps
                return Coordination(new_x, new_y)
            if command is Command.BACKWARD:
                new_x = self.current_coordination.x + steps
                return Coordination(new_x, new_y)
        if self.current_direction is Direction.EAST:
            new_y = self.current_coordination.y
            if command is Command.FORWARD:
                new_x= self.current_coordination.x + steps
                return Coordination(new_x, new_y)
            if command is Command.BACKWARD:
                new_x = self.current_coordination.x - steps
                return Coordination(new_x, new_y)

    def get_path(self):
        return ", ".join([str("(" + str(p) + ")") for p in self.path])
