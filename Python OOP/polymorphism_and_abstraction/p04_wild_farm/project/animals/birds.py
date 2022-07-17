from project.animals.animal import Bird


class Owl(Bird):
    FOOD_REQUIREMENT = 0.25

    def __init__(self, name, weight, wing_size, food_eaten=0):
        super().__init__(name, weight, wing_size, food_eaten)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if food.type != "Meat":
            return f"{self.animal_type} does not eat {food.type}!"
        total_food_weight = self.FOOD_REQUIREMENT * food.quantity
        self.weight += total_food_weight
        self.food_eaten += food.quantity


class Hen(Bird):
    FOOD_REQUIREMENT = 0.35

    def __init__(self, name, weight, wing_size, food_eaten=0):
        super().__init__(name, weight, wing_size, food_eaten)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        total_food_weight = self.FOOD_REQUIREMENT * food.quantity
        self.weight += total_food_weight
        self.food_eaten += food.quantity


