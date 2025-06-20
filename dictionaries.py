# Dictionaries
from collections import defaultdict

animals = {
    'a' : "Antellope",
    'b' : "Bear",
    'c' : "Cat" , #Trailing comma not needed but good practice
}
# Indexing and printing the values with keys
print(animals)
print(animals['a'])
print(animals['b'])
print(animals['c'])

# Change value associated with key b
animals['b'] = "Boar"
print(animals['b'])

# Can access all keys or values
print(animals.keys())
print(animals.values())

# Using the get function
print(animals.get('e')) # returns None since there is no e key
print(animals.get('c')) # returns the value if it does exist

# len function on dictionary
print(len(animals))

# Create new dictionary where the values are lists
food = {
    'a' : ["Apple, Apricot"],
    'b' : ["Butter, Bread, Bagel"],
    'c' : ["Coke, Cranberry"],
}

# Add a value into the list associated with the 'c' key
food['c'].append("Cabbage")
print(food['c'])

# Add a new key with an associated list of values
if 'd' not in food:
    food['d'] = ["Donuts, Dairymilk, Danish"]
    print(food)


"""DEFAULT DICT"""

names = defaultdict(list)

names['r'].append("Ryan")
names['r'].append("Roger")

names['t'].append("Terry")

names['r'].remove("Ryan")

print(names)