"""This module handles and processes the user's input interacting with the Store."""

from store import Store
from pathlib import Path
from file_handler import InvalidFileTypeError, FileDoesNotExistError, RequiredElementNotFoundException, \
    InvalidCellValueException


class Menu:
    """
    Process the user's input by either processing a new Order or printing the daily transaction report and exiting
    the program.
    """

    store = Store()

    def display_user_menu(self):
        """
        Manage the user's interaction with the Store but processing the user's input.
        """
        while True:
            print("\n--------Welcome to Our Store!--------\n"
                  "1) Place a new order.\n"
                  "2) Check inventory.\n"
                  "3) Create the Daily Transaction Report & Exit the store.\n")
            string_input = input("Please enter your choice (1 - 3):\n")
            menu_input = self.check_integer_input(string_input)
            if menu_input == 1:
                excel_path = input("Please enter the path to the excel file:\n")
                path = Path(excel_path)
                try:
                    Menu.store.order_prod_from_factory(path)
                except (InvalidFileTypeError, FileDoesNotExistError, RequiredElementNotFoundException,
                        InvalidCellValueException) as e:
                    print(f"--------ERROR--------\n{e}\n--------ERROR--------\n")
            elif menu_input == 2:
                Menu.store.check_inventory()
                pass
            elif menu_input == 3:
                Menu.store.create_daily_transaction_report()
                print("Thank you for visiting our Store!")
                return
            else:
                print("Please enter 1 - 3.")

    @staticmethod
    def check_integer_input(string_input):
        """
        Check that the user inputs a valid integer string.
        :param string_input: a string
        :return: an integer
        """
        try:
            integer_input = int(string_input)
            return integer_input
        except ValueError:
            print("Not a valid number input.")
