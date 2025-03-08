def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    # i < j and not i <= j because low and high cannot overlap
    while i < j:
        # find element greater than pivot on left side to swap
        while arr[i] <= pivot and i <= high-1:
            i += 1
        
        # find element smaller than pivot on right side to swap
        while arr[j] > pivot and j >= low+1:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    # j will be the correct position of pivot element
    return j

def quick_sort_algo(arr, low, high):
    if(low < high):
        pivot_index = partition(arr, low, high)
        quick_sort_algo(arr, low, pivot_index-1)
        quick_sort_algo(arr, pivot_index+1, high)

def quick_sort(arr):
    quick_sort_algo(arr, 0, len(arr)-1)


arr = [4,6,2,5,7,9,1,3]
print(arr)
quick_sort(arr)
print(arr)