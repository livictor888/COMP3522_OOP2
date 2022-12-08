"""This module ensures that each transaction is valid based on user's Budget and BankAccount restrictions"""


class Validator:
    """
    This class ensures the validity of each transaction and issues context appropriate messages to the user.
    """

    def __init__(self, current_user, transaction):
        """Initialize the Validator with a specific user, transaction and list of potential rules."""
        self._current_user = current_user
        self._current_transaction = transaction
        self.rule_key_set = ["warning_threshold", "lockout_threshold", "notification_threshold",
                             "multiple_budgets_exceeded", "reaching_threshold_warning", "exceed_budget_notification",
                             "lockout_budget_notification", "account_lockout_notification"]

    def check_sufficient_budget(self, transaction):
        """
        Checks that the specified Transaction is valid for the user, and triggers specific messages to the user.

        :param transaction: a Transaction
        :return: True if the Transaction is valid budget-wise, false otherwise.
        """
        user_conditions = self._current_user.get_user_conditions()
        user_alerts = self._current_user.get_user_alerts()
        current_budget = self._current_user.get_budgets()[transaction.budget_category]
        new_budget_balance = current_budget.get_budget_balance() + transaction.dollar_amount
        new_budget_is_locked = False
        budget_is_locked = False

        budgets_exceeded = 0
        for k, v in self._current_user.get_budgets().items():
            if v.is_budget_exceeded():
                budgets_exceeded += 1

        if self.rule_key_set[1] in user_conditions.keys():
            budget_is_locked = current_budget.get_budget_balance() > current_budget.get_budget_limit() * \
                               user_conditions[self.rule_key_set[1]]
            new_budget_is_locked = new_budget_balance > current_budget.get_budget_limit() * \
                                   user_conditions[self.rule_key_set[1]]
        if budget_is_locked:
            print("Locked: This budget has been locked out so you cannot make transactions in this budget.")
            return False
        else:
            current_budget.update_budget_balance(transaction.dollar_amount)

        if current_budget.get_budget_balance() > current_budget.get_budget_limit() * \
                user_conditions[self.rule_key_set[0]]:
            print(user_alerts[self.rule_key_set[4]])

        if current_budget.get_budget_balance() > current_budget.get_budget_limit() * \
                user_conditions[self.rule_key_set[2]]:
            print(user_alerts[self.rule_key_set[5]])

        if (self.rule_key_set[1] in user_conditions.keys()) and new_budget_is_locked:
            print(user_alerts[self.rule_key_set[6]])

        if (self.rule_key_set[1] in user_conditions.keys()) and (self.rule_key_set[3] in user_conditions.keys()) \
                and (self.rule_key_set[7] in user_alerts.keys()):
            number_of_budgets_limit = user_conditions[self.rule_key_set[3]]
            if new_budget_is_locked and (budgets_exceeded + 1) >= number_of_budgets_limit:
                print(user_alerts[self.rule_key_set[7]])
                self.trigger_account_lockout()

        return True

    def check_with_bank(self, transaction):
        """
        Checks the user's bank account for sufficient funds and that it is not locked.

        :param transaction: a Transaction
        :return: True if the account has sufficient funds and is not locked
        """
        user_bank_account = self._current_user.get_bank_account()
        return user_bank_account.check_account_lock_and_amount(transaction)

    def update_bank_account(self, transaction):
        """
        Updates the user's bank account by deducting a valid transaction's amount from the bank account.

        :param transaction: a Transaction
        """
        user_bank_account = self._current_user.get_bank_account()
        user_bank_account.process_transaction(transaction)

    def validate(self):
        """
        Checks the user's budget and bank account conditions.

        :return: True if the transaction is valid, false otherwise.
        """
        if self.check_with_bank(self._current_transaction) and \
                self.check_sufficient_budget(self._current_transaction):
            self.update_bank_account(self._current_transaction)
            return True
        return False

    def trigger_account_lockout(self):
        """
        Locks user out of their FAM account.
        """
        self._current_user.lock_user_account()
        print("Locked: You've been locked out of your FAM account.")
