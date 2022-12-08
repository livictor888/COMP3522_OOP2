""" This module houses the library"""
from book import Book
from catalogue import Catalogue


class Library:
    """
    The Library consists of a list of books and provides an
    interface for users to check out, return and find books.
    """

    def __init__(self, item_list):
        self.library_list = ["Vancouver Public Library", ]
        self.active_library = self.library_list[0]
        self.catalogue = Catalogue(item_list)

    def display_library_menu(self):
        """
        Display the library menu allowing the user to either access the
        list of books, check out, return, find, add, remove a book.
        """
        user_input = None
        while user_input != 9:
            print(f"\nWelcome to the {self.active_library}!")
            print("-----------------------")
            print("1. Display all items")
            print("2. Check Out an item")
            print("3. Return an item")
            print("4. Find an item")
            print("5. Add an item")
            print("6. Remove an item")
            print("7. Create new library")
            print("8. Change library")
            print("9. Quit")

            string_input = input("Please enter your choice (1-7)")

            # handle user pressing only enter in menu
            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                self.catalogue.display_available_items()
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                call_number = input("Enter the call number of the item"
                                    " you wish to check out.")
                self.catalogue.check_out(call_number)
            elif user_input == 3:
                call_number = input("Enter the call number of the item"
                                    " you wish to return.")
                self.catalogue.return_item(call_number)
            elif user_input == 4:
                input_title = input("Enter the title of the item:")
                found_titles = self.catalogue.find_items(input_title)
                print("We found the following:")
                if len(found_titles) > 0:
                    for title in found_titles:
                        print(title)
                else:
                    print("Sorry! We found nothing with that title")

            elif user_input == 5:
                self.catalogue.add_item()

            elif user_input == 6:
                call_number = input("Enter the call number of the item")
                self.catalogue.remove_item(call_number)

            elif user_input == 7:
                self.add_library()

            elif user_input == 8:
                self.change_library()

            elif user_input == 9:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 7.")

        print("Thank you for visiting the Library.")

    def add_library(self):
        """
        Add a new library to the library list.
        """
        library_name = input("Enter name of new library: ")
        if library_name not in self.library_list:
            self.library_list.append(library_name)
            print(f"Library name: {library_name} has been created.")
        else:
            print("That library already exists.")

    def change_library(self):
        """
        Change the active library.
        """
        to_change = input("Enter name of new library: ")
        if to_change in self.library_list:
            self.active_library = to_change
            print(f"Changed to {to_change} library.")
        else:
            print("Couldn't find that library.")


def generate_test_books():
    """
    Return a list of books with dummy data.
    """

    book_list = [
        Book("100.200.300", "Harry Potter 1", 2, "J K Rowling"),
        Book("999.224.854", "Harry Potter 2", 5, "J K Rowling"),
        Book("631.495.302", "Harry Potter 3", 4, "J K Rowling"),
        Book("123.02.204", "The Cat in the Hat", 1, "Dr. Seuss")
    ]
    return book_list


def main():
    """
    Drives the program.
    """
    test_book_list = generate_test_books()
    my_epic_library = Library(test_book_list)
    my_epic_library.display_library_menu()


if __name__ == '__main__':
    # generate_test_books()
    main()
