"""This module creates Dancing Skeleton Halloween-themed Stuffed Animals"""
from stuffedanimals import StuffedAnimals
from invaliddataerror import InvalidDataError


class DancingSkeleton(StuffedAnimals):
    """
    DancingSkeletons is a Halloween-themed StuffedAnimal.
    """

    def __init__(self, **kwargs):
        super().__init__(stuffing=self.check_stuffing_status(kwargs['stuffing']), size=kwargs['size'],
                         fabric=self.check_material_status(kwargs['fabric']), name=kwargs['name'],
                         description=kwargs['description'], product_id=kwargs['product_id'])
        self.has_glow = self.check_glow_status(kwargs['details']['has_glow'])

    def __str__(self):
        """
        Returns a nicely formatted string with the details of the DancingSkeletons.
        :return: a string
        """
        return super().__str__() + f"\nHas Glow: {self.has_glow}"

    @staticmethod
    def check_material_status(fabric):
        """
        Raises an error if the specified material is anything other than Acrylic yarn.
        :param fabric: a string representing the fabric of the stuffed animal
        :return: Acrylic if the order specifies a valid fabric, raises InvalidDataError otherwise
        """
        if (fabric is None) or not (isinstance(fabric, str)) or ("acrylic" not in fabric.lower()):
            raise InvalidDataError('Dancing Skeleton Fabric can only be Acrylic yarn.')
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
            raise InvalidDataError('Dancing Skeleton Stuffing can only be Polyester Fibrefill.')
        else:
            return stuffing

    @staticmethod
    def check_glow_status(has_glow):
        """
        Raises an error if the item does not glow.
        :param has_glow: a string representing the glow status of the item
        :return: 'Y' if the order specifies a valid glow status, raises InvalidDataError otherwise
        """
        if (has_glow is None) or not (isinstance(has_glow, str)) or (has_glow not in ['Y', 'y']):
            raise InvalidDataError('Dancing Skeleton should glow in the dark.')
        else:
            return has_glow
