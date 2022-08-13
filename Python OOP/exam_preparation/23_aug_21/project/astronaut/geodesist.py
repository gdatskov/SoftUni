from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    __DEFAULT_OXYGEN = 50
    __BREATHE = 10

    def __init__(self, name):
        super().__init__(name, self.__DEFAULT_OXYGEN)

    def breathe(self):
        self.oxygen -= self.__BREATHE
