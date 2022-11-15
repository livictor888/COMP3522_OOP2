"""
Builder Pattern example where a builder class builds a Pizza
"""

from enum import Enum


class BaseEnum(Enum):
    """
    The different base options for a Pizza
    """
    REGULAR = 0,
    WHOLEWHEAT = 1,
    CAULIFLOWER = 2


class ToppingEnum(Enum):
    """
    The different topping options for a Pizza
    """
    RED_ONION = 0,
    PEPPERS = 1,
    SPINACH = 2,
    MUSHROOM = 3,
    PEPPERONI = 4,
    CHICKEN = 5,
    BACON = 6,
    BEYOND_MEAT = 7,
    PINEAPPLE = 8


class CheeseEnum(Enum):
    """
    The different Cheese options for a Pizza
    """
    PARMESAN = 0,
    MOZZARELLA = 1,
    VEGAN_CHEESE = 2


class SauceEnum(Enum):
    """
    The different sauce options for a Pizza.
    """
    TOMATO = 0,
    ALFREDO = 1,
    BBQ = 2



class Pizza():
    """
    As a contrived example let's look at a Pizza. as a complex object
    the pizza can have multiple toppings, cheeses, a base and even be
    "half and half" , that is have 2 pizza's in one or even be folded
    into a calzone.
    """

    def __init__(self) -> None:
        self.base = None
        self.sauce_1 = None
        self.sauce_2 = None
        self.toppings_1 = []
        self.toppings_2 = []
        self.cheeses_1 = []
        self.cheeses_2 = []
        self.is_calzone = None

    def __str__(self):
        """
        Format and create a string representation of a Pizza.
        :return: a string
        """
        toppings1_str = [str(topping) for topping in self.toppings_1]
        toppings2_str = [str(topping) for topping in self.toppings_2]
        cheeses1_str = [str(cheese) for cheese in self.cheeses_1]
        cheeses2_str = [str(cheese) for cheese in self.cheeses_2]

        toppings1 = ", ".join(toppings1_str)
        toppings2 = ", ".join(toppings2_str)
        cheeses_1 = ", ".join(cheeses1_str)
        cheeses_2 = ", ".join(cheeses2_str)
        return f"Pizza:\n" \
            f"------\n" \
            f"Calzone: {self.is_calzone}" \
            f"Base: {self.base}\n" \
            f"Sauce (1st Half): {self.sauce_1}\n" \
            f"Sauce (2nd Half): {self.sauce_2}\n" \
            f"Toppings (1st Half): {toppings1}\n" \
            f"Toppings (2nd Half): {toppings2}\n" \
            f"Cheeses (1st Half): {cheeses_1}\n" \
            f"Cheeses (2nd Half): {cheeses_2}\n"


class PizzaBuilder:
    """
    The Pizza builder is a special class where we can place all the
    creation code for creating a pizza object. Here we can provide a
    different method for each component that makes up a Pizza
    """

    def __init__(self):
        self._pizza = Pizza()

    def reset(self):
        """
        Reset the pizza being built to a new blank pizza.
        :return:
        """
        self._pizza = Pizza()

    @property
    def pizza(self):
        """
        A property that "builds" the pizza when it is accessed. This
        could also be a seperate build() method.
        :return: a Pizza
        """
        completed_pizza = self._pizza
        self.reset()
        return completed_pizza



    def add_topping(self, topping: ToppingEnum, half_num: int = 0):
        """
        Add a topping component to the Pizza that is being built.
        :param topping: a ToppingEnum
        :param half_num: a int, 0 for the whole pizza, 1 for the first
        half and 2 for the second half
        """
        if half_num == 0:
            self._pizza.toppings_1.append(topping)
            self._pizza.toppings_2.append(topping)
        elif half_num == 1:
            self._pizza.toppings_1.append(topping)
        elif half_num == 2:
            self._pizza.toppings_2.append(topping)
        else:
            raise Exception("Invalid half_num!")
        return self

    def add_cheese(self, cheese: CheeseEnum, half_num: int =0):
        """
        Add a cheese component to the Pizza that is being built.
        :param cheese: a CheeseEnum
        :param half_num: a int, 0 for the whole pizza, 1 for the first
        half and 2 for the second half
        """
        if half_num == 0:
            self._pizza.cheeses_1.append(cheese)
            self._pizza.cheeses_2.append(cheese)
        elif half_num == 1:
            self._pizza.cheeses_1.append(cheese)
        elif half_num == 2:
            self._pizza.cheeses_2.append(cheese)
        else:
            raise Exception("Invalid half_num!")
        return self

    def add_sauce(self, sauce: SauceEnum, half_num: int = 0):
        """
        Add a sauce component to the Pizza that is being built.
        :param sauce: a SauceEnum
        :param half_num: a int, 0 for the whole pizza, 1 for the first
        half and 2 for the second half
        """
        if half_num == 0:
            self._pizza.sauce_1 = sauce
            self._pizza.sauce_2 = sauce
        elif half_num == 1:
            self._pizza.sauce_1 = sauce
        elif half_num == 2:
            self._pizza.sauce_2 = sauce
        return self

    def add_base(self, base: BaseEnum):
        """
        Add a base component to the Pizza that is being built.
        :param base: a BaseEnum
        :param half_num: a int, 0 for the whole pizza, 1 for the first
        half and 2 for the second half
        """
        self._pizza.base = base

    def make_calzone(self):
        """
        Turn the Pizza being built into a calzone.
        """
        self._pizza.is_calzone = True
        return self

