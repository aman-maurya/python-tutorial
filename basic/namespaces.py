"""
 Namespace and Variable Scope

 - We use `names` (such as variable name, class name, function name) in python to identify the object just like
   we use name to identify person in real life, so `Namespace` is the system which will control all the names which
   we use in our program, and it will assure the all the names which we use is unique, and it won't lead nay conflict.

   * Types of namespace

    - Built-in namespace
      When you start the python interpreter build-in namespace is created which contain all the build-in names.
      So, when Python interpreter runs solely without any user-defined modules, methods, classes, etc. Some functions
      like print(), id() are always present, these are built-in namespaces.

    - Global namespace
      When a user creates a module, a global namespace gets created, later the creation of local functions creates
      the local namespace

    - Local namespace
      Creation on local function create local namespace
"""
#################################
# Example 1 of Namespace
#################################
# var1 is in the global namespace
var1 = 5


def some_func():
    # var2 is in the local namespace
    var2 = 6

    def some_inner_func():
        # var3 is in the nested local
        # namespace
        var3 = 7


#################################
# Example 2 of Namespace
#################################
# Python program processing
# global variable

count = 5


def some_method():
    global count
    count = count + 1
    print(count)


some_method()

####################################################################
# In order to show all the build in `names`, we use dir() function
####################################################################
# Example 1
print(dir())  # will print the namespace list
num = 5
print(dir())  # you will notice namespace list has the variable name `num`

# Example 2
print("Initially", dir())


def fun():
    n = 1
    print("Inside the function ", dir())


fun()

print("Outside the function", dir())
