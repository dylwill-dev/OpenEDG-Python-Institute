# Introduction to multithreading and multiprocessing

# Need threading to use multiple threads
import threading 
import time


def longSquare(num, results):
    time.sleep(1)
    results[num] = num**2

squares = {}

t1 = threading.Thread(target=longSquare, args=(1, squares))
t2 = threading.Thread(target=longSquare, args=(2, squares))

t1.start() ; t2.start()
t1.join() ; t2.join()

print(squares)

# Second way to do this using list comprehensions

def longSquare2(num, results):
    time.sleep(1)
    results[num] = num**2

# Will store results here
squares2 = {}
# Create a list of threads that operate using the longSquare2 function
threads = [threading.Thread(target=longSquare2, args=(n, squares2)) for n in range(0, 100)]
# Iterate through the threads and start them
[t.start() for t in threads]
# Iterate through the threads again and join them
[t.join() for t in threads]

# Print the result
print(squares2)