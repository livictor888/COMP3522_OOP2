"""This module handles and processes the user's input interacting with the FAM app"""

import itertools
from transaction import Transaction
from validator import Validator


class UserMenu:
    """
    Log in as a registered user and display the FAM program menu.
    """

    def __init__(self, user_list):
        """
        Initialize the menu with the list of users.
        """
        self._user_list = user_list
        self._user_count = len(user_list)
        self._current_user = None

    def display_user_menu(self):
        """
        Select a user and show the menu options.
        """
        profile_input = None
        while profile_input not in range(1, self._user_count + 1):
            print(f"\nWelcome, the registered users are:")
            print("-----------------------")

            profile_count = itertools.count(1)
            for profile in self.user_list:
                print(f"{next(profile_count)}: {profile.get_user_name()}")

            string_input = input("Enter the number for the user you want to log in as: \n")
            profile_input = self.check_integer_input(string_input)

        self._current_user = self._user_list[profile_input - 1]
        print("Logging in...\n")

        menu_input = None
        while menu_input != 6:
            print(f"\nWelcome, {self._current_user.get_user_name()}!")
            print("-----------------------")
            print("1. View budgets")
            print("2. View transactions by budget")
            print("3. View bank account details")
            print("4. Record a transaction")
            print("5. Switch user")
            print("6. Quit")

            string_input = input("Please enter your choice (1-6)\n")

            menu_input = self.check_integer_input(string_input)

            if menu_input == 1:
                self.view_budgets()
            elif menu_input == 2:
                self.view_transactions_by_budget()
            elif menu_input == 3:
                self.view_bank_account_detail()
            elif menu_input == 4:
                self.record_transaction()
            elif menu_input == 5:
                self.switch_user()
            elif menu_input == 6:
                pass
            else:
                print("Please enter a number from 1 - 6.")

    @property
    def user_list(self):
        """ Get the user list."""
        return self._user_list

    @property
    def current_user(self):
        """ Get the current active user."""
        return self._current_user

    def switch_user(self):
        """
        Switch to another user in the user list.
        """
        user_selection = None
        while user_selection not in range(1, self._user_count + 1):
            profile_count = itertools.count(1)
            for user in self._user_list:
                print(f"{next(profile_count)}: {user.get_user_name()}")

            string_input = input(f"Enter the number of the user you want to switch to: \n")
            user_selection = self.check_integer_input(string_input)

        self._current_user = self._user_list[user_selection - 1]

    def view_budgets(self):
        """
        Print the status of all the available budget categories of the current user.
        """
        for k, v in self._current_user.get_budgets().items():
            print(k)
            print(v)

    @staticmethod
    def prompt_for_correct_transaction_amount():
        """
        Accept a valid dollar amount from the user, otherwise raise an error.
        """
        flag = False
        transaction_amount = -1
        while not flag:
            transaction_amount = input(f"Enter the dollar amount of the transaction: \n")
            try:
                if len(transaction_amount.rsplit('.')) != 2 or len(transaction_amount.rsplit('.')[-1]) != 2:
                    raise ValueError(
                        "The transaction amount must be formatted with two decimal places and a decimal point")
                transaction_amount = float(transaction_amount)
                if not transaction_amount > 0:
                    raise ValueError("The transaction amount must be a positive float (a number with a decimal point)")
            except ValueError as error:
                print("Error:", error)
                continue
            transaction_amount = float(transaction_amount)
            flag = True
        return transaction_amount

    def record_transaction(self):
        """
        Create a transaction object using inputs from the user and sent it to the bank for processing.
        """
        if self._current_user.get_lockout_status():
            print("Locked: This user is locked out of making any more transactions.")
            return

        user_selection = -1
        budget_categories_available = self._current_user.get_budgets().keys()
        while user_selection not in range(1, len(budget_categories_available) + 1):
            budget_count = itertools.count(1)
            for budget in budget_categories_available:
                print(f"{next(budget_count)}: {budget}")

            string_input = input(f"Enter the budget category of the transaction: \n")
            user_selection = self.check_integer_input(string_input)

        budget_category = list(budget_categories_available)[user_selection - 1]

        dollar_amount = self.prompt_for_correct_transaction_amount()

        user_selection = input(f"Enter the store name: \n")
        while self.check_blank_input(user_selection):
            user_selection = input(f"Enter the store name: \n")

        shop_name = user_selection

        new_transaction = Transaction(self._current_user, dollar_amount, budget_category, shop_name)
        validator = Validator(self._current_user, new_transaction)
        if validator.validate():
            print("Notification: Transaction added successfully.")
        else:
            print("Notification: Could not add this transaction.")

    def view_transactions_by_budget(self):
        """
        Print the current user's list of transaction sorted by budget category.
        """
        for budget_category in self._current_user.get_budgets().keys():
            print(f"{budget_category} transactions:")
            for transaction in self._current_user.get_all_transactions():
                if transaction.budget_category == f"{budget_category}":
                    print(f"{transaction.get_dict()['shop_name']} {transaction.get_dict()['dollar_amount']:0.2f}")
            print("\n")

    def view_bank_account_detail(self):
        """
        Print the current user's bank account details.
        :return:
        """
        self._current_user.get_bank_account().create_bank_statement()

    @staticmethod
    def check_blank_input(string_input):
        """
        Check that the user inputs a non-empty string.
        :param string_input: a string
        :return: a boolean
        """
        if string_input.isspace() or (len(string_input) == 0):
            print("Input cannot be blank.")
            return True
        return False

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

    @staticmethod
    def check_dollar_amount_format(string_input):
        """
        Check that the user inputs a valid dollar amount.
        :param string_input: a string
        :return: a float
        """
        if len(string_input.rsplit('.')[-1]) != 2:
            raise ValueError("The account balance must be formatted with two decimal places and a decimal point")
        return float(string_input)
