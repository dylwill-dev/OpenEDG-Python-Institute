from dataclasses import dataclass

"""The dataclass decorator paired with the frozen=True modifier allows you to easily create an immutable class for classes that you know aren't going to need to change."""
@dataclass(frozen=True) #This frozen attribute makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def some_func(self, newval):
        self.value2 = newval

obj = ImmutableClass()
print(obj)

#obj.value1 = "New string" #results in error since it is immutable
#obj.some_func(10) # This also results in an error

# The class can however be initialized with the initial values which will then be immutable
new_obj = ImmutableClass("New Value", 25)
print(new_obj)