def add(a, b):
    return a + b

def subtract(a, b):      # <--- Make sure this is 'subtract', not 'substrac'
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_even(n):
    return n % 2 == 0