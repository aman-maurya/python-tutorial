"""
 Local and Global Scope || LEGB Rule (Scope)

    a) Local - Variable create inside the function
    b) Global - Variable and function create at the top of file, and are available at the end of script
    c) Enclosed - Contains Names defined inside any and all enclosed function
    d) Build-In - Contains names build in to the python interpreter

 - How Python Variable scope calling work
   Local -> Enclosed -> Global -> Build-In -> (throw error)
"""

# Example

# Global
y = 10


def outer():
    z = 4

    def inner():
        # Local
        x = 2
        print("x:", x)
        print("Inside function y:", y)

    # Enclosed
    inner()
    print("z:", z)


outer()
