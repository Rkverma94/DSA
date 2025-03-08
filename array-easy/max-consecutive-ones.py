def max_consecutive_ones(arr):
    res = 0
    count = 0
    for i in arr:
        if i == 1:
            count += 1
        else:
            count = 0
        res = max(res, count)
    return res

arr = [1,1,0,0,1,1,1,1,0,1,1]
print(max_consecutive_ones(arr))