from project.space_station import SpaceStation

station = SpaceStation()
print(station.add_astronaut("Biologist", "Pesho"))
print(station.add_astronaut("Meteorologist", "Gosho"))
# print(station.add_astronaut("asdasd", "Maria"))
# print(station.add_astronaut("Geodesist", "Maria"))
print(station.add_astronaut("Geodesist", "Maria"))
print(station.add_astronaut("Biologist", "Alex"))
print(*[(x.name, x.oxygen) for x in station.astronaut_repository.astronauts], sep=", ")
print(station.recharge_oxygen())
print(*[(x.name, x.oxygen) for x in station.astronaut_repository.astronauts], sep=", ")
print(station.retire_astronaut("Pesho"))
print(*[(x.name, x.oxygen) for x in station.astronaut_repository.astronauts], sep=", ")
print(station.add_planet("Saturn", "asdasd, asda, asda, asdas, as, asdas, asdw, qwd, dqw, q, wd, qwd, qwd, dqw, qw"))
# print(station.add_planet("Saturn", ""))
print(station.send_on_mission("Saturn"))
print(station.report())