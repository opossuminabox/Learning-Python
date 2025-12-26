"""
    Chapter 8
    Decorators
"""

# What is a decorator?
#   A decorator is a function that takes another function, adds behavior, and returns a new function

# A simple decorator

def my_decorator(func):
    def wrapper():
        print("Before Call")
        func()
        print("After Call")
    return wrapper

# Usage

@my_decorator
def hello():
    print("Hello!")


hello()

# Prints: 
# Before Call
# Hello!
# After Call



# What actually happened behind the scenes
hello = my_decorator(hello)
# So the identifier "hello" now points to the wrapper, not the original function
# In Python terms, hello was bound to a new function. 




# Decorator Signature

# A decorator always looks like:

def decorator(function):
    def wrapper(*args, **kwargs):
        # Modify Behavior
        return function(*args, **kwargs)
    return wrapper

# *args = tuple of positional args
# **kwargs = dict of keyword args
# Allows wrapping ANY function regardless of signature




# Why are decorators useful?

# Logging

from functools import wraps

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

add(3, 5)

# Prints
[LOG] Calling add with args=(3, 5), kwargs={}
[LOG] add returned 8

# Great for debugging automation flows, tracing EMR actions, and monitoring scripts



# Timing

import time
from functools import wraps

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"{func.__name__} took {duration:.5f} seconds")
        return result
    return wrapper

@timed
def slow():
    time.sleep(1)   # Sleep for 1 second

slow()

# Prints
slow took 1.00021 seconds

# Great for profiling, optimizing loops, and checking on network/automation delays



# Retry logic for automation

from functools import wraps
import time

def retry(times = 3, delay = 1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt}/{times} failed: {e}")
                    if attempt < times:
                        time.sleep(delay)
            raise Exception(f"{func.__name__} failed after {times} attempts")
        return wrapper
    return decorator

@retry(times = 3, delay = 2)
def flaky_operation():
    raise ValueError("Oops")

flaky_operation()

# Prints
"""
Attempt 1/3 failed: Oops
Attempt 2/3 failed: Oops
Attempt 3/3 failed: Oops
Traceback (most recent call last):
  File "REDACTED FILE PATH BY POSSUM", line 23, in <module>
    flaky_operation()
    ~~~~~~~~~~~~~~~^^
  File "REDACTED FILE PATH BY POSSUM", line 15, in wrapper
    raise Exception(f"{func.__name__} failed after {times} attempts")
Exception: flaky_operation failed after 3 attempts
"""
# Great for EMR Login Failures, Temporary Network Issues, Selenium/Playwright flaky steps, API calls





# Access Control
from functools import wraps

def requires_admin(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("is_admin"):
            raise PermissionError("Admin privileges required")
        return func(user, *args, **kwargs)
    return wrapper

@requires_admin
def delete_patient(user, patient_id):
    print(f"Deleting patient {patient_id}")

user = {"name": "Alice", "is_admin": False}

delete_patient(user, 123)

# Prints
"""
Traceback (most recent call last):
  File "REDACTED FILE PATH BY POSSUM", line 17, in <module>
    delete_patient(user, 123)
    ~~~~~~~~~~~~~~^^^^^^^^^^^
  File "REDACTED FILE PATH BY POSSUM", line 7, in wrapper
    raise PermissionError("Admin privileges required")
PermissionError: Admin privileges required
"""

# Great for multi-user tools, sensitive features, EMR workflows where some actions require permission





# Caching

# Validation