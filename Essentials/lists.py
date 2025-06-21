""" List Slicing and Modifying lists """

my_list = [1,2,3,4,5]
print(my_list[::2]) # Add a step size throughout indexing (will return every second element)

# Using the Range class

for i in range(5):
    print(i)

# Can be used to create lists too
my_range_list = list(range(15))

print(my_range_list)

""" Modifying Lists"""
# Append to add onto the end of the list
my_list.append(6)
print(my_list)

# Instert to select index to insert new element
my_list.insert(4, "New Insertion")
print(my_list)

# Remove just takes the value as an argument and searches through the list to remove it
my_list.remove("New Insertion")
print(my_list)

# Pop removes the element of the end of the list and returns it
my_list.pop()
print(my_list)

while len(my_list):
    print(my_list.pop())