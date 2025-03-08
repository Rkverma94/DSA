def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

arr = [1,2,3,4,5,6,7]
print(is_sorted(arr))
arr.append(4)
print(is_sorted(arr))