class Menu: #director
    """
    The Menu class acts as a Director. It is only responsible for
    executing the building steps in a particular sequence. In this case,
    these sequences refer to the different common types of pizza being
    built.
    """

    def __init__(self) -> None:
        self.builder = PizzaBuilder()

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def prepare_cheese_pizza(self, half_num:int = 0) -> None:
        """
        Executes the sequence of steps to create a cheese pizza
        :param half_num: a int, 0 for the whole pizza, 1 for the first
        half and 2 for the second half
        """
        self.builder.add_sauce(SauceEnum.TOMATO, half_num)
        self.builder.add_cheese(CheeseEnum.MOZZARELLA, half_num)
        self.builder.add_cheese(CheeseEnum.MOZZARELLA, half_num)
        self.builder.add_cheese(CheeseEnum.PARMESAN, half_num)
        self.builder.add_cheese(CheeseEnum.PARMESAN, half_num)

    def prepare_pepperoni_pizza(self, half_num:int = 0) -> None:
        """
        Executes the sequence of steps to create a pepperoni pizza
        :param half_num: a int, 0 for the whole pizza, 1 for the first
        half and 2 for the second half
        """
        self.builder.add_sauce(SauceEnum.TOMATO, half_num)
        self.builder.add_cheese(CheeseEnum.MOZZARELLA, half_num)
        self.builder.add_topping(ToppingEnum.PEPPERONI, half_num)

    def prepare_vegan_pizza(self, half_num:int = 0) -> None:
        """
        Executes the sequence of steps to create a vegan pizza
        :param half_num: a int, 0 for the whole pizza, 1 for the first
        half and 2 for the second half
        """
        self.builder.add_sauce(SauceEnum.TOMATO, half_num)
        self.builder.add_cheese(CheeseEnum.VEGAN_CHEESE, half_num)
        self.builder.add_topping(ToppingEnum.BEYOND_MEAT, half_num)
        self.builder.add_topping(ToppingEnum.SPINACH, half_num)
        self.builder.add_topping(ToppingEnum.RED_ONION, half_num)
        self.builder.add_topping(ToppingEnum.PEPPERS, half_num)

    def order_half_half_pizza(self, base: BaseEnum, pizza_order1, pizza_order2) \
            -> Pizza:
        """
        Create a Half half pizza.
        :param base: a BaseEnum. The base of the Pizza
        :param pizza_order1: a Menu method, the first half of the pizza
        :param pizza_order2: a Menu method the second half of the pizza
        :return: a Pizza
        """
        self.builder.add_base(base)
        pizza_order1(1)
        pizza_order2(2)
        return self.builder.pizza

    def order_single_pizza(self, base: BaseEnum, pizza_order):
        """
        Create a whole pizza.
        :param base: a BaseEnum. The base of the Pizza
        :param pizza_order: a Menu method, the whole pizza recipe
        :return: a Pizza
        """
        self.builder.add_base(base)
        pizza_order()
        return self.builder.pizza




def main():
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    # # We can access the builder directly
    # # -------------------------
    # builder = PizzaBuilder()
    # builder.add_base(BaseEnum.CAULIFLOWER)
    # #builder.make_calzone()
    # builder.add_sauce(SauceEnum.ALFREDO, half_num=1)
    # builder.add_sauce(SauceEnum.TOMATO)
    # builder.add_cheese(CheeseEnum.MOZZARELLA, half_num=0)
    # builder.add_cheese(CheeseEnum.VEGAN_CHEESE, half_num=0)
    # builder.add_topping(ToppingEnum.SPINACH, half_num=0)
    # builder.add_topping(ToppingEnum.SPINACH)
    # builder.add_topping(ToppingEnum.BEYOND_MEAT, half_num=2)
    # pizza = builder.pizza
    # print(pizza)

    # We can access the Director class
    # ----------------
    menu = Menu()
    pizza = menu.order_half_half_pizza(BaseEnum.REGULAR,
                                       menu.prepare_cheese_pizza,
                                       menu.prepare_pepperoni_pizza)
    print(pizza)


if __name__ == "__main__":
    main()

