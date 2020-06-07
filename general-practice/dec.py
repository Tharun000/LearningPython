# this is to practice the use of decorators in python
from time import time

def display(func):
    def _print(*args, **kwargs):
        rv = func(*args, **kwargs)
        print(rv)
        return rv
    return _print

@display
def add(x = 2, y = 3):
    return x + y

add(10)

@display
def addMore(a = 1, b = 7, c = 10, d = 17, e = 20, f = 35):
    return a + b + c + d + e + f

addMore(40, 17)