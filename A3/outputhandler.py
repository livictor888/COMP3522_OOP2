"""This module handles the output of the program."""


class OutputHandler:
    """
    A utility class to handle either output mode (terminal or write to file)
    """

    @staticmethod
    def handle_output(request):
        """
        Based on the user's input, it will either write to file or print the result of the pokedex query.
        :param request: a Request object containing the information to be written
        """
        if (request.output_file is not None) and (len(request.pokedex_items) != 0):
            try:
                with open(request.output_file, "w") as file:
                    for item in request.pokedex_items:
                        file.write(item.__str__())
            except Exception as e:
                print("Error: Could not write the data into the specified output file: ", e)
        else:
            for item in request.pokedex_items:
                print(item)
