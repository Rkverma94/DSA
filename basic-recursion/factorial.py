def fact_itr(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def fact_recur_forward(n, res=1):
    if(n < 1):
        return res
    res = res * n
    return fact_recur_forward(n-1, res)

def fact_recur_backward(n):
    if(n <= 1):
        return n
    res = fact_recur_backward(n-1)
    return n*res
    

def fact_recur(n):
    if(n == 1):
        return 1
    return n * fact_recur(n-1)

print(fact_recur_backward(5))
