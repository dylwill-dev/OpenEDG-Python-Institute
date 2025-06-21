# Coding challenge to take input as a string and return a list of tuples with the character and count in order

"""Function that takes a string and encodes it into a list of tuples"""
def encodeString(inputString):
    encodedList = []
    prevLetter = inputString[0] # Initially the previous character is the first element of the inputString
    count = 0
    
    for letter in inputString:
        if letter == prevLetter:
            count += 1
            prevLetter = letter
        else:
            encodedList.append((prevLetter, count))
            prevLetter = letter
            count = 1
    
    encodedList.append((prevLetter, count)) # Add the last value
    
    return encodedList

def decodeString(encodedList):
    decodedString = "" # Empty string
    
    for item in encodedList:
        decodedString += item[0] * item[1] # For each item concatenate the letter multiplied by the count to the decoded string

    return decodedString




# Testing
encodeTestString = "AAAAABBBBAAA"
encodeTestString2 = "Bookkeeping"

print("Testing Encoding with input 'AAAAABBBBAAA' result:", encodeString(encodeTestString))
print("Testing Encoding with input 'Bookkeeping' result:", encodeString(encodeTestString2))

decodeTest = encodeString(encodeTestString)

print(decodeString(decodeTest))