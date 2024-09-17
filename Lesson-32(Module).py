'''

#main_Module.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b


#import_module.py
import main_Module

x = 10
y = 5

print("Addition:", Module.add(x, y))
print("Subtraction:", Module.subtract(x, y))
print("Multiplication:", Module.multiply(x, y))
print("Division:", Module.divide(x, y))

'''