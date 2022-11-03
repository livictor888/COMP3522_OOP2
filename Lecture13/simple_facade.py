"""
This module demonstrates a simple Facade example
"""
class Facade:
    """
    This class contains all the classes that perform complicated code
    It provides a simple interface for the client to access in order to
    begin the action of the complicated code
    """
    def __init__(self):
        self._c1 = Class1()
        self._c2 = Class2()
        self._c3 = Class3()

    def do_something(self):
        self._c1.do_something()
        self._c2.do_something_1()
        self._c3.do_something_2()

class Class1:
    def do_something(self):
        print('class 1 doing something')

class Class2:
    def do_something_1(self):
        print('class 2 doing something')

class Class3:
    def do_something_2(self):
        print('class 3 doing something')

#instantiate the facade
f = Facade()

#the client only interacts with the facade, not the classes within
f.do_something()