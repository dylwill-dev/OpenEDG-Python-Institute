# Finding prime numbers up to a given number 

import math

def allPrimesUpTo(input):
    
    primesFound = [] # Intitialize the primes found list with the value of 2 
    for num in range(2, input):
        for prime in primesFound:
            if num % prime == 0:
                break # The number is not prime
            if math.sqrt(num) > prime:
                continue
        else:
            primesFound.append(num)
    
    return primesFound

print(allPrimesUpTo(51))



    