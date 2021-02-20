from Command import Command
from helpers.CommandHelper import CommandHelper
from Robot import Robot
from errors.CommandParsingError import CommandParsingException


class Simulator:
    def __init__(self, robot: Robot):
        self.robot: Robot = robot

    def start(self):
        print('please enter a string of comma-separated commands to simulate the robot, the case is insensitive (e.g. '
              '`F1,R1,B2,L1,B3`)')

        command_list = self.get_command_input()

        for command in command_list:
            self.robot.move(command)

        min_path = self.robot.find_minimum_path()
        print(f'the minimum path is: {min_path}')

    def get_command_input(self) -> list[tuple[Command, int]]:
        command_input = input('Command:')

        try:
            command_list: list[tuple[Command, int]] = CommandHelper.transform_command(command_input)

            return command_list
        except CommandParsingException as e:
            print('please input a valid command with comma-separated')
            print(e)
            self.get_command_input()
