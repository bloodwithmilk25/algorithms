def fibonacci_memoized(num):
    """
    >>> fibonacci_memoized(9)
    34
    >>> fibonacci_memoized(16)
    987
    >>> fibonacci_memoized(100)
    354224848179261915075
    """
    cache = {}

    def _fibonacci(n: int) -> int:
        if n < 2:
            return n
        if n in cache:
            return cache[n]

        cache[n] = _fibonacci(n - 1) + _fibonacci(n - 2)
        return cache[n]

    return _fibonacci(num)
