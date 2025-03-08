def pattern(n):
    for i in range(n):
        for j in range(i):
            print("x", end="")
        print("")
    for i in range(n):
        for j in range((n-1), i, -1):
            print("x", end="")
        print("")

pattern(5)