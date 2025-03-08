def palindrome(num):
    reversedNum = 0
    numCp = num
    while numCp:
        digit = numCp%10
        reversedNum = reversedNum*10 + digit
        numCp //= 10
    
    return num == reversedNum

print(palindrome(7887))
