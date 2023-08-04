from abc import ABC, abstractmethod


class BaseService(ABC):
    SERVICE_MINIMUM_CAPACITY = 1
    SERVICE_DEFAULT_CAPACITY = SERVICE_MINIMUM_CAPACITY

    def __init__(self, name, capacity=None):
        self.name = name
        self.capacity = self.SERVICE_DEFAULT_CAPACITY if capacity is None else capacity
        self.robots = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value is not str and value.strip() == "":
            raise Exception("Service name cannot be empty!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value is not int and value <= self.SERVICE_MINIMUM_CAPACITY:
            raise Exception(f"Service capacity cannot be less than or equal to {self.SERVICE_MINIMUM_CAPACITY}!")
        self.__capacity = value

    @property
    def capacity_reached(self):
        return len(self.robots) >= self.__capacity

    @abstractmethod
    def details(self):
        pass

    @abstractmethod
    def type(self):
        pass
