""" This module houses the library"""
from book import Book
import difflib

library_book_list = []


class Library:
    """
    The Library consists of a list of books and provides an
    interface for users to check out, return and find books.
    """
    def __init__(self, book_list):
        """
        Initialize the library with a list of books.
        :param book_list: a sequence of book objects.
        """
        self._book_list = book_list

    def check_out(self, call_number):
        """
        Check out an book with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        library_book = self._retrieve_book_by_call_number(call_number)
        if library_book.check_availability():
            status = self.reduce_book_count(call_number)
            if status:
                print("Checkout complete!")
            else:
                print(f"Could not find book with call number {call_number}"
                      f". Checkout failed.")
        else:
            print(f"No copies left for call number {call_number}"
                  f". Checkout failed.")

    def return_book(self, call_number):
        """
        Return an book with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        status = self.increment_book_count(call_number)
        if status:
            print("book returned successfully!")
        else:
            print(f"Could not find book with call number {call_number}"
                  f". Return failed.")

    def display_library_menu(self):
        """
        Display the library menu allowing the user to either access the
        list of books, check out, return, find, add, remove a book.
        """
        user_input = None
        while user_input != 7:
            print("\nWelcome to the Library!")
            print("-----------------------")
            print("1. Display all books")
            print("2. Check Out a book")
            print("3. Return a book")
            print("4. Find a book")
            print("5. Add a book")
            print("6. Remove a book")
            print("7. Quit")
            string_input = input("Please enter your choice (1-7)")

# handle user pressing only enter in menu
            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                self.display_available_books()
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                call_number = input("Enter the call number of the book"
                                    " you wish to check out.")
                self.check_out(call_number)
            elif user_input == 3:
                call_number = input("Enter the call number of the book"
                                    " you wish to return.")
                self.return_book(call_number)
            elif user_input == 4:
                input_title = input("Enter the title of the book:")
                found_titles = self.find_books(input_title)
                print("We found the following:")
                if len(found_titles) > 0:
                    for title in found_titles:
                        print(title)
                else:
                    print("Sorry! We found nothing with that title")

            elif user_input == 5:
                self.add_book()

            elif user_input == 6:
                call_number = input("Enter the call number of the book")
                self.remove_book(call_number)

            elif user_input == 7:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 7.")

        print("Thank you for visiting the Library.")

    def _retrieve_book_by_call_number(self, call_number):
        """
        A private method that encapsulates the retrieval of an book with
        the given call number from the library.
        :param call_number: a string
        :return: book object if found, None otherwise
        """
        found_book = None
        for library_book in self._book_list:
            if library_book.call_number == call_number:
                found_book = library_book
                break
        return found_book

    def find_books(self, title):
        """
        Find books with the same and similar title.
        :param title: a string
        :return: a list of titles.
        """
        title_list = []
        for library_book in self._book_list:
            title_list.append(library_book.get_title())
        results = difflib.get_close_matches(title, title_list,
                                            cutoff=0.5)
        return results

    def add_book(self):
        """
        Add a brand new book to the library with a unique call number.
        """
        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies "
                               "(positive number): "))
        book_data = (call_number, title, num_copies)
        author = input("Enter Author Name: ")
        new_book = Book(book_data[0], book_data[1], book_data[2], author)

        found_book = self._retrieve_book_by_call_number(
            new_book.call_number)
        if found_book:
            print(f"Could not add book with call number "
                  f"{new_book.call_number}. It already exists. ")
        else:
            self._book_list.append(new_book)
            print("book added successfully! book details:")
            print(new_book)

    def remove_book(self, call_number):
        """
        Remove an existing book from the library
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        found_book = self._retrieve_book_by_call_number(call_number)
        if found_book:
            self._book_list.remove(found_book)
            print(f"Successfully removed {found_book.get_title()} with "
                  f"call number: {call_number}")
        else:
            print(f"book with call number: {call_number} not found.")

    def display_available_books(self):
        """
        Display all the books in the library.
        """
        print("Books List")
        print("--------------", end="\n\n")
        for library_book in self._book_list:
            print(library_book)

    def reduce_book_count(self, call_number):
        """
        Decrement the book count for an book with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the book was found and count decremented, false
        otherwise.
        """
        library_book = self._retrieve_book_by_call_number(call_number)
        if library_book:
            library_book.decrement_number_of_copies()
            return True
        else:
            return False

    def increment_book_count(self, call_number):
        """
        Increment the book count for an book with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the book was found and count incremented, false
        otherwise.
        """
        library_book = self._retrieve_book_by_call_number(call_number)
        if library_book:
            library_book.increment_number_of_copies()
            return True
        else:
            return False


def generate_test_books():
    """
    Return a list of books with dummy data.
    """
    global library_book_list

    book_list = [
        Book("100.200.300", "Harry Potter 1", 2, "J K Rowling"),
        Book("999.224.854", "Harry Potter 2", 5, "J K Rowling"),
        Book("631.495.302", "Harry Potter 3", 4, "J K Rowling"),
        Book("123.02.204", "The Cat in the Hat", 1, "Dr. Seuss")
    ]
    library_book_list = book_list


def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """
    my_epic_library = Library(library_book_list)
    my_epic_library.display_library_menu()


if __name__ == '__main__':
    generate_test_books()
    main()
