def twoStacks(maxSum, a, b):

    a.reverse()
    b.reverse()
    stack = []
    temp=0
    count = 0
    for i in range(len(a)):
        j = a.pop()
        if (temp + j) <= maxSum:
            temp += j
            count += 1
            stack.append(j)
        else: 
            break
    maxScore = count
    for j in range(len(b)):
        i = b.pop()
        temp += i
        count += 1
        while temp > maxSum and len(stack) != 0:
            temp -= stack.pop()
            count -= 1
        if temp <= maxSum and count > maxScore:
            maxScore = count

    return maxScore 
