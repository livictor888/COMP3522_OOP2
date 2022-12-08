"""This module creates Robot Bunny Easter-themed Toys"""
from toys import Toys
from invaliddataerror import InvalidDataError


class RobotBunny(Toys):
    """
    RobotBunny is a type of Toy designed for toddlers and infants.
    """

    def __init__(self, **kwargs):
        super().__init__(has_batteries=self.check_battery_status(kwargs["has_batteries"]),
                         min_age=kwargs['min_age'], name=kwargs['name'],
                         description=kwargs['description'], product_id=kwargs['product_id'])
        self.num_sound = kwargs['details']['num_sound']
        self.colour = self.check_valid_colour(kwargs['details']['colour'])

    @staticmethod
    def check_number_sound_effects(num_sound):
        """
        Raises an error if the item does not have a valid number of sound effects.
        :param num_sound: a float representing the number of sounds
        :return: the valid number of sounds if the order specifies a valid number of sounds,
        raises InvalidDataError otherwise
        """
        if (num_sound is None) or not (isinstance(num_sound, (int, float))) \
                or (num_sound <= 0):
            raise InvalidDataError('Invalid number of Robot Bunny sound effects.')
        else:
            return num_sound

    @staticmethod
    def check_valid_colour(colour):
        """
        Raises an error if the item does not have a valid colour.
        :param colour: a string representing the colour of the item
        :return: the valid colour if the order specifies a valid colour, raises InvalidDataError otherwise
        """
        if (colour is None) or not (isinstance(colour, str)) \
                or (colour.lower() not in ["orange", "blue", "pink"]):
            raise InvalidDataError('Invalid Robot Bunny colour.')
        else:
            return colour

    @staticmethod
    def check_battery_status(has_batteries):
        """
        Raises an error if the item does not have batteries.
        :param has_batteries: a string representing the battery status of the item
        :return: 'Y' if the order specifies a valid battery status, raises InvalidDataError otherwise
        """
        if (has_batteries is None) or not (isinstance(has_batteries, str)) or (has_batteries not in ['Y', 'y']):
            raise InvalidDataError('Robot Bunny must be battery operated.')
        else:
            return has_batteries

    def __str__(self):
        """
        Returns a nicely formatted string with the details of the RobotBunny Toy.
        :return: a string
        """
        return super().__str__() + f"\nNumber of Sound Effects: {self.num_sound}\n" \
                                   f"Colour: {self.colour}\n" \
