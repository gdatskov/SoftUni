from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    __MAXIMUM_SPEED = 140
    __SPEED_INCREASE = 3

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        if self.speed + self.__SPEED_INCREASE > self.__MAXIMUM_SPEED:
            self.speed = self.__MAXIMUM_SPEED
        else:
            self.speed += self.__SPEED_INCREASE

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.__MAXIMUM_SPEED:
            raise ValueError("Horse speed is too high!")
        self.__speed = value
