    list1=[0,1,0,3,12]
    list2 = []
    for i in range(len(list1)):
        if list1[i] != 0:
            list2.append(list1[i])
    counter = len(list1) - len(list2)
    for j in range(counter):
        list2.append(0)
    print(list2)
