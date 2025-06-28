"""Magic methods in Python are special methods that start and end with double underscores and can allow you to customize how your objects behave with built-in Python operations.
Normally they are called automatically during certain operations. 
They can let you define how your objects should behave in certain situations like:
- when printed
- when added or compared
- when accessed like a container
- when used in loops
Some magic methods include: __init__, __str__, __repr__, __len__, __iter__, and many more.
Any of these magic methods can be OVERRIDDEN in your own class definitions  """

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price


    #__str__
    """Represents the output when we display the object itself using the print method"""
    def __str__(self):
        return f"{self.title} by {self.author}, costs ${self.price}."
    
    #__repr__
    """Overriding the repr function for your own classes can make debugging much easier"""
    def __repr__(self):
         return f"title={self.title}, author={self.author}, price={self.price}"
    
    #__eq__
    """Checks for equality between two objects called with (==)"""
    def __eq__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Cannot compare objects of different types")
        return (self.title == other.title and 
                self.author == other.author and 
                self.price == other.price)

    #__ge__ 
    """Establishes the (>=) relationship with another object"""
    def __ge__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Cannot compare objects of different types")
        return self.price >= other.price


    #__lt__
    """Establishes (<) relationship with another object"""
    def __lt__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Cannot compare objects of different types")
        return self.price < other.price

# Create book instances
b1 = Book("Coding 101", "James Sully", 25.99)
b2 = Book("Learn Python", "Mike Wasowski", 44.45)
b3 = Book("Coding 102", "James Sully", 25.95)
b4 = Book("To kill a mocking bird", "Harper Lee", 24.95)


"""Using the standard __str__ magic method the result of the print statements below are: <__main__.Book object at 0x00000280B4814B90> 
   Using our overridden version we get: Coding 101 by James Sully, costs $25.99.
   Similar goes for the overridden repr function
"""
print(b1) 
print(repr(b2))

# Moving onto the eq, ge, and lt overrides

# __eq__ overrides
print(b1 == b3) # results in false with default as it compares addresses, not actual values
print(b1 == b2) # False

# __ge__ overrides
print(b2 >= b1) # Compares price and results in true

# __lt__ overrides
print(b2 < b1) # Compares price and results in false

# With these overridden methods we can now sort our books by price
books = [b2, b1, b4, b3]
books.sort() # This will inherantly use the overridden methods within
print([book.title for book in books])


