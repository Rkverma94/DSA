def upright_pyramid(row):
    # for spaces
    #  --*--    ---*---
    #  -***-    --***--
    #  *****    -*****-
    #           *******
    # closely observing 
    # for 1st row i=0 we have (row-1-i) 2 spaces (2*i+1) 1 star and again (row-1-i) 2 spaces
    # for 2nd row i=1 we have (row-1-i) 1 space (2*i+1) 3 star and again (row-1-i) 1 space
    # for 3rd row i=2 we have (row-1-i) 0 space (2*i+1) 5 star and again (row-1-i) 0 space
    for i in range(row):
        for _ in range(row-1-i):
            print(" ", end="")
        for _ in range(2*i+1):
            print("*", end="")
        print()

def inverted_pyramid(row):
    # *****     *******
    # -***-     -*****-
    # --*--     --***--
    #           ---*---
    for i in range(row):
        for _ in range(i):
            print(" ", end="")
        for _ in range(2*row-(2*i+1)):
            print("*", end="")
        print()

def main():
    upright_pyramid(5)
    inverted_pyramid(5)

main()