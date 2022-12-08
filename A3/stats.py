"""This module represents a Stats PokedexObject"""
from pokeretriever.pokedexobject import PokedexObject


class Stats(PokedexObject):
    """
    This class represents a Stats.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_battle_only = None
        self.base_stat = kwargs["base_stat"]

    def set_is_battle_only(self, new_is_battle_only):
        """
        Sets is_battle_only attribute of Stats.
        :param new_is_battle_only: a boolean
        """
        self.is_battle_only = new_is_battle_only

    def __str__(self):
        """
        Returns a nicely formatted string with the details of Stats.
        :return: a string
        """
        return_string = f"\n\tStat Name: {self.name}, Base Stat: {self.base_stat}"

        return_string_expanded = f"\n-------- STATS INFO: --------\n" \
                                 f"Stats Name: {self.name}\n" \
                                 f"Stats ID: {self.id}\n" \
                                 f"Is Battle Only: {self.is_battle_only}\n" \
                                 f"-----------------------------"
        if self.is_battle_only is None:
            return return_string
        else:
            return return_string_expanded
