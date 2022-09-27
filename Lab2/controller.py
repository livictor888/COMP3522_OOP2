import datetime
import random
from asteroid import Asteroid
import math
import time
import sys


class Controller:
    """A class that simulates the movements of asteroids."""

    def __init__(self):
        """
        Initialize an empty list of asteroids
        """
        self._asteroid_field = []

    def create_asteroid(self, x, y, z, v_x, v_y, v_z, radius):
        """
        Create an asteroid object and add it to the asteroid field

        :param x: an int or float representing the x-coordinate of the asteroid
        :param y: an int or float representing the y-coordinate of the asteroid
        :param z: an int or float representing the z-coordinate of the asteroid
        :param v_x: an int or float representing the velocity of the asteroid on the x-axis
        :param v_y: an int or float representing the velocity of the asteroid on the y-axis
        :param v_z: an int or float representing the velocity of the asteroid on the z-axis
        :param radius: a positive int or float representing the radius of the asteroid
        """
        circumference = 2 * math.pi * radius
        my_asteroid = Asteroid(circumference, (x, y, z), (v_x, v_y, v_z))
        self._asteroid_field.append(my_asteroid)

    def get_asteroid_field(self):
        """
        Return the list of asteroids
        :return: a list of asteroids
        """
        return self._asteroid_field

    def simulate(self, seconds):
        """
        Simulate the movement of all asteroids in the asteroid field for the duration of the input number of seconds.
        :param seconds: an integer or float representing the duration of the simulation
        """
        try:
            if not Controller.is_valid_time(seconds):
                raise ValueError("Invalid seconds, not a number greater than 0.")
        except ValueError as err:
            print("Error:", err)
            sys.exit()

        if len(self.get_asteroid_field()) == 0:
            print("Error: No asteroids in the field.")
            return

        start_time = datetime.datetime.fromtimestamp(time.time())
        # time_delta = datetime.timedelta(seconds=seconds)
        # print("time delta:", time_delta)
        # stop_time = start_time + time_delta
        print("Simulation Start Time: ", start_time, "\n")

        # current_time = start_time.second
        # 1_000_000 microseconds in 1 second
        time_to_wait = (1_000_000 - start_time.microsecond) / 1_000_000
        time.sleep(time_to_wait)
        remaining_time = seconds - time_to_wait
        if remaining_time > 0:
            while remaining_time >= 0:
                self.move_asteroids()
                time.sleep(1)
                remaining_time -= 1
        return

    def move_asteroids(self):
        """
        Move all asteroids in the asteroid field and print out information about them.
        """
        print("Moving Asteroids!\n-----------------")
        for current_asteroid in self._asteroid_field:
            old_position = str(current_asteroid.get_position_str())
            current_asteroid.move()
            new_position = str(current_asteroid.get_position_str())
            print(f"Asteroid {current_asteroid.get_id()} Moved! "
                  f"Old Pos: {old_position} -> "
                  f"New Pos: {new_position}")
            print(f"Asteroid {current_asteroid.get_id()} is currently at "
                  f"{new_position} and moving at {current_asteroid.get_velocity_str()} meters per second. "
                  f"It has a circumference of {current_asteroid.get_circumference()}")
        print("")

    def __str__(self):
        """
        Print out information about the asteroid field.
        :return: a formatted string describing the asteroids attributes within the asteroid_field list.
        """
        return f"The field contains the following asteroids: {self.get_asteroid_field()}"

    @staticmethod
    def is_valid_time(seconds):
        """
        Validate if the input number is a valid second.
        :param seconds: a number
        :return: True if the input is a positive float or integer second, otherwise False
        """
        if (type(seconds) == float or type(seconds) == int) and seconds > 0:
            return True
        return False


def main():
    """
    Drives the program.
    """
    # # asteroid test
    # test_asteroid = Asteroid(10, (1, 2, 3), (1, 2, 3))
    # print(test_asteroid)
    # test_asteroid.move()
    # print(test_asteroid)

    # controller test
    controller = Controller()
    for i in range(8):
        circumference = random.uniform(1, 20)
        controller.create_asteroid(random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),
                                   random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), circumference)
    # controller.simulate(1.5)
    # controller.simulate(1.8)
    # controller.simulate(-2.3)
    controller.simulate(1.2)


if __name__ == "__main__":
    main()
