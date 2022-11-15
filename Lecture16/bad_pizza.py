class Pizza():
    """
    As a contrived example let's look at a Pizza. as a complex object
    the pizza can have multiple toppins, cheeses, a base and even be
    "half and half" , that is have 2 pizza's in one or even be folded
    into a calzone.
    """

    def __init__(self, base, is_halfnhalf, sauce_1, sauce_2,
                 toppings_1, toppings_2, cheese_1, cheese_2,
                 is_calzone) -> None:
        self.base = None
        self.sauce_1 = None
        self.sauce_2 = None
        self.toppings_1 = []
        self.toppings_2 = []
        self.cheeses_1 = []
        self.cheeses_2 = []
        self.is_calzone = None

p = Pizza("wheat", "full", "tomato", "butter", "pepperoni", "sausage", "mozz", "cheddar", False)
