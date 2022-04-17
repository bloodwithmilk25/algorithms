cache = {}


def fibonacci(n: int) -> int:
    """
    >>> fibonacci(9)
    34
    >>> fibonacci(16)
    987
    >>> fibonacci(25)
    75025
    """
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
