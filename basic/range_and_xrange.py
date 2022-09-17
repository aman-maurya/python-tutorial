"""
Difference between range and xrange function

The range() and xrange() are two functions that could be used to iterate a certain number of times
in for loops in Python. In Python 3, there is no xrange, but the range function behaves like xrange
in Python 2. If you want to write code that will run on both Python 2 and Python 3, you should use range()

* range() – This returns a range object (a type of iterable)
  - Returns a list of integers.
  - Execution speed is slower
  - Takes more memory as it keeps the entire list of elements in memory.
  - All arithmetic operations can be performed as it returns a list.
  - In python 3, xrange() is not supported.
  - In python 3, xrange() is changed to range().

* xrange() – This function returns the generator object that can be used to display numbers only by looping.
The only particular range is displayed on demand and hence called “lazy evaluation“
 - Returns a generator object.
 - Execution speed is faster.
 - Takes less memory as it keeps only one element at a time in memory.
 - Such operations cannot be performed on xrange().
 - In python 2, xrange() is used to iterate in for loops
"""

print("============ Example 1 ================")
# printing number which will start:1 and end:6
for i in range(1, 6):
    print(i)

print("============ Example 2 ================")
# printing number which will start:0 and end:6
for i in range(6):
    print(i)

print("============ Example 3 ================")
# printing number which will start:1 , end:6 and skip:2
for i in range(1, 6, 2):
    print(i)

print("============ Example 4 ================")
# printing number which will start:20 , end:10
# will return empty list
for i in range(20, 10):
    print(i)

print("============ Example 5 ================")
# printing number which will start:-10 , end:-5
# will return empty list
for i in range(-10, -5):
    print(i)

print("============ Example 6 ================")
# printing number which will start:-10 , end:5
# will return empty list
for i in range(-10, 5):
    print(i)





