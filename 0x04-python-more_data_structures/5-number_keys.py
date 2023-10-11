#!/usr/bin/python3
def number_keys(a_dictionary):
    if not a_dictionary:
        return None
    return(len(list(a_dictionary.keys())))
