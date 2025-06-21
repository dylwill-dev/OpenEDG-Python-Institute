# Classes in Python

class Dog:
    # Class definition inside that outlines all of the methods and attributes
    
    """ Initialization function that is called whenever an instance of Dog is created """
    def __init__(self, name):
        self.name = name
        self.legs = 4

    """ Simple speak method that uses the attribute name and executes a print statement """
    def speak(self):
        print(self.name + " says 'Woof'!")


# Create a new instance of the dog class passing in the name variable
my_dog = Dog("Jonah")
another_dog = Dog("Jesse")


my_dog.speak()
another_dog.speak()

