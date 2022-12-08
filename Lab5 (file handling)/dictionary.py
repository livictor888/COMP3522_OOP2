"""This module houses the dictionary."""
from file_handler import FileHandler
from pathlib import Path


class Dictionary:
    """
    Represents a Dictionary.
    """
    FILE_HANDLER = FileHandler()

    def __init__(self):
        """
        Initialize the Dictionary with an empty dictionary.
        """
        self._dict = {}

    def load_dictionary(self, file_content):
        """
        Loads data into a dictionary.

        :param file_content:
        :return:
        """
        self._dict = file_content

    def query_dictionary(self, word):
        """
        Returns the definition(s) of a given word for a valid dictionary query.
        Returns None if it was an invalid dictionary query.
        :param word: a string
        :return: the definition(s) of a given word for a valid dictionary query, otherwise returns None
        """
        try:
            if word.lower() not in self._dict.keys():
                raise WordNotFoundError()
        except WordNotFoundError as e:
            print(e)
            return None
        else:
            definitions_list = self._dict[word.lower()]
            for item in definitions_list:
                print(item)
            return definitions_list


class WordNotFoundError(Exception):
    """
    Raises an exception if the queried word does not exist in the dictionary.
    """
    def __init__(self):
        super().__init__(f"Error: The word does not exist in the dictionary.")


def main():
    """
    Drives the program.
    """
    file_handler = FileHandler()
    my_dict = Dictionary()
    input_file_path = input("Input file path: ").strip()
    input_file_extension = Path(input_file_path).suffix
    content = file_handler.load_data(input_file_path, input_file_extension)
    my_dict.load_dictionary(content)
    output_file_path = input("Output file path: ").strip().lower()
    query_word = input("Query word: ")

    while not query_word == "exitprogram":
        query_result = my_dict.query_dictionary(query_word)
        query_result_dict = dict()
        query_result_dict[query_word] = query_result
        if query_result is not None:
            file_handler.write_lines(output_file_path, query_result_dict)
        query_word = input("Query word: ")


if __name__ == '__main__':
    main()
