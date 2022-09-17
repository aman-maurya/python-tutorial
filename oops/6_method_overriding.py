"""
Method Overriding

It is the ability of class to change the implementation of asset provided by its base class
"""


class A:
    """ Base class """
    @staticmethod
    def display():
        print("Method belong to class A")


class B(A):
    """ Derived Class"""
    @staticmethod
    def display():
        """
        In order to override the method we have to implement the same method which is defined in its
        base class
        """
        print("Method belong to class B")


b = B()
b.display()
