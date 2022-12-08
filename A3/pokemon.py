"""This module represents a Pokemon PokedexObject"""
from pokeretriever.pokedexobject import PokedexObject


class Pokemon(PokedexObject):
    """
    This class represents a Pokemon.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = kwargs["height"]
        self.weight = kwargs["weight"]
        self.stats = []
        self.types = kwargs["types"]
        self.abilities = []
        self.moves = []

    def add_stat(self, *args):
        """
        Adds a Stats to the stats list
        :param args: a Stats object
        """
        for stat in args:
            self.stats.append(stat)

    def add_ability(self, *args):
        """
        Adds an Ability to the abilities list
        :param args: an Ability object
        """
        for ability in args:
            self.abilities.append(ability)

    def add_move(self, *args):
        """
        Adds a Move to the moves list
        :param args: a Move object
        """
        for move in args:
            self.moves.append(move)

    def __str__(self):
        """
        Returns a nicely formatted string with the details of Move
        :return: a string
        """
        stats_string = ""
        for stat in self.stats:
            stat_string = stat.__str__()
            stats_string += stat_string + "\n"

        abilities_string = ""
        for ability in self.abilities:
            ability_string = ability.__str__()
            abilities_string += ability_string + "\n"

        moves_string = ""
        for move in self.moves:
            move_string = move.__str__()
            moves_string += move_string + "\n"

        returned_string = f"\n------- POKEMON INFO: -------\n" \
                          f"Pokemon Name: {self.name}\n" \
                          f"Pokemon ID: {self.id}\n" \
                          f"Height: {self.height} decimetres\n" \
                          f"Weight: {self.weight} hectograms\n" \
                          f"Types: {self.types}\n" \
                          f"Stats: {stats_string}\n" \
                          f"Abilities: {abilities_string}\n" \
                          f"Moves: {moves_string}\n" \
                          f"-----------------------------"

        return returned_string
