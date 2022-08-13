from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist


class AstronautFactory:

    @staticmethod
    def create(astronaut_type, name):
        try:
            astronauts = {
                "Biologist": Biologist(name),
                "Geodesist": Geodesist(name),
                "Meteorologist": Meteorologist(name)
            }
            return astronauts[astronaut_type]

        except:
            raise Exception("Astronaut type is not valid!")
