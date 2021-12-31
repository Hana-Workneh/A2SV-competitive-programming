def printPattern(N):
    for i in range(2):
        for j in range(1, N+1):
            if N == 1:
                print("#")
            else:
                print("#" * (N -1), end = " ")
        print()

printPattern(3)
