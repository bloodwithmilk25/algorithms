def binary_search(arr, value):
    """
    >>> binary_search([1,14,16,34,65,78,82,99,105,512], 78)
    5
    >>> binary_search([1,14,16,34,65,78,82,99,105,512], 512)
    9
    >>> binary_search([1,14,16,34,65,78,82,99,105,512], 1)
    0
    >>> binary_search([1,14,16,34,65,78,82,99,105,512], 53)
    -1
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        guess = arr[mid]

        if guess == value:
            return mid
        if guess < value:
            low = mid + 1
        else:
            high = mid - 1

    return -1
