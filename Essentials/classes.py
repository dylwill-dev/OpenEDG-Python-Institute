# Classes in Python

class Dog:
    # Class definition inside that outlines all of the methods and attributes
    
    """ Initialization function that is called whenever an instance of Dog is created """
    _legs = 4 # attributes that are meant to be protected (_) or private (__) 
    def __init__(self, name):
        self.name = name
    
    """ Getter method to get the legs """
    def getLegs(self):
        return self._legs

    """ Simple speak method that uses the attribute name and executes a print statement """
    def speak(self):
        print(self.name + " says 'Woof'!")


# Create a new instance of the dog class passing in the name variable
my_dog = Dog("Jonah")
another_dog = Dog("Jesse")


my_dog.speak()
another_dog.speak()
print(my_dog.getLegs())

class WordSet:
    # This is a static (private) variable that can be referenced by self.__replacePunctuation OR WordSet.__replacePunctuation
    __replacePunctuation = ['!', '.', ',', '\'']

    def __init__(self):
        self.words = set()

    '''This is an INSTANCE METHOD because it belongs to a particular instance of the class (self)'''
    def addText(self, text):
        text = WordSet.cleanText(text) # WordSet.cleanText means that the cleanText is found somewhere inside the WordSet class / can use self with decorator over static method
        for word in text.split():
            self.words.add(word)
    
    '''This is a STATIC METHOD because it does not have "self" in the parameter list
     - This method does not belong to any particular class instance and is instead part of the WordSet class definition itself.
     - STATIC METHODS are used to hold constants, unchanging variables, fundamental logic to the class '''
    @staticmethod #This is called a decorator which tells python that this is a static method and should ignore the self
    def cleanText(text):
        # text = text.replace('!', '').replace('.', '').replace(',', '').replace('\'', '') -- Old code before replacePunctuation list was made
        for punc in WordSet.__replacePunctuation:
            text = text.replace(punc, '')
        return text.lower()
    

wordSet1 = WordSet()

wordSet1.addText("Hello, I\'m Dylan! Here is something I want to add.")
wordSet1.addText("Here is another sentence ... AHH!")

print(wordSet1.words)


# CLASS INHERITANCE - (Parent class in the parenthesis)---------------

class LittleDog(Dog):

    """This is an overridden function from the parent class
     - If a LittleDog instance is created and told to speak it will use this speak method instead of the parent one"""
    def speak(self):
        print(f"{self.name} says: yappa yappa!")

babydoggy = LittleDog("Yapper")

babydoggy.speak()

# It is also possible to extend built-in classes

class UniqueList(list):

    def __init__(self):
        super().__init__() # This makes sure the inherited init runs first and we have all the data needed with our custom instance
        self.someDifferentProperty = "Unique Property"

    def append(self, item):
        if item in self:
            return
        else:
            # This calls the parent version of the append rather than our overwritten one.
            super().append(item)

uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(1)
uniqueList.append(2)
uniqueList.append(2)
print(f"Unique list: {uniqueList}")
print(uniqueList.someDifferentProperty)
    
