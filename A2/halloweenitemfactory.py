"""This module defines a Halloween Item Factory"""
from itemfactory import ItemFactory
from rcspider import RCSpider
from dancingskeleton import DancingSkeleton
from pumpkincarameltoffee import PumpkinCaramelToffee
from toys import Toys
from stuffedanimals import StuffedAnimals
from candy import Candy


class HalloweenItemFactory(ItemFactory):
    """
    This factory class implements the ItemFactory Interface. It
    returns an Item family consisting of RCSpider, DancingSkeleton,
    and PumpkinCaramelToffee
    """

    def create_toys(self, **kwargs) -> Toys:
        """
        :return: an RCSpider.
        """
        return RCSpider(**kwargs)

    def create_stuffed_animals(self,  **kwargs) -> StuffedAnimals:
        """
        :return: a DancingSkeleton.
        """
        return DancingSkeleton(**kwargs)

    def create_candy(self, **kwargs) -> Candy:
        """
        :return: a PumpkinCaramelToffee.
        """
        return PumpkinCaramelToffee(**kwargs)
