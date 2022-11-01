"""
This module depicts the use of the Abstract Factory Pattern for a game
that needs groups of characters for different worlds.
"""
import abc
import random
import enum


class WorldEnum(enum.Enum):
    AQUATICA = 0,
    FIRELANDS = 1


class Friendly(abc.ABC):
    """
    Friendly defines the interface for one of the products that the
    abstract factory pattern is responsible to create.
    """

    def __init__(self, name, health):
        self.name = name
        self.health = health


    @abc.abstractmethod
    def talk(self):
        pass


class MerPerson(Friendly):
    """
    MerPerson is a type of Friendly usually found in the Aquatica World.
    """

    def __init__(self):
        super().__init__("MerPerson", 50)

    def talk(self):
        print("Hi! I am a MerPerson!")


class FireSprite(Friendly):
    """
    FireSprite is a type of Friendly usually found in the Firelands
    World.
    """

    def __init__(self):
        super().__init__("FireSprite", 100)

    def talk(self):
        print("Hi! I am a FireSprite! I like hot chocolate.")


class Enemy(abc.ABC):
    """
    Enemy defines the interface for one of the products that the
    abstract factory pattern is responsible to create.
    """

    @abc.abstractmethod
    def __init__(self, name, health, strength, dodge_chance):
        self.name = name
        self.health = health
        self.strength = strength
        self.dodge_chance = dodge_chance

    def attack(self):
        print(f"{self.name}attacks your ship.")

    def defend(self) -> bool:
        if random.random() < self.dodge_chance:
            return True
        return False


class Kraken(Enemy):
    """
    Kraken is an enemy generally found in the Aquatica World
    """
    def __init__(self):
        super().__init__("Mr. Kraken", 90, 100, 0.3)


class Imp(Enemy):
    """
    Imp is an enemy generally found in the Firelands World.
    """
    def __init__(self):
        super().__init__("Imp Minion", 20, 20, 0.5)


class Animal(abc.ABC):
    """
    Animal defines the interface for one of the products that the
    abstract factory is responsible to create
    """

    @abc.abstractmethod
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self):
        print(f"{self.name} moves {self.speed} squares")


class Jellyfish(Animal):
    """
    Jellyfish is an animal that is generally found in the Aquatica World
    """

    def __init__(self):
        super().__init__("Jellyfish Critter", 2)


class Firefly(Animal):
    """
    Firefly is an animal that is generally found in the Firelands world
    """

    def __init__(self):
        super().__init__("Firefly Critter", 9)


class CharacterFactory(abc.ABC):
    """
    The base factory class. All worlds expect this factory class to
    populate the world. The CharacterFactory class defines an interface
    to create the a Product family consisting of Friendlies, Enemies,
    and Animals. These vary by world.
    """

    @abc.abstractmethod
    def create_friendly(self) -> Friendly:
        pass

    @abc.abstractmethod
    def create_enemy(self) -> Enemy:
        pass

    @abc.abstractmethod
    def create_animal(self) -> Animal:
        pass


class AquaticaCharacterFactory(CharacterFactory):
    """
    This factory class implements the CharacterFactory Interface. It
    returns a product family consisting of MerPersons, Krakens, and
    Jellyfish.
    """

    def create_friendly(self) -> Friendly:
        """
        :return: returns a MerPerson
        """
        return MerPerson()

    def create_enemy(self) -> Enemy:
        """
        :return: Returns a Kraken
        """
        return Kraken()

    def create_animal(self) -> Animal:
        """
        :return: Returns a Jellyfish
        """
        return Jellyfish()


class FirelandsCharacterFactory(CharacterFactory):
    """
    This factory class implements the CharacterFactory Interface. It
    returns a product family consisting of FireSprites, Imps and
    Fireflies
    """

    def create_friendly(self) -> Friendly:
        """
        :return: Returns a FireSprite.
        """
        return FireSprite()

    def create_enemy(self) -> Enemy:
        """
        :return: Returns an Imp.
        """
        return Imp()

    def create_animal(self) -> Animal:
        """
        :return: Returns a firefly.
        """
        return Firefly()


class WorldPopulator:
    """
    Maintains a mapping of world -> CharacterFactory. The WorldPopulator
    is responsible for retrieving the right factory for the specified
    world.
    """

    # Maps world types to their respective factories
    world_factory_mapper = {
        WorldEnum.AQUATICA : AquaticaCharacterFactory,
        WorldEnum.FIRELANDS : FirelandsCharacterFactory
    }

    def get_factory(self, world_type: WorldEnum) -> CharacterFactory:
        """
        Retrieves the associated factory for the specified WorldEnum
        :param world_type: WorldEnum
        :return: a CharacterFactory if found, None otherwise
        """
        factory_class = self.world_factory_mapper.get(world_type)
        return factory_class()


class World:
    """
    Defines a world that consists of fFriendlies, Enemies and Animals.
    Each world has a theme/variety.
    """

    def __init__(self, char_factory: CharacterFactory):
        """
        Instantiates a world with the specified character factory. The
        Character Factory specifies which type of characters inhabit
        this world.
        :param char_factory: a Character Factory
        """
        self.friendlies = []
        self.enemies = []
        self.animals = []
        self.world_populator_factory = char_factory

        for i in range(5):
            self.friendlies.append(self.world_populator_factory.create_friendly())

        for i in range(5):
            self.enemies.append(self.world_populator_factory.create_enemy())

        for i in range(5):
            self.animals.append(self.world_populator_factory.create_animal())

    def simulate(self):
        """
        Simulates behaviour of all the characters in this world.
        :return:
        """
        for friendly in self.friendlies:
            friendly.talk()

        for enemy in self.enemies:
            print(f"{enemy.name} tried to defend! Success: "
                  f"{enemy.defend()}")

        for animal in self.animals:
            animal.move()


def main():
    populator = WorldPopulator()
    #factory = populator.get_factory(WorldEnum.AQUATICA)
    factory = populator.get_factory(WorldEnum.FIRELANDS)

    world = World(factory)
    world.simulate()


if __name__ == '__main__':
    main()





