# Chapter 8 practice question - Using custom exceptions and a wrapper class 

# Inherit from the exception class and pass to create a simple custom named exception
class NonIntArgumentException(Exception):
    pass

"""This function can be used as a decorator for any function that is supposed to receive integer inputs. Theis function will raise a NonIntArgumentException if any of elements
in the function parameter list are not integers. If nothing is detected then the input is simply returned."""
def handleNonIntArguments(func):
    def wrapper(*args):
        for item in args:
            if type(item) is not int:
                raise NonIntArgumentException()
        return func(*args)
    return wrapper

# Call the code
@handleNonIntArguments
def sum(a,b,c):
    return a + b + c

try:
    result = sum(1,2,3)
    print("This should print out.")
    result2 = sum(1,2,'a')
    print("This should not print out.")
except NonIntArgumentException as e:
    print("Custom exception was caught!")