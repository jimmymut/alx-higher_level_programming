#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    list0 = my_list.copy()
    list0[idx] = element
    return list0
