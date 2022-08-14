from abc import ABC, abstractmethod


class Drink(ABC):
    def __init__(self, name, portion, price, brand):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion}ml - {self.price}lv"

    @abstractmethod
    def dummy(self):
        pass
