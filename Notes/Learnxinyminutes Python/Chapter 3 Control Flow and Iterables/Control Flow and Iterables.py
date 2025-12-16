"""
    Chapter 3
    Control Flow and Iterables
"""

# Making a variable for example use
some_var = 5

# if statement
# Note that indentation is important in python, spaces not tabs
# 4 space indents are standard
# Prints "some_var is smaller than 10"

if some_var > 10:
    print("some_var is bigger than 10")
elif some_var < 10:     #Equivalent to "else if" in C
    print("some_var is smaller than 10")
else:
    print("some_var is 10")

# Match/Case statements were introduced in 3.10. (This is wild to me coming from C)

command = "run"

match command:
    case "run":
        print("The robot started to run")
    case "speak" | "say_hi":        # Multiple options using OR
        print("The robot said hi")
    case code if command.isdigit(): # Conditional
        print(f"The robot executes code: {code}")
    case _: # Wildcard catch all that will never fail, used like default/else
        print("Invalid command")
    
# Output: "The robot started to run"



# for loops

# prints:
#     dog is a mammal
#     cat is a mammal
#     mouse is a mammal


for animal in ["dog", "cat", "mouse"]:
    # You can use format() to interpolate formatted strings
    print("{} is a mammal".format(animal))


# range(number) returns an iterable of numbers from zero up to (but excluding) the given number    
# prints:
#     0
#     1
#     2
#     3


for i in range(4):
    print(i)


# range(lower,upper) returns an iterable of numbers from zero up to (but excluding) the upper number
# prints:
#     4
#     5
#     6
#     7


for i in range(4, 8):
    print(i)


# range(lower, upper, step) returns an interable numbers from the lower number to the upper number, incrementing by the step.
# If not defined, default step is 1
# prints:
#     4
#     6


for i in range(4, 8, 2):
    print(i)


# Loop over a list to retrieve both index and value of each list item
#     0 dog
#     1 cat
#     2 mouse

animals = ["dog", "cat", "mouse"]
for i, value in enumerate(animals):
    print(i, value)


# while loops work as expected, loop until no longer true
# prints:
#     0
#     1
#     2
#     3

x = 0
while x < 4:
    print(x)
    x += 1  # Note that x++ does not work in Python because variables are pointers, not values.




# This is one of the most un-c-like things i'm going to see in Python. 
# Errors like everything else are objects
# Throwing an error is like triggering a software interrupt
# Python automatically jumps to the correct handler. 

''' Advanced Notes:
try:
    code that might fail
except ERROR HERE:
    runs ONLY if something failed
else:
    runs ONLY if nothing failed
finally:
    ALWAYS runs no matter what

    
Can also remember as

try:        # "Attempt this..."
except:     # "...if something fails, go here."
else:       # "...otherwise, if everything works, go here." (Optional)
finally:    # "...and ALWAYS finish with this."

Also note that 
pass
in python is like a placeholder. It can be used where python expects something.
It can also be used as a "I don't really care about this error" insert like below
'''

try:
    # Use raise to force an error to come up. It also has other uses. It forces something to happen RIGHT NOW.
    raise IndexError("this is an index error")
except IndexError as e:     # Stores the error as variable e, very helpful.
    pass                    # Not a great habit to pass on errors unless you TRUELY know you can. Can mask bigger issues. Avoid unless completely necessary.
except (TypeError, NameError):
    print("There is a Type Error or a Name Error")
else:
    print("Good to go!")    # Runs only if no issues
finally:
    print("We can clean up resources here")     # Runs regardless



''' Advanced Notes:
Exceptions are control-flow tools, not just error reporting. They behave more like structured jumps than error codes.

with is not error handling, it's resource management. 
with automatically does a cleanup routine for you. 

f = open("file.txt")
try:
    data = f.read()
finally:
    f.close()
    
is the same as 

with open("file.txt") as f:
    data = f.read()
    

You can still combine the two

try:
    with open("x.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("Missing file")

'''
# Reading a file
with open("myfile.txt") as f:
    for line in f:
        print(line)


contents = {"aa":12, "bb":21}
with open("myfile1.txt", "w") as file:
    file.write(str(contents))   # Casts contents as a string

# From another source
# Write plain txt file
with open("plain.txt", "w") as f:
    f.write("Hello world!\nLine2")

# Read plain text file
with open("plain.txt") as f:
    data = f.read()
print(data)

# JSON
import json

data = {"a":1, "b":2}
with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json") as f:
    data = json.load(f)


# CSV
# Good for....CSV's
import csv

rows = [
    ["name", "dob", "address"],
    ["Alice", "02-14-1990", "123 Main Street"],
    ["Bob", "07-16-1943", "321 Side Road"], 
]

# Write to CSV
with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# Read CSV lame way
with open("people.csv") as f:
    reader = csv.reader(f)
    readrows1 = list(reader)
print(readrows1)

