class Stock:
    """Init method"""
    def __init__(self, ticker, price, name):
        self.ticker = ticker
        self.price = price
        self.name = name
    
    """Method returns a formatted string of the instance variables"""
    def get_description(self):
        return f"{self.ticker}: {self.name} -- ${self.price}"
    

symbol = Stock("GOOG", 183.45, "Google LLC")
print(symbol.get_description())

