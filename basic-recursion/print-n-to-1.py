# This is forward recursion to print the number n to 1
def print_n_to_1(n):
    if(n < 1):
        return
    print(n)
    print_n_to_1(n-1)

# This is backward recursion to print the number n to 1
def print_n_to_1_backward_recur(n):
    if(n < 1):
        return
    print_n_to_1_backward_recur(n-1)
    print(n)

print_n_to_1(4)