"""This module represents an TroubleMaker User"""

from user import User


class Troublemaker(User):
    """
    This class represents a TroubleMaker.
    """

    def __init__(self, **kwargs):
        """
        Initializes a Troublemaker with the data provided, and initializes user-specific conditions and alerts.
        :param kwargs: a dictionary that may contain name, dob, bank_account, and budgets
        """
        super().__init__(**kwargs)
        self._user_specific_conditions = {"warning_threshold": 0.75,
                                          "notification_threshold": 1,
                                          "lockout_threshold": 1.2}
        self._user_specific_alerts = {"reaching_threshold_warning": "Warning: You've exceeded more than 75% of the "
                                                                    "budget.",
                                      "exceed_budget_notification": "Notification: Gentle reminder that you've "
                                                                    "exceeded your budget for this category.",
                                      "lockout_budget_notification": "Locked: You've used more than 120% of the "
                                                                     "budget and will now be locked out."
                                      }

    def get_user_conditions(self):
        """
        Returns a dictionary of TroubleMaker specific conditions.
        :return: a dict
        """
        return self._user_specific_conditions

    def get_user_alerts(self):
        """
        Returns a dictionary of TroubleMaker specific alerts.
        :return: a dict
        """
        return self._user_specific_alerts
