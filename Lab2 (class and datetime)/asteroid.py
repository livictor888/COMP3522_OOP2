import itertools
import sys


class Asteroid:
    """A class representing an asteroid."""

    id_iteration = itertools.count(start=1)
    max_speed = 5

    def __init__(self, circumference, position, velocity):
        """
        Initialize an instance of an asteroid.
        :param circumference: circumference of an asteroid in meters as a float
        :param position: position represented as a vector with x and y attributes in meters per second as a float
        :param velocity: velocity represented as a vector with x, y, and z attributes in meters per second as a float
        """
        try:
            if not Asteroid.is_valid_circumference(circumference):
                raise ValueError("Invalid circumference, not a number greater than 0.")
            self._circumference = circumference
            if not Asteroid.is_valid_position(position):
                print("Input position: x = {}, y = {}, z = {}".format(position[0], position[1], position[2]))
                raise TypeError("Invalid position entered.")
            self._position = position
            if not Asteroid.is_valid_velocity(velocity):
                print("Input velocity: x = {}, y = {}, z = {}".format(velocity[0], velocity[1], velocity[2]))
                raise ValueError("Invalid velocity, not a number less than or greater than 5.")
            self._velocity = velocity
            self.__id = Asteroid.get_new_id()
        except (ValueError, TypeError) as err:
            print("Error:", err)
            sys.exit()

    def get_id(self):
        """
        Return the id of current asteroid.
        :return: the id
        """
        return self.__id

    def get_circumference(self):
        """
        Return the circumference of current asteroid.
        :return: the circumference in metres
        """
        return self._circumference

    def get_position(self):
        """
        Return the position of current asteroid.
        :return: the position as a tuple
        """
        return self._position

    def get_position_str(self):
        """
        Return the position of current asteroid.
        :return: the position as a string
        """
        return f"{self._position[0]}, {self._position[1]}, {self._position[2]}"

    def set_position(self, position):
        """
        Set the current position of the current asteroid.
        :param position: new position of asteroid as a tuple
        """
        if Asteroid.is_valid_position(position):
            self._position = position

    def get_velocity(self):
        """
        Return the velocity of current asteroid.
        :return: the velocity as a tuple
        """
        return self._velocity

    def get_velocity_str(self):
        """
        Return the velocity of current asteroid.
        :return: the velocity as a string
        """
        return f"{self._velocity[0]}, {self._velocity[1]}, {self._velocity[2]}"

    def move(self):
        """
        Perform the movement of the asteroid based on the current position and velocity.
        :return: the new position of the asteroid after moving as a tuple
        """
        new_x = self._position[0] + self._velocity[0]
        new_y = self._position[1] + self._velocity[1]
        new_z = self._position[2] + self._velocity[2]
        self.set_position((new_x, new_y, new_z))
        return self._position

    def __str__(self):
        """
        Print out information about the asteroid.
        :return: a formatted string describing the asteroid attributes
        """
        return f"This asteroid has a circumference of {self._circumference}\n" \
               f"Its coordinates are X: {self._position[0]}, Y: {self._position[1]}, Z: {self._position[2]}\n" \
               f"Its velocity is X: {self._velocity[0]}, Y: {self._velocity[1]}, Z: {self._velocity[2]}\n"

    @staticmethod
    def get_new_id():
        """
        Generate a new ID number for the asteroid.
        :return: a new sequential ID number as an integer
        """
        return next(Asteroid.id_iteration)

    @staticmethod
    def is_number(number):
        """
        Validate if the input number is a number.
        :param number: a number
        :return: True if the input is a number, otherwise False
        """
        if type(number) == float or type(number) == int:
            return True
        return False

    @staticmethod
    def is_valid_circumference(circumference):
        """
        Validate the input circumference of the asteroid.
        :param circumference: a number
        :return: True if the input is a number greater than 0, otherwise False
        """
        if Asteroid.is_number(circumference) and circumference > 0:
            return True
        return False

    @staticmethod
    def is_valid_position(position):
        """
        Validate the input position of the asteroid.
        :param position: a tuple representing the x, y, and z coordinates of the asteroid
        :return: True if the (x, y, z) coordinates are numbers, otherwise False
        """
        for number in position:
            if not Asteroid.is_number(number):
                return False
        return True

    @staticmethod
    def is_valid_velocity(velocity):
        """
        Validate the input velocity of the asteroid.
        :param velocity: a tuple representing the x, y, and z velocity of the asteroid
        :return: True if the (x, y, z) velocity are numbers less or equal to 5, otherwise False
        """
        for number in velocity:
            if not Asteroid.is_number(number) or number > Asteroid.max_speed:
                return False
        return True
