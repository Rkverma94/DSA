# This is forward recursion and paramterized
def sum_n(n, sum=0):
    if(n < 1):
        return sum
    sum += n
    return sum_n(n-1, sum)

# This is functional way
def sum_n_functional(n):
    if(n == 0):
        return 0
    return n + sum_n_functional(n-1)

print(sum_n_functional(6))