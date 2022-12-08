"""This module represents a Rebel User"""

from user import User


class Rebel(User):
    """
    This class represents a Rebel User.
    """

    def __init__(self, **kwargs):
        """
        Initializes a Rebel with the data provided, and initializes user-specific conditions and alerts.
        :param kwargs: a dictionary that may contain name, dob, bank_account, and budgets
        """
        super().__init__(**kwargs)
        self._user_specific_conditions = {"warning_threshold": 0.5,
                                          "lockout_threshold": 1,
                                          "notification_threshold": 1,
                                          "multiple_budgets_exceeded": 2}
        self._user_specific_alerts = {"reaching_threshold_warning": "Warning: You've used more than 50% of the "
                                                                    "budget.",
                                      "exceed_budget_notification":
                                          "Notification: \nYOU'VE EXCEEDED YOUR BUDGET FOR THIS CATEGORY!\n"
                                          "YOU'VE EXCEEDED YOUR BUDGET FOR THIS CATEGORY!\n"
                                          "YOU'VE EXCEEDED YOUR BUDGET FOR THIS CATEGORY! ",
                                      "lockout_budget_notification": "Locked: You've exceeded your budget and "
                                                                     "will now be locked out.",
                                      "account_lockout_notification": "Locked: You've exceeded more than two budget "
                                                                      "categories and will now be locked out of "
                                                                      "your FAM account."
                                      }

    def get_user_conditions(self):
        """
        Returns a dictionary of Rebel specific conditions.
        :return: a dict
        """
        return self._user_specific_conditions

    def get_user_alerts(self):
        """
        Returns a dictionary of Rebel specific alerts.
        :return: a dict
        """
        return self._user_specific_alerts

