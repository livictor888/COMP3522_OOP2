"""
This module showcases different examples and aspects of generators.
"""

import sys


# -------------  Generator Method -------------
def fibonacci_sequence():
    """
    A generator that would let you iterate over the first 'n' fibonacci
    numbers
    :param n: an int, greater than 0
    :return: yield the next fibonacci number (int)
    """
    current = 0
    previous = 1
    while True:
        yield current
        previous, current = current, previous + current


print("-------------  Generator Method -------------")
print("Printing the first 100 fibonacci numbers via a generatpr method:")
fib = fibonacci_sequence()
for x in range(0,100):
    print(next(fib), end=", ")


print("\n\n-------------  Comparing List Comprehension with Generator "
      "Expressions -------------")
# -------------  List Comprehension -------------
even_num = [i for i in range(100) if i % 2 == 0]
print(f"Return type from list comprehension: {type(even_num)}")
print(f"Size of even_num (list comprehension): {sys.getsizeof(even_num)}")
for i in even_num:
    print(i, end = ", ")

print()
# -------------  Generator Expressions -------------
even_num_generator = (i for i in range(100) if i % 2 == 0)
print(f"Return type from generator expression: {type(even_num_generator)}")
print(f"Size of even_num_gen (generator expression): "
      f"{sys.getsizeof(even_num_generator)}")
for i in even_num_generator:
    print(i, end = ", ")


print("\n-------------  Generator Expression to filter warnings -------------")


# -------------  Generator Expressions in use (Yield From) -------------
def warning_filter_generator(file_object):
    """
    Yields a line from the provided file_object with the '[Warning]'
    tag. This showcases how to use generator expressions.
    :param file_object: A file object in read mode.
    :return: a line with the '[Warning]' tag.
    """
    yield from (line for line in file_object if '[Warning]' in line)


print("Printing result from using a generator expression to extract lines with"
      " '[Warning]' tag")
with open("log_file.txt", mode='r', encoding='utf-8') as log_file:
    filter = warning_filter_generator(log_file)
    for warning_line in filter:
        print(warning_line)
