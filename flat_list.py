def flat_list(list1):
    list3 =[]
    for i in list1:
        if type(i)==list:
            list3.extend(i)
        elif type(i) == int:
            list3.append(i)
    list2 =[]
    for i in list3:
        if type(i) == list:
            list2.extend(i)
        elif type(i) == int:
            list2.append(i)
    list2 = list(set(list2))
    print(list2)

list1 =[1, [2, [3, 4], 5], 6, [7, [8, 9]], 10]
flat_list(list1)