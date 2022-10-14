"""
This example shows how list comprehensions can be used to read a log
file.
"""


def main():
    """
    This function opens a log file for reading, and creates a new list
    which contains all the lines with the '[Warning]' tag.
    """
    with open("log_file.txt", mode='r', encoding='utf-8') as log_file:
        tag = "[Warning]"
        tag_lines = [line for line in log_file if tag in line]

        for line in tag_lines:
            print(line)


if __name__ == '__main__':
    main()

