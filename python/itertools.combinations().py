from itertools import combinations
s,k = map(str,input().split())
k = int(k)
s = sorted(s)
for i in range(1,k+1):
    for j in combinations(s,i):
        print("".join(j))
