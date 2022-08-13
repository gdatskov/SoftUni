from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    __DEFAULT_OXYGEN = 70
    __BREATHE = 5

    def __init__(self, name):
        super().__init__(name, self.__DEFAULT_OXYGEN)

    def breathe(self):
        self.oxygen -= self.__BREATHE
