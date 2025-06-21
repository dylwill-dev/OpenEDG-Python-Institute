# This file uses datetime from the datetime package
from datetime import datetime

print("Get the current date and time:",datetime.now()) # This will get the current date and time and return it
print("Get just the date: ", datetime.now().date()) # Get just the date from the date and time

# Make a loop that waits a specific amount of time before finishing

time_delay = (datetime.now().second + 2) % 60

while True:
    if datetime.now().second == time_delay:
        break
print(f"We are at {time_delay} seconds.")