# Similar to list comprehensions but with dictionaries

# A list of tuples, each with two elements
animalList = [('a', 'antelope'), ('b', 'baboon'), ('c', 'cat'), ('d', 'dog')]

# Can create a dictionary using a dictionary comprehension 
# Remember touse curly brackets for this type of comprehension
animalDict = {item[0]: item[1] for item in animalList} # Must use indexing for the key value pairs to create dict
print(animalDict)

# There is another way to do this without indexing as well that results in the same thing
# We can unpack the values into multiple variables at once
animalDict2 = {key: value for key,value in animalList}
print(animalDict2)


