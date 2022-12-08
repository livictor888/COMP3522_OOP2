"""This module processes web orders"""
from holidays import HolidayEnum
from easteritemfactory import EasterItemFactory
from christmasitemfactory import ChristmasItemFactory
from halloweenitemfactory import HalloweenItemFactory
from itemfactory import ItemFactory
from order import Order
from file_handler import FileHandler


class OrderProcessor:
    """
    Maintains a mapping of holiday-seasons -> ItemFactory. The OrderProcessor
    is responsible for retrieving the right factory for the specified
    order and generating a list of orders to be processed.
    """

    FILE_HANDLER = FileHandler()

    # Maps holiday types to their respective factories
    holiday_factory_mapper = {
        HolidayEnum.EASTER: EasterItemFactory,
        HolidayEnum.CHRISTMAS: ChristmasItemFactory,
        HolidayEnum.HALLOWEEN: HalloweenItemFactory
    }

    def get_factory(self, holiday: HolidayEnum) -> ItemFactory:
        """
        Retrieves the associated factory for the specified HolidayEnum
        :param holiday: HolidayEnum
        :return: a CharacterFactory if found, None otherwise
        """
        factory_class = self.holiday_factory_mapper.get(holiday)
        return factory_class()

    def create_orders(self, path):
        """
        Reads order details from an Excel file from the specified path
        and generates a list of Order Objects.

        :param path: a Path to the user's Excel file containing the Order details
        :return: a list of Orders
        """
        list_of_orders = []

        dataset = OrderProcessor.FILE_HANDLER.load_data(path)

        for row in range(len(dataset)):
            holiday = dataset.loc[row]["holiday"].upper()
            holidayEnum = HolidayEnum.EASTER if holiday == "EASTER" else (
                HolidayEnum.CHRISTMAS if holiday == "CHRISTMAS" else HolidayEnum.HALLOWEEN)
            factory_type = self.get_factory(holidayEnum)
            order_details = {
                "quantity": dataset.loc[row]["quantity"],
                "description": dataset.loc[row]["description"],
                "has_batteries": dataset.loc[row]["has_batteries"],
                "min_age": dataset.loc[row]["min_age"],
                "dimensions": dataset.loc[row]["dimensions"],
                "num_rooms": dataset.loc[row]["num_rooms"],
                "speed": dataset.loc[row]["speed"],
                "jump_height": dataset.loc[row]["jump_height"],
                "has_glow": dataset.loc[row]["has_glow"],
                "spider_type": dataset.loc[row]["spider_type"],
                "num_sound": dataset.loc[row]["num_sound"],
                "colour": dataset.loc[row]["colour"],
                "has_lactose": dataset.loc[row]["has_lactose"],
                "has_nuts": dataset.loc[row]["has_nuts"],
                "variety": dataset.loc[row]["variety"],
                "pack_size": dataset.loc[row]["pack_size"],
                "stuffing": dataset.loc[row]["stuffing"],
                "size": dataset.loc[row]["size"],
                "fabric": dataset.loc[row]["fabric"]
            }

            order = Order(dataset.loc[row]["order_number"],
                          dataset.loc[row]["product_id"],dataset.loc[row]["item"],
                          dataset.loc[row]["name"], order_details, factory_type)
            list_of_orders.append(order)
        return list_of_orders
