
class Stock:
    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company

    # __eq__ override
    def __eq__(self, other):
        return self.price == other.price

    # __lt__ override
    def __lt__(self, other):
        return self.price < other.price

    # __gt__ override
    def __gt__(self, other):
        return self.price > other.price

    # __le__ override'
    def __le__(self, other):
        return self.price <= other.price

    # __ge__ override
    def __ge__(self, other):
        return self.price >= other.price
    
    # Override __repr__ method for clear print out
    def __repr__(self):
        return f"Ticker = {self.ticker}, Price = {self.price}, Company = {self.company}"
    

ticker1 = "XYZ"
ticker2 = "ABCD"
price1 = 100.0
price2 = 105.1
company1 = "XYZ Corporation"
company2 = "ABCD Company"

# ***** DO NOT CHANGE THIS CODE ******
stock1 = Stock(ticker1, price1, company1)
stock2 = Stock(ticker2, price2, company2)

is_eq = (stock1 == stock2)
is_gt = (stock1 > stock2)
is_lt = (stock1 < stock2)
is_gte = (stock1 >= stock2)
is_lte = (stock1 <= stock2)

print(f"Stock 1 information: {repr(stock1)}\nStock 2 information: {repr(stock2)}")
print(f"Stock 1 and 2 equal? - {is_eq}\nStock 1 greater? - {is_gt}\nStock 1 smaller? - {is_lt}\nStock 1 greater or equal? - {is_gte}\nStock 1 smaller or equal? - {is_lte}")