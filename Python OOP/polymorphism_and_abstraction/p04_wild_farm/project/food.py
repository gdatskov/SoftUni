from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def __init__(self, quantity):
        self.quantity = quantity

    @property
    def type(self):
        return self.__class__.__name__


class Vegetable(Food):
    def __init__(self, quantity):
        self.quantity = quantity


class Fruit(Food):
    def __init__(self, quantity):
        self.quantity = quantity


class Meat(Food):
    def __init__(self, quantity):
        self.quantity = quantity


class Seed(Food):
    def __init__(self, quantity):
        self.quantity = quantity


