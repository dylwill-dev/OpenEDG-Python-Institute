# Basic examples of how to handle files in python

with open(r"C:\Dev\Training Courses\Python\OpenEDG Python Institute\Essentials\examplefile.txt",'r') as file:    
    for line in file.readlines():
        print(line.strip())

# Writing files - Wreite mode overrides any existing data within the file

file = open(r"C:\Dev\Training Courses\Python\OpenEDG Python Institute\Essentials\examplefileOutput.txt",'w')

file.write("Line 1\n")
file.write("Line 2")

file.close() # Make sure to close files when done with them

# Appending to files - Append allows

# using 'with' and having everythin indented beneth the statement automatically closes the file for you
with open(r"C:\Dev\Training Courses\Python\OpenEDG Python Institute\Essentials\examplefileOutput.txt",'a') as file:
    file.write("\nLine 3\n")
    file.write("Line 4")



