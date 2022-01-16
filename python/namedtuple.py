# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

N = int(input())
name = list(input().split())
s = 0
Marks = namedtuple('Marks', [name[0], name[1], name[2], name[3]])
for i in range(N):  
    x = list(input().split())
    average = Marks(x[0], x[1], x[2], x[3])
    s += int(average.MARKS)
s = s / N

print("{:.2f}".format(s))
