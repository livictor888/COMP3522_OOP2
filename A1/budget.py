"""This module creates a budget"""


class Budget:
    """This class represents a budget"""

    def __init__(self, budget_limit):
        """
        Initializes the budget's limit and
        starting budget balance
        :param budget_limit: a float
        """
        self._budget_limit = budget_limit
        self._current_balance = 0.00

    def get_budget_limit(self):
        """
        :return: a float representing a budget's spending limit
        """
        return self._budget_limit

    def get_budget_balance(self):
        """
        :return: a float representing how much has been spent
        of the budget's allowed amount
        """
        return self._current_balance

    def is_budget_exceeded(self):
        """
        Calculates if budget is exceeded
        :return: True if budget is exceeded, else False
        """
        return self._current_balance > self._budget_limit

    def update_budget_balance(self, amount_spent):
        """
        Updates the budget's current balance with the
        current amount that has been spent
        :param amount_spent: a float
        :return: the updated current balance
        """
        self._current_balance = self._current_balance + amount_spent
        return self._current_balance

    def __str__(self):
        """
        :return: A user-friendly formatted string depicting the budget's attributes
        """
        return f"-------------\n" \
               f"Budget Exceeded: {self.is_budget_exceeded()}\n" \
               f"Budget Limit: {self._budget_limit:.2f}\n" \
               f"Budget Balance: {self._current_balance:.2f}\n"
