from robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    DEFAULT_ROBOT_WEIGHT = 7

    def eating(self):
        self.weight += 1

    def type(self):
        return "FemaleRobot"

    def __repr__(self):
        return self.type()
