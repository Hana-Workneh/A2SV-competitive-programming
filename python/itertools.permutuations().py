from itertools import permutations
s, k = input().split()
k = int(k)
x = list(permutations(s,k))
x.sort()
for i in x:
    print("".join(i))
