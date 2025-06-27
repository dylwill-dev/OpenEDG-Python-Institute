"""In Python, you can inherit from multiple classes"""

class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name = "Class A"

class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name = "Class B"

# Can inherit from more than one class by separating with commas
class C(A, B):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.prop1)
        print(self.prop2)
        print(self.name)

# Create a C type object
c = C()
c.showprops()