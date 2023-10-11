#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    diction = dict(filter(lambda dictionary: dictionary[1] != value, a_dictionary.items()))
    a_dictionary.clear()
    a_dictionary.update(diction)
    return a_dictionary
