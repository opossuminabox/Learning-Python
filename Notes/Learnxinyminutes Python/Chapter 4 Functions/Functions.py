"""
    Chapter 4
    Functions
"""

# In Python:
# Functions are first class objects
# created at runtime
# stored in memory like any other object
# assignable to variables
# passable as arguments
# returnable from other functions
# dynamically typed
# closures capture surrounding variables

def add(a, b):
    return a + b




# Note that if return is not used, it returns None (think void but explicit)

# BIGGEST DIFFERENCE FROM C
# Python functions are NOT PASS BY REFERENCE OR VALUE
# Python functions are pass by object assignment
#   the name inside the function points to the same object
#   but rebinding the name does not modify the caller's name
#   mutating the object DOES affect the caller if the object is mutable

# Example
def f(x):
    x.append(99)

a = [1, 2, 3]
f(a)
print(a)    # [1, 2, 3, 99]
# This works because lists are mutable

def g(x):
    x = 5

y = 10
g(y)
print(y)
# This does not work because integers are immutable and rebinding doesn't propagate outward. 

# This is the key to python argument semantics





# Python supports Default Arguments
def repeat(message, times=2):
    return message * times

repeat("ha")    # "haha"
repeat("ha", 5) # "hahahahaha"

# NOTE default arguments are evaluated ONCE, not each function call

def bad(x, lst=[]):
    lst.append(x)
    return lst
# Bad because the parameter exists across calls
# Instead do this
def good(x, lst=None):
    if lst is None:
        lst = []
    lst.append(x)
    return lst





# You can call functions using parameter names
# Doing this allows self-documenting calls and order independance
def move(x, y):
    print(x, y)

move(y = 5, x = 10) # This is valid






# Python supports:

# Arbitrary positional arguments (*args)
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4))
# args is a tuple of all extra positional arguments

# Arbitrary keyword arguments (**kwargs)
def debug(**kwargs):
    print(kwargs)

debug(a = 1, b = 2, c = 3)    # {'a': 1, 'b': 2, 'c': 3}
# kwargs is a dict of keyword arguments

# Mixed Arguments (ORDER MATTERS)
def f(a, b, *args, **kwargs):
    return None

# Order is as follows:
#   1) named parameters
#   2) *args
#   3) Keyword-only params
#   4) **kwargs





# Functions are Objects
# You can assign them
def hello():
    print("Hi")

f = hello
f()     # Prints "Hi"

# You can store them in lists or dicts
ops = {
    "add": lambda x, y: x + y,
    "mul": lambda x, y: x * y,
}
print(ops["mul"](3, 4))
# Super powerful







# Lambda (Anonymous Functions)
lambda x, y: x + y

# Useful for short callbacks
sorted(data, key=lambda x: x.age)
# Lambdas must be a single expression, not a block
# Lambdas are not a required thing to learn, they just make life a lil easier

sorted(users, key=lambda u: u.age)

# versus

def get_age(u):
    return u.age

sorted(users, key=get_age)
# Lambdas avoid "function clutter" --- They keep things compact and readable. 

# They help pass behavior to another function
evens = filter(lambda x: x % 2 == 0, nums)

# versus

def is_even(x):
    return x % 2 == 0

evens = filter(is_even, nums)

# Saves a ton of lines of code

# Building functions inside of functions

def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15

# Another practical example

users = [
    {"name": "Adam", "age": 24},
    {"name": "Ben", "age": 19},
    {"name": "Cara", "age": 32},
]

sorted_users = sorted(users, key=lambda u: u["age"])    # One Line

# Versus

def get_age(u):
    return u["age"]

sorted_users = sorted(users, key=get_age)   # Multiple lines







# Docstrings
# Python supports built in documentation via triple-quoted strings:
def square(x):
    """Returns x squared"""
    return x * x

print(square.__doc__)



# Type Hints (Optional but extremely helpful)
# They're not enforced, but nice for tooling
def addv2(x: int, y: int) -> int:
    return x + y



# Scopes (VERY IMPORTANT)
# Python uses the LEGB rule:
#   1) Local (inside function)
#   2) Enclosing (outer function, closures)
#   3) Global
#   4) Built-in

x = 10

def k():
    x = 20
    print(x)    # will print 20

# To modify a global
def m():
    global x
    x = 50

# Closures use nonlocal instead
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20




# Returning Multiple Values (Tuple Return)
def minmax(values):
    return min(values), max(values)

low, high = minmax([1, 2, 3])
print(low)
print(high)
# Under the hood, it's a tuple


'''
Python function calls include:
    stack frame creation
    dictionary lookups
    dynamic argument binding
    reference passing
    optional destructuring
    possible default evaluation
    creating a closure (if needed)
    
They are MUCH HEAVIER than C function calls, but way more flexable.
'''

