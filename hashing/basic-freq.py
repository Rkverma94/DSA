def arr_freq(arr):
    # without using dict
    visited = [False] * len(arr)
    for i in range(len(arr)):
        if(visited[i] == True):
            continue
        count = 1
        for j in range(i+1, len(arr)):
            if(arr[i] == arr[j]):
                visited[j] = True
                count += 1
        print(arr[i], count)

def arr_freq_dict(arr):
    map = {}
    for i in range(len(arr)):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
    for x in map:
        print(x, map[x])

arr_freq_dict([2,3,4,2,4,5])