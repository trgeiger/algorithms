"""
Different factorial functions
"""


def factorial(n):
    """Should be O(n)
    """
    if n <= 1:
        return 1
    return(n * factorial(n-1))


def facIter(n):
    """I think O(n) complexity?
    """
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
