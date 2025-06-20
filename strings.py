"""
Strings
- Slicing
- Formatting
- Multiple line Strings
"""
import math
my_string = "My name is Dylan!"
my_list = [1,2,3,4,5]

"""SLICING"""
# Indexing certain elements of the string
print(my_string[0]) # Get the first element = 'M'
print(my_string[0:7]) # Get a range of elements = 'My name' Gets characters up to index 7 but not including it
print(my_string[:7]) # Can ommit the 0 if starting from the beginning
print(my_string[11:]) # Can start at index and leave second argument to get the rest of the string = Dylan!

# This type of indexing also works with lists
print(my_list[1]) # = 2
print(my_list[3:]) # [4, 5]
print(my_list[:3]) # [1,2,3] - Remember it doesn't include the last element (actually elements at indexes 0-2)

"""FORMATTING"""
# Can use f"string here {var}" to format strings easier

# Instead of this: 
print("The number is", 5, "using comma separators")
# Or
print("The number is " + str(5) + "using '+' concatenation")

# Using f-strings
print(f"The number is {5} using f-strings")

# Additional capabilities with f-strings
print(f"My number is now {6} and double that is {6*2}") # Can use expressions within curly brackets
print(f"Pi rounded to two decimal places is {math.pi:.2f}") # Special rounding syntax


"""Multi-line String"""
print("""
This is a multi-line string using triple 
quotes and will not stop until it sees \"\"\"

""")
