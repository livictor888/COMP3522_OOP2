""" This module represents the abstract PokedexObject class """
import abc


class PokedexObject(abc.ABC):
    """
    A class to represent the abstract PokedexObject class intended to be extended to concrete types.
    """

    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.id = kwargs["id"]
