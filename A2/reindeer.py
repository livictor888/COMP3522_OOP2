"""This module creates Reindeer Christmas-themed Stuffed Animals"""
from stuffedanimals import StuffedAnimals
from invaliddataerror import  InvalidDataError


class Reindeer(StuffedAnimals):
    """
    Reindeer is a Christmas-themed StuffedAnimal that comes with its own mini sleigh.
    """

    def __init__(self, **kwargs):
        super().__init__(stuffing=self.check_stuffing_status(kwargs["stuffing"]), size=kwargs['size'],
                         fabric=self.check_material_status(kwargs["fabric"]), name=kwargs['name'],
                         description=kwargs['description'],
                         product_id=kwargs['product_id'])
        self.has_glow = self.check_glow_status(kwargs['details']['has_glow'])

    def __str__(self):
        """
        Returns a nicely formatted string with the details of the Reindeer.
        :return: a string
        """
        return super().__str__() + f"\nHas Glow: {self.has_glow}"

    @staticmethod
    def check_glow_status(has_glow):
        """
        Raises an error if the item does not glow.
        :param has_glow: a string representing the glow status of the item
        :return: 'Y' if the order specifies a valid glow status, raises InvalidDataError otherwise
        """
        if (has_glow is None) or not (isinstance(has_glow, str)) or (has_glow not in ['Y', 'y']):
            raise InvalidDataError('Reindeer should have a glow-in-the-dark nose.')
        else:
            return has_glow

    @staticmethod
    def check_material_status(fabric):
        """
        Raises an error if the specified material is anything other than cotton.
        :param fabric: a string representing the fabric of the stuffed animal
        :return: cotton if the order specifies a valid fabric, raises InvalidDataError otherwise
        """
        if (fabric is None) or not (isinstance(fabric, str)) or ("cotton" not in fabric.lower()):
            raise InvalidDataError('Reindeer Fabric can only be Cotton.')
        else:
            return fabric

    @staticmethod
    def check_stuffing_status(stuffing):
        """
        Raises an error if the specified stuffing is anything other than Wool.
        :param stuffing: a string representing the stuffing of the stuffed animal
        :return: Wool if the order specifies a valid stuffing, raises InvalidDataError otherwise
        """
        if (stuffing is None) or not (isinstance(stuffing, str)) or ("wool" not in stuffing.lower()):
            raise InvalidDataError('Reindeer stuffing can only be Wool.')
        else:
            return stuffing
