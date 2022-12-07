"""
Implements the observer pattern and simulates a simple auction.
"""
import random


class Auctioneer:
    """
    The auctioneer acts as the "core". This class is responsible for
    tracking the highest bid and notifying the bidders if it changes.
    """

    def __init__(self):
        self.bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    def register_bidder(self, bidder):
        """
        Adds a bidder to the list of tracked bidders.
        :param bidder: object with __call__(auctioneer) interface.
        """
        self.bidders.append(bidder)

    def reset_auctioneer(self):
        """
        Resets the auctioneer. Removes all the bidders and resets the
        highest bid to 0.
        """
        self.bidders = []
        self._highest_bid = 0

    def start_auction(self, start_price):
        """
        Start the auction with the starting price and notify the bidders.
        :param start_price: a float
        """
        self._highest_bid = start_price
        self._notify_bidders()

    def _notify_bidders(self):
        """
        Executes all the bidder callbacks. Should only be called if the
        highest bid has changed.
        """
        print("Notifying the bidders...")
        for bidder in self.bidders:
            bidder(self)

    def get_highest_bid(self):
        """
        Return the highest bid.
        :return: a float
        """
        return self._highest_bid

    def get_highest_bidder(self):
        """
        Return the highest bidder.
        :return: a Bidder object
        """
        return self._highest_bidder

    def accept_bid(self, bid, bidder):
        """
        Accepts a new bid and updates the highest bid. This notifies all
        the bidders via their callbacks.
        :param bid: a float.
        :precondition bid: should be higher than the existing bid.
        :param bidder: The object with __call__(auctioneer) that placed
        the bid.
        """
        if bid > self.get_highest_bid():
            print(f"{bidder} placed a bid of {bid} "
                  f"in response to {'Starting bid' if self._highest_bidder is None else self._highest_bidder}'s "
                  f"bid of {self._highest_bid}!")
            self._highest_bid = bid
            self._highest_bidder = bidder
        self._notify_bidders()

    def print_bidder_records(self):
        for bidder in self.bidders:
            print(f"Bidder: {bidder} \t Highest Bid: {bidder.get_highest_bid()}")
        return 0


class Bidder:

    def __init__(self, name, budget=100.00, bid_increase_perc=1.1):
        self.name = name
        self.budget = budget
        self.bid_increase_perc = bid_increase_perc
        self.bid_probability = random.uniform(0, 1)
        self.highest_bid = 0

    def get_highest_bid(self):
        return self.highest_bid

    # Auctioneer will notify the bidders by calling them as a function
    def __call__(self, auctioneer):
        # Don't bet over self
        if self != auctioneer.get_highest_bidder():
            willing_to_bid = random.random() < self.bid_probability
            # Have budget to bet
            bid = auctioneer.get_highest_bid() * self.bid_increase_perc
            if (willing_to_bid and
                    self.budget >= auctioneer.get_highest_bid() and
                    self.budget >= bid):
                # Place bet
                self.highest_bid = bid
                auctioneer.accept_bid(bid, self)

    def __str__(self):
        return self.name


class Auction:
    """
    Simulates an auction. Is responsible for driving the auctioneer and
    the bidders.
    """

    def __init__(self, bidders):
        """
        Initialize an auction. Requires a list of bidders that are
        attending the auction and can bid.
        :param bidders: sequence type of objects of type Bidder
        """
        self.auctioneer = Auctioneer()
        for bidder in bidders:
            self.auctioneer.register_bidder(bidder)

    def simulate_auction(self, item, start_price):
        """
        Starts the auction for the given item at the given starting
        price. Drives the auction till completion and prints the results.
        :param item: string, name of item.
        :param start_price: float
        """
        print(f"Auctioning the {item} starting at {start_price}")
        self.auctioneer.start_auction(start_price)
        # if no one bids, end the auction

        # print result
        print(f"\nThe winner of the auction is: {self.auctioneer.get_highest_bidder()} "
              f"at ${self.auctioneer.get_highest_bid()}\n")
        print(f"Highest Bids Per Bidder")
        self.auctioneer.print_bidder_records()


def main():
    bidders = []

    # Ask for item's name
    item = input("Enter the name of the item being auctioned: ")

    # Ask for starting price
    starting_price = float(input("Enter the starting price: "))

    # Ask for number of bidders
    print(f"This auction already has {len(bidders)} bidders, but you can add more.")
    number_of_bidders = None
    while number_of_bidders is None:
        number_of_bidders = int(input("Enter the number of bidders to add: "))

    # Input bidder's details
    for i in range(1, number_of_bidders + 1):
        print(f"-------- Bidder #{i} --------")

        # Ask for bidder's name
        name = input("Enter bidder's name: ")

        # Ask for bidder's budget
        budget = float(input("Enter bidder's budget: "))

        # Ask for bidder's increase percentage
        bid_increase_perc = float(input("Enter bidder's increase percentage: "))

        # Create the bidder and add to the list of bidders
        current_bidder = Bidder(name, budget, bid_increase_perc)
        number_of_bidders += 1
        bidders.append(current_bidder)

    # Create an auction
    auction = Auction(bidders)

    print("\n\nStarting Auction!!")
    print("------------------")
    auction.simulate_auction(item, starting_price)


if __name__ == '__main__':
    main()
