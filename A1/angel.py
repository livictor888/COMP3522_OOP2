"""This module represents an Angel User"""

from user import User


class Angel(User):
    """
    This class represents an Angel.
    """

    def __init__(self, **kwargs):
        """
        Initializes an Angel with the data provided, and initializes user-specific conditions and alerts.
        :param kwargs: a dictionary that may contain name, dob, bank_account, and budgets
        """
        super().__init__(**kwargs)
        self._user_specific_conditions = {"warning_threshold": 0.9,
                                          "notification_threshold": 1}
        self._user_specific_alerts = {
                                      "reaching_threshold_warning": "Warning: Gentle reminder that you've used more "
                                                                    "than 90% of the budget.",
                                      "exceed_budget_notification": "Notification: Gentle reminder that you've "
                                                                    "exceeded your budget for this category.",
                                      }

    def get_user_conditions(self):
        """
        Returns a dictionary of Angel specific conditions.
        :return: a dict
        """
        return self._user_specific_conditions

    def get_user_alerts(self):
        """
        Returns a dictionary of Angel specific alerts.
        :return: a dict
        """
        return self._user_specific_alerts
