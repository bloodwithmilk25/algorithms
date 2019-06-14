def bubble_sort(arr):
  for i in range(len(arr)-1):
    for n in range(len(arr)-i-1):
      if arr[n] > arr[n+1]:
        arr[n], arr[n+1] = arr[n+1], arr[n]
  return arr

arr = [5,7,2,9,11,5,64,31,0,1,3]

print(bubble_sort(arr))
