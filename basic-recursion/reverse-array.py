def reverse_array_itr(arr):
    j = len(arr)-1
    i=0
    while(i<j):
        arr[j], arr[i] = arr[i], arr[j]
        i+=1
        j-=1
    
    print(arr)
    
def reverse_arr_recur(arr, start, end):
    if(start >= end):
        return arr
    arr[start], arr[end] = arr[end], arr[start]
    reverse_arr_recur(arr, start+1, end-1)

    

# reverse_array([2,3,4,5,74,34])
array = [2,3,4,5,6,7,8]
array = reverse_arr_recur([2,3,4,5,6,7,8], 0, len(array)-1)
print(array)