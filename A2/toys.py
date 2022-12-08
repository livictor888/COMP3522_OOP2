"""This module creates Toys"""
import abc
from invaliddataerror import InvalidDataError


class Toys(abc.ABC):
    """
    Toys defines the interface for one of the items that the
    abstract factory pattern is responsible to create.
    """

    def __init__(self, has_batteries, min_age, name, description, product_id):
        self.has_batteries = has_batteries
        self.min_age = self.check_valid_age(min_age)
        self.name = self.check_not_empty(name)
        self.description = self.check_not_empty(description)
        self.product_id = self.check_not_empty(product_id)

    @staticmethod
    def check_valid_age(value):
        """
        Checks if minimum age is valid
        :param value: a number
        :return: value if valid, else Raise InvalidDataError
        """
        if (value is None) or not (isinstance(value, (int, float))):
            raise InvalidDataError("Toys must have a valid minimum age")
        else:
            return value

    @staticmethod
    def check_not_empty(value):
        """
        Checks if values are strings and not None
        :param value: a number
        :return: value if valid, else Raise InvalidDataError
        """
        if (value is None) or not (isinstance(value, str)):
            raise InvalidDataError("Toys must have a valid name, description, or product ID")
        else:
            return value

    def __str__(self):
        """
        Returns a nicely formatted string with the details of the Toy.
        :return: a string
        """
        return f"---- Toy Info----\n" \
               f"Product ID: {self.product_id}\n" \
               f"Name: {self.name}\n" \
               f"Battery Operated: {self.has_batteries}\n" \
               f"Recommended Minimum Age: {self.min_age}\n" \
               f"Toy Description: {self.description}"
