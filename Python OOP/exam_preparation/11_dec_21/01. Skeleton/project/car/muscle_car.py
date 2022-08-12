from project.car.car import Car


class MuscleCar(Car):
    __MINIMUM_LIMIT = 250
    __MAXIMUM_LIMIT = 450

    @property
    def car_type(self):
        return "MuscleCar"

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if value > self.__MAXIMUM_LIMIT or value < self.__MINIMUM_LIMIT:
            raise ValueError(f"Invalid speed limit! Must be between {self.__MINIMUM_LIMIT} and {self.__MAXIMUM_LIMIT}!")
        self.__speed_limit = value
