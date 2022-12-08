"""This module creates Easter Bunny Easter-themed Stuffed Animals"""
from stuffedanimals import StuffedAnimals
from invaliddataerror import InvalidDataError


class EasterBunny(StuffedAnimals):
    """
    EasterBunny is an Easter-themed StuffedAnimal.
    """

    def __init__(self, **kwargs):
        super().__init__(stuffing=self.check_stuffing_status(kwargs["stuffing"]), size=kwargs['size'],
                         fabric=self.check_material_status(kwargs["fabric"]), name=kwargs['name'],
                         description=kwargs['description'],
                         product_id=kwargs['product_id'])
        self.colour = self.check_valid_colour(kwargs['details']['colour'])

    @staticmethod
    def check_valid_colour(colour):
        """
        Raises an error if the specified Colour is anything other than a valid colour.
        :param colour: a string representing the colour of the stuffed animal
        :return: valid colour if the order specifies a valid colour, raises InvalidDataError otherwise
        """
        if (colour is None) or not (isinstance(colour, str)) \
                or (colour.lower() not in ["white", "grey", "pink", "blue"]):
            raise InvalidDataError('Invalid Easter Bunny colour.')
        else:
            return colour

    @staticmethod
    def check_material_status(fabric):
        """
        Raises an error if the specified material is anything other than Linen.
        :param fabric: a string representing the fabric of the stuffed animal
        :return: Linen if the order specifies a valid fabric, raises InvalidDataError otherwise
        """
        if (fabric is None) or not (isinstance(fabric, str)) or ("linen" not in fabric.lower()):
            raise InvalidDataError('Easter Bunny Fabric can only be Linen.')
        else:
            return fabric

    @staticmethod
    def check_stuffing_status(stuffing):
        """
        Raises an error if the specified stuffing is anything other than Polyester Fibrefill.
        :param stuffing: a string representing the stuffing of the stuffed animal
        :return: Polyester Fibrefill if the order specifies a valid stuffing, raises InvalidDataError otherwise
        """
        if (stuffing is None) or not (isinstance(stuffing, str)) or ("polyester fibrefill" not in stuffing.lower()):
            raise InvalidDataError('Easter Bunny Stuffing can only be Polyester Fibrefill.')
        else:
            return stuffing

    def __str__(self):
        """
        Returns a nicely formatted string with the details of the EasterBunny.
        :return: a string
        """
        return super().__str__() + f"\nColour: {self.colour}"
