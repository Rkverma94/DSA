import sys
def high_low_freq(arr):
    map = {}
    for i in range(len(arr)):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1

    most_common_ele = None
    high_freq = 0
    least_common_ele = None
    low_freq = 999999
    for k,v in map.items():
        if v > high_freq:
            most_common_ele = k
            high_freq = v
        if v <= low_freq:
            least_common_ele = k
            low_freq = v
    return (least_common_ele, most_common_ele)

low, high = high_low_freq([2,3,45,2,3])
print(low, high)