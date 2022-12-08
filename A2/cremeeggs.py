"""This module creates Creme Egg Easter-themed Candy"""
from candy import Candy
from invaliddataerror import InvalidDataError


class CremeEggs(Candy):
    """
    CremeEggs are an Easter-themed Candy.
    """

    def __init__(self, **kwargs):
        super().__init__(has_nuts=self.check_nuts_status(kwargs['has_nuts']), has_lactose=self.check_lactose_status(kwargs['has_lactose']),
                         name=kwargs['name'], description=kwargs['description'], product_id=kwargs['product_id'])
        self.pack_size = self.check_valid_pack_size(kwargs['details']['pack_size'])

    def __str__(self):
        """
        Returns a nicely formatted string with the details of the CremeEggs.
        :return: a string
        """
        return super().__str__() + f"\nPack Size: {self.pack_size}"

    @staticmethod
    def check_valid_pack_size(size):
        """
        Raises an error if the order does not specify a valid pack size.
        :param size: a float
        :return: size if pack size is valid, raises InvalidDataError otherwise
        """
        if (size is None) or not (isinstance(size, (int, float))) or (size <= 0):
            raise InvalidDataError('Invalid Creme Egg pack size.')
        else:
            return size

    @staticmethod
    def check_lactose_status(has_lactose):
        """
        Raises an error if the order does not specify that the order is not lactose-free.
        :param has_lactose: a string, either 'Y' or 'N' to indicate if the order is lactose-free or not
        :return: 'Y' if the order has a valid not-lactose-free status, raises InvalidDataError otherwise
        """
        if (has_lactose is None) or not (isinstance(has_lactose, str)) or (has_lactose not in ['Y', 'y']):
            raise InvalidDataError('Invalid Creme Egg Lactose status.')
        else:
            return has_lactose

    @staticmethod
    def check_nuts_status(has_nuts):
        """
        Raises an error if the order does not specify that the order is not nut-free.
        :param has_nuts: a string, either 'Y' or 'N' to indicate if the order is nut-free or not
        :return: 'Y' if the order has a valid not-lactose-free status, raises InvalidDataError otherwise
        """
        if (has_nuts is None) or not (isinstance(has_nuts, str)) or (has_nuts in ['N', 'n']):
            raise InvalidDataError('Invalid Creme Egg Nuts status.')
        else:
            return has_nuts
