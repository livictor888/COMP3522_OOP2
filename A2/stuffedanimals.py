"""This module creates Stuffed Animals"""
import abc
from invaliddataerror import InvalidDataError


class StuffedAnimals(abc.ABC):
    """
    StuffedAnimals defines the interface for one of the items that the
    abstract factory pattern is responsible to create.
    """

    @abc.abstractmethod
    def __init__(self, stuffing, size, fabric, name, description, product_id):
        self.stuffing = stuffing
        self.size = self.check_valid_size(size)
        self.fabric = fabric
        self.name = self.check_not_empty(name)
        self.description = self.check_not_empty(description)
        self.product_id = self.check_not_empty(product_id)

    @staticmethod
    def check_not_empty(value):
        """
        Raises an error if values checked are not strings or are empty
        :param value: a string
        :return: value if valid, raises InvalidDataError otherwise
        """
        if (value is None) or not (isinstance(value, str)):
            raise InvalidDataError("Toys must have a valid name, description, or product ID")
        else:
            return value

    @staticmethod
    def check_valid_size(size):
        """
        Raises an error if the order does not specify a valid size.
        :param size: a string, either "s", "m", or "l" to indicate a size
        :return: valid size if the order has a valid size, raises InvalidDataError otherwise
        """
        if (size is None) or not (isinstance(size, str)) or (size.lower() not in ["s", "m", "l"]):
            raise InvalidDataError('Invalid Size.')
        else:
            return size

    def __str__(self):
        """
        Returns a nicely formatted string with the details of the StuffedAnimals.
        :return: a string
        """
        return f"---- Stuffed Animal Info----\n" \
               f"Product ID: {self.product_id}\n" \
               f"Name: {self.name}\n" \
               f"Stuffing: {self.stuffing}\n" \
               f"Fabric: {self.fabric}\n" \
               f"Size: {self.size}\n" \
               f"Toy Description: {self.description}"
