# Hackerrank
import re

T = int(input())
for i in range(T):
    s = input()
    flag = True
    try:
        re.compile(s)
    except re.error:
        flag = False
    print(flag)
