"""This module represents a chequing bank account class"""


from bankaccount import BankAccount


class Chequing(BankAccount):
    """
    A class representing a Chequing bank account.
    """

    def __init__(self, bank_name, account_holder_name: str, account_number: str, account_balance):
        super().__init__(bank_name, account_holder_name, account_number, account_balance)
