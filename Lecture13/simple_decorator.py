"""
This module demonstrates a simple Decorator example
"""

import abc

class Component(abc.ABC):
    """
    The Component interface that all concrete donuts and
    decorators must adhere to. This interface defines description
    abstract method that do not have an implementation.
    """
    @abc.abstractmethod
    def description(self):
        pass

class WheatDonut(Component):
    """
    A WheatDonut is responsible describing what kind of donut it is.
    It implements the Component Interface as defined by the parent
    Component class. This is the object that we want to add optional
    behaviours to.
    """
    def description(self):
        return 'wheat donut'

class RiceDonut(Component):
    """
    A RiceDonut is responsible describing what kind of donut it is.
    It implements the Component Interface as defined by the parent
    Component class. This is the object that we want to add optional
    behaviours to.
    """
    def description(self):
        return 'rice donut'

class Decorator(Component):
    """
    This is the base decorator. This is a wrapper around a
    concrete donut (such as WheatDonut) and does not add any new
    behaviours or implementation. All other decorators inherit from this
    class. It's CRITICAL to pass in a component in the intializer.
    That component will be ether Concrete Donuts (WheatDonut, RiceDonut)
    or Concrete Decorators (Sprinkles, Gummies)
    """
    def __init__(self, component):
        self.component = component

class Sprinkles(Decorator):
    """
    This is a decorator (read: wrapper) that adds an
    description behaviour to a donut. This decorator can
    wrap around a concrete donut (like WheatDonut) or it can
    also wrap around another Decorator.

    The description is appended to other components or decorators.
    """
    def description(self):
        return self.component.description() + ' and sprinkles'

class Gummies(Decorator):
    """
    This is a decorator (read: wrapper) that adds an
    description behaviour to a donut. This decorator can
    wrap around a concrete donut (like WheatDonut) or it can
    also wrap around another Decorator.

    The description is appended to other components or decorators.
    """
    def description(self):
        return self.component.description() + ' and gummies'

class Chocolate(Decorator):
    """
    This is a decorator (read: wrapper) that adds an
    description behaviour to a donut. This decorator can
    wrap around a concrete donut (like WheatDonut) or it can
    also wrap around another Decorator.

    The description is appended to other components or decorators.
    """
    def description(self):
        return self.component.description() + ' and chocolate'

#begin by instantiating the base donut components
wheat_donut = WheatDonut() #WD Wheat donut object created
rice_donut = RiceDonut() #RD Rice donut object created

print(wheat_donut.description())
print(rice_donut.description())

# add toppings to the wheat donut by wrapping it in the decorators
# think of it like a linked lists
wheat_donut = Sprinkles(wheat_donut) #S -> WD. Internally sprinkes points to wheat donut
wheat_donut = Gummies(wheat_donut) #G -> S -> WD. Internally, gummies points to sprinkles, which points to wheat donut

# add toppings to the rice donut by wrapping it in the decorators
rice_donut = Sprinkles(rice_donut) #S -> RD
rice_donut = Sprinkles(rice_donut) #S -> S -> RD
rice_donut = Chocolate(rice_donut) #C -> S -> S -> RD
rice_donut = Chocolate(rice_donut)
rice_donut = Chocolate(rice_donut)

# print(wheat_donut.description())
print(rice_donut.description())