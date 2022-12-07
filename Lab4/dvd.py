from item import Item


class DVD(Item):
    """
    Represent a DVD library item with release date and region attributes.
    """
    def __init__(self, call_num, title, num_copies, release_date, region):
        super().__init__(call_num, title, num_copies)
        self._release_date = release_date
        self._region = region

    def __str__(self):
        """
        Return a user friendly formatted string.
        """
        return f"{super().__str__()}" \
               f"Release Date: {self._release_date}\n" \
               f"Region: {self._region}"
