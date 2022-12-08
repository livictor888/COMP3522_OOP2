"""This module creates RC Spider Halloween-themed Toys"""
from toys import Toys
from invaliddataerror import InvalidDataError


class RCSpider(Toys):
    """
    RCSpider (Remote Controlled Spider), is a type of Halloween-themed Toy.
    """

    def __init__(self, **kwargs):
        super().__init__(has_batteries=self.check_battery_status(kwargs["has_batteries"]), min_age=kwargs['min_age'],
                         name=kwargs['name'], description=kwargs['description'],
                         product_id=kwargs['product_id'])
        self.speed = self.check_valid_speed(kwargs['details']['speed'])
        self.jump_height = self.check_valid_jump_height(kwargs['details']['jump_height'])
        self.has_glow = kwargs['details']['has_glow']
        self.spider_type = self.check_spider_type_status(kwargs['details']['spider_type'])

    @staticmethod
    def check_valid_jump_height(height):
        """
        Raises an error if the item does not have a valid jump height.
        :param height: a float representing the jump height
        :return: the valid speed if the order specifies a valid jump height,
        raises InvalidDataError otherwise
        """
        if (height is None) or not (isinstance(height, (int, float))) or (height <= 0):
            raise InvalidDataError('Invalid speed for RC Spider.')
        else:
            return height

    @staticmethod
    def check_valid_speed(speed):
        """
        Raises an error if the item does not have a valid speed.
        :param speed: a float representing the speed
        :return: the valid speed if the order specifies a valid speed,
        raises InvalidDataError otherwise
        """
        if (speed is None) or not (isinstance(speed, (int, float))) or (speed <= 0):
            raise InvalidDataError('Invalid speed for RC Spider.')
        else:
            return speed

    @staticmethod
    def check_battery_status(has_batteries):
        """
        Raises an error if the item does not have batteries.
        :param has_batteries: a string representing the battery status of the item
        :return: 'Y' if the order specifies a valid battery status, raises InvalidDataError otherwise
        """
        if (has_batteries is None) or not (isinstance(has_batteries, str)) or (has_batteries not in ['Y', 'y']):
            raise InvalidDataError('RC Spider is battery operated.')
        else:
            return has_batteries

    @staticmethod
    def check_spider_type_status(spider_type):
        """
        Raises an error if the item does not have batteries.
        :param spider_type: a string representing the type of spider
        :return: valid type of spider if the order specifies a valid spider type, raises InvalidDataError otherwise
        """
        if (spider_type is None) or not (isinstance(spider_type, str)) \
                or (spider_type.lower() not in ['tarantula', 'wolf spider']):
            raise InvalidDataError('RC Spider can only be a Tarantula or a Wolf Spider.')
        else:
            return spider_type

    def __str__(self):
        """
        Returns a nicely formatted string with the details of the RCSpider Toy.
        :return: a string
        """
        return super().__str__() + f"\nSpeed: {self.speed}\n" \
                                   f"Jump Height: {self.jump_height}\n" \
                                   f"Glows in the Dark: {self.has_glow}\n" \
                                   f"Spider Type: {self.spider_type}"
