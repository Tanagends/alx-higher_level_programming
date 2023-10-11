#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if not a_dictionary:
        return ({})
    a_dictionary_copy = a_dictionary.copy()
    for key in a_dictionary_copy:
        a_dictionary_copy[key] = a_dictionary_copy[key] * 2
    return a_dictionary_copy
