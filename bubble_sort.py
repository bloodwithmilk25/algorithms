from typing import List


def bubble_sort(arr: List) -> None:
    """
    >>> array = [5, 7, 2, 9, 11, 5, 64, 31, 0, 1, 3]
    >>> bubble_sort(array)
    >>> array
    [0, 1, 2, 3, 5, 5, 7, 9, 11, 31, 64]
    """
    for i in range(len(arr) - 1):
        for n in range(len(arr) - 1 - i):
            if arr[n] > arr[n + 1]:
                arr[n], arr[n + 1] = arr[n + 1], arr[n]
