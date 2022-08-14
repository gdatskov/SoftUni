from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water


class Bakery:
    # add as object (Food Child object), do not call
    __FOODS = {
        "Bread": Bread,
        "Cake": Cake
    }
    __DRINKS = {
        "Tea": Tea,
        "Water": Water
    }

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    def add_food(self, food_type, name, price):
        food_name = self.__get_food_object_by_name(name)
        if food_name not in self.__FOODS:
            food = self.__FOODS[food_type](name, price)
            self.food_menu.append(food)
            return f"Added {food.name} ({food.__class__.__name__}) to the food menu"
        else:
            return f"{food_type} {name} is already in the menu!"    # Something smelly here

    def add_drink(self, drink_type, name, portion, brand):
        drink_name = self.__get_drink_object_by_name(name)
        if drink_name not in self.__DRINKS:
            drink = self.__DRINKS[drink_type](name, portion, brand)
            self.drinks_menu.append(drink)
            return f"Added {drink.name} ({drink.brand}) to the drink menu"
        else:
            return f"{drink_type} {name} is already in the menu!"   # Something smelly here

    def add_table(self, table_type, table_number, capacity):
        table = self.__get_table_object_by_number(table_number)

    def __get_food_object_by_name(self, food_name):
        for food in self.food_menu:
            if food.name == food_name:
                return food.__class__.__name__

    def __get_drink_object_by_name(self, drink_name):
        for drink in self.drinks_menu:
            if drink.name == drink_name:
                return drink.__class__.__name__

    def __get_table_object_by_number(self, table_number):
        for table in self.tables_repository:
            if table.name == table_number:
                return table.__class__.__name__


bakery = Bakery("Pri Gosho's")
print(bakery.add_food("Bread", "French", 1))
print(bakery.add_food("Bread", "French", 1))
print(bakery.add_drink("Water", "Holy water", 330, "Perrier"))
print(bakery.add_drink("Water", "Holy water", 330, "Perrier"))
