from item import Item


class Book(Item):
    """
    Represent a Book library item with an author attribute.
    """
    def __init__(self, call_num, title, num_copies, author):
        super().__init__(call_num, title, num_copies)
        self._author = author

    def __str__(self):
        """
        Return a user friendly formatted string.
        """
        return f"{super().__str__()}" \
               f"Author: {self._author}"
