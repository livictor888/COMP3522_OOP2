"""This module represents a Savings bank account class"""

from bankaccount import BankAccount


class Savings(BankAccount):
    """
    A class representing a Saving bank account.
    """

    def __init__(self, bank_name, account_holder_name: str, account_number: str, account_balance):

        super().__init__(bank_name, account_holder_name, account_number, account_balance)

    def check_number_of_transactions_of_the_month(self, transaction):
        """
        Checks the number of transactions already done in the month that the specified transaction is taking place,
        and locks the account if there are already 2 transactions in that month.

        :param transaction: a Transaction
        """
        transaction_info = transaction.get_dict()
        transaction_time_stamp = transaction_info["time_stamp"]
        transaction_year = transaction_time_stamp.year
        transaction_month = transaction_time_stamp.month
        transaction_year_month = int(str(transaction_year) + str(transaction_month))
        if transaction_year_month in self.transactions.keys() and len(self.transactions[transaction_year_month]) > 1:
            self.lock_account()
            print("Warning: You cannot make more than 2 withdrawals from your savings account per month.")

    def check_account_lock_and_amount(self, transaction):
        """
        Checks the Savings account to ensure there is sufficient money and that it is not locked. If both conditions
        are satisfied, it returns True, False otherwise.

        :param transaction: a Transaction
        :return: True if there is enough money in the account and the account is not locked, False otherwise
        """
        transaction_info = transaction.get_dict()
        transaction_amount = transaction_info["dollar_amount"]
        enough_money = self.check_enough_balance_for_transaction(transaction_amount)
        self.check_number_of_transactions_of_the_month(transaction)
        if enough_money and not self.locked:
            return True
        elif not enough_money:
            print("Warning: Insufficient Funds--available funds: {:.2f}".format(self.account_balance))
            return False
        elif self.locked:
            print(f"Locked: Account is Locked, please visit your local {self.bank_name} branch for assistance.")
            return False
