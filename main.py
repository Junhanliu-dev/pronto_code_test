

# Press the green button in the gutter to run the script.
from Robot import Robot
from Simulator import Simulator

if __name__ == '__main__':
    robot = Robot()

    simulator = Simulator(robot)

    simulator.start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
