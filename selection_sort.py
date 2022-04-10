from typing import List


def selection_sort(arr: List) -> None:
    """
    >>> array = [5, 7, 2, 9, 11, 5, 64, 31, 0, 1, 3]
    >>> selection_sort(array)
    >>> array
    [0, 1, 2, 3, 5, 5, 7, 9, 11, 31, 64]
    """
    for i in range(len(arr)):
        smallest = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j

        arr[i], arr[smallest] = arr[smallest], arr[i]
