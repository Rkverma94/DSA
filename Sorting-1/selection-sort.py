'''
Selection sort:
We take each element in turns
we select index and compare it's element with all other element after it
if we find any number smaller than index element 
smallest element will be swapped with index element.
Basically, we are finding smallest element and placing it in correct position
'''
def selection_sort(arr):
    n = len(arr)
    print(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
        print(f"{i+1} iteration of arr : {arr}")




arr = [2,3,1,8,4,9,5]
selection_sort(arr)