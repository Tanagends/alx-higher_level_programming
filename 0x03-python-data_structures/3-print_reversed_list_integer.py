#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_copy = my_list.copy()
    list_copy.reverse()
    for integer in list_copy:
        print("{:d}".format(integer))
print_reversed_list_integer([1, 2, 3])
