def print_n_times(n, i=1):
    if(i > n): 
        return
    print(f"{i} Hello")
    i += 1
    print_n_times(n, i)

print(print_n_times(4))