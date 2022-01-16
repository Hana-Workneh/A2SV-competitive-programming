l = []
e = []
u = []
o = []
for i in input():
    if i.isdigit():
        if int(i)%2 == 0: e.append(i)
        else: o.append(i)
    else:
        if i.isupper():u.append(i) 
        else: l.append(i)
l.sort()
e.sort()
u.sort()
o.sort()
print("".join(l+u+o+e))
