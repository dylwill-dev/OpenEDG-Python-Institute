
import random

"""This function can take in any number of arguments which represent the number of faces each die has and will calculate the frequency of the value of each possible outcome.
- args must be integer values
- the function simulates 1 million roles and calculates the probability of each result."""
def diceProbability(*args):

    outputdictionary = {}
    iterations = 1000000 #number is iterations to perform
    original_iterations = iterations # set the initial number of iterations to calculate the frequency at the end
    arguments = [dice for dice in args] # Creates a list containing the arguments 
    
    # Start running simulation with inputs
    for itr in range(iterations - 1):
        turn_role = [random.randint(1, dice) for dice in arguments]
        total = sum(turn_role)
        
        # Add to the dictionary if it doesn't exist with the total as the key and the frequency as the value, if it exists then increment the frequency
        if total in outputdictionary:
            outputdictionary[total] += 1
        else:
            outputdictionary[total] = 1
        iterations -= 1
    
    # Add the last value to the dictionary after the while loop breaks
    if total in outputdictionary:
            outputdictionary[total] += 1
    else:
        outputdictionary[total] = 1
    
    sorted_dict = dict(sorted(outputdictionary.items()))

    # Now calculate the probability of each role by dividing the frequency by the number of iterations within the dictionary
    for key, value in sorted_dict.items():
         print(f"Probability of {key} is: {round((value / original_iterations) * 100, 6)}%")
    print(sorted_dict)

        
diceProbability()