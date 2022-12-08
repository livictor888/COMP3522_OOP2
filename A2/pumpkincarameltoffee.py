"""This module creates Pumpkin Caramel Toffee Halloween-themed Candy"""
from candy import Candy
from invaliddataerror import InvalidDataError


class PumpkinCaramelToffee(Candy):
    """
    PumpkinCaramelToffee are a Halloween-themed Candy.
    """

    def __init__(self, **kwargs):
        super().__init__(has_nuts=kwargs['has_nuts'], has_lactose=self.check_lactose_status(kwargs['has_lactose']),
                         name=kwargs['name'],
                         description=kwargs['description'], product_id=kwargs['product_id'])
        self.variety = self.check_variety(kwargs['details']['variety'])

    @staticmethod
    def check_lactose_status(has_lactose):
        """
        Raises an error if the order does not specify that the order is not lactose free.
        :param has_lactose: a string, either 'Y' or 'N' to indicate if the order is lactose free or not
        :return: 'Y' if the order has a valid not-lactose-free status, raises InvalidDataError otherwise
        """
        if (has_lactose is None) or not (isinstance(has_lactose, str)) or (has_lactose not in ['Y', 'y']):
            raise InvalidDataError('Invalid Pumpkin Caramel Toffee Lactose status.')
        else:
            return has_lactose

    @staticmethod
    def check_nuts_status(has_nuts):
        """
        Raises an error if the order does not specify that the order is not nut-free.
        :param has_nuts: a string, either 'Y' or 'N' to indicate if the order is nut-free or not
        :return: 'N' if the order has a valid nut status, raises InvalidDataError otherwise
        """
        if (has_nuts is None) or not (isinstance(has_nuts, str)) or (has_nuts in ['N', 'n']):
            raise InvalidDataError('Invalid Pumpkin Caramel Toffee Nuts status.')
        else:
            return has_nuts

    @staticmethod
    def check_variety(variety):
        """
        Validates the variety of the candy, throws an error if not valid.
        :param variety: a String representing the flavour of the candy
        :return: the variety if it is valid, raises InvalidDataError otherwise
        """
        if (variety is None) or not (isinstance(variety, str)) or (variety.lower() not in ["sea salt", "regular"]):
            raise InvalidDataError('Invalid Pumpkin Caramel Toffee flavour.')
        else:
            return variety

    def __str__(self):
        """
        Returns a nicely formatted string with the details of the Pumpkin Caramel Toffee.
        :return: a string
        """
        return super().__str__() + f"\nStripes Colour: {self.variety}"
