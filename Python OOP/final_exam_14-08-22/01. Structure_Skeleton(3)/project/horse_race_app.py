from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if self.__get_horse_by_name(horse_name) is not None:
            raise Exception(f"Horse {horse_name} has been already added!")
        if horse_type not in ["Appaloosa", "Thoroughbred"]:
            return
        if horse_type == "Appaloosa":
            self.horses.append(Appaloosa(horse_name, horse_speed))
        if horse_type == "Thoroughbred":
            self.horses.append(Thoroughbred(horse_name, horse_speed))
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.__get_jockey_by_name(jockey_name) is not None:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        self.jockeys.append(Jockey(jockey_name,age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self.__get_race_by_type(race_type) is not None:
            raise Exception(f"Race {race_type} has been already created!")
        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__get_jockey_by_name(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horse = self.__get_horse_by_type(horse_type)
        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey.name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.__get_race_by_type(race_type)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.__get_jockey_by_name(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.__get_race_by_type(race_type)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = sorted(race.jockeys, key=lambda jockey: -jockey.horse.speed)[0]

        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h" \
               f" is {winner.name}! Winner's horse: {winner.horse.name}."

    def __get_horse_by_type(self, horse_type):
        for idx in range(1, len(self.horses)+1):
            horse = self.horses[-idx]
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                return horse

    def __get_horse_by_name(self, name):
        for horse in self.horses:
            if horse.name == name:
                return horse

    def __get_jockey_by_name(self, name):
        for jockey in self.jockeys:
            if jockey.name == name:
                return jockey

    def __get_race_by_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race

