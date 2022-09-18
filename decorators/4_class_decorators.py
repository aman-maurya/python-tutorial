"""
Class Decorators
"""


class CheckDivide:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        if args[1] == 0:
            return "Can't Divide by Zero"
        else:
            self.func(*args, **kwargs)


@CheckDivide
def div(x, y):
    return x / y


print(div(1, 0))
