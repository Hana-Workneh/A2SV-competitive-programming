from collections import Counter

x = int(input())
shoeSize = Counter(input().split())
n = int(input())
sumOfPrice = 0
for i in range(n):
    desiredSize = input().split()
    if shoeSize[desiredSize[0]] != 0:
        shoeSize[desiredSize[0]]-= 1
        sumOfPrice += int(desiredSize[1])
print(sumOfPrice)
