"""This module represents the abstract bank account class"""

from abc import ABC
import datetime


class BankAccount(ABC):
    """
    A class to represent a Bank Account
    """

    def __init__(self, bank_name, account_holder_name: str, account_number: str, account_balance: float):
        """
        Constructs a BankAccount object.

        :param bank_name: a string
        :param account_holder_name: a string
        :param account_number: a string
        :param account_balance: a float
        """
        self.bank_name = bank_name
        self.account_holder = account_holder_name
        self.account_number = account_number
        self.account_balance = account_balance
        self.transactions = {}
        self.locked = False

    def get_total_number_of_transactions(self):
        """
        Returns the total number of transactions in the bank account.

        :return: an int
        """
        counter = 0
        for key, value in self.transactions.items():
            for transactions in value:
                counter += 1
        return counter

    def check_enough_balance_for_transaction(self, amount):
        """
        Checks to see if there is sufficient funds in the bank account.

        :param amount: a float, representing the dollar amount of the putative transaction
        :return: True if the account's balance is equal to or greater than the amount, False otherwise.
        """
        if self.account_balance >= amount:
            return True
        else:
            return False

    def add_transaction_to_account(self, transaction):
        """
        Adds a transaction to the account.

        :param transaction: a Transaction object
        """
        transaction_info = transaction.get_dict()
        transaction_time_stamp = transaction_info["time_stamp"]
        transaction_year = transaction_time_stamp.year
        transaction_month = transaction_time_stamp.month
        transaction_year_month = int(str(transaction_year) + str(transaction_month))
        try:
            self.transactions[transaction_year_month].append(transaction)
        except KeyError:
            self.transactions[transaction_year_month] = [transaction]

    def withdraw_from_account(self, amount):
        """
        Reduces the account balance by the specified amount.

        :param amount: a float representing the amount of the transaction to be deducted from the account balance
        """
        self.account_balance -= amount

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
        if enough_money and not self.locked:
            return True
        elif not enough_money:
            print("Warning: Insufficient Funds--available funds: {:.2f}".format(self.account_balance))
            return False
        elif self.locked:
            print(f"Locked: Account is Locked, please visit your local {self.bank_name} branch for assistance.")
            return False

    def process_transaction(self, transaction):
        """
        Processes a transaction by adjusting the account balance and adding it to the transaction list.

        :param transaction: a Transaction
        """
        transaction_info = transaction.get_dict()
        transaction_amount = transaction_info["dollar_amount"]
        self.withdraw_from_account(transaction_amount)
        self.add_transaction_to_account(transaction)

    def get_locked_status(self):
        """
        Returns the locked/unlocked status of the account.

        :return: True if the account is locked, false otherwise
        """
        return self.locked

    def lock_account(self):
        """
        Sets the account's locked status to True.
        """
        self.locked = True

    def print_all_transactions(self):
        """
        Prints the details of all transactions in the account.
        """
        for key, values in self.transactions.items():
            for transactions in values:
                transactions = transactions.get_dict()
                print("{:20} {:30} {:20} {:9} {:.2f}".format(transactions["time_stamp"].strftime("%d %b, %Y"),
                                                             transactions["budget_category"][:29],
                                                             transactions["shop_name"][:19],
                                                             "",
                                                             transactions["dollar_amount"]))

    def get_all_transactions(self):
        all_transactions = []
        for key, values in self.transactions.items():
            for transactions in values:
                all_transactions.append(transactions)
        return all_transactions

    def create_bank_statement(self):
        """
        Prints a nicely formatted bank statement. It includes the details of the account and all transactions contained
        therein.
        """
        print(f"$------------------------------Bank of {self.bank_name}---------------------------------------------$\n"
              f"Statement Date: {datetime.date.today()}\n"
              f"Account Holder: {self.account_holder}\n"
              f"Account Number: {self.account_number}\n"
              f"Account Balance: {self.account_balance:.2f}\n"
              f"Number of Transactions: {self.get_total_number_of_transactions()}\n\n"
              f"{'Date':21}{'Description':31}{'Vendor':31}{'Withdrawal':20}")
        self.print_all_transactions()
        print("\nClosing Balance:{:67}{:.2f}".format("", self.account_balance))

    def __str__(self):
        """
        Returns a nicely formatted string containing the state of the bank account.
        :return: a string
        """
        return f"---- Account Info----\n" \
               f"Bank: {self.bank_name}\n" \
               f"Account Holder: {self.account_holder}\n" \
               f"Account Number: {self.account_number}\n" \
               f"Account Balance: {self.account_balance}\n" \
               f"Number of Transactions: {self.get_total_number_of_transactions()}\n"
