from itertools import groupby

for i, j in groupby(input()):
    x = [len(list(j)),int(i)]
    print(tuple(x), end=" ")
