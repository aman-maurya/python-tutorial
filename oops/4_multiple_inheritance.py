"""
Multiple Inheritance

Class can inherit from more than one base classes
"""


class Father:
    """ Base class Father """
    @staticmethod
    def sing():
        print("Hey, I can sing.")


class Mother:
    """ Base class Mother """
    @staticmethod
    def dance():
        print("Hey, I can dance.")


class Child(Father, Mother):
    """ Child class  """

    def show(self):
        self.sing()
        self.dance()


c = Child()
c.show()