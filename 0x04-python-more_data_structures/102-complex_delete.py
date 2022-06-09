#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    listKeys = list(a_dictionary.keys())

    for ic in listKeys:
        if value == a_dictionary.get(ic):
            del a_dictionary[ic]

    return (a_dictionary)
