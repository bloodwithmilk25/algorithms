from typing import List
#  https://en.wikipedia.org/wiki/Merge_sort


def merge_sort(arr: List) -> None:
    """
    >>> array = [5, 7, 2, 9, 11, 5, 64, 31, 0, 1, 3]
    >>> merge_sort(array)
    >>> array
    [0, 1, 2, 3, 5, 5, 7, 9, 11, 31, 64]
    """
    if len(arr) == 1:
        return

    # Finding the mid of the array
    mid = len(arr) // 2

    # Dividing the array elements
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    # Copy data to temp arrays left[] and right[]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
