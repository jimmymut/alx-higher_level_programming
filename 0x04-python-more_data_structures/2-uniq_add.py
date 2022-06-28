#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlist = set(my_list)
    res = 0
    for i in range(len(newlist)):
        res += newlist[i]
    return res
