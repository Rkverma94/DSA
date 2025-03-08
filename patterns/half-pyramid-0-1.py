# 1             i = 0 -> 1
# 0 1           i = 1 -> 0
# 1 0 1         i = 2 -> 1
# 0 1 0 1       i = 3 -> 0
# for odd row it is 0 and for even row it is 1
#
def pattern(n):
    prnt = 1
    for i in range(n):
        if(i%2==0):
            prnt = 1
        else:
            prnt = 0
        for j in range(i):
            prnt = 1-prnt
            print(prnt, end="")
        print()
pattern(7)