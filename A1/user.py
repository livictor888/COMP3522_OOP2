"""This module represents the abstract User class"""

import abc
import itertools


class User(abc.ABC):
    """
    A class to represent the abstract User class intended to be extended to concrete types.
    """

    # ID auto-incrementation
    id_iteration = itertools.count(start=1)

    def __init__(self, **kwargs):
        """
        Initializes a User with the data provided.
        :param kwargs: a dictionary that may contain name, dob, bank_account, and budgets
        """
        self.__id = next(User.id_iteration)
        self._name = kwargs["name"]
        self._dob = kwargs["dob"]
        self._bank_account = kwargs["bank_account"]
        self._budgets = kwargs["budgets"]
        self._locked_out = False

    def get_user_name(self):
        """
        Gets the user's name
        :return: user's name as a string
        """
        return self._name

    def get_budgets(self):
        """
        Gets the user's budgets
        :return: a dictionary of Budgets
        """
        return self._budgets

    def get_bank_account(self):
        """
        Gets the user's bank account.
        :return: a BankAccount
        """
        return self._bank_account

    def lock_user_account(self):
        """
        Locks the user's account.
        """
        self._locked_out = True

    def get_all_transactions(self):
        """
        Gets all the transactions from the user's bank account.
        :return: a dictionary of transactions
        """
        return self._bank_account.get_all_transactions()

    def get_lockout_status(self):
        """
        Gets the user's lockout status.
        :return: user's account lockout status as a boolean
        """
        return self._locked_out

    @abc.abstractmethod
    def get_user_conditions(self):
        """
        Gets the user's specific conditions
        """
        pass

    @abc.abstractmethod
    def get_user_alerts(self):
        """
        Gets the user's specific alerts
        """
        pass
