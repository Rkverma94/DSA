def fib_itr(n):
    fib_series = [0,1]
    for i in range(n):
        fib_series.append(fib_series[-1]+fib_series[-2])
    print(fib_series[:len(fib_series)-1])
arr = []
def fib_recur(n):
    if(n == 0):
        arr[0] = 0
        return 0
    elif(n == 1):
        arr[1] = 1
        return 1
    else:
        arr[n] = fib_recur(n-1) + fib_recur(n-2)
        return arr[n]

for i in range(7):
    arr.append(-1)
# fib_itr(6)
fib_recur(6)
print(arr)