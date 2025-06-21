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

# Using 'in' in a different fashion (checks if 6 is in my_list)
print (6 in my_list, '\n') # = False


# While Loops -------------------------------
print('While Loop:')
iterator = 0
while (iterator < 5):
  print(iterator)
  iterator += 1
