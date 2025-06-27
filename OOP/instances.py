# Chapter 1 material included in this file - Creating a class, initializing it, working with attributes

# Create a class called Book
class Book:

    # Attributes can be defined at the class level that are shared by ALL instances of the class
    # Here we create a tuple defining the possible types of books there can be
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    __booklist = None

    def __init__(self, title, author, pages, price, booktype):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        if (booktype not in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype

        # Attributes with a double underscore are considered private and will raise an error it is accessed by other files
        self.__secret = "This is a secret attribute"

    """Retreives the price attribute from the instance"""
    def getPrice(self):
        # Use built in method hasattr which is checks if an object has a specific attribute (ie. the setDiscount method was called)
        if hasattr(self, "_discount"):
            return round(self.price - (self.price * self._discount), 2)
        else:
            return self.price
    
    """Have the ability to set a discount attribute and apply it when we retrive the price"""
    def setDiscount(self, amount):
        self._discount = amount

    def setTitle(self, newTitle):
        self.title = newTitle

    # Defining a CLASS METHOD with the @classmethod decorator
    # Class methods are bound to the class but NOT the instance and uses cls as the first argument 
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES
    
    # Defining a STATIC METHOD which is usually used for utility functions that don't need access to the class or instance
    # This also follows the singleton pattern to ensure that there is only one version of the booklist checking it for none before initializing it
    @staticmethod
    def get_book_list():
        if Book.__booklist == None:
            Book.__booklist = []
            return Book.__booklist
        else:
            return Book.__booklist


# Create another simple class called Newspaper with just a single attribute 'name'
class Newspaper:
    def __init__(self, name):
        self.name = name
        
# Create some instanes
b1 = Book("Keys to Success", "James Murphy", 677, 45.95, "HARDCOVER")
b2 = Book("Coding 101", "Jeff Long", 112, 32.90, "EBOOK")
n1 = Newspaper("Saskatoon Times")
n2 = Newspaper("Regina Pheonix")

# Use classmethod to get the possible book types
print(f"Book types are: {Book.get_book_types()}")

# Use staticmethod to access singleton object and add books to the booklist
book_collection = Book.get_book_list()
book_collection.append(b1)
book_collection.append(b2)
print(book_collection)


# Using the built in type() function to determine what type each instance is
# print(type(b1)) # Will return Book
# print(type(n1)) # Will return Newspaper

# Can also use type with conditionals
# print(type(b1) == type(b2)) # True
# print(type(b2) == type(n1)) # False


# Using the built in isinstance() method to compare specific instances with a known type
# print(isinstance(b1, Book)) # True
# print(isinstance(n2, Book)) # False
# print(isinstance(n2, object)) # True because all instances inherit from the object class


# print(b1.getPrice())
# b1.setDiscount(0.30)
# print(b1.getPrice())

        