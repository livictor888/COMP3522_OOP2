"""
A simple calculator program that showcases how functions can be used as
objects in a dictionary. Pay special attention to the fact that all the
functions need to accept the same number and type of parameters for a
setup like this to work.
"""

def sum(a, b):
    """
    Calculates the sum of 2 numbers
    :param a: int or float
    :param b: int or float
    :return: int or float
    """
    return a + b


def subtract(a, b):
    """
    Calculates the difference between 2 numbers
    :param a: int or float
    :param b: int or float
    :return: int or float
    """
    return a - b


def multiply(a, b):
    """
    Calculates the product of 2 numbers
    :param a: int or float
    :param b: int or float
    :return: int or float
    """
    return a * b


def divide(a, b):
    """
    Calculates the result when dividing the first number by the second.
    :param a: int or float
    :param b: int or float
    :return: int or float
    """
    return a / b


def main():
    """
    Runs the calculator program and presents the user with a menu. Runs
    the appropriate function accordingly.
    """
    print("Calculator")
    print("----------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4, Divide")

    choice = int(input("Enter your choice: "))
    #choice is an int from 1-4
    input_map = {
        1: sum,
        2: subtract,
        3: multiply,
        4: divide,
    }
    # choice is an int from 1-4
    # if i pass in choice == 1,
    calculator_operation = input_map[choice]
    #at this point calculator_operation is pointing at the function sum

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"The result is {calculator_operation(num1, num2)}")
    # print(f"The result is {sum(num1, num2)}")


if __name__ == '__main__':
    main()
    i