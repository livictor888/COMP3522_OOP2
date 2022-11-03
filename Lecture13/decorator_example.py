"""
This module depicts the decorator pattern in action and how it adds
encryption/decryption and compression/decompression behaviours to a
DataSource dynamically based on the user configuration.

Refer to Decorator_Datasource_UML.png for the associated UML diagram.
"""

import abc

class DataSource(abc.ABC):
    """
    The Data Source interface that all concrete Data Sources and
    decorators must adhere to. This interface defines a read and write
    abstract method that do not have an implementation.
    """
    @abc.abstractmethod
    def read(self):
        pass

    @abc.abstractmethod
    def write(self, data):
        pass


class FileDataSource(DataSource):
    """
    A FileDataSource is responsible for reading and writing to a file.
    It implements the DataSource Interface as defined by the parent
    DataSource class. This is the object that we want to add optional
    behaviours to.
    """
    def __init__(self, destination_file):
        self.destination_file = destination_file

    def read(self):
        data = None
        with open(self.destination_file, mode='r', encoding='utf-8') as \
            target_file:
            data = target_file.read()
        return data

    def write(self, data):
        with open(self.destination_file, mode='w', encoding='utf-8') as \
                target_file:
            target_file.write(data)


class BaseDataSourceDecorator(DataSource):
    """
    This is the base decorator. This is a wrapper around a
    ConcreteDataSource (such as FileDataSource) and does not add any new
    behaviours or implementation. All other decorators inherit from this
    class.
    """
    def __init__(self, data_source):
        self.data_source = data_source

    @abc.abstractmethod
    def write(self, data):
        self.data_source.write(data)

    @abc.abstractmethod
    def read(self):
        return self.data_source.read()


class EncryptedDataSourceDecorator(BaseDataSourceDecorator):
    """
    This is a decorator (read: wrapper) that adds an
    encryption/decryption behaviour to a datasource. This decorator can
    wrap around a concrete DataSource (like FileDataSource) or it can
    also wrap around another Decorator.

    The encryption converts each letter to its ASCII code, while the
    decryption algorithm does the same.
    """

    def write(self, data):
        """
        Encrypts the given data and calls the write function of the
        DataSource that is being wrapped around.
        :param data: a string
        :return: None
        """
        # convert each letter to its int ASCII code
        encrypted_data = [ord(i) for i in data]
        # convert each element of the list to a string
        encrypted_data = [str(i) + " " for i in encrypted_data]
        # convert from a list to a string
        encrypted_data = ''.join(encrypted_data)
        print(f"Writing encrypted  {data} as {encrypted_data}")
        # call the object that this class is wrapped around. This could
        # be another DataSource or another Decorator.
        super().write(encrypted_data)
        print(f"Finished writing encrypted data {encrypted_data}")

    def read(self):
        """
        Reads data from a data source and decrypts it to a string value.
        :precondition: The data being read is encrypted where each
        character is represented by its ASCII code.
        :return: the data read as a string
        """
        print("reading encrypted data")
        # read data from the object that this class is wrapped around.
        encrypted_data = super().read()
        #split the data around spaces to form a list of ASCII codes
        encrypted_data = encrypted_data.split()
        # convert each element of the list to an integer
        encrypted_data = [int(i) for i in encrypted_data]
        # convert each element from an int to a character and then
        # use the join method to create a string.
        decrypted_data = [chr(i) for i in encrypted_data]
        data = ''.join(decrypted_data)
        print(
            f"Encrypted data {encrypted_data} read and decrypted into {data}")
        return data


class CompressedDataSourceDecorator(BaseDataSourceDecorator):
    """
    This is a decorator (read: wrapper) adds compression/decompression
    behaviour to a datasource (just place holder print statements for
    this example). This decorator can wrap around a concrete DataSource
    (like FileDataSource) or it can also wrap around another Decorator
    (like the EncryptionDataSourceDecorator).
    """

    def read(self):
        """
        "Decompress" the data read from the object that this decorator
        is wrapped around.
        :return: the data read as a string
        """
        data = super().read()
        print(f"Read and decompressed {data}")
        return data

    def write(self, data):
        """
        "Compress" data before writing it to a data source that this
        decorator is wrapped around.
        :param data: a string
        :return: None
        """
        print(f"Compressing {data}")
        super().write(data)
        print(f"Compressed {data} written")


def main():
    """
    Prompt the user to find out if compression and encryption is enabled.
    Accordingly wrap the FileDataSource and write "Hello world" to a
    file.
    """
    data_source = FileDataSource("decorator_test.txt")

    has_encyption = input("Has encryption? Y/N")
    if has_encyption.lower() == 'y':
        has_encyption = True
    else:
        has_encyption = False

    has_compression_option = input("Has compress option? Y/N")
    if has_compression_option.lower() == 'y':
        has_compression_option = True
    else:
        has_compression_option = False

    if has_compression_option:
        # wrap the CompressedDataSource around the current data source
        # and overwrite the variable reference.
        data_source = CompressedDataSourceDecorator(data_source)
    if has_encyption:
        # wrap the EncryptedDataSource around the current data source
        # and overwrite the variable reference.
        data_source = EncryptedDataSourceDecorator(data_source)

    data_source.write("Hello World")

if __name__ == '__main__':
    main()
