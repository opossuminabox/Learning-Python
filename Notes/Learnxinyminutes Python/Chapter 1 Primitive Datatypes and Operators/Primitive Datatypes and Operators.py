# for single line comments

""" for 
    multi
    line
    comments
"""

##################################################
## Numbers and Variables
##################################################

3       # Just a number
7 + 1     # Addition
6 - 2     # Subtraction
3 * 6     # Multiplication
12 / 4    # Division result is ALWAYS a float
10 // 3   # Floor Division rounds DOWN or MORE NEGATIVE always, also works on floats
7 % 4     # Modulo
6 ** 3    # Exponents

1 + 3 * 2   # Use Parentheses to enforce precedence.
(1 + 3) * 2 # The first line evals to 7, the second to 8


''' Advanced Note: 
    In C, the value is stored in the spaced allocated for a.
    reassigning a different value to a changed the value. 
    
    In Python, it creates a name binding, or a pointer, for a to the value of 20.
    reassigning a different value to a points it towards a different object with the permanent value of the new value.

    It's important to note that many python features (Iterators, generators, decorators) rely on the fact that variables are references to objects, not values. 
    This explains a lot later.   

    Everything in Python is an object.
    == compares equality, is compares if they're the same object or not. 

    All integers are big numbers. No overflow, no bit worries. Char, int, long, long long in C are all Ints in Python
'''
a = 20      # Int
print(type(a))
b = 6.24    # Float
print(type(b))
c = True    # Bool (True/False, not true/false or TRUE/FALSE)
print(type(c))
d = "Dee"   # String
print(type(d))

not True        # False
True and False  # False

# True and False are actually 1 and 0 but with different keywords
True + True  # 2
True * 8     # 8
False - 5    # -5

# Comparison operators look at the numerical value of True and False
0 == False   # True
2 > True     # True
2 == True    # False
-5 != False  # True  # noqa: E712

# None, 0, and empty strings/lists/dicts/tuples/sets all evaluate to False.
# All other values are True
bool(0)      # False
bool("")     # False
bool([])     # False
bool({})     # False
bool(())     # False
bool(set())  # False
bool(4)      # True
bool(-6)     # True

# Note that bool() casts the inputs to Booleen type first then evaluates
# and, or, not evaluate the inputs as given

# Equality, Inequality, and comparisons
2 == 2  # True
2 != 2  # False
7 == 4  # False
7 != 4  # True
7 > 1   # True
7 < 1   # False
7 >= 1  # True
7 <= 1  # False

# Chaining
1 < 2 and 2 < 3 # True
1 < 2 and 2 < 1 # False
1 < 2 < 3       # True
2 < 3 < 2       # False

# is checks if they're the same object, == checks if they're the same value.
a = [1, 2, 3, 4]  # Point a at a new list, [1, 2, 3, 4]
b = a             # Point b at what a is pointing to
b is a            # True, a and b refer to the same object
b == a            # True, a's and b's objects are equal
b = [1, 2, 3, 4]  # Point b at a new list, [1, 2, 3, 4]
b is a            # False, a and b do not refer to the same object
b == a            # True, a's and b's objects are equal

# Strings and String math
"This is a string"
'Also a string'
"Hello " + "World"  # "Hello World"
"Hello " "World"    # also "Hello World"
"Use an index"[0]   # U
len("Hello")        # 5

# With Python3.6 or greater, f-strings or Formatted String Literals exist. 
name = "Possum"
f"Hello my name is {name}."             # Hello, my name is Possum.
f"{name} is {len(name)} letters long."  # Possum is 6 letters long.

# NULL does not exist in Python, instead it's None
# The guide is telling me to use is when comparing to None, but ruff says
# Use `==` to compare constant literals
None    # Like Null
"AAA" is None   #False  # noqa: F632
None is None    # True