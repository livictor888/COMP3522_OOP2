"""
This module is responsible for unit testing the calculator.py module.
"""

from unittest import TestCase
import calculator


class TestCalculator(TestCase):
    """
    Inherits from TestCase and is responsible for executing and housing
    the different unit tests for calculator.py
    """

    def test_add_numbers_int(self):
        """
        Unit test for add_numbers. Tests if the function works with 2
        integers as input.
        """
        result = calculator.add_numbers(5, 3)
        self.assertEqual(result, 8)

    def test_add_numbers_float(self):
        """
        Unit test for add_numbers. Tests if the function works with 2
        floats as input.
        """
        result = calculator.add_numbers(5.0, 3.5)
        self.assertEqual(result, 8.5)

    def test_add_numbers_strings(self):
        """
        Unit test for add_numbers. Asserts that the function raises a
        type error if provided with 2 strings as parameters.
        """
        self.assertRaises(TypeError, calculator.add_numbers, '5', '3')

    def test_add_numbers_different_type(self):
        """
        Unit test for add_numbers. Asserts that the function raises a
        type error if provided with a string and a valid type.
        """
        self.assertRaises(TypeError, calculator.add_numbers, 5, '3')

    def test_check_number_type_int(self):
        """
        Unit test for check_number_type. Asserts that the functions
        returns true if passed an integer as the parameter.
        """
        self.assertTrue(calculator.check_number_type(5))

    def test_check_number_type_float(self):
        """
        Unit test for check_number_type. Asserts that the functions
        returns true if passed an float as the parameter.
        """
        self.assertTrue(calculator.check_number_type(3.0))

    def test_check_number_type_string(self):
        """
        Unit test for check_number_type. Asserts that the functions
        returns false if passed a string as the parameter.
        """
        self.assertFalse(calculator.check_number_type('5'))

    def test_subtract_numbers(self):
        self.assertEqual(calculator.subtract_numbers(2, 1), 1)


class Test(TestCase):
    def test_add_numbers(self):
        self.fail()
