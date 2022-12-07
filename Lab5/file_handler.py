"""This module houses the file handler."""
import json
from json import loads
from file_extensions import FileExtensions
from pathlib import Path


class FileHandler:
    """
    Represents a file handler that is responsible for reading and writing to files.
    """
    @staticmethod
    def load_data(path, file_extension):
        """
        Checks file extension, reads the file accordingly, and returns the file content if no exception occurs.

        :param path: a string
        :param file_extension: a string
        :return: contents of the file as a dictionary
        """
        my_path = Path(path)
        try:
            if FileExtensions.JSON.value != file_extension.lower():
                raise InvalidFileTypeError()
            if not my_path.is_file():
                raise FileDoesNotExistError()
            if not path == "data.json":
                raise WrongFileError()
        except InvalidFileTypeError as e:
            print(e)
        except FileDoesNotExistError as e:
            print(e)
        except WrongFileError as e:
            print(e)
        else:
            try:
                with open(path, mode='r', encoding='utf-8') as my_file:
                    contents = loads(my_file.read())
            except IOError:
                print("Error: An error occurred when opening and reading the file.")
            else:
                return contents

    @staticmethod
    def write_lines(path, lines):
        """
        Writes the given lines to a file.

        :param path: a string
        :param lines: a dictionary
        """
        file_extension = Path(path).suffix
        try:
            if file_extension.lower() not in (FileExtensions.JSON.value, FileExtensions.TXT.value):
                raise InvalidFileTypeError()
        except InvalidFileTypeError as e:
            print(e)

        with open(path, mode='a', encoding='utf-8') as my_file:
            json_data = json.dumps(lines)
            my_file.write(json_data)
            my_file.write("\n")


class InvalidFileTypeError(Exception):
    """
    Raises exception if the user attempts to read a file that's not a json or txt file.
    """
    def __init__(self):
        super().__init__(f"Error: Invalid file type error.")


class FileDoesNotExistError(Exception):
    """
    Raises an exception if the file does not exist.
    """
    def __init__(self):
        super().__init__(f"Error: File does not exist.")


class WrongFileError(Exception):
    """
    Raises an exception if the wrong file is entered.
    """
    def __init__(self):
        super().__init__(f"Error: Wrong file entered. The only valid input file is data.json.")
