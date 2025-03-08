'''
Insertion sort:
We run first loop till n
we run from 1st variable index till it is more than 0 and we compare element and the element before it
if element before it is greater than we swap it
so basically we take a element and insert it at a correct position comparing backwards
'''
def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1
        print(arr)
    print(arr)

arr = [5,44,2,6,7,14,8]
insertion_sort(arr)