#   1             1
#   1 2         2 1
#   1 2 3     3 2 1
#   1 2 3 4 4 3 2 1
#   Each line is printing second loop till j then some spaces and then again j in reverse order
#   spaces are:
#               i=0 N=4 there are six spaces 2*n - 2*(i+1)
#
def crownPattern(n):
    # this loop will be for number of lines
    for i in range(n):
        # this loop will be printing number
        for j in range(i+1):
            print(j+1, end="")
        # this loop will be for printing spaces
        for j in range(2*n - 2*(i+1)):
            print(" ", end="")
        # this loop will be for printing number
        for j in range(i+1, 0, -1):
            print(j, end="")
        print()

crownPattern(6)