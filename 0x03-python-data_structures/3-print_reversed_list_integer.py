#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        leng = len(my_list)
        my_list.reverse()
        for i in range(leng):
            print("{:d}".format(my_list[i]))
