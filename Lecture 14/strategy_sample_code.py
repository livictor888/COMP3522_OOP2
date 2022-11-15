import abc
"""
This code simulates a game where characters can swap weapons at any time to attack other characters
"""

# strategy interface
class Weapon(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        self.damage = 0

    @abc.abstractmethod
    def attack(self, enemy):
        return self.damage

# concrete strategy
class Sword(Weapon):
    def __init__(self):
        self.damage = 5

    def attack(self, enemy):
        print(f"hit {enemy.name} with a Sword for {self.damage} damage")
        enemy.health -= self.damage
        return self.damage

# concrete strategy
class Spear(Weapon):
    def __init__(self):
        self.damage = 10

    def attack(self, enemy):
        print(f"hit {enemy.name} with a Spear for {self.damage} damage")
        enemy.health -= self.damage
        return self.damage

# concrete strategy
class BowAndArrow(Weapon):
    def __init__(self):
        self.damage = 15

    def attack(self, enemy):
        print(f"hit {enemy.name} with a Bow and Arrow for {self.damage} damage")
        enemy.health -= self.damage
        return self.damage

# concrete strategy
class Cannon(Weapon):
    def __init__(self):
        self.damage = 75

    def attack(self, enemy):
        print(f"hit {enemy.name} with a Cannon for {self.damage} damage")
        enemy.health -= self.damage
        return self.damage

# context
class Character:
    def __init__(self, name, health, weapon):
        self.name = name
        self.weapon = weapon #use strategy
        self.health = health

    def set_weapon(self, weapon):
        self.weapon = weapon

    def attack(self, enemy):
        print(f"{self.name}", end = " ")
        damage = self.weapon.attack(enemy) #calling strategy to perform its behavior
        return damage

    def __str__(self):
        return f"{self.name} has {self.health} health"

def main():
    #create strategies
    sword = Sword()
    spear = Spear()
    bow_and_arrow = BowAndArrow()
    cannon = Cannon()

    #create contexts. Contexts are using the sword strategy initially
    aragorn = Character("Aragorn", 100, sword)
    sauron = Character("Sauron", 100, spear)

    # aragorn attacks with the sword with which it was initialized
    aragorn.attack(sauron)

    #aragorn can dynamically change attack behavior by changing the weapon
    aragorn.set_weapon(spear)
    aragorn.attack(sauron)

    # aragorn can dynamically change attack behavior by changing the weapon
    aragorn.set_weapon(bow_and_arrow)
    aragorn.attack(sauron)

    sauron.attack(aragorn)

    # sauron can dynamically change attack behavior by changing the weapon
    sauron.set_weapon(cannon)
    sauron.attack(aragorn)

    # print character name and health
    print(aragorn)
    print(sauron)


if __name__ == '__main__':
    main()