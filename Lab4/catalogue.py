import difflib
from enum import Enum

from journal import Journal
from dvd import DVD
from book import Book


class ItemType(Enum):
    """
    Represent the types of items available at the library.
    """
    BOOK = 1
    DVD = 2
    JOURNAL = 3


class Catalogue:
    """
    The Catalogue consists of a list of items and gives an interface for the library to manage the items.
    """

    def __init__(self, item_list):
        """
        Initialize the library with a list of items.
        :param item_list: a sequence of item objects.
        """
        self._item_list = item_list

    def check_out(self, call_number):
        """
        Check out an item with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        library_item = self._retrieve_item_by_call_number(call_number)
        if library_item is None:
            print(f"Could not find item with call number {call_number}"
                  f". Checkout failed.")
        else:
            if library_item.check_availability():
                status = self.reduce_item_count(call_number)
                if status:
                    print("Checkout complete!")
            else:
                print(f"No copies left for call number {call_number}"
                      f". Checkout failed.")

    def return_item(self, call_number):
        """
        Return an item with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        status = self.increment_item_count(call_number)
        if status:
            print("Item returned successfully!")
        else:
            print(f"Could not find item with call number {call_number}"
                  f". Return failed.")

    def _retrieve_item_by_call_number(self, call_number):
        """
        A private method that encapsulates the retrieval of an item with
        the given call number from the library.
        :param call_number: a string
        :return: item object if found, None otherwise
        """
        found_item = None
        for library_item in self._item_list:
            if library_item.call_number == call_number:
                found_item = library_item
                break
        return found_item

    def find_items(self, title):
        """
        Find items with the same and similar title.
        :param title: a string
        :return: a list of titles.
        """
        title_list = []
        for library_item in self._item_list:
            title_list.append(library_item.get_title())
        results = difflib.get_close_matches(title, title_list,
                                            cutoff=0.5)
        return results

    def add_item(self):
        """
        Add a brand-new item to the library with a unique call number.
        """

        selected_item_type = None
        while selected_item_type not in set(item.value for item in ItemType):
            for item_type in ItemType:
                print(item_type.value, item_type.name)
            selected_item_type = int(input("Enter item type: "))
        call_number = input("Enter Call Number: ")
        found_item = self._retrieve_item_by_call_number(call_number)
        if found_item in self._item_list:
            print(f"Could not add item with call number "
                  f"{call_number}. It already exists. ")
        else:
            new_item = None
            title = input("Enter title: ")
            num_copies = int(input("Enter number of copies (positive number): "))
            if selected_item_type == 1:
                author = input("Enter author: ")
                new_item = Book(call_number, title, num_copies, author)
            elif selected_item_type == 2:
                release_date = input("Enter release date: ")
                region = input("Enter region: ")
                new_item = DVD(call_number, title, num_copies, release_date, region)
            elif selected_item_type == 3:
                name = input("Enter journal name: ")
                issue_number = input("Enter journal issue number: ")
                publisher = input("Enter publisher: ")
                new_item = Journal(call_number, title, num_copies, name, issue_number, publisher)
            self._item_list.append(new_item)
            print("item added successfully! item details:")
            print(new_item)

    def display_available_items(self):
        """
        Display all the items in the library.
        """
        print("Items List")
        print("--------------", end="\n\n")
        for library_item in self._item_list:
            print(library_item)

    def reduce_item_count(self, call_number):
        """
        Decrement the item count for an item with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the item was found and count decremented, false
        otherwise.
        """
        library_item = self._retrieve_item_by_call_number(call_number)
        if library_item:
            library_item.decrement_number_of_copies()
            return True
        else:
            return False

    def increment_item_count(self, call_number):
        """
        Increment the item count for an item with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the item was found and count incremented, false
        otherwise.
        """
        library_item = self._retrieve_item_by_call_number(call_number)
        if library_item:
            library_item.increment_number_of_copies()
            return True
        else:
            return False

    def remove_item(self, call_number):
        """
        Remove an existing item from the library
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        found_item = self._retrieve_item_by_call_number(call_number)
        if found_item:
            self._item_list.remove(found_item)
            print(f"Successfully removed {found_item.get_title()} with "
                  f"call number: {call_number}")
        else:
            print(f"item with call number: {call_number} not found.")
