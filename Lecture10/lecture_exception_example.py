"""
This module depicts the use of exception handling as a way of dealing
with errors in Python.
"""

class EvenList(list):
    """
    This class represent a custom list data structure that can only hold
    even integers. The EvenList inherits from List.
    """

    def append(self, value):
        """
        Overriden append method. Raises an exception if the system
        attempts to append anything that is not an even integer. Appends
        the value otherwise.
        :param value: an int
        :precondition value: an even number
        """
        if not isinstance(value, int):
            raise TypeError("Attempted to append an invalid type! Only "
                            "integers accepted.")
            return
        if value % 2:
            raise ValueError("Error! You can only append even numbers to this "
                             "list")
        super().append(value)


def main():
    """
    Appends a number of different values to an EvenList to depict the
    use of the try-catch-else-finally construct to handle exceptions.
    """
    my_list = EvenList()
    try:
        try:
            my_list.append(2)
            #my_list.append(3) #throw value exception
            #my_list.append('4') #throw type exception
            return #finally block executed even when returning right away
        except ValueError as e:
            print(f"Value Exception caught! Exception: {e.args[0]}")
        except TypeError as e:
            print(f"Type Exception caught! Exception: {e}")
            raise Exception() #outer try catches this
        except Exception as e:
            print(f"Unknown Exception caught! {e}")
        else: #runs when no exceptions
            print("No exceptions")
        finally: #runs with or without exceptions
            print("Finally block executed")
        print("my_list contains:", my_list)
    except Exception as e:
        print("Class caught something!!!!!!")


if __name__ == '__main__':
    main()