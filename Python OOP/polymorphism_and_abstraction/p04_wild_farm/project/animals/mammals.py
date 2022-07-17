from project.animals.animal import Mammal


class Mouse(Mammal):
    FOOD_REQUIREMENT = 0.1

    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if food.type not in ["Vegetable", "Fruit"]:
            return f"{self.animal_type} does not eat {food.type}!"
        total_food_weight = self.FOOD_REQUIREMENT * food.quantity
        self.weight += total_food_weight
        self.food_eaten += food.quantity


class Dog(Mammal):
    FOOD_REQUIREMENT = 0.4

    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if food.type not in ["Meat"]:
            return f"{self.animal_type} does not eat {food.type}!"
        total_food_weight = self.FOOD_REQUIREMENT * food.quantity
        self.weight += total_food_weight
        self.food_eaten += food.quantity


class Cat(Mammal):
    FOOD_REQUIREMENT = 0.3

    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if food.type not in ["Meat"]:
            return f"{self.animal_type} does not eat {food.type}!"
        total_food_weight = self.FOOD_REQUIREMENT * food.quantity
        self.weight += total_food_weight
        self.food_eaten += food.quantity


class Tiger(Mammal):
    FOOD_REQUIREMENT = 1

    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        # if food.type not in ["Meat"]:
        if food.type != "Meat":
            return f"{self.animal_type} does not eat {food.type}!"
        total_food_weight = self.FOOD_REQUIREMENT * food.quantity
        self.weight += total_food_weight
        self.food_eaten += food.quantity



