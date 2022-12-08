"""This module defines an InvalidDataError exception"""


class InvalidDataError(Exception):
    """This class represents an InvalidDataError exception"""

    def __init__(self, *args):
        """
        Initialize an InvalidDataError's message
        :param *args: a string
        """
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        """
        Returns a nicely formatted string with the details of the InvalidDataError's message.
        :return: a string
        """
        if self.message:
            return 'InvalidDataError - {0} '.format(self.message)
        else:
            return 'InvalidDataError'
