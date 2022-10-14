"""
This example showcases how to impelment generator-like behaviour using
iterators. In this example, the log_file.txt is read line by line by the
LogWarningFilter iterator. We can avoid this complexity by just
implementing the warning_filter_generator() instead.
"""


def warning_filter_generator(file_object):
    """
    A generator that can avoid all the complexity shown in the iterator
    below. Yields a line from the provided file_object with the
    '[Warning]' tag in it.
    :param file_object: A file object in read mode.
    :return: yields a line with the '[Warning]' tag.
    """
    for line in file_object:
        if '[Warning]' in line:
            yield line

class LogFileWarningFilter:
    """
    A custom iterator that iterates over all the lines with a
    '[Warning]' tag in the given file.
    """

    def __init__(self, file_object):
        self.file = file_object

    #iterators have to override __iter__
    def __iter__(self):
        return self

    # iterators have to override __next__
    def __next__(self):
        """
        This method is responsible for iterating to the next line in
        the file with the '[Warning]' tag.
        :return: a line with the '[Warning]' tag, otherwise raises the
        StopIteration exception if there are no more lines to iterate
        over.
        """

        #read one line
        line = self.file.readline()

        # if the initial line does not have the warning tag,
        # then skip it and keep reading until you hit a line with the
        # tag
        while line and '[Warning]' not in line:
            line = self.file.readline()
        #found a line with a warning
        # If there are no more lines, raise StopIteration
        if not line:
            raise StopIteration
        else:
            return line


def main():
    """
    Open the log_file.txt for reading and print out all the lines with
    the '[Warning]' tag.
    """
    with open("log_file.txt", mode='r', encoding='utf-8') as log_file:
        # using the iterator
        #filter = LogFileWarningFilter(log_file)

        # uncomment this line to use the generator
        filter = warning_filter_generator(log_file)

        print(type(filter))
        for warning_line in filter:
            print(warning_line)

if __name__ == '__main__':
    main()