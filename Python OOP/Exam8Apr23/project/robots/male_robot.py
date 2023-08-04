from robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    DEFAULT_ROBOT_WEIGHT = 9

    def eating(self):
        self.weight += 3

    def type(self):
        return "MaleRobot"

    def __repr__(self):
        return self.type()