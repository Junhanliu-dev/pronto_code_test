

# Press the green button in the gutter to run the script.
from Robot import Robot
from Simulator import Simulator
from helpers.DefaultPathFinder import DefaultPathFinder

if __name__ == '__main__':
    robot = Robot()

    simulator = Simulator(robot, DefaultPathFinder)

    simulator.start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
