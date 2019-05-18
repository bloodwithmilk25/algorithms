def find_smallest(arr):
    smallest = arr[0]
    smallest_i = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_i = i

    return smallest_i

def selection_sort(arr):
    for i in range(len(arr)):
        smallest = find_smallest(arr[i:])
        arr.insert(i, arr.pop(smallest+i))
    return arr


a = [5,7,2,9,11,5,64,31,0,1,3]
print(selection_sort(a))
