"""
Difference between input() and raw_input() functions in Python

Python input() function is used to take the values from the user. The input function explicitly converts the
input you give to type string. But Python 2.x input function takes the value and type of the input you enter
as it is without modifying the type.

In python 3.x there is no raw_input()
In python 3.x input() function behave similar to raw_input()

* input()
 - input() function take the user input.
 - Its syntax is -: input(prompt)
 - It takes only one parameter that is prompt.
 - It return the input that it takes.
 - It converts the input into a string by removing the trailing newline

* raw_input()
 - raw_input() function takes the input from the user.
 - Its syntax is -: raw_input(prompt)
 - It takes only one parameter that is the input.
 - Its return type is of string.
 - It is only introduced in python 2.0 version

"""

# Python program to demonstrate
# input() function in Python3.x


val1 = input("Enter the name: ")

# print the type of input value
print(type(val1))
print(val1)


val2 = input("Enter the number: ")
print(type(val2))

val2 = int(val2)
print(type(val2))
print(val2)



