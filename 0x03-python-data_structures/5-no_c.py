#!/usr/bin/python3
def no_c(my_string):
    new = my_string[:]
    i = 0
    while i in range(len(my_string) - 1):
        if my_string[i] == 'c' or my_string[i] == 'C':
            new = new[:i] + my_string[(i + 1):]
            i += 1
    return new
