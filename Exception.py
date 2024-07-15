"""try:# Code that might raise an exception
    result = 10 / 0 # This will raise a ZeroDivisionError
except ZeroDivisionError:# Handle the exception here
    print("Division by zero is not allowed.")"""


"""try:# Code that might raise an exception
    result = int("abc") # This will raise a ValueError
except ValueError:# Handle the ValueError
    print("Invalid conversion to integer.")
except ZeroDivisionError:# Handle the ZeroDivisionErrr
    print("Division by zero is not allowed.")"""


"""try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print(f"Result: {result}")"""

"""try:
    file = open("D:\Anudip\example.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close() # Ensure the file is always closed"""

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y
try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")
 
