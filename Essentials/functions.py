"""
Functions
"""
import math

# We use the keyword def to define a new function

"""Mutiply by 3 function"""
def multiplyby3(value):
    return value * 3

my_number = 3
my_new_number = multiplyby3(my_number)
print(my_new_number)

"""Multiply function with two inputs"""
def multiply(value1, value2):
    return value1 * value2

my_val1 = 10 ; my_val2 = 5
print(multiply(my_val1, my_val2))

# Using default values 

def performOperation(num1, num2, operation = "sum", message = "Default Message"):
    print(message, end = ": ")
    if operation == "sum":
        return num1 + num2
    if operation == "mult":
        return num1 * num2
    
print(performOperation(2,5)) # Will result in Default Message: 7
print(performOperation(5,5,'mult','New message')) # Will result in New Message: 25

# Anything that has a defualt value can be altered in any order after the ones without in like below
print(performOperation(6,2, message = "Explicit Override", operation = "mult"))


# Using args*
# - Args are used in a function definition as a pointer to the inputs that are being passed in, for example:

def printAnything(*args):
    print(args)

val1 = [1,2,3,4]
val2 = [('a', 1), ('b',2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)]
val3 = {
    "key1" : 1.1,
    "key2" : 1.2,
    "key3" : 1.3,
}
    
printAnything(val1)
printAnything(val2)
printAnything(val3)

# Using **kwargs can take any amount of keyword arguments and puts then into a dictionary
def printAnythingKwargs(*args, **kwargs):
    print(args)
    print(kwargs)

printAnythingKwargs([1,2,3], operation="do nothing", message='Hello There')


# Lets refactor our performOperation function to use *args

def performOperationArgs(*args, operation = "sum", message = "Default Message"):
    print(message, end = ": ")
    if operation == "sum":
        return sum(args)
    if operation == "mult":
        return math.prod(args)

print(performOperationArgs(1,1,1,2,1,1, operation="mult", message="Multiplication"))
print(performOperationArgs(15,5,-5,-10))