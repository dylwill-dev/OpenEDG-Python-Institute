"""Class composition is similar to inheritance but instead of having a 'is-a' relationship, a composition instead has a 'has-a' relationship. 
- Use composition in instances were there is a 'has-a' or 'uses-a' relationship
- In most cases it composition is creating a self.attribute to be equal to the instantiation of another class
- Ex. A car class can have an attribute called self.engine that instantiates another class Engine because a car 'has-a' engine
- self.engine = Engine()
- The car class does not have to inherit from Engine and can instantiate an engine providing it is in the same file, if not then import it."""

# Below is an example of composition

class Author():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Book():
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        result = 0
        for chapter in self.chapters:
            result += chapter.pagecount
        return result

class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount

auth = Author("Amy", "Douglas") # Create an author object
b1 = Book("The art of Kung-Foo", 89.75, auth) # Create a book object - last argument is an author object
# Add chapters to the book - Note how addchapter takes a chapter object as an argment
b1.addchapter(Chapter("The Basics", 13))
b1.addchapter(Chapter("Your first test", 22))
b1.addchapter(Chapter("Moving forward", 43))
print(b1.title)
print(b1.author)
print(f"{b1.getbookpagecount()} pages")
