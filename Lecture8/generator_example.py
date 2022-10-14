"""
This module showcases a simple generator example and the use of the
yield statement.
"""


def generate_numbers():
    """
    This generate yields an incremented number n starting from 0 and will
    continue to provide numbers until three calls are made
    :return: an int
    """
    n = 1
    print(n)
    print('This is printed first')
    # Generator function contains yield statements
    yield '\n'
    n += 1 #notice how the local variable n retains its value in subsequent calls
    print(n)
    print('This is printed second')
    yield '\n'
    n += 1 #notice how the local variable n retains its value in subsequent calls
    print(n)
    print('This is printed at last')
    yield '\n'

gen = generate_numbers()
print(next(gen))
print(next(gen))
print(next(gen))

# print('starting for loop')
#
# for item in generate_numbers():
#     print(item)
#
# print('end for loop')