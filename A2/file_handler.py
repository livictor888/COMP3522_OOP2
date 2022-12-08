"""This module is responsible for reading and writing to txt and json files."""
import os
import pandas as pd
import numpy as np


class InvalidFileTypeError(Exception):
    """
    This class represents the exception where the file type extension is invalid.
    """

    def __init__(self):
        super().__init__('Error: Invalid file extension. Can only work with XLSX file type.')


class FileDoesNotExistError(Exception):
    """
    Raises an exception if the file does not exist.
    """

    def __init__(self):
        super().__init__("Error: File does not exist. Please enter a valid file path.")


class RequiredElementNotFoundException(Exception):
    """
    Raises an exception if a required element in a column is not found.
    """

    def __init__(self):
        super().__init__("Error: A required value is missing from order_number, holiday, item, or quantity.")


class InvalidCellValueException(Exception):
    """
    Raises an exception if an invalid cell value for required column is round.
    """

    def __init__(self):
        super().__init__("Error: An invalid cell value exists in order_number, holiday, item, or quantity.")


class FileHandler:
    """
    This class represents utility functions for reading and writing into files.
    """

    @staticmethod
    def load_data(path):
        """
        Returns the data contained in the specified path.
        :param path: a Path
        :return: a dataframe
        """
        FileHandler.check_file_extension(path)
        FileHandler.check_file_exists(path)
        dataset = pd.read_excel(path, engine='openpyxl',
                                names=('order_number', 'holiday', 'item', 'name', 'quantity',
                                       'product_id', 'description', 'has_batteries', 'min_age',
                                       'dimensions', 'num_rooms', 'speed', 'jump_height', 'has_glow',
                                       'spider_type', 'num_sound', 'colour', 'has_lactose', 'has_nuts',
                                       'variety', 'pack_size', 'stuffing', 'size', 'fabric'))

        FileHandler.check_required_columns(dataset)

        for column in dataset:
            dataset[column] = dataset[column].fillna(np.nan).replace([np.nan], [None])

        return dataset

    @staticmethod
    def check_file_extension(path):
        """
        Checks that the specified path's extension is valid ("xlsx").
        :param path: a Path
        """
        extension = path.suffix
        if extension.lower() != ".xlsx":
            raise InvalidFileTypeError

    @staticmethod
    def check_file_exists(path):
        """
        Checks that the specified path's extension is valid ("xlsx").
        :param path: a Path
        """
        if not os.path.isfile(path):
            raise FileDoesNotExistError

    @staticmethod
    def check_required_columns(data):
        """
        Checks that required columns order_number, holiday, item, and quantity do not have any empty values
        and checks that these values are valid
        :param data: a dataframe
        """
        fundamental_columns = ['order_number', 'holiday', 'item', 'quantity']
        for column in fundamental_columns:
            if data[column].isnull().values.any():
                raise RequiredElementNotFoundException
            if (column == 'order_number') and (len(data) != data[column].nunique()):
                raise InvalidCellValueException
            if (column == 'quantity') and ((data[column] <= 0).values.any()):
                raise InvalidCellValueException
