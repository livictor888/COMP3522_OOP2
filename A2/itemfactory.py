"""This module defines Holiday-themed factories"""
import abc
from toys import Toys
from stuffedanimals import StuffedAnimals
from candy import Candy


class ItemFactory(abc.ABC):
    """
    The base factory class. All factories expect this factory class to
    create their items. The ItemFactory class defines an interface
    to create an Item family consisting of Toys, Stuffed Animals,
    and Candy. These vary by holiday season.
    """

    @abc.abstractmethod
    def create_toys(self, **kwargs) -> Toys:
        """
        Returns Toys.
        """
        pass

    @abc.abstractmethod
    def create_stuffed_animals(self, **kwargs) -> StuffedAnimals:
        """
        Returns StuffedAnimals.
        """
        pass

    @abc.abstractmethod
    def create_candy(self, **kwargs) -> Candy:
        """
        Returns Candy.
        """
        pass
