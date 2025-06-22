# Different ways to enhance the safety of your code by handling exceptions

# Try / Except block
import time

def causeError():
    try:
        return 1/0
    except Exception as e:
        # Can catch and return e
        return e
    
print(causeError())

def causeError2():
    try:
        return 1/0
    except Exception:
        # Can just catch and print something
        print("An exception was caught")

causeError2()

# There is such thing as a finally: block that will always exectute no matter what happens with the try and except
def causeError3():
    try:
        return 1/0
    except Exception:
        print("An exception was caught")
    finally:
        print("This will always execute.")

causeError3()

# Use time class to time how long the execution took
def causeError4():
    start = time.time() # Sets the current time to start in seconds
    try:
        time.sleep(1.5) # Pauses execution for 0.5 seconds
        return 1/0
    except Exception:
        print("An exception was caught")
    finally:
        print(f"This code took {round(time.time() - start, 4)} second(s) to complete.")
    
causeError4()

# Can add multiple different except statements to catch different types of errors
def causeError5():
    try:
        return 1/0
    except TypeError:
        print("There was a type error!")
    except ZeroDivisionError:
        print("There was a zero division error!")
    except Exception:
        print("An exception was caught!")
    finally:
        print("This will always execute.")

causeError5()

# Having all of these exceptions in multiple different functions in a program can get repetative and messy. To deal with that we can use custom decorators to tidy up our code

# Below we will create a function to handle all of our exception types 

"""This function accepts a function as a parameter and calls a wrapper function within """
def handleException(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            print("There was a type error!")
        except ZeroDivisionError:
            print("There was a zero division error!")
        except Exception:
            print("Some sort of exception was caught!")
    return wrapper

@handleException
def causeError10(n):
    if n == 0:
        raise Exception()
    print(n)

# The above is equivalent to:
# causeError10 = handleException(causeError10)

causeError10(1)


# CUSTOM EXCEPTIONS
class HttpException(Exception):
    statusCode = None
    message = None
    
    #Override the parent construtor
    def __init__(self):
        super().__init__(f"Status code: {self.statusCode} and message is: {self.message}")

class NotFound(HttpException):
    # Override attributes
    statusCode = 404
    message = "Resource not found"

class ServerError(HttpException):
    # Override attributes
    statusCode = 500
    message = "The server failed"

def raiseServerError():
    raise ServerError()

raiseServerError()