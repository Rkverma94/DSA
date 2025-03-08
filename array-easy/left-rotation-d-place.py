def reverse(arr, start, end):
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start+=1
        end-=1

def rot_k_ele(arr, k, side):
    n = len(arr)
    if side == 'left':
        key = k-1
    else:
        key = n-k-1

    reverse(arr, 0, key)
    reverse(arr, key+1, n-1)
    reverse(arr, 0, n-1)


arr = [1,2,4,5,6,7]
rot_k_ele(arr, 3, 'right')
print(arr)