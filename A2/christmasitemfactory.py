"""This module defines a Christmas Item Factory"""
from itemfactory import ItemFactory
from santasworkshop import SantasWorkshop
from reindeer import Reindeer
from candycanes import CandyCanes
from toys import Toys
from stuffedanimals import StuffedAnimals
from candy import Candy


class ChristmasItemFactory(ItemFactory):
    """
    This factory class implements the ItemFactory Interface. It
    returns an Item family consisting of SantasWorkshop, Reindeer,
    and CandyCanes
    """

    def create_toys(self, **kwargs) -> Toys:
        """
        :return: a SantasWorkshop.
        """
        return SantasWorkshop(**kwargs)

    def create_stuffed_animals(self, **kwargs) -> StuffedAnimals:
        """
        :return: a Reindeer.
        """
        return Reindeer(**kwargs)

    def create_candy(self, **kwargs) -> Candy:
        """
        :return: a CandyCane.
        """
        return CandyCanes(**kwargs)
