from random import choice
def qs(arr):
    if len(arr) < 2:
        return arr
    else:
        piv = arr.pop(arr.index(choice(arr))) # chose random element prom arr and pop it
        less = [i for i in arr if i <= piv]
        greater = [i for i in arr if i > piv]
        return qs(less) + [piv] + qs(greater)
print(qs([7,13,7,89,1,2,3,9,687,4,548,79,23,1,0,0,-1,12,3]))
