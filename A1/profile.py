"""This module controls the creation of users"""

from dateutil.parser import parse
from datetime import date
import re
from budget import Budget
from chequing import Chequing
from savings import Savings
from angel import Angel
from troublemaker import Troublemaker
from rebel import Rebel
from usermenu import UserMenu


class Profile:
    """This class controls the creation of users"""

    USER_TYPES = ("Angel", "Troublemaker", "Rebel")
    BANK_ACCOUNT_TYPES = ("Checking", "Savings")
    BUDGET_TYPES = ("Games and Entertainment", "Clothing and Accessories", "Eating Out", "Miscellaneous")
    USER_TYPE_AGE_LIMIT = {"Angel": 16}

    def __init__(self):
        """
        Initialize the user list
        """
        self._user_list = []

    @staticmethod
    def get_budget_info(budget_type):
        """
        Creates a budget of the passed budget type
        and checks that the budget information
        passed is correct
        :param budget_type: a string
        :return: a budget
        """
        validate_info = False
        budget_limit = 0
        while validate_info is False:
            budget_limit = input(f"Enter a budget limit for {budget_type} (with two decimal places, no dollar "
                                 f"sign): ")
            try:
                if len(budget_limit.rsplit('.')) != 2 or len(budget_limit.rsplit('.')[-1]) != 2:
                    raise ValueError(
                        "The account balance must be formatted with two decimal places and a decimal point")
            except ValueError as error:
                print("Error:", error)
                continue
            try:
                float(budget_limit)
            except ValueError:
                print("Error: The budget limit must be a float (a number with a decimal point)")
                continue
            budget_limit = float(budget_limit)
            validate_info = True
        return Budget(budget_limit)

    def validate_bank_info(self, account, account_type, institution_name, balance):
        """
        Checks that the inputs for a bank account's information is correct
        :param account: a string
        :param account_type: a string
        :param institution_name: a string
        :param balance: a string
        :return: True if values do not raise errors, else False
        """
        try:
            account_type = int(account_type)
        except ValueError:
            print("Error: The account type choice must be a number in the account types list")
            return False
        try:
            if bool(re.match("^[0-9-]*$", account)) is False:
                raise ValueError("A bank account must be digits and dashes only")
            if account_type not in range(1, len(self.BANK_ACCOUNT_TYPES) + 1):
                raise ValueError("Bank account type must be selected from valid account types")
            if len(balance.rsplit('.')[-1]) != 2:
                raise ValueError("The account balance must be formatted with two decimal places and a decimal point")
            if institution_name.isspace() | (len(institution_name) == 0):
                raise ValueError("The bank name cannot be blank")
        except ValueError as error:
            print("Error:", error)
            return False
        try:
            float(balance)
        except ValueError:
            print("Error: The account balance must be a float (a number with a decimal point)")
            return False
        return True

    def get_bank_info(self):
        """
        Gets all relevant bank information
        :return: bank information as a tuple
        """
        validate_info = False
        bank_info = None
        while validate_info is False:
            bank_account = input("Enter the user's bank account number (numbers and dashes only): ")
            for number, account_type in enumerate(self.BANK_ACCOUNT_TYPES, start=1):
                print(number, account_type)
            bank_account_type = input("\nEnter the number of a bank account type: ")
            bank_name = input("Enter the name of the bank associated with the account: ")
            bank_balance = input("Enter the current bank balance (with two decimal places, no dollar sign): ")
            if self.validate_bank_info(bank_account, bank_account_type, bank_name, bank_balance):
                bank_balance = float(bank_balance)
                bank_info = (bank_account, bank_account_type, bank_name, bank_balance)
                validate_info = True
        return bank_info

    """
    Code Citation
    ***************************************************************************************
    *    Title: Python How to Calculate Age from Birthdate
    *    Author: Artturi Jalli
    *    Availability: https://www.codingem.com/how-to-calculate-age-in-python/
    *
    ***************************************************************************************
    """
    @staticmethod
    def calculate_age(birthdate):
        """
        Calculates the user's age
        :param birthdate: a datetime object
        :return: the user's age as an int
        """
        today = date.today()

        # Subtract the birth year from the current year and
        # subtract 1 if the current month/day comes before the birth month/day
        # to account for leap years
        one_or_zero = ((today.month, today.day) < (birthdate.month, birthdate.day))
        year_difference = today.year - birthdate.year
        age = year_difference - one_or_zero
        return age

    def validate_user_info(self, name, dob, mod_level):
        """
        Checks that the inputs for a user's information is correct
        :param name: a string
        :param dob: a string
        :param mod_level: a string
        :return: True if values do not raise errors, else False
        """
        try:
            parse(dob)
        except ValueError:
            print("Error: The date of birth is not formatted correctly. Must be a valid date formatted YYYY/MM/DD")
            return False
        try:
            mod_level = int(mod_level)
        except ValueError:
            print("Error: The user type choice must be a number in the user types list")
            return False
        try:
            if name.isspace() | (len(name) == 0):
                raise ValueError("The user name cannot be blank")
            if mod_level not in range(1, len(self.USER_TYPES) + 1):
                raise ValueError("The user type must be selected from the user types list")
            if (self.USER_TYPES[int(mod_level) - 1] in self.USER_TYPE_AGE_LIMIT) and \
                    (self.calculate_age(parse(dob)) <= self.USER_TYPE_AGE_LIMIT[self.USER_TYPES[int(mod_level) - 1]]):
                raise ValueError(f"The user's age must be greater than "
                                 f"{self.USER_TYPE_AGE_LIMIT[self.USER_TYPES[int(mod_level) - 1]]}")
        except (ValueError, TypeError) as error:
            print("Error:", error)
            return False
        return True

    def get_user_info(self):
        """
        Gets all relevant user information
        :return: user information as a tuple
        """
        validate_info = False
        user_info = None
        while validate_info is False:
            user_name = input("Enter your user's first and last name: ")
            user_dob = input("Enter your user's date of birth (YYYY/MM/DD): ")
            for number, user_type in enumerate(self.USER_TYPES, start=1):
                print(number, user_type)
            user_type = input("\nEnter the number of a user type: ")
            if self.validate_user_info(user_name, user_dob, user_type):
                user_dob = parse(user_dob)
                user_info = (user_name, user_dob, user_type)
                validate_info = True
        return user_info

    def create_user(self):
        """
        Drives user creation
        :return: None when user creation is finished
        """
        process_finished = False
        while process_finished is False:
            user_info = self.get_user_info()
            bank_info = self.get_bank_info()
            if bank_info[1] == "1":
                bank = Chequing(bank_info[2], user_info[0], bank_info[0], bank_info[3])
            else:
                bank = Savings(bank_info[2], user_info[0], bank_info[0], bank_info[3])
            budgets = {}
            for budget_type in self.BUDGET_TYPES:
                budget = self.get_budget_info(budget_type)
                budgets[budget_type] = budget
            if user_info[2] == "1":
                user = Angel(name=user_info[0], dob=user_info[1], bank_account=bank, budgets=budgets)
            elif user_info[2] == "2":
                user = Troublemaker(name=user_info[0], dob=user_info[1], bank_account=bank, budgets=budgets)
            else:
                user = Rebel(name=user_info[0], dob=user_info[1], bank_account=bank, budgets=budgets)
            self._user_list.append(user)
            proceed = False
            while proceed is False:
                choices = ("yes", "no")
                for number, choice in enumerate(choices, start=1):
                    print(number, choice)
                user_choice = input("Would you like to create another user?: ")
                if user_choice == "1":
                    break
                elif user_choice == "2":
                    return
                else:
                    print("Please enter a valid choice")

    def driver(self):
        """
        Drives the user registration process
        """
        print("Welcome to the Family Appointed Moderator (FAM) System!")
        print("Please create your first user\n")
        self.create_user()
        user_menu = UserMenu(self._user_list)
        user_menu.display_user_menu()
