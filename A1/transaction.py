"""This module represents a Transaction"""

import datetime


class Transaction:
    """
    Represents a Transaction object for the bank.
    """

    def __init__(self, current_user, dollar_amount, budget_category, shop_name):
        """
        Initialize a Transaction object.
        :param current_user: a User object
        :param dollar_amount:  a float
        :param budget_category: a string
        :param shop_name: a string
        """
        self._current_user = current_user
        self._time_stamp = datetime.datetime.now()
        if float(dollar_amount) < 0:
            raise ValueError("Dollar amount must be equal or greater than 0.")
        self._dollar_amount = float(dollar_amount)
        if budget_category not in current_user.get_budgets().keys():
            raise ValueError("Invalid budget category.")
        self._budget_category = budget_category
        self._shop_name = shop_name

    @property
    def dollar_amount(self):
        """Gets the dollar amount."""
        return self._dollar_amount

    @property
    def budget_category(self):
        """Gets the budget category."""
        return self._budget_category

    @property
    def shop_name(self):
        """Gets the shop name."""
        return self._shop_name

    @dollar_amount.setter
    def dollar_amount(self, value):
        """Sets the dollar amount."""
        self._dollar_amount = value

    @budget_category.setter
    def budget_category(self, value):
        """Sets the budget category."""
        self._budget_category = value

    @shop_name.setter
    def shop_name(self, value):
        """Sets the shop name."""
        self._shop_name = value

    def get_dict(self):
        """Returns a dictionary with the Transactions attributes."""
        dictionary = dict(time_stamp=self._time_stamp,
                          dollar_amount=self.dollar_amount,
                          budget_category=self.budget_category,
                          shop_name=self.shop_name)
        return dictionary
