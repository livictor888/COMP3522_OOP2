"""This module depicts the use of a custom exception."""


class InvalidCharacterError(Exception):
    """
    The InvalidCharacterError (It's a pun! Get it? .. no? ... FINE) is
    an exception that should be raised when a string is encountered that
    has an invalid character in it (what those invalid characters are
    depends on the context that the string is used in).
    """

    def __init__(self, invalid_char):
        """
        Instantiates the exception with the following message: "Error!
        Invalid character detected!"
        :param invalid_char: a single character, the invalid character
        detected
        """
        super().__init__(f"Error! Invalid character detected!")
        self.invalid_char = invalid_char


class Character:
    """
    Responsible for depicting a character with a name. The name cannot
    have special characters in it.
    """

    # The list of invalid characters that can't appear in the name
    invalid_chars = ['!', '@', '_', '<', '>', '$']

    def __init__(self, name):
        """
        Inititalizes the character with the specified name. Raises a
        InvalidCharacterError if the name contains special characters.
        :param name: a string
        :precondition name: Does not contain any special characters.
        """
        #'Z0r4k th3 d3$troy3r'
        for i in Character.invalid_chars:
            if i in name:
                # send '$' into i
                raise InvalidCharacterError(i)
        self.name = name


def main():
    """
    Attempts to create a character with an invalid name. Uses the
    try-except-else-finally construct to handle exceptions.
    """

    try:
        name = 'Z0r4k th3 d3troy3r'
        print(f"Creating character: {name}")
        zorak = Character(name)
    except InvalidCharacterError as e:
        print(e)
        print(f"Invalid character: {e.invalid_char}")
    else:
        print(f"Everything's fine - Character {zorak.name} created.")
    finally:
        print("Program execution complete.")

if __name__ == '__main__':
    main()
