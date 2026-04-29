from array import *
'-------inner function-----'
def outer_fn():
    def inner_fn():
        print('inside inner function')
    inner_fn()    
    return "Nothing"

something = outer_fn
# something()
'-------Decorators--------'
from functools import wraps
def decorator(func):
    def wrap():
        data = func()
        filtered = list(filter(lambda x : x > 20,data))
        print(filtered)
        return func
    return wrap
"""@decorator
def first_operation():
    ls = [23,45,12,4,56,98]
    return ls

@decorator
def second_operation():
    ls2 = [34.5,12.6,39.06,32.12]
    return ls2"""
def first_operation():
    ls = [23,45,12,4,56,98]
    return ls


def second_operation():
    ls2 = [34.5,12.6,39.06,32.12]
    return ls2

first = decorator(first_operation)
second = decorator(second_operation)
print(first(),second())
"""
A decorator:
Takes a function,Wraps it with extra logic,Returns a new function
Flow: 
first_operation → decorator(first_operation) → wrap() """