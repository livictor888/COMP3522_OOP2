"""
This module showcases how callbacks work by implementing a Timer class
which executes a number of callback functions when the timer has reached
0 seconds.
"""
import time


class Timer:
    """
    A countdown timer that executes any callbacks subscribed to it at
    the end of the countdown. Pay special attention to how all the
    callback functions need to accept the same number and type of
    parameters.
    """

    def __init__(self, duration_in_seconds):
        """
        Initialize the timer with the number of seconds that it is
        counting down to.
        :param duration_in_seconds: an int
        """
        self.duration = duration_in_seconds
        self.callbacks = []

    def call_me_back(self, callback):
        """
        Responsible for adding the provided function to the list of
        callbacks to execute at the end of the countdown.
        :param callback: a function with the following signature:
                        function_name(timer: Timer)
        """
        self.callbacks.append(callback)

    def run_timer(self):
        """
        Starts the timer countdown. At the end of this countdown all the
        subscribed callbacks are executed.
        """
        for second in range(self.duration):
            print(f"Tick {second}")
            time.sleep(1)

        for callback in self.callbacks:
            callback(self)


def callback_one(timer):
    """
    A event handler that prints the duration of a countdown timer.
    :param timer: A Timer object
    """
    print(f"Event handler 1 Called after {timer.duration} seconds")


def callback_two(timer):
    """
    A second event handler that prints the duration of a countdown
    timer.
    :param timer: A Timer object
    """
    print(f"Event handler 2 Called after {timer.duration} seconds")


def callback_three(timer):
    """
    A third event handler that prints the duration of a countdown timer.
    :param timer: A Timer object
    """
    print(f"Event handler 3 Called after {timer.duration} seconds")


def main():
    """
    Creates a countdown timer, assigns some callbacks to it and executes
    it.
    """
    my_timer = Timer(3)
    my_timer.call_me_back(callback_one) # subscribing
    my_timer.call_me_back(callback_two)
    my_timer.call_me_back(callback_three)
    my_timer.run_timer()

if __name__ == '__main__':
    main()