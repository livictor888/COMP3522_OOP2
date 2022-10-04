"""This module depicts how inheritance works in Python."""
import random


class Enemy:
    """
    An enemy class that models an enemy with a name, lives and health.

    This class serves as a base class and should be inherited from if
    any enemies are required with specialized behaviors. An enemy has a
    name, health and number of lives. The enemy can also take damage.
    """

    def __init__(self, name="", lives=0, health=0):
        """
        Initialize an enemy object with a name, health and lives.
        :param name: a string
        :param lives: an int
        :param health: an int
        :precondition lives: must be a positiive non-zero int
        :precondition health: must be a positive non-zero int
        """
        self._name = name
        self._lives = lives
        self._health = health
        self._original_health = health

    def take_damage(self, damage):
        """
        Simulates damage dealt to this enemy. If this damage causes
        the health of the enemy to go below zero, it's lives are
        decremented.
        :param damage: an int
        """
        self._health -= damage
        if self._health <= 0:
            self._lives -= 1
            self._health = self._original_health
        print(f"{self._name} took {damage} damage.")
        print(self)

    def __str__(self):
        """Overridden to print the enemy attributes"""
        return f"{self._name}, Lives: {self._lives}, Health: {self._health}"


class Troll(Enemy):
    """
    A troll is a specialized enemy that is stronger than your average
    enemy and has more health.

    The troll can speak and has a dodge_chance that allows it to dodge
    attacks and take no damage.
    """

    def __init__(self, name, lives=5, health=90,
                 dodge_chance=0.1):
        """
        Initialize a troll object with a default life count of 5, 90
        health and a 10% dodge chance unless specified otherwise
        :param name: a string
        :param lives: an int
        :param health: an int
        :param dodge_chance: a float
        :precondition lives: a non-zero positive value
        :precondition health: a non-zero positive value
        :precondition dodge_chance: a percentage ranging from 0.0 - 1.0
        """
        self._dodge_chance = dodge_chance
        super().__init__(name, lives, health)

    def speak(self):
        """Simulates troll speech."""
        print("Grunt")

    def take_damage(self, damage):
        """
        An example of how to override a function and introduce
        specialized behaviour. This troll will attempt to dodge the
        attack before taking damage. The super() method which returns
        the object as an instance of its parent class allows us to
        re-use code and avoid code duplication.

        :param damage: an int
        """
        dodge = random.random()
        print("Dodge: " + str(dodge))
        if dodge > self._dodge_chance:
            super().take_damage(damage)
        else:
            print(f"{self._name} dodged the attack!")

    def __str__(self):
        """ Overrriden to print the troll's current stats"""
        return f"{super().__str__()} Dodge Chance: {self._dodge_chance}"


class Player:
    """
    A player class that is similar to Enemy but does not inherit
    from it. Since the player has a similar interface to Enemy (the same
    public methods and attributes) , it can be used wherever an Enemy
    is expected. This depicts polymorphism using duck-typing and
    interfaces.
    """

    def __init__(self, name="", lives=1, health=40):
        """
        Initializes a player object with a default health of 40 and 1
        life.
        :param name: a string
        :param lives: an int
        :param health: an int
        :precondition lives: a non-zero positive value
        :precondition health: a non-zero positive value
        """
        self._name = name
        self._lives = lives
        self._health = health
        self._original_health = health

    def take_damage(self, damage):
        """
        Simulates damage dealt to this enemy. If this damage causes
        the health of the enemy to go below zero, it's lives are
        decremented.
        :param damage: an int
        """
        self._health -= damage
        print(f"{self._name} took damage. Current health {self._health}")


def deal_damage(an_object):
    """Simulates dealing damage to a Player or an Enemy"""
    an_object.take_damage(7)


def main():
    """
    Some sample code to show inheritance in action. Note how you can
    share behaviours (methods) and data across a wide range of different
    classes and objects. Inheritance is a great way to add special
    behaviour while re-using code.
    """

    # Enemy Objects
    spider = Enemy("Spider")
    print(spider)
    print(type(spider))
    spider.take_damage(7)
    mutant_rat = Enemy("Mutant Rat", 2, 10)
    mutant_rat.take_damage(15)

    # Troll Object
    vudu_troll = Troll("Vudu", 4, 100)
    print(vudu_troll)
    print(type(vudu_troll))
    vudu_troll.take_damage(20)
    vudu_troll.speak()

    print("-------------")

    # Polymorphism through duck-typing and similar interfaces in python.
    deal_damage(spider)
    my_player = Player("P1")
    deal_damage(my_player)
    deal_damage(vudu_troll)

    # How to check type and inheritance
    print(f"Is troll an enemy? {isinstance(vudu_troll, Enemy)}")
    print(f"Is player an enemy? {isinstance(my_player, Enemy)}")
    print(f"Troll type: {type(vudu_troll)}, is equal to enemy: "
          f"{Enemy == Troll}")


if __name__ == '__main__':
    main()
