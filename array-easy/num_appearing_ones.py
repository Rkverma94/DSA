def xor_for_single_ele(arr):
    xorr = 0
    for num in arr:
        xorr ^= num
    return xorr

def number_appearing_ones(arr) :
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    for num in freq:
        if freq[num] == 1:
            return num
        
print(xor_for_single_ele([4,3,2,2,3]))