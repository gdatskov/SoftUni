from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        for aus in self.astronauts:
            if aus.name == name:
                return aus

    def ready_for_mission(self, oxygen_requirement, number):
        suitable = [a for a in self.astronauts if a.oxygen > oxygen_requirement]
        sorted_astros = sorted([a for a in suitable], key=lambda a: a.oxygen, reverse=True)
        best_pick = sorted_astros[:number]
        return best_pick
