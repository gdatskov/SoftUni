from abc import ABC, abstractmethod


class BaseRobot(ABC):
    DEFAULT_ROBOT_WEIGHT = None

    def __init__(self, name, kind, price, weight=None):
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = self.DEFAULT_ROBOT_WEIGHT if weight is None else weight

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def eating(self):
        pass

    @abstractmethod
    def type(self):
        return

