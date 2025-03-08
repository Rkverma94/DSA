''''''
def longest_subarray_two_pointer(arr, k):
    n = len(arr)
    left, right = 0, 0
    sum = arr[0]
    maxLen = 0
    while right < n:
        if sum == k:
            maxLen = max(maxLen, right - left + 1)
        right += 1
        if right < n: sum += arr[right]
        while left <= right and sum > k:
            sum -= arr[left]
            left += 1
    return maxLen
def longest_subarray(arr, k):
    prefix_sum_map = {}
    maxLen = 0
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum == k:
            maxLen = max(maxLen, i + 1)
        rem = sum - k
        if rem in prefix_sum_map:
            length = i - prefix_sum_map[rem]
            maxLen = max(maxLen, length)
        
        if sum not in prefix_sum_map:
            prefix_sum_map[sum] = i
    return maxLen


arr = [1,2,3,4,5,6]
'''[1,2,3,4,5,6]
    prefixSumMap = {
        1 : 0
        3 : 1
        6 : 2
        10: 3
        15: 4
        21: 5
    }


'''
print(longest_subarray_two_pointer(arr, 12))