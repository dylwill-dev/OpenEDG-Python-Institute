
from abc import ABC, abstractmethod

class Asset(ABC):
    def __init__(self, price):
        super().__init__()
        self.price = price

    """Must be implemented in subclasses"""
    @abstractmethod
    def get_description(self):
        pass

class Stock(Asset):
    def __init__(self, ticker, price, description):
        super().__init__(price)
        self.ticker = ticker
        self.description = description

    def get_description(self):
        return f"{self.ticker}: {self.price} -- {self.description}"


class Bond(Asset):
    def __init__(self, bondprice, bondname, duration, interest):
        super().__init__(bondprice)
        self.bondname = bondname
        self.duration = duration
        self.interest = interest

    def get_description(self):
        return f"{self.bondname}: {self.duration} : ${self.bondprice} : {self.interest}%"


# This is how your code will be called.
# DO NOT change the variable names. You CAN try different values.
ticker = "MSFT"
price = 400.00
description = "Microsoft Corporation"
bondname = "30 Year US Treasury"
bondprice = 100.00
duration = 30
interest = 4.38

# ******* DO NOT CHANGE THIS CODE ********
stock = Stock(ticker, price, description)
stock_description = stock.get_description()
print(stock_description)

bond = Bond(bondprice, bondname, duration, interest)
bond_description = bond.get_description()
print(bond_description)