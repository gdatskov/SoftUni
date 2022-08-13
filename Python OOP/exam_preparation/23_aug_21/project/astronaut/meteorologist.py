from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    __DEFAULT_OXYGEN = 90
    __BREATHE = 15

    def __init__(self, name):
        super().__init__(name, self.__DEFAULT_OXYGEN)

    def breathe(self):
        self.oxygen -= self.__BREATHE