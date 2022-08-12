from collections import deque

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    __VALID_CAR_TYPES = ["MuscleCar", "SportsCar"]

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car_exists = self.__get_car_by_name(model)
        if car_exists:
            raise Exception(f"Car {model} is already created!")
        if car_type in self.__VALID_CAR_TYPES:
            car = None
            if car_type == "MuscleCar":
                car = MuscleCar(model, speed_limit)
            if car_type == "SportsCar":
                car = SportsCar(model, speed_limit)
            if car is not None:
                self.cars.append(car)
                return f"{car.car_type} {car.model} is created."

    def create_driver(self, driver_name: str):  # OK ?
        driver_exists = self.__get_driver_by_name(driver_name)
        if driver_exists:
            raise Exception("Driver {driver_name} is already created!")
        driver = Driver(driver_name)
        if driver is not None:
            self.drivers.append(driver)
            return f"Driver {driver.name} is created."

    def create_race(self, race_name: str):  # OK
        race_exists = self.__get_race_by_name(race_name)
        if race_exists:
            raise Exception("Race {race_name} is already created!")
        race = Race(race_name)
        if race is not None:
            self.races.append(race)
            return f"Race {race.name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):   # Wrong answer x1
        driver = self.__get_driver_by_name(driver_name)

        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        for idx in range(1, len(self.cars)+1):
            car: Car = self.cars[-idx]
            if car.car_type == car_type and not car.is_taken:
                car.is_taken = True
                driver = self.__get_driver_by_name(driver_name)
                if driver.car is not None:
                    old_car = driver.car
                    old_car.driver = None
                    old_car.is_taken = False
                    driver.car = car
                    car.driver = driver
                    return f"Driver {driver_name} changed his car from {old_car.model} to {car.model}."
                else:
                    driver.car = car
                    car.driver = driver
                    return f"Driver {driver_name} chose the car {car.model}."
        raise Exception(f"Car {car_type} could not be found!")


    def add_driver_to_race(self, race_name: str, driver_name: str):
        driver = self.__get_driver_by_name(driver_name)
        race = self.__get_race_by_name(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        elif not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        elif driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        elif driver in self.races:
            return f"Driver {driver_name} is already added in {race_name} race."
        else:
            self.races.append(driver)
            race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."
        # pass

    def start_race(self, race_name: str):
        race = self.__get_race_by_name(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        return_message_list = []
        fastest_three = sorted(self.cars, reverse=True)[:3]
        for car in fastest_three:
            car.driver.number_of_wins += 1
            return_message_list.append(
                f"Driver {car.driver.name} wins the {race_name} race with a speed of {car.speed_limit}.")
        return "\n".join(return_message_list)
        # pass

    def __get_driver_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver

    def __get_race_by_name(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race

    def __get_car_by_name(self, car_name):
        for car in self.cars:
            if car.model == car_name:
                return car


controller = Controller()
print(controller.create_driver("asd"))

