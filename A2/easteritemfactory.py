"""This module defines an Easter Item Factory"""
from itemfactory import ItemFactory
from robotbunny import RobotBunny
from easterbunny import EasterBunny
from cremeeggs import CremeEggs
from toys import Toys
from stuffedanimals import StuffedAnimals
from candy import Candy


class EasterItemFactory(ItemFactory):
    """
    This factory class implements the ItemFactory Interface. It
    returns an item family consisting of RobotBunny, EasterBunny,
    and CremeEggs
    """

    def create_toys(self, **kwargs) -> Toys:
        """
        :return: a RobotBunny
        """
        return RobotBunny(**kwargs)

    def create_stuffed_animals(self, **kwargs) -> StuffedAnimals:
        """
        :return: an EasterBunny
        """
        return EasterBunny(**kwargs)

    def create_candy(self, **kwargs) -> Candy:
        """
        :return: a CremeEgg
        """
        return CremeEggs(**kwargs)
