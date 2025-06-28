
"""This function will take an integer as input and find all the prime numbers that when multiplied together results in the value of num
- The function returns a list of these prime numbers.
- ex. 630 = [2, 3, 3, 5, 7]"""
def findPrimeFactors(num, primefactors=None):
    if primefactors is None:
        primefactors = []
    if num == 1:
        return f"The prime factors are: {primefactors}"
    for i in range(2, int(num + 1)):
        if isPrime(i) and num % i == 0:
            num = num // i # Divide the num by the prime number that can divide equally into it
            primefactors.append(i)
            return findPrimeFactors(num, primefactors)
        else:
            continue

"""Helper function to determine if the current iteration is a prime number or not.
If it isnt then don't bother trying to divide it."""
def isPrime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

print(findPrimeFactors(630))


