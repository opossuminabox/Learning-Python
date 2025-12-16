"""
    Chapter 6
    Classes and Objects
"""

# A class is just a template for creating objects
# A class is itself an object
# Everything is dynamic - no compile-time structure
# Unless restricted, you can add attributes at runtime. 
# It's like a C style struct, but with 
#   methods attached
#   inheritance
#   dynamic fields
#   built in memory model
#   no manual allocation
#   no headers
#   no separate compilation




# Defining a basic class
class Person:
    pass
# Creates an class object named Person

# Instantiate it like this
p = Person()

# It's similar to:
# class defines the struct layout + methods 
# p = Person() allocates the struct
# Python handles all memory/allocation internally

p.name = "Jacob"
p.age = 31

# Attributes are stored in a dict inside the object
print(p.__dict__)   # Prints {'name': 'Jacob', 'age': 31}

# This is important because:
#   Python objects store attributes in a dictionary
#   fields can be added at any time
#   no fixed memory layout like C structs
#   everything is dynamic


# The __init__ Constructor
# Almost always want to initialize objects:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Jacob", 31)

# Self refers to the class itself
# It's an argument referring to the instance



# Methods are just functions

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hello, I'm", self.name)

p = Person("Jacob", 31)
p.greet()   # Python does Person.greet(p)




# Class attributes vs Instance Attributes
# Instance attribute belongs to the object

# self.x = 5

# Class attribute is shared by all instances

# class Counter:
#    count = 0


# Useful for
#   constants
#   global state associated with the class
#   caches
#   default values

# Never put mutable defaults (lists, dicts, sets) at the class level unless shared state is intentional.

# Example
class A:
    shared = []

a1 = A()
a2 = A()

a1.shared.append(1)
print(a2.shared)    # Prints [1]

# Important
#   Mutating class attributes affects all instances
#   Rebinding class attributes affects only the class






# The Python Object Model (VERY Important)

# Every object has:
#   a type (__class__)
#   a dictionary of attributes (__dict__)
#   possibly a slot-based structure (come back to this later)

# Lookups happen in this order
#   instance.__dict__
#   class.__dict__
#   parent classes (for inheritance)

# Fall through from instance -> class -> parent




# Special Methods (Magic Methods)
# Python uses "dunder" methods (double underscore)
#   __init__ - constructor
#   __repr__ - debug representation
#   __str__ - user-friendly string
#   __len__ - length of object
#   __getitem__ - indexing (obj[key])
#   __setitem__ - item assignment
#   __iter__ - iteration
#   __next__ - next() calls

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vec2({self.x}, {self.y})"
    



# Inheritance (Simple and Flexable)

class Animal:
    def speak(self):
        print("sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

# Python uses Method Resolution Order (MRO) to look up attributes. 





class Cat(Animal):
    def speak(self):
        super().speak() # Will print "sound" because it's a call to the parent method
        print("Meow")   # Will print "Meow" because it's calling from the child

c = Cat()
d = Dog()

c.speak()   # Prints "sound \n Meow"
d.speak()   # Prints "Woof"




# Everything is dynamic
# Wild things you can do
#   add methods at runtime
#   modify classes dynamically
#   mix classes together
#   monkey-patch attributes

class Person:
    pass        # Make a blank class

def new_method(self):
    print("Added later!")

Person.say = new_method     # Method has been added to Person Class

p = Person()

p.say()             # Prints "Added later!"





# Dataclasses (HIGHLY Useful)
# Python's way of saying:
# "I want a C struct with convenience methods"

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age:int

# Automatically generates
#   __init__
#   __repr__
#   Comparisons
#   Optional Immutability

# It's the cleanest way to represent small data containters. 



# Objects in Python
#   Carry overhead (dict + metadata)
#   are slower than C structs
#   but allow rapid prototyping
#   allow dynamic behavior
#   integrate perfectly with high-level features

# When you need REAL performance
#   use dataclasses
#   use __slots__
#   offload to NumPy or C
#   consider struct/array modules

# But 95% of all automation scripts run fine with standard classes