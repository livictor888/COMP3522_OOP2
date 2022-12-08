"""This module creates Orders"""
from itemfactory import ItemFactory


class Order:
    """
    Represents an Order.
    :pram order_num: an integer representing the order number
    :param product_id: a string representing the SK
    :param item_type: a string representing the item type
    :param name: a string representing the name
    :param details: a dictionary of details specific to the item
    :param prod_factory: an ItemFactory that is used to instantiate the item
    """
    def __init__(self, order_num, product_id, item_type, name, details: dict, prod_factory: ItemFactory):
        self.order_num = order_num
        self.product_id = product_id
        self.item_type = item_type
        self.name = name
        self.details = details
        self.prod_factory = prod_factory

    def get_product_id(self):
        """Return the product ID of the item."""
        return self.product_id

    def get_quantity(self):
        """Return the quantity to be produced."""
        return self.details["quantity"]

    def print_report(self):
        """Print a detailed report of the item."""
        return f'Order {self.order_num}, Item {self.item_type}, Product ID {self.product_id}, Name "{self.name}",' \
               f' Quantity {self.details["quantity"]}'

    def __str__(self):
        """
        Returns a nicely formatted string with the details of the Order.
        :return: a string
        """
        return f"---- Order Info----\n" \
               f"Order Number: {self.order_num}\n" \
               f"Product ID: {self.product_id}\n" \
               f"Name: {self.name}\n" \
               f"Item Type: {self.item_type}\n" \
               f"Details: {self.details}\n" \
               f"Factory Type: {self.prod_factory}"
