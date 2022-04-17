cache = {}


def fibonacci(n: int) -> int:
    """
    >>> fibonacci(9)
    34
    >>> fibonacci(16)
    987
    >>> fibonacci(100)
    354224848179261915075
    """
    if n < 2:
        return n
    if n in cache:
        return cache[n]

    cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n]
