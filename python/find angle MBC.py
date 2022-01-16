#hackerrank
import math
AB = int(input())
BC = int(input())
MC= math.sqrt((AB**2) + (BC**2)) / 2.0
adj= BC/2.0
x=math.acos(adj/MC)
print(int(round(math.degrees(x))),chr(176),sep='')
