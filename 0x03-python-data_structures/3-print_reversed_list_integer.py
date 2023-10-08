#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        list_copy = my_list.copy()
        list_copy.reverse()
        for integer in list_copy:
            print("{:d}".format(integer))
    else:
        return None