# Read CSV as a dict, super cool
# Maps each row to a dict
with open("people.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["dob"])

# XML
# XML requires a parser
# This one is funky, will have to come back to it. It's not a bad code problem, it's just how XML works. Will need practice.
# Legacy systems, as well as many hospital functions. Some HL7, Claims, etc. 

import xml.etree.ElementTree as ET

# Write
root = ET.Element("people")
ET.SubElement(root, "person", name="Alice")
ET.SubElement(root, "person", name="Bob")

tree = ET.ElementTree(root)
tree.write("people.xml")

# Read
tree = ET.parse("people.xml")
root = tree.getroot()

for child in root:
    print(child.tag, child.text)


# Binary Files
# Reading/Writing raw bytes
# Useful for dealing with images, network packets, binary logs, embedded / low level formats

with open("data.bin", "wb") as f:
    f.write(b"\x01\x02\x03\x04")

with open("data.bin", "rb") as f:
    databinary = f.read()
print(databinary)


# Pickles (Python's built in object serializer)
# Use with caution, only unpickle trusted data
"""
import pickle


obj = {"a":1, "b":[1, 2, 3]}

# Write
with open("state.pkl", "wb") as f:
    pickle.dump(obj, f)

# Read
with open("state.pkl") as f:
    objread = pickle.load(f)
"""

# YAML
# Used for configs, DevOps, Docker, cloud
# Commenting most of this out, needs a module installed by pip
# run in term, pip install pyyaml

"""
import yaml

datayaml = {"project": "test", "version": 1}

# Write
with open("config.yaml", "w") as f:
    yaml.dump(datayaml, f)

# Read
with open("config.yaml") as f:
    datayamlread = yaml.safe_load(f)
"""

# SQLite
# File based Database, super helpful for local automation

import sqlite3

conn = sqlite3.connect("people.db")
cursor = conn.cursor()

# Write
cursor.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER)")
cursor.execute("INSERT INTO users VALUES (?, ?)", ("Alice", 30))
conn.commit()
conn.close()

# Read
conn = sqlite3.connect("people.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print(rows)
conn.close()


# INI/ConfigParser

import configparser


# Write
config = configparser.ConfigParser()
config["User"] = {"name": "Alice", "role": "Admin"}

with open("settings.ini", "w") as f:
    config.write(f)

# Read
config = configparser.ConfigParser()
config.read("settings.ini")

print(config["User"]["name"])


''' Advanced Notes:

Python iterable = "A thing you can loop over that knows how to give you one item at a time"
Also note: 
    Dicts and sets rely on hashing, which is why iteration order was historically undefined pre 3.7. 
    Modern Python preserves insertion order, but lookup behavior is still hash-based, not index based.

In C terms
Iterable is like a collection
Iterator is like an opaque pointer + next() function

Iterable:
    a container you can iterate over
    
    Examples:
        list [1, 2, 3]
        tuple (1, 2, 3)
        dict {a:1}
        string "hello"
        file object
        range object
        many others

    Iterable has __iter__()

    It produces an iterator.

Iterator:
    The machinery that keeps track of the iteration state

    An iterator has:
        __next__()
        raises StopIteration when done


Python turns 
    for x in something:

into
    it = iter(something)
    while True:
        try:
            x = next(it)
        except StopIteration:
            break

With C style thinking
    iter() gives you a special pointer/iterator object
    next() dereferences the next value
    but the iterator moves forward, like incrementing a pointer with state
    once it's out of data, it throws a StopIteration exception

This is why it feels like pointer arithmetic

How different objects iterate:
    list iterator:
        stores a reference + index -> gets element by index
    dict iterator:
        iterates over keys, unless you specify .items() or .values()
    file object iterator
        returns one line per iteration
    range iterator:
        does not store the whole list - counts upward lazily
    generator:
        creates values on demand using yield

Different containers, same protocol



Why python does it this way

Saves massive memory
    Range(1_000_000_000) uses the memory of about THREE integers
    in C, you'd need to malloc gigabytes for an array

It decouples the container from traversal
    you can iterate:
        sorted
        reversed
        filtered
        transformed
        zipped
        enumerated
    all without modifying the data

It supports infinite sequences
    def count_up():
        i = 0
        while True:
            yield i
            i += 1

Impossible with arrays

It enables streaming data
    you can iterate over:
        logs
        network packets
        database rows
        stdin
        EMR Datastreams
all without loading them into memory
'''

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable)     # Prints dict_keys(['one', 'two', 'three']) . This is an object that implements over our iterable interface.

# We can loop it
for i in our_iterable:
    print(i)    # Prints one, two, three

# However we cannot address the values by index
our_iterable[1]     # Raises a TypeError

# our_iterator is an object that can remember the state as whe traverse through it. We get the next object with next()
next(our_iterable)  # "one"
next(our_iterable)  # "two"
next(our_iterable)  # "three"

# At the end, it will raise a StopIteration exception
next(our_iterable)  # Raises StopIteration

# We can also loop over it, for does this easily
our_iterator = iter(our_iterable)
for i in our_iterator:
    print(i)  # Prints one, two, three

# You can grab all the elements of an iterable or iterator by call of list()
list(our_iterable)  # Returns ["one", "two", "three"]
list(our_iterator)  # Returns [] because the state is saved