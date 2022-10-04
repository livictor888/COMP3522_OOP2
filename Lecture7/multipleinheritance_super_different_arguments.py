"""
This module showcases how to use variable keyword arguments in
conjunction with function overloading using variable keyword arguments
to pass different sets of arguments up an inheritance heirarchy
"""

class BaseClass:
    """
    The base class from which all other classes derive from.
    """

    def call_me(self, name='', age=0, **kwargs):
        """
        Example method that is overridden in the child classes.
        :param name: a string
        :param age: an int
        :param kwargs: optional additional keyword arguments
        """
        print(f"BaseClass - {kwargs}")
        print(f"BaseClass Method executed Name: {name} "
              f"age: {age}")


class LeftSubClass(BaseClass):
    """
    LeftSubClass inherits from BaseClass and overrides the call_me
    methods with the exact same argument list.
    """

    def call_me(self, name='', age=0, **kwargs):
        """
        Overridden method from the BaseClass.
        :param name: a string
        :param age: an int
        :param kwargs: optional additional keyword arguments
        """
        print(f"LeftSubClass - Kwargs: {kwargs}")
        print(f"LeftSubClass Method executed Name: {name} "
              f"age: {age}")
        super().call_me(name=name, age=age, **kwargs)

        #equivalent to - super().call_me(name=name, age=age, **kwargs)
        # kwargs['name'] = name
        # kwargs['age'] = age
        # super().call_me(**kwargs)


class RightSubClass(BaseClass):
    """
    RightSubClass inherits from BaseClass and overrides the call_me
    methods with a different argument list.
    """

    def call_me(self, weight='', **kwargs):
        """
        Overridden method from the BaseClass.
        :param weight: an int
        :param kwargs: optional additional keyword arguments
        """
        print(f"RightSubClass - Kwargs: {kwargs}")
        print(f"RightSubClass Method executed Weight: "
              f"{weight}")
        super().call_me(**kwargs)


class ChildClass(LeftSubClass, RightSubClass):
    """
    ChildClass inherits from LeftSubClass and RightSubClass. This class
    overrides the call_me method found in both parents with a completely
    different parameter list.
    """

    # NOTE - height = "" extracts height key/value from kwargs
    def call_me(self, height="", **kwargs):
        """
        Overrides the method with the same name found in BaseClass,
        LeftSubClass and RightSubClass with a different parameter list/
        :param height: a string
        :param kwargs: optional additional keyword arguments
        :return:
        """
        print(f"ChildClass - {kwargs}")
        print(f"ChildClass Method executed Height: {height}")
        super().call_me(**kwargs)
        return height


def main():
    """
    Prints out the MRO of ChildClass and showcases the use of variable
    keyword arguments.
    """
    print("Child Class Method Resolution Order (MRO)")
    print("-----------------------------------------")
    i = 1
    # for method in ChildClass.mro():
    #     print(f"{i}. {method}")

    print("\nCall Me Execution Order:")
    print("------------------------")
    test_object = ChildClass()
    #keyword arguments
    test_object.call_me(name="Smurfy", age="99", weight="80", height="140 cm")


if __name__ == '__main__':
    main()
