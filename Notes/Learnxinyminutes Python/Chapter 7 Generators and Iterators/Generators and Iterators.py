"""
    Chapter 7
    Advanced
"""



# What is an iterable?
# An iterable is any object you can loop over using:
for x in obj:

# Examples are
#   Lists
#   Tuples
#   Sets
#   Dicts
#   Strings
#   Files
#   Generator Objects

# Technically, an object is iterable if it has 
__iter__()
# Which must return an iterator.





# What is an iterator?
# An iterator is an object with 2 methods
#   __iter__() -> returns the iterator itself
#   __next__() -> returns the next value OR raises StopIteration
# In C terms, it's like a struct that has a pointer to the current position, a function that moves to the next position, and a sentinel to detect end-of-data
# In ASM terms, __next__ is like dereferencing a pointer and then incrementing it. When you hit the end, branch to exit via StopIteration





# How for loops really work in Python

for x in iterable:
    print(x)

# Python secretly does

iterator = iter(iterable)
while True:
    try:
        x = next(iterator)
    except StopIteration:
        break
    print(x)

# This is why python can iterate through anything, even things that aren't sequences. 

# Compare this to C:
'''
while (ptr != end) {
    x = *ptr;
    ptr++;
}
'''




# Generator functions (yield)
# A generator is a spceial kind of iterator created by a function

def count(n):
    while n > 0:
        yield n
        n -= 1

for x in count(5):
    print(x)

# Prints
# 5
# 4
# 3
# 2
# 1

# What yield does:
#   pauses the function
#   returns a value
#   saves the local state
#   resumes the function when next() is called again

# This is a powerful thing







# Generators versus functions

# Normal functions
#   Run to completion
#   Return once
#   Returns a final value
#   Uses return

# Generators
#   Pause / Resume
#   Yields multiple values
#   Can stream values
#   Uses yield

# Generators give python lazy evalustion, like C pointer iteration over large buffers





# Generator Expressions
squares = (x*x for x in range(10))
# Does not create a list
# Creates a lazy generator object





# Why generators matter
#   You don't want to store the whole result in memory, you can parse a 2GB file line by line
#   You want to stream data, like reading CSVs processing one row at a time
#   You want efficient pipelines, used for filtering, transforming, and mapping
#   You want expressive code without intermediate lists





# Custom iterators
# You can build classes that behave like Python Iterators

class Countdown:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        val = self.n
        self.n -= 1
        return val
    
# To use it

for x in Countdown(5):
    print(x)

# It's like creating a struct with an internal pointer




# Why not just use lists?
# Lists can be too large, too slow, unnecessary
# Generators only produce data on demand

# This is a huge advantage over C Style malloc'd buffers when memory is tight. 





# Files are iterators
with open("data.txt") as f:
    for line in f:
        print(line)

# The file object implements __iter__ and __next__ internally




# Chain generators for pipelines

def read_numbers(path):
    with open(path) as f:
        for line in f:
            yield int(line)

def evens(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

for x in evens(read_numbers("nums.txt")):
    print(x)

# Does the same as piping in the shell
cat nums.txt | grep even






# In a Generator, you almost never use return value
# Instead use yield
# Return means StopIteration, no more values. 




# Python            C                                       ASM
# Generator         Pointer + Loop state                    Register increments + Branch
# next()            dereference + increment                 LDR + ADD + BNE
# StopIteration     loop termination                        conditional branch to exit
# yield             save registers + return temporarily     push/pop state


