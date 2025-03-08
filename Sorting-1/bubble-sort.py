'''
Bubble sort means bubble max element at the end
so 
1st loop will start from last element
2nd loop will start from 0 to i
compare 1st 1st element with last element if 1st element is greater than swap it
so in this way at last position there will be max element 
and in subsequent iterations max element will be bubbled at last and array will be sorted
'''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        for j in range(0, i):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
        print(arr)
    print(arr)



arr = [13,46,24,52,20,9]
bubble_sort(arr)