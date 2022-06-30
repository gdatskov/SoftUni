from project.pokemon import Pokemon

class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = list()

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        for pok in self.pokemons:
            if pokemon_name == pok.name:
                self.pokemons.remove(pok)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        data = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]
        for pok in self.pokemons:
            data.append(f"- {pok.pokemon_details()}")
        return "\n".join(data)

