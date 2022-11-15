import time


class Car:
    """
    An expensive object that is computationally intensive.
    """

    def __init__(self):
        """
        Creating this object takes a while.
        """
        print("Building a car. This is a time consuming process")
        time.sleep(2)
        print("Wait for it...")
        time.sleep(1)
        print("Car has been made")

    def __str__(self):
        return "I am an expensive car that uses a lot of resources"

class Client:

    def __init__(self):
        """
        The client has access to a car. In Lazy Inititalization we don't
        initialize it outright.
        """
        self._car = None

    @property
    def car(self) -> Car:
        """
        When the car is accessed we check to see if it is initialized.
        If it isn't initialized then we initialize it and return it.
        This is lazy intialization. We have delayed the initialization
        of an expensive object until we needed it.
        :return: a Car
        """
        if not self._car:
            self._car = Car() #initialize Car for the first time

        return self._car


def main():
    client = Client() #creates an instance of Client, BUT inside the client CAR is NOT initialized
#    print(client.car) #car is initialized here when we access client.car for the first time
    print("hello")
    #do some other code
    #if we never access client.car, we never have to make memory for Car

if __name__ == '__main__':
    main()