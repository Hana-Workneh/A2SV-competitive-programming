t = int(input())
for i  in range(t):
    alpha = str(input())
    word = str(input())
    res = 0
    for j in range(len(word)-1):
        res += abs(alpha.index(word[j]) - alpha.index(word[j+1]))
    print(res)
