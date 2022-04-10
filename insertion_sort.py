from typing import List


def insertion_sort(arr: List) -> None:
    """
    >>> array = [5, 7, 2, 9, 11, 5, 64, 31, 0, 1, 3]
    >>> insertion_sort(array)
    >>> array
    [0, 1, 2, 3, 5, 5, 7, 9, 11, 31, 64]
    """
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            for k in range(i, -1, -1):
                if arr[i+1] >= arr[k]:
                    arr.insert(k + 1, arr.pop(i+1))
                    break
            else:
                arr.insert(0, arr.pop(i + 1))
