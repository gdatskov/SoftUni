from project.astronaut.astronaut import Astronaut
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.meteorologist import Meteorologist
from project.astronaut_factory import AstronautFactory
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    __OXYGEN_FOR_MISSION = 30
    __ASTRONAUTS_FOR_MISSION = 5

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.unsuccessful_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."
        astro: Astronaut = AstronautFactory.create(astronaut_type, name)
        self.astronaut_repository.add(astro)
        return f"Successfully added {astro.__class__.__name__}: {astro.name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        planet = Planet(name)
        planet.items.extend(items.split(", "))
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {planet.name}."
        pass

    def retire_astronaut(self, name: str):
        astro = self.astronaut_repository.find_by_name(name)
        if astro is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        else:
            self.astronaut_repository.remove(astro)
            return f"Astronaut {astro.name} was retired!"

    def recharge_oxygen(self):
        for astro in self.astronaut_repository.astronauts:
            astro.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet: Planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception("Invalid planet name!")

        mission_team = self.astronaut_repository.ready_for_mission(
            self.__OXYGEN_FOR_MISSION, self.__ASTRONAUTS_FOR_MISSION)

        if len(mission_team) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        participated = 0
        for astro in mission_team:
            if len(planet.items) == 0:
                break
            while astro.oxygen > 0 and len(planet.items) != 0:
                astro.backpack.append(planet.items.pop())
                astro.breathe()
            participated += 1

        if planet.items:
            self.unsuccessful_missions += 1
            return "Mission is not completed."
        else:
            self.successful_missions += 1
            return f"Planet: {planet.name} was explored. " \
                   f"{participated} astronauts participated in collecting items."

    def report(self):
        result = [
            f"{self.successful_missions} successful missions!",
            f"{self.unsuccessful_missions} missions were not completed!",
            "Astronauts' info:"
        ]
        for astro in self.astronaut_repository.astronauts:
            backpack = ', '.join(astro.backpack) if len(astro.backpack) != 0 else "none"
            result.extend([
                f"Name: {astro.name}",
                f"Oxygen: {astro.oxygen}",
                f"Backpack items: {backpack}"
            ])
        return "\n".join(result)
        pass

