def primeNum(num):
    divisor = [num]
    for i in range(num//2,0,-1):
        if(num % i == 0):
            if len(divisor) > 2:
                return False
            divisor.append(i)
    return True

print(primeNum(464))