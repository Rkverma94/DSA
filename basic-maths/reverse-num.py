def reverseNum(num):
    # 21 = 2*10 + 1*1
    # 12 = 1*10 + 2*1
    #
    #
    reversedNum = 0
    while num:
        digit = num % 10
        reversedNum = reversedNum * 10 + digit
        num //= 10
    return reversedNum

print(reverseNum(870900))