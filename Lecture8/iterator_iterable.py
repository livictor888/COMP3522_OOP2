class UpperCaseIterator:
    """
    An iterators which iterates over the words in a string and converts
    it to upper case.
    """

    def __init__(self, string):
        """
        Initializes the iterator by creating a list of upper case words
        from the given string and setting the index that the iterator is
        pointing to 0.
        :param string: a string
        """
        list_of_words = string.split() #splits into list of individual words
        # list comprehension - mapping elements from one list to another
        self.words = [word.upper() for word in list_of_words]
        self.index = 0

    def __next__(self):
        """
        A python dunder/magic method. __next__ is responsible for
        iterating to the next element in the container and returning
        that. If there are no more elements to iterate over, it raises
        the StopIteration error.
        :return: string, if there are still words to iterate over,
        raise StopIteration otherwise.
        """
        if self.index == len(self.words):
            raise StopIteration()
        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        """
        Returns an iterator over this class. (Which in this case is the
        class itself)
        :return: a UpperCaseIterator
        """
        return self


class UpperCaseIterable:
    """
    This class represents the container object that can be iterated
    over. In this case it represents a string of words.
    """

    def __init__(self, string):
        """
        Initializes the iterable with a string of words seperated by a
        space.
        :param string: string of words seperated by a single space.
        """
        self.string = string

    def __iter__(self):
        """
        Creates an UpperCaseIterator which can be used to iterate over
        each word (treating it as upper case characters)
        :return: UpperCaseIterator object
        """
        return UpperCaseIterator(self.string)


def main():
    """
    Creates a UpperCaseIterable object and showcases how an iterator can
    be used to iterate over this object.
    """
    sentence = UpperCaseIterable("comp3522 students are the best!")
    # invokes the __iter__(self) method.
    sentence_iterator = iter(sentence)

    # the long java way of doing it. Not pythonic.
    has_elements = True
    while has_elements:
        try:
            print(next(sentence_iterator))
        except StopIteration:
            has_elements = False

    # # the python way of doing it. The For loop handles the iterator
    # # behind the scenes.
    # for word in sentence_iterator:
    #     print(word)

if __name__ == '__main__':
    main()



