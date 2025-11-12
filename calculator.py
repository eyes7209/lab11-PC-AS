# https://github.com/eyes7209/lab11-PC-AS/settings/access?guidance_task=
# Partner 1: Patrick Carey
# Patrner 2: Austin Stephenson

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# First exam
import math
def add(a, b):
    return a+b
    pass

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError('division by zero')
    return b / a # raise ZeroDivisionError if a == 0

def log(a, b):
    if a < 0:
        raise ValueError("Input cannot be a negative number.")
    return math.log(a,b)

def exp(a, b):
    return a**b





import math

def square_root(a):
    if a < 0: raise ValueError
    else: return math.sqrt(a)
def hypotenuse(a,b): return math.hypot(a,b)
# First example
def add(a, b): return a + b
def sub(a,b): return a - b
def mul(a,b): return a* b
def log(a,b):
    if a < 0 or b < 0: raise ValueError
    else: return math.log(b,a)
def exp(a,b): return a ** b


