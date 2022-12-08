"""This module creates Candy Cane Christmas-themed Candy"""
from candy import Candy
from invaliddataerror import InvalidDataError


class CandyCanes(Candy):
    """
    CandyCanes are a Christmas-themed Candy.
    """

    def __init__(self, **kwargs):
        super().__init__(has_nuts=self.check_nuts_status(kwargs['has_nuts']),
                         has_lactose=self.check_lactose_status(kwargs['has_lactose']), name=kwargs['name'],
                         description=kwargs['description'], product_id=kwargs['product_id'])
        self.stripes_colour = self.check_stripes_colour(kwargs['details']['colour'])

    @staticmethod
    def check_lactose_status(has_lactose):
        """
        Raises an error if the order does not specify that the order is not lactose-free.
        :param has_lactose: a string, either 'Y' or 'N' to indicate if the order is lactose-free or not
        :return: 'Y' if the order has a valid not-lactose-free status, raises InvalidDataError otherwise
        """
        if (has_lactose is None) or not (isinstance(has_lactose, str)) or (has_lactose not in ['N', 'n']):
            raise InvalidDataError('Candy Canes has Invalid Lactose status.')
        else:
            return has_lactose

    @staticmethod
    def check_nuts_status(has_nuts):
        """
        Raises an error if the order does not specify that the order is not nut-free.
        :param has_nuts: a string, either 'Y' or 'N' to indicate if the order is nut-free or not
        :return: 'Y' if the order has a valid not-lactose-free status, raises InvalidDataError otherwise
        """
        if (has_nuts is None) or not (isinstance(has_nuts, str)) or (has_nuts not in ['N', 'n']):
            raise InvalidDataError('Invalid Candy Cane Nuts status.')
        else:
            return has_nuts

    @staticmethod
    def check_stripes_colour(colour):
        """
        Validates the colour of candy, throws an error if not valid.
        :param colour: a String representing the colour of the candy's stripes
        :return: the Colour if it is valid, raises InvalidDataError otherwise
        """
        if (colour is None) or not (isinstance(colour, str)) or (colour.lower() not in ["red", "green"]):
            raise InvalidDataError('Invalid Candy Cane Stripes colour.')
        else:
            return colour

    def __str__(self):
        """
        Returns a nicely formatted string with the details of the CandyCanes.
        :return: a string
        """
        return super().__str__() + f"\nStripes Colour: {self.stripes_colour}"
