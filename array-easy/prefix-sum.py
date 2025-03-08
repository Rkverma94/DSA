def prefix_sum(arr):
    p_sum = [0] * len(arr)
    p_sum[0] = arr[0]

    for i in range(1, len(arr)):
        p_sum[i] = p_sum[i-1] + arr[i]
    return p_sum

arr = [2, 4, 6, 8, 10]
prefixSum = prefix_sum(arr)
k = 14
length = 0
for i in range(len(arr)):
    sum = 0
    for j in range(i, len(arr)):
        sum += arr[j]
        if sum == k:
            length = max(length, j-i+1)

print(length)
    

