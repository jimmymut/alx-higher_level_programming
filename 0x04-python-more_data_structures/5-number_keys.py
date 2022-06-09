#!/usr/bin/python3
def number_keys(a_dictionary):
    sum1 = 0
    list_of_keys = list(a_dictionary.keys())

    for i in list_of_keys:
        sum1 += 1

    return (sum1)
