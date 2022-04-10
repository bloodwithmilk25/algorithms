from typing import List


def quicksort(arr: List) -> List:
    """
    >>> array = [5, 7, 2, 9, 11, 5, 64, 31, 0, 1, 3]
    >>> quicksort(array)
    [0, 1, 2, 3, 5, 5, 7, 9, 11, 31, 64]
    """
    if len(arr) < 2:
        return arr

    piv = arr.pop(len(arr) // 2)
    less = [n for n in arr if n <= piv]
    greater = [n for n in arr if n > piv]

    return quicksort(less) + [piv] + quicksort(greater)
