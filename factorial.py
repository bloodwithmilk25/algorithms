def factorial(number: int) -> int:
    """
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(6)
    720
    """
    if number <= 2:
        return number
    return number * factorial(number - 1)
