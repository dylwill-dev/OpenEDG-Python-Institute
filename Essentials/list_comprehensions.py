"""List Comprehensions
- With filters
- With functions
- Nested comprehensions
"""

"""BASIC COMPREHENSIONS"""
my_list = [1,2,3,4,5]

# To write a list comprehension we surround it is [sqaure brackets]
print([2*item for item in my_list])

"""USING LIST COMPREHENSION TO FILTER DATA"""
my_bigger_list = list(range(101))
filtered_list = [item for item in my_bigger_list if item % 25 == 0]

print(filtered_list)

"""USING FUNCTIONS"""
my_string = "Hello my name is Dylan, I am learning Python"
print(my_string.split(',')) # Split can be used to split a string based on a given variable

print(my_string.split()) # By default is splits on spaces

def cleanWord(word):
    return word.replace(',','').lower()

# Lets use this function in a list comprehension now
filtered_list = [cleanWord(word) for word in my_string.split()]
print(filtered_list)


# Quiz question using list comprehension as a deconstructor 

values = [[1,'i','a'], [2, 'we', 'be', 'it'], [3, 'are', 'few', 'too']]

# Use list comprehension to extract the first element (integer) followed by a list of the rest of the elements

deconstruction = {item[0]: item[1:] for item in values}
deconstruction[4] = ["common", "to", "understand"]
deconstruction[4] = ["new", "new", "new"]

print(deconstruction)

