from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name, weight, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @property
    def animal_type(self):
        return self.__class__.__name__

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass


class Bird(Animal):
    @abstractmethod
    def __init__(self, name, weight, wing_size, food_eaten=0):
        super().__init__(name, weight,food_eaten)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.animal_type} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal):
    @abstractmethod
    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight,food_eaten)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.animal_type} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"