"""This module creates Santa's Workshop Christmas-themed Toys"""
from toys import Toys
from invaliddataerror import InvalidDataError


class SantasWorkshop(Toys):
    """
    SantasWorkshop is a type of Christmas-themed Toy.
    """

    def __init__(self, **kwargs):
        super().__init__(has_batteries=self.check_battery_status(kwargs["has_batteries"]),
                         min_age=kwargs['min_age'], name=kwargs['name'], description=kwargs['description'],
                         product_id=kwargs['product_id'])
        self.dimensions = kwargs['details']['dimensions']
        self.num_rooms = self.check_valid_number_rooms(kwargs['details']['num_rooms'])

    @staticmethod
    def check_valid_number_rooms(num_rooms):
        """
        Raises an error if the item does not have a valid number of rooms.
        :param num_rooms: a float representing the number of rooms
        :return: the valid number of sounds if the order specifies a valid number of sounds,
        raises InvalidDataError otherwise
        """
        if (num_rooms is None) or not (isinstance(num_rooms, (int, float))) \
                or (num_rooms <= 0):
            raise InvalidDataError('Invalid number of rooms in Santa\'s Workshop.')
        else:
            return num_rooms

    @staticmethod
    def check_battery_status(has_batteries):
        """
        Raises an error if the item has batteries.
        :param has_batteries: a string representing the battery status of the item
        :return: 'N' if the order specifies a valid glow status, raises InvalidDataError otherwise
        """
        if (has_batteries is None) or not (isinstance(has_batteries, str)) or (has_batteries not in ['N', 'n']):
            raise InvalidDataError('Santa\'s Workshop is not battery operated.')
        else:
            return has_batteries

    def __str__(self):
        """
        Returns a nicely formatted string with the details of the Santa\'s Workshop Toy.
        :return: a string
        """
        return super().__str__() + f"\nDimensions: {self.dimensions}\n" \
                                   f"Number of Rooms: {self.num_rooms}"
