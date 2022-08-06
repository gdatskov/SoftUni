from project.player import Player
from project.supply.supply import Supply
from project.supply.food import Food
from project.supply.drink import Drink


class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args: Player):
        successfully_added = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                successfully_added.append(player.name)
        return f"Successfully added: {', '.join(successfully_added)}"

    def add_supply(self, *args: Supply):
        [self.supplies.append(x) for x in args]

    def __get_player_by_name(self, player_name: str):
        for player in self.players:
            if player.name == player_name:
                return player

    def __get_last_supply_of_given_type(self, supply_type: str):
        for idx in range(-1, -len(self.supplies), -1):
            if self.supplies[idx].__class__.__name__ == supply_type:
                return idx

    def sustain(self, player_name: str, sustenance_type: str):

        player = self.__get_player_by_name(player_name)
        available_supply_idx = self.__get_last_supply_of_given_type(sustenance_type)

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."
        if player is None:
            return
        if sustenance_type not in ["Food", "Drink"]:
            return
        if not available_supply_idx:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        available_supply = self.supplies.pop(available_supply_idx)
        total_stamina_increase = available_supply.energy + player.stamina
        if total_stamina_increase > 100:
            player.stamina = 100
        else:
            player.stamina = total_stamina_increase

        return f"{player_name} sustained successfully with {available_supply.name}."

    @staticmethod
    def __check_players_can_duel(*players):
        result = []
        for player in players:
            if player.stamina == 0:
                result.append(f"Player {player.name} does not have enough stamina.")
        return result

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__get_player_by_name(first_player_name)
        second_player = self.__get_player_by_name(second_player_name)

        players = [first_player, second_player]
        attack_order = sorted(players, key=lambda x: x.stamina)

        cannot_fight = self.__check_players_can_duel(*players)
        if cannot_fight:
            return '\n'.join(cannot_fight)

        for player_turn in range(len(players)):
            this_player, other_player = attack_order
            other_player.stamina -= this_player.stamina / 2
            winner: Player = sorted(players, key=lambda x: -x.stamina)[0]
            if other_player.stamina <= 0:
                other_player.stamina = 0
                return f"Winner: {winner.name}"
            attack_order = [other_player, this_player]
        if winner:
            return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            next_day_stamina = player.stamina - player.age * 2
            if next_day_stamina < 0:
                player.stamina = 0
            elif next_day_stamina > 100:
                player.stamina = 100
            else:
                player.stamina = next_day_stamina
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")
        pass

    def __str__(self):
        result = [
            f"Player: {player.name}, {player.age}, {player.stamina}, "
            f"{player.need_sustenance}" for player in self.players]
        result.extend([
            f"{supply.__class__.__name__}: {supply.name}, {supply.energy}" for supply in self.supplies
        ])
        return "\n".join(result)

