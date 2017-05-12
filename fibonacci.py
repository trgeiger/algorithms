"""
Different implementations of the fibonacci sequence
"""


def fib(n):
    """Returns nth fibonacci number, recursive
    """
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    return(fib(n-1) + fib(n-2))


def fibIter(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a