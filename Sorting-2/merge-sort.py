def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid+1
    while left <= mid and right <= high :
        if arr[left] <= arr[right]:
            print(f"arr[{left}] is {arr[left]}, arr[{right}] is {arr[right]}")
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1
    return temp

def merge_sort(arr, start, end):
    if start >= end:
        return
    mid = (start + end)//2
    i=start
    print(f"divided array into : \n")
    while(i<=end):
        print(f"{arr[i]} ", end="")
        i+=1
    print("")
    merge_sort(arr, start, mid)
    merge_sort(arr, mid+1, end)
    arr = merge(arr, start, mid, end)
    print(arr)
    return arr
    
arr = [2,3,52,38,5,6,84]

merge_sort(arr, 0, len(arr)-1)
print(arr)