def next_smallest_greatest(arr):
    max = float('-inf')
    second_max = float('-inf')
    min = float('inf')
    second_min = float('inf')

    for i in range(len(arr)):
        if arr[i] > max:
            second_max = max
            max = arr[i]
        elif arr[i] > second_max and arr[i] != max:
            second_max = arr[i]
        if arr[i] < min:
            second_min = min
            min = arr[i]
        elif arr[i] < second_min and arr[i] != min:
            second_min = arr[i]
    
    return (second_max, second_min)


arr = [1,5,3,1,7,6]
second_tupple = next_smallest_greatest(arr)
print(second_tupple)