"""Creating a function that calculates the factorial of integer inputs only"""

def factorial(num):
    # First filter out any invalid input and return None if detected
    if (type(num) != int or num < 0):
        return None
    
    # Handle the valid input
    if (num == 0):
        return 1 # Base Case
    else:
        return num * factorial(num-1)
    
"""Create Testing Function"""
def test(value, expected):
    result = factorial(value)
    print("Testing the value:",value)

    if (result == expected):
        print("Pass!")
    else:
        print("Fail")

# Use test function to test the factorial function
test(5, 120)
test(2, 2)
test(1.5, None)
test("Hello", None)
test(-12 , None)
test(-1.2, None)
test(0, 1)
test(9, 362880)
    
    
    
