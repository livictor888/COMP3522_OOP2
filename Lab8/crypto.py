import struct
import des
import argparse
import abc
import enum


class CryptoException(Exception):
    """
    Exception for the Crypto class.
    """
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return "Error: " + self.msg


class CryptoMode(enum.Enum):
    """
    Lists the various modes that the Crypto application can run in.
    """
    # Encryption mode
    EN = "en"
    # Decryption Mode
    DE = "de"


class Request:
    """
    The request object represents a request to either encrypt or decrypt
    certain data. The request object comes with certain accompanying
    configuration options as well as a field that holds the result. The
    attributes are:
        - encryption_state: 'en' for encrypt, 'de' for decrypt
        - data_input: This is the string data that needs to be encrypted or
        decrypted. This is None if the data is coming in from a file.
        - input_file: The text file that contains the string to be encrypted or
        decrypted. This is None if the data is not coming from a file and is
        provided directly.
        - output: This is the method of output that is requested. At this
        moment the program supports printing to the console or writing to
        another text file.
        - key: The Key value to use for encryption or decryption.
        - result: Placeholder value to hold the result of the encryption or
        decryption. This does not usually come in with the request.

    """

    def __init__(self):
        self.desKey = None
        self.encryption_state = None
        self.data_input = None
        self.input_file = None
        self.output = None
        self.key = None
        self.result = None

    def __str__(self):
        return f"Request: State: {self.encryption_state}, Data: {self.data_input}" \
               f", Input file: {self.input_file}, Output: {self.output}, " \
               f"Key: {self.key}"


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="The key to use when encrypting or "
                                    "decrypting. This needs to be of "
                                    "length 8, 16 or 24")
    parser.add_argument("-s", "--string", help="The string that needs to be "
                                               "encrypted or decrypted")
    parser.add_argument("-f", "--file", help="The text file that needs to be"
                                             "encrypted or decrypted")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a file name as well.")
    parser.add_argument("-m", "--mode", default="en",
                        help="The mode to run the program in. If 'en' (default)"
                             " then the program will encrypt, 'de' will cause "
                             "the program to decrypt")
    try:
        args = parser.parse_args()
        request = Request()
        request.encryption_state = CryptoMode(args.mode)
        request.data_input = args.string
        request.input_file = args.file
        request.output = args.output
        request.key = args.key
        print(request)
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


class Crypto:
    """
    Represents a Crypto tool for encrypting and decrypting user inputs.
    """

    def __init__(self):
        """
        Initialize a Crypto object
        """
        self.encryption_start_handler = None
        self.decryption_start_handler = None
        self.initialize_handler_for_encryption()
        self.initialize_handler_for_decryption()

    def initialize_handler_for_encryption(self):
        """
        Initialize the handlers for the encryption mode
        """
        key_reader_handler = Crypto.KeyCheckingHandler()
        source_reader_handler = Crypto.SourceCheckingHandler()
        encryption_handler = Crypto.EncryptionHandler()

        key_reader_handler.set_handler(source_reader_handler)
        source_reader_handler.set_handler(encryption_handler)
        self.encryption_start_handler = key_reader_handler

    def initialize_handler_for_decryption(self):
        """"
        Initialize the handlers for the decryption mode
        """
        key_reader_handler = Crypto.KeyCheckingHandler()
        source_reader_handler = Crypto.SourceCheckingHandler()
        decryption_handler = Crypto.DecryptionHandler()

        key_reader_handler.set_handler(source_reader_handler)
        source_reader_handler.set_handler(decryption_handler)
        self.decryption_start_handler = key_reader_handler

    def execute_request(self, request: Request):
        """
        Execute a request with the
        :param request: a Request object
        :return:
        """
        if request.encryption_state == CryptoMode.EN:
            handler = self.encryption_start_handler
        else:
            handler = self.decryption_start_handler
        try:
            result, is_successful = handler.handle_form(request)

            if is_successful:
                if request.output == 'print':
                    print(result)
                else:
                    with open(request.output, "wb") as open_file:
                        open_file.write(result)
        except CryptoException as error:
            print(error)
        except FileNotFoundError as error:
            print("Error: File not found" + str(error))
        except Exception as error:
            print("Error: " + str(error))

    class CryptoHandlerBase:
        """
        Baseclass for all handlers that handle crypto requests.
        """

        def __init__(self, next_handler=None):
            self.next_handler = next_handler

        @abc.abstractmethod
        def handle_form(self, request: Request) -> (str, bool):
            """
            Each handler inheriting this class has its own implementation of how
            it will process a form.
            :param request: a Request
            :return: a tuple, the first element is a string, the second is a bool
            showing the success of the handling of the form.
            """
            pass

        def set_handler(self, handler):
            """
            Each handler can call another handler at the end of it's processing.
            :param handler: a CryptoHandlerBase
            """
            self.next_handler = handler

    class KeyCheckingHandler(CryptoHandlerBase):
        """
        Check that a key is entered.
        """

        def handle_form(self, request: Request) -> (str, bool):
            if request.key is not None and request.key != '':
                request.desKey = des.DesKey(str.encode(request.key))
                return self.next_handler.handle_form(request)
            else:
                raise CryptoException("Cannot find a key in the input.")

    class SourceCheckingHandler(CryptoHandlerBase):
        """
        Check that text can be read.
        """
        def handle_form(self, request: Request) -> (str, bool):
            if request.data_input:
                if request.encryption_state == CryptoMode.EN:
                    return self.next_handler.handle_form(request)
                else:
                    request.data_input = convert_string_to_bytes(request.data_input)
                    return self.next_handler.handle_form(request)
            elif request.input_file:
                if request.encryption_state == CryptoMode.EN:
                    with open(request.input_file, "r") as open_file:
                        request.data_input = open_file.read()
                else:
                    with open(request.input_file, "rb") as open_file:
                        request.data_input = open_file.read()
                return self.next_handler.handle_form(request)
            else:
                raise CryptoException("Could not find the source content.")

    class EncryptionHandler(CryptoHandlerBase):
        def handle_form(self, request: Request) -> (str, bool):
            if hasattr(request, 'desKey') and request.desKey is not None:
                encrypted_message = request.desKey.encrypt(str.encode(request.data_input), padding=True)
                return encrypted_message, True
            else:
                raise CryptoException("An error occurred while encrypting.")

    class DecryptionHandler(CryptoHandlerBase):
        def handle_form(self, request: Request) -> (str, bool):
            if hasattr(request, 'desKey') and request.desKey is not None:
                decrypted_message = request.desKey.decrypt(request.data_input, padding=True)
                return decrypted_message, True
            else:
                raise CryptoException("An error occurred while decrypting.")


def convert_string_to_bytes(string):
    """
    Convert a string into bytes.
    :param string: a string
    :return: bytes
    """
    converted_bytes = b''
    for i in string:
        converted_bytes += struct.pack("B", ord(i))
    return converted_bytes


def main(request: Request):
    """
    Drives the program.
    :param request: a Request
    """
    crypto = Crypto()
    crypto.execute_request(request)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
