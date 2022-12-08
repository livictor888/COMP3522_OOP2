"""This module represents a Move PokedexObject"""
from pokeretriever.pokedexobject import PokedexObject


class Move(PokedexObject):
    """
    This class represents a Move.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.generation = None
        self.accuracy = None
        self.pp = None
        self.power = None
        self.type = None
        self.damage_class = None
        self.effect_short = None
        self.level_learned_at = None

    def set_generation(self, new_generation):
        """
        Sets the generation of the move.
        :param new_generation: a string
        """
        self.generation = new_generation

    def set_accuracy(self, new_accuracy):
        """
        Sets the accuracy of the move.
        :param new_accuracy: an int
        """
        self.accuracy = new_accuracy

    def set_pp(self, new_pp):
        """
        Sets the pp of the move.
        :param new_pp: an int
        """
        self.pp = new_pp

    def set_power(self, new_power):
        """
        Sets the power of the move.
        :param new_power: an int
        """
        self.power = new_power

    def set_type(self, new_type):
        """
        Sets the type of the move.
        :param new_type: a string
        """
        self.type = new_type

    def set_damage_class(self, new_damage_class):
        """
        Sets the damage class of the move.
        :param new_damage_class:
        :return:
        """
        self.damage_class = new_damage_class

    def set_short_effect(self, new_effect_short):
        """
        Sets the effect (short) of the move.
        :param new_effect_short: a string
        """
        self.effect_short = new_effect_short

    def set_level_learned_at(self, new_level_learned_at):
        """
        Sets the level learned at of the move.
        :param new_level_learned_at: a string
        """
        self.level_learned_at = new_level_learned_at

    def set_level_learned_at_to_none(self):
        """
        Sets level learned at to None (for controlling what string to return in __str__).
        """
        self.level_learned_at = None

    def __str__(self):
        """
        Returns a nicely formatted string with the details of Move
        :return: a string
        """
        return_string = f"\n\tMove Name: {self.name}, Level Learned At: {self.level_learned_at}"
        return_string_expanded = f"\n-------- MOVE INFO: --------\n" \
                                 f"Move Name: {self.name}\n" \
                                 f"Move ID: {self.id}\n" \
                                 f"Generation: {self.generation}\n" \
                                 f"Accuracy: {self.accuracy}\n" \
                                 f"PP: {self.pp}\n" \
                                 f"Power: {self.power}\n" \
                                 f"Type: {self.type}\n" \
                                 f"Damage Class: {self.damage_class}\n" \
                                 f"Effect (Short): {self.effect_short}\n" \
                                 f"-----------------------------\n"
        if self.level_learned_at is None:
            return return_string_expanded
        else:
            return return_string
