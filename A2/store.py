"""This module represents an online storefront"""
from orderprocessor import OrderProcessor
from datetime import datetime, date
from invaliddataerror import InvalidDataError


class InvalidProductType(Exception):
    """Raise error when an invalid product type is produced."""
    def __init__(self):
        super().__init__('Error: Invalid Product Type')


class Store:
    """
    Defines a Store that carries holiday themed products such as Toys, Candies, and StuffedAnimals.
    """

    __instance = None

    @staticmethod
    def get_instance():
        if Store.__instance is None:
            Store()
        return Store.__instance

    def __init__(self):
        if Store.__instance is not None:
            raise Exception("Error: This is a singleton class")
        else:
            Store.__instance = self
            Store.__instance.inventory = {}
            Store.__instance.daily_transaction_orders = []

    def get_inventory(self):
        """
        Return the inventory of the Store.
        """
        return self.get_instance().inventory

    def check_enough_stock_for_item(self, product_id, requested_quantity):
        """
        Return True if there is enough stock of a specific item, otherwise false.
        :param product_id: a string
        :param requested_quantity: an integer
        :return: a boolean
        """
        return len(self.get_inventory()[product_id]) >= requested_quantity

    def order_item(self, order, quantity=100):
        """
        :param order: an Order with item details
        :param quantity: an integer amount of items to be produced by the factory
        """
        try:
            if order.item_type.lower() == "toy":
                for item in range(quantity):
                    if order.product_id not in self.__instance.inventory.keys():
                        self.__instance.inventory[order.product_id] = [order.prod_factory.create_toys(
                            has_batteries=order.details["has_batteries"], min_age=order.details["min_age"],
                            name=order.name, description=order.details["description"],
                            product_id=order.product_id, details=order.details)]
                    else:
                        self.__instance.inventory[order.product_id].append(order.prod_factory.create_toys(
                            has_batteries=order.details["has_batteries"], min_age=order.details["min_age"],
                            name=order.name, description=order.details["description"],
                            product_id=order.product_id, details=order.details))
            elif order.item_type.lower() == "stuffedanimal":
                for quantity in range(quantity):
                    if order.product_id not in self.__instance.inventory.keys():
                        self.__instance.inventory[order.product_id] = [order.prod_factory.create_stuffed_animals(
                            stuffing=order.details["stuffing"], size=order.details["size"],
                            fabric=order.details["fabric"], name=order.name, description=order.details["description"],
                            product_id=order.product_id, details=order.details)]
                    else:
                        self.__instance.inventory[order.product_id].append(
                            order.prod_factory.create_stuffed_animals(
                                stuffing=order.details["stuffing"], size=order.details["size"],
                                fabric=order.details["fabric"], name=order.name,
                                description=order.details["description"],
                                product_id=order.product_id, details=order.details))
            elif order.item_type.lower() == "candy":
                for quantity in range(quantity):
                    if order.product_id not in self.__instance.inventory.keys():
                        self.__instance.inventory[order.product_id] = [order.prod_factory.create_candy(
                            has_nuts=order.details['has_nuts'], has_lactose=order.details['has_lactose'],
                            name=order.name, description=order.details["description"], product_id=order.product_id,
                            details=order.details)]
                    else:
                        self.__instance.inventory[order.product_id].append(order.prod_factory.create_candy(
                            has_nuts=order.details['has_nuts'], has_lactose=order.details['has_lactose'],
                            name=order.name, description=order.details["description"], product_id=order.product_id,
                            details=order.details))
            else:
                raise InvalidProductType
        except InvalidDataError as e:
            return False, e
        return True, None

    def take_from_inventory(self, product_id: str, quantity):
        """
        Remove the number of items of a specific product from the inventory.
        :param product_id: a string
        :param quantity: an integer
        """
        for item in range(quantity):
            self.get_inventory()[product_id].pop()

    def order_prod_from_factory(self, path):
        """
        Processes a batch of Orders by first checking the inventory and either:
        a) remove the specified items from the inventory (update inventory and track for the Daily Transaction Report)
        b) send a request to the appropriate product factory to create 100 of each item for which the specified quantity
        in the order sheet was insufficient (e.g. if we have 8 in inventory but the order comes in for 10, we'll be \
        default order 100, UNLESS the quantity in the order sheet exceeds 100 (e.g., they request 150)).

        :param path: a Path to the order Excel sheet
        """
        order_processor = OrderProcessor()
        current_list_of_orders = order_processor.create_orders(path)
        orders_dict = {}
        # self.get_instance().daily_transaction_orders.append(current_list_of_orders)
        for order in current_list_of_orders:
            product_id = order.get_product_id()
            quantity = order.get_quantity()

            if (product_id not in self.get_inventory() or
                    not self.check_enough_stock_for_item(product_id, quantity)):
                quantity = quantity if quantity > 100 else 100
                if self.order_item(order, quantity)[0]:
                    self.take_from_inventory(product_id, order.get_quantity())
                    orders_dict[order] = True
                else:
                    orders_dict[order] = self.order_item(order, quantity)[1]
            else:
                self.take_from_inventory(product_id, quantity)
                orders_dict[order] = True

        self.get_instance().daily_transaction_orders.append(orders_dict)

    def check_inventory(self):
        """
        Print inventory details and their stock levels.
        """
        if len(self.get_inventory()) == 0:
            print("Inventory is empty.")
        else:

            for item in self.get_inventory():
                quantity = len(self.get_inventory()[item])
                if quantity == 0:
                    stock_level = "OUT OF STOCK"
                elif quantity < 3:
                    stock_level = "VERY LOW"
                elif quantity < 10:
                    stock_level = "LOW"
                else:
                    stock_level = "IN STOCK"
                print(f"{item}: {stock_level} - {len(self.get_inventory()[item])}")

    def create_daily_transaction_report(self):
        """
        Print a detailed report of the orders processed by the program.
        """
        time = datetime.now().strftime("%H:%M")
        today = date.today().strftime("%d-%m-%y")
        print("HOLIDAY STORE - DAILY TRANSACTION REPORT (DRT)")
        for report in self.get_instance().daily_transaction_orders:
            print(today, time)
            for order in report:
                # print(order.print_report())
                if report[order] is True:
                    print(order.print_report())
                else:
                    print(f"Order {order.order_num}, Could not process order data was corrupted, "
                          f"{report[order]}")
