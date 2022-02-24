""" __author__: 730335383"""

list1: list[int] = list()
list0: list[int] = list()
list1.append(10)
list1.append(20)
list1.append(30)
list1.append(40)
list0.append(1) 


def only_evens(list1):
    list2: list[int] = list()
    for num in list1:
        if num % 2 == 0:
            list2.append(num)
    return(list2)


print(only_evens(list1))


def sub(list1, int1, int2):
    print(list1) 
    list2: list[int] = list() 
    if int1 < 0:
        int1 = 0
    if int2 > len(list1):
        int2 = len(list1)
    if len(list1) == 0:
        return list2
    for index in list1[int1:int2]:
        list2.append(index)
    return(list2)


print(sub(list1, -1, 6))


def concat(list0, list1):
    list2: list[int] = list(list0) 
    for index in list1:
        list2.append(index)
    return(list2)


print(concat(list0, list1))
