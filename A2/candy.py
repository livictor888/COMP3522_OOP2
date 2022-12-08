"""This module creates Candy"""
import abc
from invaliddataerror import InvalidDataError


class Candy(abc.ABC):
    """
    Candy defines the interface for one of the items that the
    abstract factory pattern is responsible to create.
    """

    @abc.abstractmethod
    def __init__(self, has_nuts, has_lactose, name, description, product_id):
        self.has_nuts = has_nuts
        self.has_lactose = has_lactose
        self.name = self.check_not_empty(name)
        self.description = self.check_not_empty(description)
        self.product_id = self.check_not_empty(product_id)

    @staticmethod
    def check_not_empty(value):
        """
        Checks if values are strings and not None
        :param value: a number
        :return: value if valid, else Raise InvalidDataError
        """
        if (value is None) or not (isinstance(value, str)):
            raise InvalidDataError("Candies must have a valid name, description, or product ID")
        else:
            return value

    def __str__(self):
        """
        Returns a nicely formatted string with the details of the Candy.
        :return: a string
        """
        return f"---- Candy Info----\n" \
               f"Product ID: {self.product_id}\n" \
               f"Name: {self.name}\n" \
               f"Has Nuts: {self.has_nuts}\n" \
               f"Has Lactose: {self.has_lactose}\n" \
               f"Candy Description: {self.description}"
