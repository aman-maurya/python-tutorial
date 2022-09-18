"""
What is Closures

Function object that remembers value in the enclosing scope even if they are not in memory

Benefit of using Closures
- Can avoid using of global value
- data hiding
- Let us implement decorator

"""


def outer():
    x = 3

    # Enclosed
    def inner():
        y = 5
        result = x + y
        return result

    return inner


a = outer()
print(a())
