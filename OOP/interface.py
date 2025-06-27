# ABC stands for Abstract Base Class and makes the class abstract if it inherits from it
# It tells the compiler that this is a base class with some methods that require implementation within the subclasses
from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def calcArea(self):
        pass

class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    """Must implement calcArea from base class to function"""
    def calcArea(self):
        return 3.14 * (self.radius ** 2)
    
    """Must also implement toJSON from JSONifty class to function"""
    def toJSON(self):
        return f"{{'Circle': {str(self.calcArea())}}}"

    

circle = Circle(4)
print(circle.calcArea())
print(circle.toJSON())