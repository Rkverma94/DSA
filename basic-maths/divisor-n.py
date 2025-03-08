def nDivisor(num):
    divisors = [num]
    for i in range(num//2, 0, -1):
        if num % i == 0:
            divisors.append(i)
    return divisors

print(nDivisor(12))