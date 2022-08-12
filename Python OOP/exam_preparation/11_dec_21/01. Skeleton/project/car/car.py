from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, model, speed_limit):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False
        self.driver = None

    def __ge__(self, other):
        return self.speed_limit >= other.speed_limit

    def __lt__(self, other):
        return self.speed_limit < other.speed_limit

    @property
    @abstractmethod
    def car_type(self):
        pass

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    @abstractmethod
    def speed_limit(self):
        pass

    @speed_limit.setter
    @abstractmethod
    def speed_limit(self, value):
        pass
