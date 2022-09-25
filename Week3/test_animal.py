class Cat:
    def __init__(self, age):
        self.__age = age

    def print_age(self):
        print(self.__age)

my_cat = Cat(10)
my_cat._Cat__age = 5
my_cat.print_age()