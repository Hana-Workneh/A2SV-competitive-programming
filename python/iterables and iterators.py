from itertools import combinations

N = int(input())
lowercase = input().split()
K = int(input())
outcome = tuple(combinations(lowercase,K))
count=0
for c in outcome:
    if 'a' in c:
        count+=1
print(round((count/len(outcome)),3))
