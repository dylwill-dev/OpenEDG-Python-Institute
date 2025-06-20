# Using the decimal module (good for instances when working with money)

from decimal import Decimal, getcontext

print(getcontext()) # See all the parameters of what this returns
getcontext().prec = 2 # Change the precision to 2 decimal places

print(Decimal(1) / Decimal(3)) # = 0.33

# Using the decimal class can be useful in some instances when using decimal numbers (especially with money), but there is another way to go about his using round()

float_result = 1.2 - 1.0
print("Result before rounding:", float_result) # will result in 0.199999...
print("Result after rounding:",round(float_result, 2)) # 2 indicates the number of decimal places to round to resulting in 0.2