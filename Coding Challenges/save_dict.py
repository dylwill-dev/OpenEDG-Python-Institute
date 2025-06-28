"""Challenge requirements
- Write a function to save a dictionary to a file that takes 2 arguments (dictionary to save, output file path)
- Write a second function to load a saved dictionary back into python with 1 argument(the file path to the saved dictionary)"""

"""This function writes the input to the given filepath"""
def saveDict(input, filepath):
    with open(rf"{filepath}",'w') as file:
        file.write(str(input))

def loadDict(filepath):
    with open(rf"{filepath}",'r') as file:
        for line in file.readlines():
            print(line)


mydict = {'a':'apple', 'b':'banana', 'c': 'carrot'}
destination = "C:\Dev\Training Courses\Python\OpenEDG Python Institute\Coding Challenges\saved_dict.txt"

saveDict(mydict,destination)
loadDict(destination)