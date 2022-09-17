"""
Difference between append and extend
"""

print("================= Example 1 ===================")
# append is used to add element at the end of list
_list = [1, 2, 3]
_list.append(4)
_list.append(5)
_list.append(6)
print(_list)

print("================= Example 2 ===================")
# extend is used to add iterable( which can be looped) at the end of list
_list1 = [1, 2, 3]
_list2 = [7, 8, 9]
_list1.extend(_list2)
print(_list1)

_list1 = [1, 2, 3]
_str = "Hello"  # string is also iterable
_list1.extend(_str)
print(_list1)
