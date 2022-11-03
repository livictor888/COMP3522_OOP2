"""
This module demonstrates a simpler Bridge example by bridging the shape
(abstractions) and color (implementation) dimensions. Refer to the
share_bridge_uml.png diagram while reading this code.
"""
import abc


class Color(abc.ABC):
    """
    An interface for the Color dimension. This is the implementation
    layer that actually does all the work.
    """
    def __init__(self):
        self._color = None

    @property
    @abc.abstractmethod
    def color(self):
        pass


class Red(Color):

    def __init__(self):
        self._color = "Red"

    @property
    def color(self):
        return self._color


class Blue(Color):

    def __init__(self):
        self._color = "Blue"

    @property
    def color(self):
        return self._color


class Shape:
    """
    The Shape class represents the Abstraction dimension (this doesn't
    have to be an ABC and may have child classes, not necessarily).
    """
    def __init__(self, color: Color):
        self._my_color = color #here is our bridge to the color object/class

    @abc.abstractmethod
    def draw(self):
        print("I am a Shape with color {}".format(self._my_color.color))


class Square(Shape):

    def draw(self):
        print("I am a Square with color {}".format(self._my_color.color))


class Circle(Shape):

    def draw(self):
        print("I am a Circle with color {}".format(self._my_color.color))


def main():
    print("---- COMBO 1: Red Square ----")
    red_square = Square(Red())
    red_square.draw()

    print("\n---- COMBO 2: Blue Circle ----")
    blue_circle = Circle(Blue())
    blue_circle.draw()

    print("\n---- COMBO 3: Red Circle ----")
    red_circle = Circle(Red())
    red_circle.draw()



if __name__ == '__main__':
    main()
