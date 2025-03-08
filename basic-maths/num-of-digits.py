import math
# 98/10 = 9
# 98 % 10 = 8
# 
def numOfDigits(num):
    count = 0
    while num != 0:
        num = num // 10
        count += 1
    return count

def optimalApproach(num):
    return int(math.log10(num)+1)

#print(numOfDigits(9838477))
print(optimalApproach(98))