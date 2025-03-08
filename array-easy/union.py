def union_arrays(arr1, arr2) :
    union = []
    arr1_left, arr2_left = 0,0

    while arr1_left < len(arr1) and arr2_left < len(arr2):
        if arr1[arr1_left] <= arr2[arr2_left]:
            if len(union) == 0 or union[-1] != arr1[arr1_left]:
                union.append(arr1[arr1_left])
            print(union)
            arr1_left += 1
        else:
            if len(union) == 0 or union[-1] != arr2[arr2_left]:
                union.append(arr2[arr2_left])
            print(union)
            arr2_left += 1

    while arr1_left < len(arr1):
        print(f'previous element in union : {union[-1]}')
        if union[-1] != arr1[arr1_left]:
            union.append(arr1[arr1_left])
        print(union)
        arr1_left += 1
    
    while arr2_left < len(arr2):
        print(f'previous element in union : {union[-1]}')
        if union[-1] != arr2[arr2_left]:
            union.append(arr2[arr2_left])
        print(union)
        arr2_left += 1

    return union

print(union_arrays([2,3,4,4,5], [1,4,5,7,8,9]))