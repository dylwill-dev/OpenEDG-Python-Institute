"""
Abstract base classes can define a template for other classes to inherit from without the subclass classes being able to create instances of the BASE class itself.
 - An abstract base class in just intended to be a blueprint or a place where you collect some common attributes.
 - There can be certain methods in the base class that require an implementation by the subclass that is required for it's specific needs.
"""
# ABC stands for Abstract Base Class and makes the class abstract if it inherits from it
# It tells the compiler that this is a base class with some methods that require implementation within the subclasses
from abc import ABC, abstractmethod

# Lets create a class for drawing shapes and lets make it extensible for a variety of different shapes

class GraphicShape(ABC):
    """We want to prvent the GraphicShape class from being instantiated by any subclasses"""
    def __init__(self):
        super().__init__()
    
    """We want to enforce that all sublasses need to implement the calcArea method for itself
     - Using @abstractmethod indicates to the compiler that no implementation is provided in the base class
     - Each subclass MUST override this method or else there will be an error."""
    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    """Must implement calcArea from base class to instatiate"""
    def calcArea(self):
        return 3.14 * (self.radius ** 2)
    

class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    """Must implement calcArea from base class to instatiate"""
    def calcArea(self):
        return self.side * self.side

circle = Circle(10)
square = Square(5)

print(f"Area of circle with radius of {circle.radius} is: {circle.calcArea()}")
print(f"Area of square with side lenght of {square.side} is: {square.calcArea()}")