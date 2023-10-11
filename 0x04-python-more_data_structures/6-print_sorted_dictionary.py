#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        return None
    for pair in sorted(a_dictionary.items()):
        print("{0}: {1}".format(pair[0], pair[1]))
