from dataclasses import dataclass, field
import random


def price_func():
    return float(random.randrange(20,40))

"""The dataclass decorator allows for a simpler structure to classes that are primarily used to store data without the need to write a bunch of boilerplate code.
Boilerplate code is code that is repatative, necessary to make something work, and doesn't add any unique logic or value, often have to write it over and over.
 - It automatically adds and overrides the methods __init__, __repr__, __eq__, __lt__, __gt__, and __hash__
 - Use this for classes that mainly function to hold data"""
@dataclass
class Book:
    # The sequence of how these attributes should be passed to the instance go from top to bottom (title, author, pages, price)
    # You can also assign default values to these attributes allowing the user to create a Book with no arguments
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory=price_func) # This field allows you to run a function to set the defuault value

    """With a dataclass, we can still perform additional object initialization after the automated __init__ runs with a dataclass. To do this we can override the __post_init__ method. 
    - This will be called after the bult-in __init__ function runs. 
    - All it does is create an attribute detail that is just a combination of the attributes that are set in the __init__"""
    def __post_init__(self):
        self.detail = f"{self.title} by {self.author} has {self.pages} pages"


    def bookinfo(self):
        if(self.pages == 0):
            return "The book has not been initialized and has no data"
        else:
            return f"{self.title} by {self.author}"



# Create some instances of books
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("Catching Fire", "JD Salinger", 234, 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
default_book = Book()
random_price1 = Book("Harry Potter", "That Girl", 500)
random_price2 = Book("How to cry", "Crybaby Joe", 1)

print(b1.title)
print(b2.price)

# Print the book itself - dataclass implement __repr__
print(b1) # This will use __repr__, with a dataclass there is an automatic overridden __repr__ method that prints out more clearly

# These two will automatically work as well without error thanks to the dataclass decorator
print(b1 == b3)
print(b1 == b2)

# Modify some fields 
b1.title = "Mr.Bean the book"
b1.pages = 219
print(b1.bookinfo())
print(b1.detail)
print(default_book.bookinfo())
print(default_book)

print(random_price1)
print(random_price2)
