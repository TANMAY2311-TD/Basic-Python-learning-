'''

#import_packages:
    math_operations.py
    string_operations.py
    __init__.py

# math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# string_operations.py
def uppercase(text):
    return text.upper()

def lowercase(text):
    return text.lower()

# __init__.py
# You can leave this file empty or import functions from modules for easier access
from .math_operations import add, subtract
from .string_operations import uppercase, lowercase


# main.py
import main_package

# Using math operations from the package
result_add = my_package.add(5, 3)
result_subtract = my_package.subtract(5, 3)

# Using string operations from the package
upper_text = my_package.uppercase("hello")
lower_text = my_package.lowercase("WORLD")

print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Uppercase: {upper_text}")
print(f"Lowercase: {lower_text}")

'''