from item import Item


class Journal(Item):
    """
    Represent a Journal library item with name, issue number, and publisher attributes.
    """
    def __init__(self, call_num, title, num_copies, name, issue_number, publisher):
        super().__init__(call_num, title, num_copies)
        self._name = name
        self._issue_number = issue_number
        self._publisher = publisher

    def __str__(self):
        """
        Return a user friendly formatted string.
        """
        return f"{super().__str__()}Name: {self._name}\n" \
               f"Issue Number: {self._issue_number}\n" \
               f"Publisher: {self._publisher}"
