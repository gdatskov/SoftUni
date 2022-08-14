from abc import ABC, abstractmethod


class BakedFood(ABC):
    def __init__(self, name, portion, price):
        self.name = name
        self.portion = portion
        self.price = price

    def __repr__(self):
        return f" - {self.name}: {self.portion}g - {self.price}lv"

    @abstractmethod
    def dummy(self):
        pass
