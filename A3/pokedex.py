from request import setup_request_commandline
from pokefacade import PokeFacade
from requesthandler import RequestValidator
from outputhandler import OutputHandler


def main():
    """Drives the program by processing and validating the user's request."""

    request = setup_request_commandline()
    request_validator = RequestValidator()
    validated_request = request_validator.validate_request(request)
    if validated_request:
        pokefacade = PokeFacade()
        for input_item in request.input:
            request.current_item = input_item
            pokedex_object = pokefacade.execute_request(validated_request)
            if pokedex_object is not None:
                validated_request.pokedex_items.append(pokedex_object)
        OutputHandler.handle_output(validated_request)


if __name__ == '__main__':
    main()
