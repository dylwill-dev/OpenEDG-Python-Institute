# Demonstration of inheritance in python

# Declare the parent class:
"""The parent class to all publications. What is common in all child classes is the title and the price. Both attributes
are accounted for in this superclass"""
class Publication:
    # This class will define the common attributes
    def __init__(self, title, price):
        self.title = title
        self.price = price

"""This class inherits from Publication and Calling the super init class forthe title and price attributes
defining period and publisher to be inherited by Magazine and Newspaper"""
class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

"""Book inherits from Publication, calling the super init function to initialize the title and price. It goes further to intialize the 
unique attributes of author and pages"""
class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price) # Call the super function's init method and pass in the title and price
        self.author = author
        self.pages = pages

"""Magazine inherits from Periodical and is able to fully call the super init function to compeletely initialize all attributes of the instance"""
class Magazine(Periodical):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price, period, publisher)

"""Newspaper inherits from Periodical and is able to fully call the super init function to compeletely initialize all attributes of the instance"""
class Newspaper(Periodical):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price, period, publisher)


        
