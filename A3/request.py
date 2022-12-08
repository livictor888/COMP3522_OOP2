"""This represents a Request."""
import enum
import argparse


class PokedexMode(enum.Enum):
    """
    Lists the various modes that the pokedex can be in.
    """
    POKEMON = "pokemon"
    ABILITY = "ability"
    MOVE = "move"


class Request:
    """
    The request object represents a request for data about a pokemon, ability or move.
    The request object comes with certain accompanying
    configuration options as well as a field that holds the pokedex items. The
    attributes are:
        - mode: pokemon, ability or move
        - input_data: This is the string data (name or id) that needs to be queried.
        This is None if the data is coming in from a file.
        - input_file: The path of the input file
        - output_file: This is the method of output that is requested. At this
        moment the program supports printing to the console or writing to
        another text file.
        - expanded: a boolean indicating if the expanded information mode has been specified
        - input: a list to hold the query params specified, from the terminal or a text file
        - current_item: a string from input_data to be queried
        - pokedex_items: a list of PokedexObjects
    """

    def __init__(self):
        self.mode = None
        self.input_data = None
        self.input_file = None
        self.output_file = None
        self.expanded = None
        self.input = []
        self.current_item = None
        self.pokedex_items = []

    def __str__(self):
        return f"Mode: {self.mode}, Input data: {self.input_data}" \
               f", Input file: {self.input_file}, Output: {self.output_file}, " \
               f"Expanded: {self.expanded}, Input: {self.input}"


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

    # FIRST POSITIONAL ARGUMENT
    parser.add_argument("mode", help="pokemon, ability, or move", nargs="?", choices=("pokemon", "ability", "move"))

    # SECOND POSITIONAL ARGUMENT
    group_input = parser.add_mutually_exclusive_group()
    group_input.add_argument("--inputfile",
                             help="Input a file, offer a file path", type=str, nargs=1)
    group_input.add_argument("--inputdata",
                             help="Input data, offer a name or an id", type=str, nargs=1)

    # THIRD POSITIONAL ARGUMENT
    parser.add_argument("--expanded", action="store_true",
                        help="Expand the inner JSON.")

    # FOURTH POSITIONAL ARGUMENT
    parser.add_argument("--output",
                        help="Output file, offer a file path", type=str, nargs=1)
    try:
        args = parser.parse_args()
        request = Request()

        # assign mode
        if args.mode == "pokemon":
            request.mode = PokedexMode.POKEMON
        elif args.mode == "ability":
            request.mode = PokedexMode.ABILITY
        else:
            request.mode = PokedexMode.MOVE

        # input file .txt or input data: eg pikachu OR 25
        if args.inputfile is not None:
            request.input_file = args.inputfile[0]
        else:
            request.input_data = args.inputdata[0].lower()

        # enable expanded
        request.expanded = args.expanded

        # output path name with .txt
        if args.output:
            request.output_file = args.output[0]
        else:
            request.output_file = None

        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


def main():
    """Drives the program from the command line"""
    setup_request_commandline()


if __name__ == '__main__':
    main()
