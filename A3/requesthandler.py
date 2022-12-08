"""This module contains the Request Validation Chain of Responsibility classes."""

from request import Request
import abc
import os
from request import PokedexMode


class BaseRequestHandler(abc.ABC):
    """
    Baseclass for all handlers that handle requests for pokedex query.
    """
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abc.abstractmethod
    def handle_request(self, request: Request) -> (str, bool):
        """Handles the request"""
        pass

    def set_handler(self, handler):
        """Sets the next handler in the chain"""
        self.next_handler = handler


class ValidateMode(BaseRequestHandler):
    """
    This handler ensures that the request mode is one of pokemon, ability, or move.
    """
    def handle_request(self, request: Request) -> (str, bool):
        if request.mode in PokedexMode:
            if not self.next_handler:
                return "", True
            return self.next_handler.handle_request(request)
        else:
            return "Mode can only be pokemon, ability, or move.", False


class ValidateInput(BaseRequestHandler):
    """
    This handler ensures that either data from the terminal or a valid inputfile exists.
    """
    def handle_request(self, request: Request) -> (str, bool):
        """
        Checks to see if any input has been specified.
        :param request: a Request
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating
        successful handling of the request or not.
        """
        if request.input_file is None and request.input_data is None:
            return "No data or file has been specified", False
        if request.input_file is not None and request.input_data is not None:
            return "Cannot specify a string and an input-file. Pick one!", False
        if request.input_data is not None and len(request.input_data) == 0:
            return "Input data cannot be empty, please specify a name or id.", False
        if request.input_file is not None and not request.input_file.endswith('.txt'):
            return "The file must be .txt!", False
        if request.input_file is not None and not os.path.exists(request.input_file):
            return "Input file not found", False
        if request.input_file is not None and os.stat(request.input_file).st_size == 0:
            return "Input file cannot be empty.", False
        if request.input_data is not None:
            request.input.append(request.input_data.lower())
        if request.input_file is not None:
            with open(request.input_file) as f:
                for line in f:
                    request.input.append(line.strip().lower())
        if not self.next_handler:
            return "", True
        return self.next_handler.handle_request(request)


class ValidateOutputFile(BaseRequestHandler):
    """
    This handler ensure that the output file format is .txt.
    """

    def handle_request(self, request: Request) -> (str, bool):
        """
        Checks to see if the output file exists.
        :param request: a Request
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating
        successful handling of the request or not.
        """
        if request.output_file is not None and not request.output_file.endswith('.txt'):
            return "The file must be .txt!", False
        if not self.next_handler:
            return "", True
        return self.next_handler.handle_request(request)


class RequestValidator:
    """
    A utility class to define the chain of responsibility by linking the handlers and validate the request object.
    """

    def __init__(self):
        """
        Initializes the request handler chain.
        """
        mode_validator = ValidateMode()
        input_validator = ValidateInput()
        output_validator = ValidateOutputFile()

        mode_validator.set_handler(input_validator)
        input_validator.set_handler(output_validator)

        self.request_handler = mode_validator

    def validate_request(self, request):
        """
        Returns a validated request or prints the error.
        :param request: a Request
        :return: a validated Request object, or error message.
        """
        result = self.request_handler.handle_request(request)
        if result[1]:
            return request
        else:
            print("----Invalid Request!---")
            print(result[0])
            return False
