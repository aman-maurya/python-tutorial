"""
Multi Level Inheritance

The multi-level inheritance includes the involvement of at least two or more
than two classes. One class inherits the features from a parent class and the newly
created subclass becomes the base class for another new class
"""


class Person:
    """ Base Class """

    @staticmethod
    def display():
        print("Hello, this is the person class.")


class Employee(Person):
    """ Derived Class form Person """

    @staticmethod
    def printing():
        print("Hello, this is the derived class employee.")


class Programmer(Employee):
    """ Derived Class form Employee """

    @staticmethod
    def show():
        print("Hello, this is the another derived class programmer.")


p1 = Programmer()
p1.display()
p1.printing()
p1.show()