"""This module represents an Ability PokedexObject"""
from pokeretriever.pokedexobject import PokedexObject


class Ability(PokedexObject):
    """
    This class represents an Ability.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.generation = None
        self.effect = None
        self.effect_short = None
        self.pokemon = []

    def set_generation(self, new_generation):
        """
        Sets the generation of the ability.
        :param new_generation: a string
        """
        self.generation = new_generation

    def set_effect(self, new_effect):
        """
        Sets the effect of the ability.
        :param new_effect: a string
        """
        self.effect = new_effect

    def set_short_effect(self, new_effect_short):
        """
        Sets the effect (short) of the ability.
        :param new_effect_short: a string
        """
        self.effect_short = new_effect_short

    def set_pokemon(self, new_pokemon):
        """
        Sets the list of pokemon names that uses this ability.
        :param new_pokemon: a list of pokemon names
        """
        self.pokemon = new_pokemon

    def __str__(self):
        """
        Returns a nicely formatted string with the details of Move
        :return: a string
        """
        return_string = f"\n\tAbility Name: {self.name}"

        return_string_expanded = f"\n------- ABILITY INFO: -------\n" \
                                 f"Ability Name: {self.name}\n" \
                                 f"Ability ID: {self.id}\n" \
                                 f"Generation: {self.generation}\n" \
                                 f"Effect: {self.effect}\n" \
                                 f"Effect (Short): {self.effect_short}\n" \
                                 f"Pokemon: {self.pokemon}\n" \
                                 f"-----------------------------\n"
        if self.generation is None:
            return return_string
        else:
            return return_string_expanded
