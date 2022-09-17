"""
Encapsulation

In Oops, we can restrict access to the variable and method this is called encapsulation

- Why we are using this Encapsulation?
* To prevent data to be modified by accidentally, we can prevent data with the help of access modifier
* There are two type access modifier `public` , `private` & `protected`

- Public access modifier
Public members are those members which can be access with in or outside the class

- Private access modifier
Private members are similar to protected members, the difference is that the class members declared
private should neither be accessed outside the class nor by any base class, to define a private member
prefix the member name with double underscore “__”.

- Protected access modifier
Protected members are those members of the class that cannot be accessed outside the class but can be
accessed from within the class and its subclasses. To accomplish this in Python, just follow the convention
by prefixing the name of the member by a single underscore “_”.

Note: Python’s private and protected members can be accessed outside the class through "python name mangling".

"""


# Python program to
# demonstrate protected members

# Creating a base class
class Base:
    def __init__(self):
        # Protected member
        self._a = 2


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling protected member of base class: ",
              self._a)

        # Modify the protected variable:
        self._a = 3
        print("Calling modified protected member outside class: ",
              self._a)


obj1 = Derived()

obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)

print("#" * 100)

"""
# Python program to
# demonstrate private members

# Creating a Base class
"""


class Base:
    def __init__(self):
        self.a = "Hello World"
        self.__c = "Hello World"


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)

# Uncommenting print(obj1.c) will
# raise an AttributeError
# print(obj1.c)

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class
# obj2 = Derived()
