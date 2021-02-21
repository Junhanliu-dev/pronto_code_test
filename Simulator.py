from Command import Command
from helpers.CommandHelper import CommandHelper
from Robot import Robot
from errors.CommandParsingError import CommandParsingException


class Simulator:
    """
    A robot simulator that takes a robot instance as an input and receive the commands from terminal
    to move the robot.
    """

    def __init__(self, robot: Robot):
        """
        :param robot:
            A robot object in order to let simulator control the robot
        """
        self.robot: Robot = robot

    def start(self):
        """
        start the simulator, it takes commands as input, interprets them and make robot move
        :return:
        It returns robots final position and a list of path for how to get back to its original position (0,0)
        with minimum unit
        """
        print('please enter a string of comma-separated commands to simulate the robot, the case is insensitive (e.g. '
              '`F1,R1,B2,L1,B3`)')

        command_list = self.get_command_input()

        # use split command list to make robot move one by one
        for command in command_list:
            self.robot.move(command)

        # calculate the minimum path count to original position
        min_path = self.robot.find_minimum_path()
        print(f'the minimum path is: {min_path}')

        # returns paths how to get back to original position
        path_list = self.robot.find_way_back()
        print("your current path:" + str(self.robot.current_coordination))
        print("the paths to go back are: " + str(path_list))

    def get_command_input(self) -> list[tuple[Command, int]]:
        """
        the method interprets commands string to each single command
        the method will ensure the commands string are valid, the method will
        keep repeat until the command string is valid
        :return: list of command and steps

        """
        command_input = input('Command:')

        try:
            command_list: list[tuple[Command, int]] = CommandHelper.transform_command(command_input)

            return command_list
        except CommandParsingException as e:
            print('please input a valid command with comma-separated')
            print(e)
            self.get_command_input()
