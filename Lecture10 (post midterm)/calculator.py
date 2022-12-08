"""
This module defines some simple methods for the purpose of demonstrating
Unit Tests.
"""

def subtract_numbers(val1, val2):
    return val1 - val2

def add_numbers(val1, val2):
    """
    Adds 2 numbers and returns the result. Raises a type error
    otherwise.
    :param val1: an int or float
    :param val2: an int or float
    :return: an int or float
    """
    if not check_number_type(val1) or not check_number_type(val2):
        raise TypeError("Invalid Type! Only int and float accepted")
    return val1 + val2


def check_number_type(val):
    """
    Checks to see if the specified value is an int or a float
    :param val: an object
    :return: True if val is an int or a float, False otherwise
    """
    return type(val) == int or type(val) == float


if __name__ == '__main__':
    print(check_number_type(1))
    print(check_number_type(2.0))
    print(check_number_type('3'))
    print(add_numbers(3, 5))
    print(add_numbers(3, 5.0))
    print(add_numbers(3.2, 5.0))
    print(add_numbers(3, '5'))
