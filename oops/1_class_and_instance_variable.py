"""
Different between class and instance variable
"""


class Student:
    """
    1. Variable which are create inside the class and without the `self` keyword are called as class variable
    2. Variable which are with the `self` keyword are called as instance variable
    """
    college = "ABC"  # Class variable

    def __init__(self, roll_no, name):
        self.roll_no = roll_no  # Instance variable
        self.name = name  # Instance variable

    def display(self):
        print("Student name :: ", self.name)
        print("Student roll no :: ", self.roll_no)
        # to access the class variable we use class name followed by name of variable
        print("College :: ", Student.college)


std1 = Student("john", 123)
std1.display()

std2 = Student("bob", 456)
std2.display()


