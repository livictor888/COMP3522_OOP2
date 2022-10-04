"""
This module depicts the use of variable keyword arguments as the
parameter list to initialize a Character Object.
"""


class Character:
    """
    Represents a simple game character with some data.
    """

    # default character data in case all parameters are not provided
    # upon initialization.
    default_character_data = {
        'name': "Untitled",
        'level': 4,
        'max_level': 10,
        'weapon': "Sword",
        'gender': "Male"
    }

    def __init__(self, **kwargs):
        """
        Initializes the character object with the data provided. If all
        the data is not provided then it will fill the missing
        attributes with default values.
        :param kwargs: a dictionary that may contain name, level,
        max_level, weapon, gender.
        """
        print(kwargs)  # keyword argument
        self.character_data = Character.default_character_data #defaulting character data
        print("Kwargs max level: " + str(kwargs["max_level"])) #directly access single value with key in kwargs
        print("Kwargs items(): " + str(kwargs.items()))

        # for key, item in kwargs.items():
        #     self.character_data[key] = item

    def __getitem__(self, key):
        """
        Get Item protocol to access character data by key values
        directly.
        :param key: the name of the attribute as a string
        :return: the value of that attribute.
        """
        return self.character_data[key]


def main():
    """
    Initializes a character object using variable keyword arguments.
    """
    my_character = Character(name="Zorak the Destroyer", max_level=100,
                             level=99)
    print(f'Name: {my_character["name"]}')
    print(f'Weapon: {my_character["weapon"]}') #default weapon
    print(f'Gender: {my_character["gender"]}') #default gender
    print(f'Level: {my_character["level"]}')
    print(f'Max Level: {my_character["max_level"]}')


if __name__ == '__main__':
    main()
