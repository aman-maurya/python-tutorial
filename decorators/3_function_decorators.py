"""
What is Decorators

Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour
of a function or class.But before diving deep into decorators let us understand some concepts that will come in
handy in learning the decorators.

* First Class Objects
 In Python, functions are first class objects which means that functions in Python can be used or passed as
 arguments.

 Properties of first class functions:

 - A function is an instance of the Object type.
 - You can store the function in a variable.
 - You can pass the function as a parameter to another function.
 - You can return the function from a function.
 - You can store them in data structures such as hash tables, lists, …

"""


# Example (You can store the function in a variable)
def func1():
    print("I'm function 1")


def func2(func):
    func()
    print("calling function 2")


func2(func1)


# Example of decorator
def str_upper(func):
    def inner():
        _str = func()
        return _str.upper()

    return inner


def print_str():
    return "hello world"


decor = str_upper(print_str)  # str_upper(print_str) == @str_upper
print(decor())


# Example of decorator with parameters

def wish_to(name):
    def outer(func):
        def inner():
            _str = f"{func()}, {name}"
            return _str

        return inner

    return outer


@wish_to('Aman Maurya')
def greeting():
    return "Good Morning"


print(greeting())

"""
print(greeting.__name__)
In this example if we print the name of the function the it will output `inner`, to solve this we use 
functions tool
"""
print(greeting.__name__)

"""
Example of decorator with functions tools
"""
import functools


def wish_to_new(name):
    def outer(func):
        @functools.wraps(func)
        def inner():
            _str = f"{func()}, {name}"
            return _str

        return inner

    return outer


@wish_to_new('Aman Maurya')
def greeting_new():
    return "Good Night"


print(greeting_new())
print(greeting_new.__name__)
