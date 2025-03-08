# This is forward recursion approach where we perform operation in forward stack 
def print_till_n(n, i=1):
    if(i > n):
        return
    print(i)
    print_till_n(n, i+1)

# This is backward recursion approach where we perform operation when base case is executed and stack comes back
def print_till_n_backward_recur(n):
    if(n < 1):
        return
    print_till_n_backward_recur(n-1)
    print(n)

print_till_n_backward_recur(4)