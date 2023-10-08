#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = -1
    length = len(my_list)
    for _ in range(length):
        print("{:d}".format(my_list[i]))
        i -= 1
