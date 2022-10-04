""""This module showcases how OOP in Python works through the implementation of a Cat class"""

class Cat:
    """This class embodies the basic functions and attributes of a cat"""

    # all cats start with 9 lives
    # lives is a class variable
    lives = 9

    def __init__(self, name, age, favorite_food):
        """
        Initialize the cat name, age and list of favorite foods
        :param name: a string
        :param age: an int
        :param favorite_food: list of food string names
        """
        self._age = age
        self._name = name
        self._food_prefs = favorite_food
        self._num_lives = Cat.lives

    def scratch_and_pet(self):
        """
        Simulates a cats reaction to being petted and scratched
        :return: a string depicting the cats reaction
        """
        return '{0} purrs'.format(self._name)

    def __repr__(self):
        """
        :return: a string, a depiction of the cat object state
        """
        return "name: {0} age: {1} food_prefs: {2}, num_lives: {3}".format(
            self._name, self._age, self._food_prefs, self._num_lives)

    def __str__(self):
        """
        :return: A user friendly formatted string depicting the cat attributes
        """
        return "My name is {0} and I'm {1} years old.\nlove eating {2}\nI have {3} lives remaining".format(
            self._name, self._age, str(self._food_prefs), self._num_lives)

    def celebrate_birthday(self):
        """
        Celebrate the cat's birthday! Increments age by 1.
        """
        self._age = self._age + 1

    @classmethod
    def set_default_lives(cls, num_lives):
        """
        Changes the default lives that all cats start with.
        :param num_lives: an int. The number of lives a cat starts with
        :precondition: num_lives must be an int greater than 0
        """
        if num_lives > 0:
            cls.lives = num_lives

    @staticmethod
    def get_list_of_celebrity_cats():
        return ["Tom", "Garfield", "Snagglepuss", "Cheshire Cat", "Cat in the Hat"]


def main():
    """
    Creates a cat and demonstrates its methods and features
    """
    tobias = Cat("Tobias", 3, ["Sushi", "Raw fish"])
    # print(tobias.scratch_and_pet())
    #
    # print("only tobias")
    # print(tobias)
    #
    # print("repr tobias")
    # print(repr(tobias))
    #
    # print("str tobias")
    # print(str(tobias))

    # print("All cats start with {} lives".format(tobias.lives))
    # print("All cats start with {} lives".format(Cat.lives))

    print("Celebrity cats:", end="\n")
    for name in Cat.get_list_of_celebrity_cats():
        print(name, end="\n")

    print(type(tobias))


    Cat.set_default_lives(10)

    furball = Cat('Furball', 5, ['candy'])
    print(furball)
    x = Cat('X', 5, ['candy'])
    print(x)

if __name__ == "__main__":
    main()

