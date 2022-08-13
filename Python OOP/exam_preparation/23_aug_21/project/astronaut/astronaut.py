from abc import ABC, abstractmethod


class Astronaut(ABC):
    __BREATHE = 10

    @abstractmethod
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    def breathe(self):
        self.oxygen -= self.__BREATHE

    def increase_oxygen(self, amount):
        self.oxygen += amount

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value
