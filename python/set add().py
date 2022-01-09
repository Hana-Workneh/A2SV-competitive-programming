# Hackerrank
N=int(input())
distinct=set()
for i in range(N):
    countries=input()
    distinct.add(countries)
print(len(distinct))
