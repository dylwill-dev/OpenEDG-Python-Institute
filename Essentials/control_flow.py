""" Control flow in Python
 - If / Else
 - For Loops
 - While Loops
   """

# If / Else Statements
a = True
b = True
c = False
if (a):
  print("A is True")
else:
  print ("A is False")   
if(b):
  print("B is also True")
else:
  print("B is not true")    
if(c):
  print("C is also True")        
else:      
    print("C is not true")              

print ("--- Check is complete ---\n")

# For Loops -------------------------------
print("For Loop: ")
my_list = [1, 2, 3, 4, 5]

for number in my_list:
  print(number)

# For / Else Loops
print("\nFinding prime numbers")
for number in range(2,100):
  for factor in range(2, int(number**0.5)+ 1):
    if number % factor == 0:
      # If the number has a factor of any kind, then we break out of the loop and continue on with the outer loop (increasing the number)
      # If this statement doesn't satisfy then it means that the number is prime
      break
  # Else statement on the level of the second for loop to print out the prime number
  else:
    # This will only happen if the break in the if condition is never thrown
    print(f"{number} is a prime number!")




# Using 'in' in a different fashion (checks if 6 is in my_list)
print (6 in my_list, '\n') # = False

# Ternary with if/else statements - One liner way of getting quick output
num = 9
print("Even" if num % 2 == 0 else "Odd",num if num % 2 == 1 else num) # This says print even if the num is even and if it is not print the number out


# While Loops -------------------------------
print('While Loop:')
iterator = 0
while (iterator < 5):
  print(iterator)
  iterator += 1
