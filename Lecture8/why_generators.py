"""
This module shows how generators can save tons of space by not storing
the actual iterable.
"""

import sys

my_range = range(1000)
a_list = [i for i in range(1000)]

print("my_range:", my_range)
print("a_list:", a_list)

print(f"Range Size in bytes: {sys.getsizeof(my_range)}")
print(f"List Size in bytes: {sys.getsizeof(a_list)}")