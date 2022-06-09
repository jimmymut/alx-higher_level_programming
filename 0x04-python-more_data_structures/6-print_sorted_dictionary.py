#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_of_keys = list(a_dictionary.keys())
    list_of_keys.sort()
    for i in list_of_keys:
        print("{}: {}".format(i, a_dictionary.get(i)))
