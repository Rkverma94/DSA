def insert_sort(arr, index, n):
    if index == n:
        return
    i = index
    while i > 0 and arr[i] < arr[i-1]:
        arr[i], arr[i-1] = arr[i-1], arr[i]
        i -= 1
    
    insert_sort(arr, index+1, n)

arr = [5,4,2,7,5,4,9]
insert_sort(arr, 0, len(arr))
print(arr)
