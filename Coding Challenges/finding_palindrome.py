
"""This function checks if an input string is a palindrome. If it is it returns true, and false otherwise."""
def isPalindrome(word):
    forward = []
    # First clean the input string to have no whitespaces and lowercase to ignore case sensativity
    cleaned = ''.join(word.split()).lower()

    #Iterate through the cleaned word and add to the forward list
    for letter in cleaned:
        forward.append(letter)
    
    #Create a reverse version of the list and call it backward
    backward = forward[::-1]

    return backward == forward
       

print(isPalindrome("racecar"))
print(isPalindrome("RacEcAr"))
print(isPalindrome("RACE car"))
print(isPalindrome("NOttaPal in drome"))

    
    
