def bubble_sort(arr, n):
    if( n == 1):
        return
    
    didSwap = 0

    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            didSwap += 1
    
    if didSwap == 0:
        return

    bubble_sort(arr, n-1)

arr = [4,2,6,3,8,5]
bubble_sort(arr, len(arr))
print(arr)
    