def gcd(a, b):
    if(a < b):
         a, b = b, a
    
    if a % b == 0:
        return b

    while a != 0 and b != 0:
        if a < b:
            a, b = b, a
        sub = a - b
        a, b = b, sub

    if a == 0:
        return b
    else:
        return a

print(gcd(9, 12))